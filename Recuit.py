from Flowshop import Flowshop
from Ordonnancement import Ordonnancemement
import random
import math
import time

class Recuit:
    def step(temperature : float, ordoActuel : Ordonnancemement):
        ordoVois = ordoActuel.getRandomVoisInverseSeq()
        if ordoActuel.getCMax() > ordoVois.getCMax():
            return ordoVois
        else :
            if Recuit.probPrendreNext(temperature, ordoVois.getCMax() - ordoActuel.getCMax()):
                return ordoVois
            else:
                return ordoActuel
    
    def probPrendreNext(temperature, deltaE):
        return random.random() <= math.exp(- deltaE/temperature)
    
    def recherche(flowshop : Flowshop, temperature : int, time_limit : int = 60, ordoInit : Ordonnancemement|None = None) -> Ordonnancemement:
        if ordoInit == None:
            lst_job_shuffled = flowshop.liste_jobs.copy()
            random.shuffle(lst_job_shuffled)
            ordoInit = Ordonnancemement(flowshop.nb_machines, lst_job_shuffled)
        print("Ordo Init")
        ordoInit.afficher_ordo()
        ordo = ordoInit
        ordoOpti = ordo
        start_time = time.perf_counter()
        while (time.perf_counter() - start_time <= time_limit):
            ordoSuivant : Ordonnancemement = Recuit.step(temperature, ordo)
            if ordoSuivant.getCMax() < ordoOpti.getCMax():
                ordoOpti = ordoSuivant
        return ordoOpti