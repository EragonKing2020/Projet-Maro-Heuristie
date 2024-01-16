from Flowshop import Flowshop
from Ordonnancement import Ordonnancement
import random
from random import randint,shuffle
from math import floor
import time

class Genetique():
    def __init__(self,pop_size : int , flowshop : Flowshop, taux_mutation : float):
        self.taille_population = pop_size
        self.flowshop = flowshop
        self.taux_mutation = taux_mutation
        self.population = [None for _ in range(pop_size)]
        i = 0
        while i < pop_size:
            ordo_candidat = random.sample(range(len(flowshop.liste_jobs)),len(flowshop.liste_jobs))
            test = True
            for j in range(i):
                if self.population[j] == ordo_candidat:
                    test = False
            if test == True :
                self.population[i] = ordo_candidat
                i+=1
        self.meilleur_temps = 10**20
        self.meilleure_solution = [None for _ in range(len(flowshop.liste_jobs))]
        self.copied=self.population.copy()
        
                   
    def croisement(self,pos : int):
        """On choisit aléatoirement des élément de la population des parent que l'on croise à l'indice pos puis on les corrige et on récupère la moitié des parents et la moitié des enfants"""
        # print(self.population,"\n")
        population = self.population.copy()
        new_population = [None for _ in range(self.taille_population)]
        for i in range(floor(self.taille_population/2)):
            parent1 = random.choice(population)
            population.remove(parent1)
            parent2 = random.choice(population)
            population.remove(parent2)
            enfant1 = parent1[:pos] + parent2[pos:]
            enfant2 = parent2[:pos] + parent1[pos:]
            new_population[2*i] = enfant1
            new_population[2*i+1] = enfant2
            # print(parent1,"\t",parent2,"\t",enfant1,"\t",enfant2)
        for i in range(self.taille_population):
            if new_population[len(new_population)-1-i] == None:
                new_population[len(new_population)-1-i] = population[i]
        for child in new_population:
            infos = [None for _ in range(len(child))]
            doublons = []
            for i in range(len(child)):
                if infos[child[i]] == None:
                    infos[child[i]] = i
                else:
                    doublons.append(i)
            manquants = []
            for i in range(len(infos)):
                if infos[i] == None:
                    manquants.append(i)
            for doublon in doublons :
                e = random.choice(manquants)
                child[doublon] = e
                manquants.remove(e)
        population = [None for _ in range(self.taille_population)]
        for i in range(self.taille_population):
            if i%2 == 0:
                population[i] = random.choice(self.population)
                self.population.remove(population[i])
            if i%2 == 1:
                population[i] = random.choice(new_population)
                new_population.remove(population[i])
        self.population = population
        # print("\n",self.population)

    def mutation(self):
        """Mutation de la population en echangeant la position de deux jobs"""
        for i in range(round(self.taille_population*self.taux_mutation)):
            mutant = random.choice(self.population)
            pos1,pos2 = random.randint(0,len(mutant)-1),random.randint(0,len(mutant)-1)
            while (pos1==pos2):
                pos2 = random.randint(0,len(mutant)-1)
            mutant[pos1],mutant[pos2] = mutant[pos2],mutant[pos1]
    
    def eval(self):
        """evalue le meilleur temps d'une population donnée"""
        for candidat in self.population:
            liste_jobs = [None for _ in range(len(candidat))]
            for i in range(len(candidat)) :
                for job in self.flowshop.liste_jobs:
                    if job.num_job == candidat[i] :
                        liste_jobs[i] = job
            ordo = Ordonnancement(self.flowshop.nb_machines,liste_jobs)
            # ordo.afficher_ordo()
            # for job in liste_jobs :
            #     job.afficher_job()
            if ordo.getCMax()<self.meilleur_temps:
                self.meilleur_temps = ordo.getCMax()
                self.meilleure_solution = candidat
        

    def recherche(self,nb_iterations : int,flowshop : Flowshop,taux_mutation : int,duree : int, ordoInit : Ordonnancement|None = None):
        """méthode principale du GA pour trouver une solution optimale à un flow shop"""
        pos = random.randint(0,len(self.population[0]))
        self.croisement(pos)
        self.mutation()
        self.eval()
        liste_jobs = [None for _ in range(len(self.meilleure_solution))]
        if ordoInit == None:
            lst_job_shuffled = flowshop.liste_jobs.copy()
            shuffle(lst_job_shuffled)
            ordoInit = Ordonnancement(flowshop.nb_machines, lst_job_shuffled)
        print("Solution Initiale :")
        ordoInit.afficher_ordo()
        temps_debut=time.time()
        while (time.time() - temps_debut) < duree:
            pos = random.randint(0,len(self.population[0]))
            self.croisement(pos)
            self.mutation()
            self.eval()
        "for i in range(nb_iterations):"
        "pos = random.randint(0,len(self.population[0]))"
        "self.croisement(pos)"
        "self.mutation()"
        "self.eval()"
        print("La meilleur solution trouvée avec l'algorithme génétique au bout de ",nb_iterations," itérations est :")
        
        for i in range(len(self.meilleure_solution)) :
            for job in self.flowshop.liste_jobs:
                if job.num_job == self.meilleure_solution[i] :
                    liste_jobs[i] = job
        Ordonnancement(self.flowshop.nb_machines,liste_jobs).afficher_ordo()
        print("population de ",self.taille_population,".")

if __name__ == "__main__":
    # print(Flowshop.lire_flowshop("jeu2-704.txt").afficher_flowshop())
    flowshop = Flowshop.lire_flowshop("tai31.txt")
    taux_mutation = 0.4
    duree = 300
    taille_population = 500
    nombre_iterations = 5000
    algo = Genetique(taille_population,flowshop,taux_mutation)
    algo2 = Genetique(taille_population,flowshop,taux_mutation)
    algo3 = Genetique(taille_population,flowshop,taux_mutation)
    algo4 = Genetique(taille_population,flowshop,taux_mutation)
    algo5 = Genetique(taille_population,flowshop,taux_mutation)
    # algo.croisement(2)
    algo.recherche(nombre_iterations,flowshop,taux_mutation,duree)
    "algo2.recherche(5000)"
    "algo3.recherche(5000)"
    "algo4.recherche(5000)"
    "algo5.recherche(5000)"
