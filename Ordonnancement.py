from Job import Job

class Ordonnancemement:
    def __init__(self, nb_machines : int) -> None:
        self.nb_machines : int = nb_machines
        self.date_dispo : list[int] = [0 for i in range(nb_machines)]
        self.ordreJob : list[Job] = []
    
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