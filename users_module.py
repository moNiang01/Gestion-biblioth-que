import mysql.connector

def connecter_base_donnees():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bibliotheque"
    )

def creer_table_utilisateurs():
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100) NOT NULL,
            prenom VARCHAR(100) NOT NULL,
            categorie VARCHAR(50) NOT NULL
        )
    '''

    cursor.execute(query)
    db.close()

def enregistrer_utilisateur(nom, prenom, categorie):
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = "INSERT INTO utilisateurs (nom, prenom, categorie) VALUES (%s, %s, %s)"
    values = (nom, prenom, categorie)

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

def recuperer_utilisateurs():
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = "SELECT * FROM utilisateurs"
    cursor.execute(query)

    utilisateurs = cursor.fetchall()
    db.close()

    return utilisateurs

def modifier_utilisateur(id_utilisateur, nouveau_nom, nouveau_prenom, nouvelle_categorie):
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = "UPDATE utilisateurs SET nom=%s, prenom=%s, categorie=%s WHERE id=%s"
    values = (nouveau_nom, nouveau_prenom, nouvelle_categorie, id_utilisateur)

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

def supprimer_utilisateur(id_utilisateur):
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = "DELETE FROM utilisateurs WHERE id=%s"
    values = (id_utilisateur,)

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
