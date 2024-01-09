from Flowshop import Flowshop
from Ordonnancement import Ordonnancement
import random

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
                
    # def croisement(self,pos):

if __name__ == "__main__":
    # print(Flowshop.lire_flowshop("jeu2-704.txt").afficher_flowshop())
    Genetique(10,Flowshop.lire_flowshop("jeu2-704.txt"),0.1)
