class Job :
    def __init__(self, num_job : int, temps_machines : list[int]):
        self.num_job = num_job
        self.temps_machines = temps_machines
        self.debut_operation = [None for i in range(len(temps_machines))]
    
    def afficher_job(self):
        print("Job n°", self.num_job,  
            "de durée totale", sum(self.temps_machines), ":")
        nb_op = len(self.temps_machines)
        for numero in range(nb_op):
            print("  opération n°", numero, ": durée =", self.temps_machines[numero],
                "démarre à", self.debut_operation[numero])