from Ordonnancement import Ordonnancemement
from Job import Job
from Flowshop import Flowshop
import os

ordo = Ordonnancemement(3)
ordo2 = Ordonnancemement(3)
job1 = Job(1, [1,2,3])
job2 = Job(2, [3,2,4])
job3 = Job(3, [2,2,2])
flowshop = Flowshop([job2, job3, job1], 3)
flowshop.afficher_flowshop()

flowshop = Flowshop.lire_flowshop(os.getcwd() + "\jeu2-704.txt")
flowshop.afficher_flowshop()
lst_NEH = flowshop.liste_NEH()
Ordonnancemement(5, lst_NEH).afficher_ordo()