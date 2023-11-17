import mysql.connector
from datetime import datetime, timedelta

# Fonction pour la connexion à la base de données
def connecter_base_donnees():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bibliotheque"
    )

# Fonction pour créer la table des prêts si elle n'existe pas
def creer_table_prets():
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS prets (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_livre INT,
            id_utilisateur INT,
            date_pret DATE,
            date_retour_prevue DATE,
            date_retour_effectif DATE,
            FOREIGN KEY (id_livre) REFERENCES livres(id),
            FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id)
        )
    '''

    cursor.execute(query)
    db.close()

# Fonction pour enregistrer un prêt
def enregistrer_emprunt(id_livre, id_utilisateur, duree_emprunt=14):
    db = connecter_base_donnees()
    cursor = db.cursor()

    date_pret = datetime.now().date()
    date_retour_prevue = date_pret + timedelta(days=duree_emprunt)

    query = '''
        INSERT INTO prets (id_livre, id_utilisateur, date_pret, date_retour_prevue)
        VALUES (%s, %s, %s, %s)
    '''
    values = (id_livre, id_utilisateur, date_pret, date_retour_prevue)

    try:
        cursor.execute(query, values)
        db.commit()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        db.close()
        print(f"Erreur: {str(e)}")
        return False

# Fonction pour récupérer les prêts en cours
def recuperer_prets_en_cours():
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = '''
        SELECT prets.id, livres.titre, utilisateurs.nom, utilisateurs.prenom, prets.date_pret, prets.date_retour_prevue
        FROM prets
        JOIN livres ON prets.id_livre = livres.id
        JOIN utilisateurs ON prets.id_utilisateur = utilisateurs.id
        WHERE prets.date_retour_effectif IS NULL
    '''

    cursor.execute(query)

    prets_en_cours = cursor.fetchall()
    db.close()

    return prets_en_cours

# Fonction pour enregistrer un retour
def enregistrer_retour(id_pret):
    db = connecter_base_donnees()
    cursor = db.cursor()

    date_retour_effectif = datetime.now().date()

    query = "UPDATE prets SET date_retour_effectif=%s WHERE id=%s"
    values = (date_retour_effectif, id_pret)

    try:
        cursor.execute(query, values)
        db.commit()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        db.close()
        print(f"Erreur: {str(e)}")
        return False

# Fonction pour vérifier les retards
def verifier_retards():
    db = connecter_base_donnees()
    cursor = db.cursor()

    date_actuelle = datetime.now().date()

    query = '''
        SELECT prets.id, livres.titre, utilisateurs.nom, utilisateurs.prenom, prets.date_retour_prevue
        FROM prets
        JOIN livres ON prets.id_livre = livres.id
        JOIN utilisateurs ON prets.id_utilisateur = utilisateurs.id
        WHERE prets.date_retour_effectif IS NULL
        AND prets.date_retour_prevue < %s
    '''

    cursor.execute(query, (date_actuelle,))

    retards = cursor.fetchall()
    db.close()

    return retards
