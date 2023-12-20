from Flowshop import Flowshop
from Ordonnancement import Ordonnancemement
import random
import math

class Recuit:
    def __init__(self, flowshop : Flowshop, temperature : float, timeLimit : int) -> None:
        self.flowshop = flowshop
    
    def step(self, temperature : float, ordoActuel : Ordonnancemement):
        ordoVois = ordoActuel.getRandomVois()
        if ordoActuel.getCMax() > ordoVois.getCMax():
            return ordoVois
        else :
            if self.probPrendreNext(temperature, ordoVois.getCMax() - ordoActuel.getCMax())
                return ordoVois
            else:
                return ordoActuel
    

    def probPrendreNext(self, temperature, deltaE):
        return random.random() <= math.exp(- deltaE/temperature)