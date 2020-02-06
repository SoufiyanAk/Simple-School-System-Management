##############################
#Script : Simple School System Administration (Without DataBase)
#Programmed by : EBF LEARN - COMIX
#Version : V0.001
#05/2019
#Youtube : https://www.youtube.com/c/ebflearn
##############################
 
#Class pour regrouper les fonctions (Parametre)
class Administration() :
    def __init__ (self) :
        self.i = 0
        self.aj_et = []
        self.exam = []
    #Parametre pour ajouter un groupe des etudiants
    def aj_etudiant (self) :
            N = int(input("Entrer le nombre d'etudiant a saisie : "))
            for self.i in range (0,N) :
                ID = int(input("Entrer id etudiant : "))
                self.aj_et.append (ID)
                Nom = str(input("Entrer le nom d'etudiant : "))
                self.aj_et.append(Nom)
                Class = str(input("Entrer le class d'etudiant : "))
                self.aj_et.append(Class)
                print (self.aj_et)
    #Parametre pour rechercher des etudiant Si il existe il affiche ses details
    def Search(self) :
        sr = int(input("Entrer ID d'etudiant :"))
        if sr in self.aj_et :
            print ("EXISTE")
            self.a = self.aj_et.index(sr)
            self.b = self.a + 3
            print(self.aj_et[self.a: self.b])   
        else :
            print ("NOT EXISTE")
    #Parametre pour editer les etudiants
    def edit(self) :
        ed = int(input("Entrer ID d'etudiant :"))   #1
        a = self.aj_et.index(ed) #0
        g = a + 3 #3
        self.aj_et[a + 1] = input("entrer un nouveau nom :")
        self.aj_et[a + 2] = input("entrer un nouveau class :")
        print (self.aj_et[a:g])
    #Parametre pour supprimer un etudiant
    def rm(self) :
        ef = int(input("Entrer ID d'etudiant : "))
        c = self.aj_et.index(ef)
        self.aj_et.pop(c + 0)
        self.aj_et.pop(c + 0)
        self.aj_et.pop(c + 0)
        print (self.aj_et)
    #Saisir les notes
    def class99(self) :
        idU = int(input("Entrer ID d'etudiant : "))
        self.exam.append(idU)
        ex1 = float(input("ENtrer la note d'examin : "))
        self.exam.append(ex1)
        ex2 = float(input("ENtrer la note d'examin : "))
        self.exam.append(ex2)
        ex3 = float(input("ENtrer la note d'examin : "))
        self.exam.append(ex3)
    #Calculer les notes
    def calc (self) :
        idc = 0
        idc = int(input("Entrer ID d'etudiant : ")) #1
        wa = self.exam.index(idc) #0
        wa = wa + 1 # 1
        ba = wa + 4
        print (sum(self.exam[wa:ba])/3)
#Nomer l'object
Admin = Administration()
#Panel
print ("-| EBF SCHOOL |-")
print (">>>>>>>>>>>> Administration <<<<<<<<<<<<<")
print ("1 - Ajouter des etudiant")
print ("2 - chercher des etudiant")
print ("3 - editer des etudiant  ")
print ("4 - Supprimer un etudiant")
print ("5 - Saisir les notes des etudiant")
print ("6 - Calculer les notes des etudiant")
print ("7 - exit")
while True :
    choose = int(input("Entrer votre choix : "))
    if (choose == 1) :
        Admin.aj_etudiant ()
    elif (choose == 2) :
        Admin.Search ()
    elif (choose == 3) :
        Admin.edit()
    elif (choose == 4) :
        Admin.rm ()
    elif (choose == 5) :
        Admin.class99()
    elif (choose == 6) :
        Admin.calc()
    elif (choose == 7) :
        break
    else :
        print ("Veillez choisir un nombre entre 1 et 7")
