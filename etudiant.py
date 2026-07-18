
def rechercher_etudiant(matricule):
   
    if matricule not in etudiants:
        print(f"Erreur : Aucun étudiant avec le matricule '{matricule}' trouvé.")
        return None
    
    infos = etudiants[matricule]
    
    print("\n" + "="*50)
    print(f"Résultat de la recherche - Matricule: {matricule}")
    print("="*50)
    print(f"Nom        : {infos['nom']}")
    print(f"Prénom     : {infos['prenom']}")
    print(f"Âge        : {infos['age']}")
    print(f"Classe     : {infos['classe']}")
    print(f"Moyenne    : {infos['moyenne']}")
    print("="*50 + "\n")
    
    return infos
# dictionnaire d'etudiants

etudiants = {
    "MAT001": {
        "nom": "Fall",
        "prenom": "Assane",
        "age": 23,
        "classe": "L3",
        "moyenne": 15.5
    }
}


def ajouter_etudiant(matricule, nom, prenom, age, classe, moyenne):
   
    if matricule in etudiants:
        print(f"Erreur : Un étudiant avec le matricule '{matricule}' existe déjà.")
        return False
    
    etudiants[matricule] = {
        "nom": nom,
        "prenom": prenom,
        "age": age,
        "classe": classe,
        "moyenne": moyenne
    }
    print(f"Étudiant '{prenom} {nom}' ajouté avec succès (matricule: {matricule}).")
    return True


def afficher_tous_etudiants():
   
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return
    
    print("\n" + "="*80)
    print(f"{'Matricule':<12} {'Nom':<15} {'Prénom':<15} {'Âge':<5} {'Classe':<8} {'Moyenne':<8}")
    print("="*80)
    
    for matricule, infos in etudiants.items():
        print(f"{matricule:<12} {infos['nom']:<15} {infos['prenom']:<15} {infos['age']:<5} {infos['classe']:<8} {infos['moyenne']:<8}")
    
    print("="*80 + "\n")


def modifier_etudiant(matricule, **kwargs):
   
    if matricule not in etudiants:
        print(f"Erreur : Aucun étudiant avec le matricule '{matricule}' trouvé.")
        return False
    
    champs_valides = {"nom", "prenom", "age", "classe", "moyenne"}
    
    for cle, valeur in kwargs.items():
        if cle not in champs_valides:
            print(f"Avertissement : Le champ '{cle}' n'existe pas.")
            continue
        
        etudiants[matricule][cle] = valeur
    
    print(f"Étudiant avec le matricule '{matricule}' modifié avec succès.")
    return True


def supprimer_etudiant(matricule):
  
    if matricule not in etudiants:
        print(f"Erreur : Aucun étudiant avec le matricule '{matricule}' trouvé.")
        return False
    
    nom_prenom = f"{etudiants[matricule]['prenom']} {etudiants[matricule]['nom']}"
    del etudiants[matricule]
    print(f"Étudiant '{nom_prenom}' supprimé avec succès.")
    return True


def afficher_statistiques():
 
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return
    
    moyennes = [infos['moyenne'] for infos in etudiants.values()]
    
    nombre_total = len(etudiants)
    moyenne_generale = sum(moyennes) / nombre_total
    meilleure_moyenne = max(moyennes)
    plus_faible_moyenne = min(moyennes)
    
    # Afficher les statistiques
    print("\n" + "="*50)
    print("     STATISTIQUES DES ÉTUDIANTS".center(50))
    print("="*50)
    print(f"Nombre total d'étudiants    : {nombre_total}")
    print(f"Moyenne générale            : {moyenne_generale:.2f}")
    print(f"Meilleure moyenne           : {meilleure_moyenne:.2f}")
    print(f"Plus faible moyenne         : {plus_faible_moyenne:.2f}")
    print("="*50 + "\n")
