from Job import Job
from Ordonnancement import Ordonnancement

class Flowshop:
    def __init__(self, liste_jobs : list[Job], nb_machines : int) -> None:
        self.liste_jobs = liste_jobs
        self.nb_machines = nb_machines
    
    def lire_flowshop(nom_fichier):
        """ crée un problème de flowshop à partir d'un fichier """
        # ouverture du fichier en mode lecture
        fdonnees = open(nom_fichier,"r")
        # lecture de la première ligne
        ligne = fdonnees.readline() 
        l = ligne.split() # on récupère les valeurs dans une liste
        nb_jobs : int = int(l[0])
        nb_machines : int = int(l[1])
        liste_jobs : list[Job] = []
        # création des jobs
        for num in range(nb_jobs):
            ligne = fdonnees.readline() 
            l = ligne.split()
            # on transforme la suite de chaînes de caractères représentant
            # les durées des opérations en une liste d'entiers
            l_op = [int(d_op) for d_op in l]
            # puis on crée le job
            job = Job(num, l_op)
            liste_jobs.append(job)
        # fermeture du fichier
        fdonnees.close()
        return Flowshop(liste_jobs, nb_machines)
    
    def afficher_flowshop(self):
        print("nb_machines : " + str(self.nb_machines))
        Cmax = 0
        for job in self.liste_jobs:
            job.afficher_job()
            if job.debut_operation[self.nb_machines - 1] != None and Cmax < job.debut_operation[self.nb_machines - 1] + job.temps_machines[self.nb_machines - 1]:
                Cmax = job.debut_operation[self.nb_machines - 1] + job.temps_machines[self.nb_machines - 1]
        print("Cmax : " + str(Cmax))

    def liste_NEH(self):
        ''' Renvoie la liste obtenue par l'algorithme NEH pour le problème défini
            par 'flow_shop'.
        '''
        seq_NEH = [] # liste dans l'ordre NEH
        temps_tot_jobs = [[sum(job.temps_machines), job] for job in self.liste_jobs]
        temps_tot_jobs.sort(key=lambda j: j[0], reverse = True)
        seq_NEH.append(temps_tot_jobs[0][1])
        print("dGQGEZQG")
        for j in temps_tot_jobs:
            j[1].afficher_job()
        for i in range(1,len(temps_tot_jobs)):
            seq_NEH_Avant = seq_NEH.copy()
            seq_NEH.append(temps_tot_jobs[i][1])
            ordo = Ordonnancement(self.nb_machines, seq_NEH)
            ordoMin = ordo.date_dispo[self.nb_machines-1]
            for j in range(i):
                seq_j = seq_NEH_Avant.copy()
                seq_j.insert(j, temps_tot_jobs[i][1])
                ordo = Ordonnancement(self.nb_machines, seq_j)
                if ordoMin > ordo.date_dispo[self.nb_machines-1]:
                    ordoMin = ordo.date_dispo[self.nb_machines-1]
                    seq_NEH = seq_j
        Ordonnancement(self.nb_machines, seq_NEH).afficher_ordo()
        return seq_NEH