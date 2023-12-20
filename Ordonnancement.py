from Job import Job

class Ordonnancemement:
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