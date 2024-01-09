from Job import Job
import random

class Ordonnancement:
    def __init__(self, nb_machines : int, liste_jobs : list[Job] = []) -> None:
        self.nb_machines : int = nb_machines
        self.date_dispo : list[int] = [0 for i in range(nb_machines)]
        self.ordreJob : list[Job] = []
        self.ajouter_liste_jobs(liste_jobs)
    
    def afficher_ordo(self):
        print("Ordre des jobs :", end='')
        for job in self.ordreJob:
            print(" ", job.num_job," ", end='')
        print()
        nb_machines = self.nb_machines
        for job in self.ordreJob:
            print("Job", job.num_job, ":", end='')
            for machine in range(nb_machines):
                print(" op", machine, 
                    "à t =", job.debut_operation[machine],
                    "|", end='')
            print()
        print("Cmax =", self.date_dispo[nb_machines-1])

    def ajouter_job(self, job : Job):
        self.ordreJob.append(job)
        job.debut_operation[0] = self.date_dispo[0]
        self.date_dispo[0] = job.debut_operation[0] + job.temps_machines[0]
        for iMachine in range(1, self.nb_machines):
            job.debut_operation[iMachine] = max(self.date_dispo[iMachine], self.date_dispo[iMachine - 1])
            self.date_dispo[iMachine] = job.temps_machines[iMachine] + job.debut_operation[iMachine]

    def ajouter_liste_jobs(self, jobs : list[Job]):
        for job in jobs:
            self.ajouter_job(job)

    def getCMax(self):
        return self.date_dispo[self.nb_machines - 1]
    
    def getNbJobs(self):
        return len(self.ordreJob)

    def getRandomVois(self):
        lstVois = self.ordreJob.copy()
        random.shuffle(lstVois)
        return Ordonnancemement(self.nb_machines, lstVois)
    
    def getRandomVoisCouple(self):
        lstVois = self.ordreJob.copy()
        jobsExchanges = random.sample(range(self.getNbJobs()), 2)
        lstVois[jobsExchanges[0]], lstVois[jobsExchanges[1]] = lstVois[jobsExchanges[1]], lstVois[jobsExchanges[0]]
        return Ordonnancemement(self.nb_machines, lstVois)
    
    def getRandomVoisInverseSeq(self):
        bornesSeq = random.sample(range(self.getNbJobs() + 1), 2)
        bornesSeq.sort()
        lstVois = self.ordreJob.copy()
        for i in range(bornesSeq[0], bornesSeq[1]):
            lstVois[i] = self.ordreJob[bornesSeq[1] + bornesSeq[0] - i - 1]
        return Ordonnancemement(self.nb_machines, lstVois)
    
    def getRandomVoisPermSeq(self):
        bornesSeq = random.sample(range(self.getNbJobs() + 1), 2)
        bornesSeq.sort()
        lstVois = self.ordreJob.copy()
        for i in range(bornesSeq[0], bornesSeq[1] - 1):
            lstVois[i] = self.ordreJob[i + 1]
        lstVois[bornesSeq[1] - 1] = self.ordreJob[bornesSeq[0]]
        return Ordonnancemement(self.nb_machines, lstVois)