from Flowshop import Flowshop
from Ordonnancement import Ordonnancement
import queue
from random import shuffle
from time import time


class Tabou :
    def add_tabou(tabouList : queue.Queue, sol : Ordonnancement):
        if tabouList.full():
            tabouList.get()
        tabouList.put(sol)

    def recherche(flowshop : Flowshop, maxTabou : int, ordoInit : Ordonnancement|None = None, repmax=1000, durationMax = 300) -> Ordonnancement:
        nb_machines = flowshop.nb_machines
        if ordoInit == None:
            lst_job_shuffled = flowshop.liste_jobs.copy()
            shuffle(lst_job_shuffled)
            ordoInit = Ordonnancement(flowshop.nb_machines, lst_job_shuffled)
        print("Solution Initiale :")
        ordoInit.afficher_ordo()
        # Initialisation
        best = Ordonnancement(nb_machines, ordoInit.ordreJob)
        bestCandidate = Ordonnancement(nb_machines, ordoInit.ordreJob)
        tabouList = queue.Queue(maxsize=maxTabou)
        Tabou.add_tabou(tabouList, ordoInit)
        i = 0
        imax = nb_machines**5
        # print("imax = ", imax)
        # Make a break if the solution is not improving for repmax iterations
        lastBestValueCount = 0
        timeStart = time()
        while lastBestValueCount < repmax and i < imax and time() - timeStart < durationMax:
            i += 1
            listNeighbours = bestCandidate.getAllVoisCouple()
            for candidate in listNeighbours:
                if not Tabou.candidateInQueue(candidate, tabouList):
                    candidateValue = candidate.getCMax()
                    if candidateValue < bestCandidate.getCMax():
                        # print("candidateValue = ", candidateValue)
                        bestCandidate = candidate
            Tabou.add_tabou(tabouList, bestCandidate)
            if bestCandidate.getCMax() < best.getCMax():
                best = bestCandidate
                lastBestValueCount = 0
            else :
                lastBestValueCount += 1
        
        return best
    

    def candidateInQueue(candidate : Ordonnancement, queue : queue.Queue):
        for elem in queue.queue :
            isSame = True
            for i in range(len(candidate.ordreJob)):
                if candidate.ordreJob[i] != elem.ordreJob[i]:
                    isSame = False
            if (isSame):
                return True
        return False