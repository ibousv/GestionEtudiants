# menu principal



from etudiant import (
    ajouter_etudiant,
    afficher_tous_etudiants,
    modifier_etudiant,
    supprimer_etudiant,
    afficher_statistiques
)


def afficher_menu():
   
    print("\n" + "="*50)
    print("     GESTION DES ÉTUDIANTS".center(50))
    print("="*50)
    print("1. Ajouter un étudiant")
    print("2. Afficher tous les étudiants")
    print("3. Modifier un étudiant")
    print("4. Supprimer un étudiant")
    print("5. Quitter")
    print("="*50)


def option_ajouter():
   
    print("\n--- Ajouter un étudiant ---")
    matricule = input("Matricule: ")
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    age = int(input("Âge: "))
    classe = input("Classe: ")
    moyenne = float(input("Moyenne: "))
    
    ajouter_etudiant(matricule, nom, prenom, age, classe, moyenne)


def option_afficher():
   
    print("\n--- Liste des étudiants ---")
    afficher_tous_etudiants()


def option_modifier():
   
    print("\n--- Modifier un étudiant ---")
    afficher_tous_etudiants()
    
    matricule = input("Matricule de l'étudiant à modifier: ")
    
    print("\nLaissez vide pour ne pas modifier un champ.\n")
    
    modifications = {}
    
    nom = input("Nouveau nom (vide pour ignorer): ")
    if nom:
        modifications['nom'] = nom
    
    prenom = input("Nouveau prénom (vide pour ignorer): ")
    if prenom:
        modifications['prenom'] = prenom
    
    age = input("Nouvel âge (vide pour ignorer): ")
    if age:
        modifications['age'] = int(age)
    
    classe = input("Nouvelle classe (vide pour ignorer): ")
    if classe:
        modifications['classe'] = classe
    
    moyenne = input("Nouvelle moyenne (vide pour ignorer): ")
    if moyenne:
        modifications['moyenne'] = float(moyenne)
    
    if modifications:
        modifier_etudiant(matricule, **modifications)
    else:
        print("Aucune modification effectuée.")


def option_supprimer():
    
    print("\n--- Supprimer un étudiant ---")
    afficher_tous_etudiants()
    
    matricule = input("Matricule de l'étudiant à supprimer: ")
    supprimer_etudiant(matricule)


def main():
   
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-5): ")
        
        if choix == "1":
            option_ajouter()
        elif choix == "2":
            option_afficher()
        elif choix == "3":
            option_modifier()
        elif choix == "4":
            option_supprimer()
        elif choix == "5":
            print("\nMerci d'avoir utilisé le programme de gestion des étudiants.")
            print("Au revoir !")
            break
        else:
            print("Option invalide.")



if __name__ == "__main__":
    main()
