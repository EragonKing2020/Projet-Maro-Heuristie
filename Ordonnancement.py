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
        return Ordonnancement(self.nb_machines, lstVois)
    
    def getVoisCouple(self, i1, i2):
        lstVois = self.ordreJob.copy()
        lstVois[i1], lstVois[i2] = lstVois[i2], lstVois[i1]
        return Ordonnancement(self.nb_machines, lstVois)

    def getRandomVoisCouple(self):
        jobsExchanges = random.sample(range(self.getNbJobs()), 2)
        return self.getVoisCouple(jobsExchanges[0], jobsExchanges[1])
    
    def getAllVoisCouple(self):
        lstAllVois = [None for _ in range(int(self.getNbJobs() * (self.getNbJobs() - 1) / 2))]
        i = 0
        for i1 in range(self.getNbJobs() - 1):
            for i2 in range(i1 + 1, self.getNbJobs()):
                lstAllVois[i] = self.getVoisCouple(i1, i2)
                i += 1
        return lstAllVois

    def getVoisInverseSeq(self, i1, i2):
        lstVois = self.ordreJob.copy()
        for i in range(i1, i2):
            lstVois[i] = self.ordreJob[i2 + i1 - i - 1]
        return Ordonnancement(self.nb_machines, lstVois)

    def getRandomVoisInverseSeq(self):
        bornesSeq = random.sample(range(self.getNbJobs() + 1), 2)
        bornesSeq.sort()
        return self.getVoisInverseSeq(bornesSeq[0], bornesSeq[1])
    
    def getAllVoisInverseSeq(self):
        lstAllVois = [None for _ in range(int(self.getNbJobs() * (self.getNbJobs() - 1) / 2))]
        i = 0
        for i1 in range(self.getNbJobs() - 2):
            for i2 in range(i1 + 2, self.getNbJobs()):
                lstAllVois[i] = self.getVoisCouple(i1, i2)
                i += 1
        return lstAllVois

    def getVoisPermSeq(self, i1, i2):
        lstVois = self.ordreJob.copy()
        for i in range(i1, i2 - 1):
            lstVois[i] = self.ordreJob[i + 1]
        lstVois[i2 - 1] = self.ordreJob[i1]
        return Ordonnancement(self.nb_machines, lstVois)

    def getRandomVoisPermSeq(self):
        bornesSeq = random.sample(range(self.getNbJobs() + 1), 2)
        bornesSeq.sort()
        return self.getVoisPermSeq(bornesSeq[0], bornesSeq[1])
    
    def getAllVoisPermSeq(self):
        lstAllVois = [None for _ in range(int(self.getNbJobs() * (self.getNbJobs() - 1) / 2))]
        i = 0
        for i1 in range(self.getNbJobs() - 2):
            for i2 in range(i1 + 2, self.getNbJobs()):
                lstAllVois[i] = self.getVoisCouple(i1, i2)
                i += 1
        return lstAllVois
    
    def getVoisExchangeSeq(self, i1, i2, i3, i4):
        lstVois = self.ordreJob[:i1]
        lstVois += self.ordreJob[i3:i4]
        lstVois += self.ordreJob[i2:i3]
        lstVois += self.ordreJob[i1:i2]
        lstVois += self.ordreJob[i4:]
        return Ordonnancement(self.nb_machines, lstVois)
    
    def getRandomVoisExchangeSeq(self):
        bornesSeq = random.sample(range(self.getNbJobs() + 1), 4)
        bornesSeq.sort()
        return self.getVoisExchangeSeq(bornesSeq[0], bornesSeq[1], bornesSeq[2] - 1, bornesSeq[3] - 1)

    def getAllVoisExchangeSeq(self):
        n = self.getNbJobs()
        lstAllVois = [None for _ in range()]
        i = 0
        for i1 in range(self.getNbJobs()-1):
            for i2 in range(i1 + 1, self.getNbJobs()):
                for i3 in range(i2, self.getNbJobs()):
                    for i4 in range(i3 + 1, self.getNbJobs() + 1):
                        lstAllVois[i] = self.getVoisExchangeSeq(i1, i2, i3, i4)
                        i += 1
