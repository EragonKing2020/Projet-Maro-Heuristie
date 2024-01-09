from Flowshop import Flowshop
from Ordonnancement import Ordonnancement
import random
from math import floor

class Genetique():
    def __init__(self,pop_size, flowshop, taux_mutation):
        self.taille_population = pop_size
        self.flowshop = flowshop
        self.taux_mutation = taux_mutation
        self.population = [None for _ in range(pop_size)]
        i = 0
        while i < pop_size:
            ordo_candidat = random.sample(range(flowshop.nb_machines),flowshop.nb_machines)
            test = True
            for j in range(i):
                if self.population[j] == ordo_candidat:
                    test = False
            if test == True :
                self.population[i] = ordo_candidat
                i+=1
                   
    def croisement(self,pos):
        print(self.population)
        new_population = [None for _ in range(self.taille_population)]
        for i in range(floor(self.taille_population/2)):
            parent1 = random.choice(self.population)
            self.population.remove(parent1)
            parent2 = random.choice(self.population)
            self.population.remove(parent2)
            enfant1 = parent1[:pos] + parent2[pos:]
            enfant2 = parent2[:pos] + parent1[pos:]
            new_population[2*i] = enfant1
            new_population[2*i+1] = enfant2
        for i in range(self.taille_population):
            if new_population[len(new_population)-1-i] == None:
                new_population[len(new_population)-1-i] = self.population[i]
        # TO DO : correction des enfants
        self.population = new_population
            



if __name__ == "__main__":
    # print(Flowshop.lire_flowshop("jeu2-704.txt").afficher_flowshop())
    Genetique(11,Flowshop.lire_flowshop("jeu2-704.txt"),0.1).croisement(2)
