
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
