from Flowshop import Flowshop
from Ordonnancement import Ordonnancement
import random
import math
import time

class Recuit:
    def step(temperature : float, ordoActuel : Ordonnancement):
        ordoVois = ordoActuel.getRandomVoisCouple()
        if ordoActuel.getCMax() > ordoVois.getCMax():
            return ordoVois
        else :
            if Recuit.probPrendreNext(temperature, ordoVois.getCMax() - ordoActuel.getCMax()):
                return ordoVois
            else:
                return ordoActuel
    
    def probPrendreNext(temperature, deltaE):
        return random.random() <= math.exp(- deltaE/temperature)
    
    def recherche(flowshop : Flowshop, temperatureInit : int, time_limit : int = 60, ordoInit : Ordonnancement|None = None) -> Ordonnancement:
        if ordoInit == None:
            lst_job_shuffled = flowshop.liste_jobs.copy()
            random.shuffle(lst_job_shuffled)
            ordoInit = Ordonnancement(flowshop.nb_machines, lst_job_shuffled)
        print("Ordo Init")
        ordoInit.afficher_ordo()
        ordo = ordoInit
        ordoOpti = ordo
        start_time = time.perf_counter()
        temperature = temperatureInit
        while (time.perf_counter() - start_time <= time_limit):
            ordoSuivant : Ordonnancement = Recuit.step(temperature, ordo)
            if ordoSuivant.getCMax() < ordoOpti.getCMax():
                ordoOpti = ordoSuivant
            temperature *= 0.99999
        #print(temperature)
        return ordoOpti