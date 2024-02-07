from Ordonnancement import Ordonnancement
from Job import Job
from Flowshop import Flowshop
from Recuit import Recuit
from Tabou import Tabou
import os

def test():
    flowshop = Flowshop.lire_flowshop(os.getcwd() + "\\tai01.txt")
    lst_NEH = flowshop.liste_NEH()
    print("liste NEH")
    Ordonnancement(flowshop.nb_machines, lst_NEH).afficher_ordo()
    Recuit.recherche(flowshop, 1e14, 300, Ordonnancement(flowshop.nb_machines, flowshop.liste_NEH())).afficher_ordo()
    #Recuit.recherche(flowshop, 1e14, 300).afficher_ordo()
    #Tabou.recherche(flowshop, 25).afficher_ordo()
    #Tabou.recherche(flowshop, 25, ordoInit=Ordonnancement(flowshop.nb_machines, flowshop.liste_NEH())).afficher_ordo()

#test()

def allTest():
    files = ["\\tai01.txt", "\\tai11.txt", "\\tai21.txt", "\\tai31.txt" , "\\tai41.txt", "\\tai51.txt"] #
    for file in files:
        print("##################################################################")
        print(file)
        print("##################################################################")
        flowshop = Flowshop.lire_flowshop(os.getcwd() + file)
        lst_NEH = flowshop.liste_NEH()
        print("liste NEH")
        Ordonnancement(flowshop.nb_machines, lst_NEH).afficher_ordo()
        Recuit.recherche(flowshop, 1e14, 300, Ordonnancement(flowshop.nb_machines, flowshop.liste_NEH())).afficher_ordo()

#allTest()

def test1():
    job1 = Job(1, [1,2,3])
    job2 = Job(2, [3,2,4])
    job3 = Job(3, [2,2,2])
    ordo = Ordonnancement(3, [job1, job2, job3])
    ordo.getRandomVoisCouple().afficher_ordo()
    ordo.getRandomVoisInverseSeq().afficher_ordo()
    flowshop = Flowshop([job2, job3, job1], 3)
    flowshop.afficher_flowshop()

#test1()

def test2():
    job1 = Job(1, [1])
    job2 = Job(2, [1])
    job3 = Job(3, [1])
    job4 = Job(4, [1])
    job5 = Job(5, [1])
    job6 = Job(6, [1])
    ordo = Ordonnancement(1, [job1, job2, job3, job4, job5, job6])
    ordo.getRandomVoisExchangeSeq().afficher_ordo()

#test2()