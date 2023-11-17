import mysql.connector

def connecter_base_donnees():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bibliotheque"
    )

def creer_table_livres():
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS livres (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titre VARCHAR(255) NOT NULL,
            auteur VARCHAR(255) NOT NULL,
            isbn VARCHAR(20) NOT NULL,
            genre VARCHAR(50) NOT NULL
        )
    '''

    cursor.execute(query)
    db.close()

def enregistrer_livre(titre, auteur, isbn, genre):
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = "INSERT INTO livres (titre, auteur, isbn, genre) VALUES (%s, %s, %s, %s)"
    values = (titre, auteur, isbn, genre)

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

def recuperer_livres():
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = "SELECT * FROM livres"
    cursor.execute(query)

    livres = cursor.fetchall()
    db.close()

    return livres

def modifier_livre(id_livre, nouveau_titre, nouveau_auteur, nouveau_isbn, nouveau_genre):
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = "UPDATE livres SET titre=%s, auteur=%s, isbn=%s, genre=%s WHERE id=%s"
    values = (nouveau_titre, nouveau_auteur, nouveau_isbn, nouveau_genre, id_livre)

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

def supprimer_livre(id_livre):
    db = connecter_base_donnees()
    cursor = db.cursor()

    query = "DELETE FROM livres WHERE id=%s"
    values = (id_livre,)

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
