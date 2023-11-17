from tkinter import *
from livres_module import enregistrer_livre, recuperer_livres, creer_table_livres, modifier_livre, supprimer_livre
from users_module import enregistrer_utilisateur, recuperer_utilisateurs, creer_table_utilisateurs, modifier_utilisateur, supprimer_utilisateur

# Fonctions pour la gestion des livres
def enregistrer_livre_interface():
    auteur = entry_auteur.get()
    isbn = entry_isbn.get()
    titre = entry_titre.get()
    genre = entry_genre.get()

    if enregistrer_livre(titre, auteur, isbn, genre):
        label_resultat_livre.config(text="Livre enregistré avec succès!")
        afficher_livres()
    else:
        label_resultat_livre.config(text="Erreur lors de l'enregistrement du livre.")

def afficher_livres():
    liste_livres = recuperer_livres()
    texte_livres.delete(1.0, END)  # Efface le contenu précédent

    for livre in liste_livres:
        texte_livres.insert(END, f"{livre[0]}. {livre[1]} - ISBN: {livre[3]}, Genre: {livre[4]}\n")

def modifier_livre_interface():
    id_livre = int(entry_id_modif.get())
    nouveau_titre = entry_nouveau_titre.get()
    nouveau_auteur = entry_nouveau_auteur.get()
    nouveau_isbn = entry_nouveau_isbn.get()
    nouveau_genre = entry_nouveau_genre.get()

    if modifier_livre(id_livre, nouveau_titre, nouveau_auteur, nouveau_isbn, nouveau_genre):
        label_resultat_modif.config(text="Livre modifié avec succès!")
        afficher_livres()
    else:
        label_resultat_modif.config(text="Erreur lors de la modification du livre.")

def supprimer_livre_interface():
    id_livre = int(entry_id_suppr.get())

    if supprimer_livre(id_livre):
        label_resultat_suppr.config(text="Livre supprimé avec succès!")
        afficher_livres()
    else:
        label_resultat_suppr.config(text="Erreur lors de la suppression du livre.")

# Fonctions pour la gestion des utilisateurs
def enregistrer_utilisateur_interface():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    categorie = entry_categorie.get()

    if enregistrer_utilisateur(nom, prenom, categorie):
        label_resultat_utilisateur.config(text="Utilisateur enregistré avec succès!")
        afficher_utilisateurs()
    else:
        label_resultat_utilisateur.config(text="Erreur lors de l'enregistrement de l'utilisateur.")

def afficher_utilisateurs():
    liste_utilisateurs = recuperer_utilisateurs()
    texte_utilisateurs.delete(1.0, END)  # Efface le contenu précédent

    for utilisateur in liste_utilisateurs:
        texte_utilisateurs.insert(END, f"{utilisateur[0]}. {utilisateur[1]} {utilisateur[2]} - Catégorie: {utilisateur[3]}\n")

def modifier_utilisateur_interface():
    id_utilisateur = int(entry_id_modif_utilisateur.get())
    nouveau_nom = entry_nouveau_nom.get()
    nouveau_prenom = entry_nouveau_prenom.get()
    nouvelle_categorie = entry_nouvelle_categorie.get()

    if modifier_utilisateur(id_utilisateur, nouveau_nom, nouveau_prenom, nouvelle_categorie):
        label_resultat_modif_utilisateur.config(text="Utilisateur modifié avec succès!")
        afficher_utilisateurs()
    else:
        label_resultat_modif_utilisateur.config(text="Erreur lors de la modification de l'utilisateur.")

def supprimer_utilisateur_interface():
    id_utilisateur = int(entry_id_suppr_utilisateur.get())

    if supprimer_utilisateur(id_utilisateur):
        label_resultat_suppr_utilisateur.config(text="Utilisateur supprimé avec succès!")
        afficher_utilisateurs()
    else:
        label_resultat_suppr_utilisateur.config(text="Erreur lors de la suppression de l'utilisateur.")

# Crée les tables si elles n'existent pas encore
creer_table_livres()
creer_table_utilisateurs()

root = Tk()
root.title("Gestion de Bibliothèque")

# Interface pour la gestion des livres
label_auteur = Label(root, text="Auteur:")
label_isbn = Label(root, text="ISBN:")
label_titre = Label(root, text="Titre:")
label_genre = Label(root, text="Genre:")
label_resultat_livre = Label(root, text="")
texte_livres = Text(root, height=10, width=50)

entry_auteur = Entry(root)
entry_isbn = Entry(root)
entry_titre = Entry(root)
entry_genre = Entry(root)

bouton_enregistrer_livre = Button(root, text="Enregistrer Livre", command=enregistrer_livre_interface)

label_id_modif = Label(root, text="ID du livre à modifier:")
label_nouveau_titre = Label(root, text="Nouveau titre:")
label_nouveau_auteur = Label(root, text="Nouvel auteur:")
label_nouveau_isbn = Label(root, text="Nouvel ISBN:")
label_nouveau_genre = Label(root, text="Nouveau genre:")
label_resultat_modif = Label(root, text="")

entry_id_modif = Entry(root)
entry_nouveau_titre = Entry(root)
entry_nouveau_auteur = Entry(root)
entry_nouveau_isbn = Entry(root)
entry_nouveau_genre = Entry(root)

bouton_modifier_livre = Button(root, text="Modifier Livre", command=modifier_livre_interface)

label_id_suppr = Label(root, text="ID du livre à supprimer:")
label_resultat_suppr = Label(root, text="")

entry_id_suppr = Entry(root)

bouton_supprimer_livre = Button(root, text="Supprimer Livre", command=supprimer_livre_interface)

# Interface pour la gestion des utilisateurs
label_nom = Label(root, text="Nom:")
label_prenom = Label(root, text="Prénom:")
label_categorie = Label(root, text="Catégorie:")
label_resultat_utilisateur = Label(root, text="")
texte_utilisateurs = Text(root, height=10, width=50)

entry_nom = Entry(root)
entry_prenom = Entry(root)
entry_categorie = Entry(root)

bouton_enregistrer_utilisateur = Button(root, text="Enregistrer Utilisateur", command=enregistrer_utilisateur_interface)

label_id_modif_utilisateur = Label(root, text="ID de l'utilisateur à modifier:")
label_nouveau_nom = Label(root, text="Nouveau nom:")
label_nouveau_prenom = Label(root, text="Nouveau prénom:")
label_nouvelle_categorie = Label(root, text="Nouvelle catégorie:")
label_resultat_modif_utilisateur = Label(root, text="")

entry_id_modif_utilisateur = Entry(root)
entry_nouveau_nom = Entry(root)
entry_nouveau_prenom = Entry(root)
entry_nouvelle_categorie = Entry(root)

bouton_modifier_utilisateur = Button(root, text="Modifier Utilisateur", command=modifier_utilisateur_interface)

label_id_suppr_utilisateur = Label(root, text="ID de l'utilisateur à supprimer:")
label_resultat_suppr_utilisateur = Label(root, text="")

entry_id_suppr_utilisateur = Entry(root)

bouton_supprimer_utilisateur = Button(root, text="Supprimer Utilisateur", command=supprimer_utilisateur_interface)

# Positionnement des éléments dans la fenêtre
label_auteur.grid(row=0, column=0, padx=10, pady=10)
entry_auteur.grid(row=0, column=1, padx=10, pady=10)
label_isbn.grid(row=1, column=0, padx=10, pady=10)
entry_isbn.grid(row=1, column=1, padx=10, pady=10)
label_titre.grid(row=2, column=0, padx=10, pady=10)
entry_titre.grid(row=2, column=1, padx=10, pady=10)
label_genre.grid(row=3, column=0, padx=10, pady=10)
entry_genre.grid(row=3, column=1, padx=10, pady=10)
bouton_enregistrer_livre.grid(row=4, column=0, columnspan=2, pady=10)
label_resultat_livre.grid(row=5, column=0, columnspan=2)
texte_livres.grid(row=6, column=0, columnspan=2, pady=10)

label_id_modif.grid(row=7, column=0, padx=10, pady=10)
entry_id_modif.grid(row=7, column=1, padx=10, pady=10)
label_nouveau_titre.grid(row=8, column=0, padx=10, pady=10)
entry_nouveau_titre.grid(row=8, column=1, padx=10, pady=10)
label_nouveau_auteur.grid(row=9, column=0, padx=10, pady=10)
entry_nouveau_auteur.grid(row=9, column=1, padx=10, pady=10)
label_nouveau_isbn.grid(row=10, column=0, padx=10, pady=10)
entry_nouveau_isbn.grid(row=10, column=1, padx=10, pady=10)
label_nouveau_genre.grid(row=11, column=0, padx=10, pady=10)
entry_nouveau_genre.grid(row=11, column=1, padx=10, pady=10)
bouton_modifier_livre.grid(row=12, column=0, columnspan=2, pady=10)
label_resultat_modif.grid(row=13, column=0, columnspan=2)

label_id_suppr.grid(row=14, column=0, padx=10, pady=10)
entry_id_suppr.grid(row=14, column=1, padx=10, pady=10)
bouton_supprimer_livre.grid(row=15, column=0, columnspan=2, pady=10)
label_resultat_suppr.grid(row=16, column=0, columnspan=2)

label_nom.grid(row=0, column=2, padx=10, pady=10)
entry_nom.grid(row=0, column=3, padx=10, pady=10)
label_prenom.grid(row=1, column=2, padx=10, pady=10)
entry_prenom.grid(row=1, column=3, padx=10, pady=10)
label_categorie.grid(row=2, column=2, padx=10, pady=10)
entry_categorie.grid(row=2, column=3, padx=10, pady=10)
bouton_enregistrer_utilisateur.grid(row=3, column=2, columnspan=2, pady=10)
label_resultat_utilisateur.grid(row=4, column=2, columnspan=2)
texte_utilisateurs.grid(row=5, column=2, columnspan=2, pady=10)

label_id_modif_utilisateur.grid(row=6, column=2, padx=10, pady=10)
entry_id_modif_utilisateur.grid(row=6, column=3, padx=10, pady=10)
label_nouveau_nom.grid(row=7, column=2, padx=10, pady=10)
entry_nouveau_nom.grid(row=7, column=3, padx=10, pady=10)
label_nouveau_prenom.grid(row=8, column=2, padx=10, pady=10)
entry_nouveau_prenom.grid(row=8, column=3, padx=10, pady=10)
label_nouvelle_categorie.grid(row=9,column=2, padx=10, pady=10)
entry_nouvelle_categorie.grid(row=9, column=3, padx=10, pady=10)
bouton_modifier_utilisateur.grid(row=10, column=2, columnspan=2, pady=10)
label_resultat_modif_utilisateur.grid(row=11, column=2, columnspan=2)

label_id_suppr_utilisateur.grid(row=12, column=2, padx=10, pady=10)
entry_id_suppr_utilisateur.grid(row=12, column=3, padx=10, pady=10)
bouton_supprimer_utilisateur.grid(row=13, column=2, columnspan=2, pady=10)
label_resultat_suppr_utilisateur.grid(row=14, column=2, columnspan=2)

# Affiche les livres et utilisateurs au lancement de l'application
afficher_livres()
afficher_utilisateurs()

# ...

from prets_retours import creer_table_prets, enregistrer_emprunt, recuperer_prets_en_cours, enregistrer_retour, verifier_retards

# ...

# Crée la table des prêts si elle n'existe pas encore
creer_table_prets()

# ...

# Fonctions pour la gestion des prêts et retours
def enregistrer_emprunt_interface():
    id_livre_emprunt = int(entry_id_livre_emprunt.get())
    id_utilisateur_emprunt = int(entry_id_utilisateur_emprunt.get())

    if enregistrer_emprunt(id_livre_emprunt, id_utilisateur_emprunt):
        label_resultat_emprunt.config(text="Emprunt enregistré avec succès!")
        afficher_prets_en_cours()
    else:
        label_resultat_emprunt.config(text="Erreur lors de l'enregistrement de l'emprunt.")

def enregistrer_retour_interface():
    id_pret_retour = int(entry_id_pret_retour.get())

    if enregistrer_retour(id_pret_retour):
        label_resultat_retour.config(text="Retour enregistré avec succès!")
        afficher_prets_en_cours()
        verifier_et_afficher_retards()
    else:
        label_resultat_retour.config(text="Erreur lors de l'enregistrement du retour.")

def verifier_et_afficher_retards():
    retards = verifier_retards()
    texte_retards.delete(1.0, END)

    if retards:
        texte_retards.insert(END, "Livres en retard :\n")
        for retard in retards:
            texte_retards.insert(END, f"ID Prêt: {retard[0]}, Livre: {retard[1]}, Emprunteur: {retard[2]} {retard[3]}, Date retour prévue: {retard[4]}\n")
    else:
        texte_retards.insert(END, "Aucun livre en retard.\n")

# ...

# Interface pour la gestion des prêts et retours
label_id_livre_emprunt = Label(root, text="ID du livre emprunté:")
label_id_utilisateur_emprunt = Label(root, text="ID de l'utilisateur emprunteur:")
label_resultat_emprunt = Label(root, text="")

entry_id_livre_emprunt = Entry(root)
entry_id_utilisateur_emprunt = Entry(root)

bouton_enregistrer_emprunt = Button(root, text="Enregistrer Emprunt", command=enregistrer_emprunt_interface)

label_id_pret_retour = Label(root, text="ID du prêt à retourner:")
label_resultat_retour = Label(root, text="")

entry_id_pret_retour = Entry(root)

bouton_enregistrer_retour = Button(root, text="Enregistrer Retour", command=enregistrer_retour_interface)

texte_retards = Text(root, height=10, width=50)

# ...

# Positionnement des éléments dans la fenêtres
label_id_livre_emprunt.grid(row=0, column=4, padx=10, pady=10)
entry_id_livre_emprunt.grid(row=0, column=5, padx=10, pady=10)
label_id_utilisateur_emprunt.grid(row=1, column=4, padx=10, pady=10)
entry_id_utilisateur_emprunt.grid(row=1, column=5, padx=10, pady=10)
bouton_enregistrer_emprunt.grid(row=2, column=4, columnspan=2, pady=10)
label_resultat_emprunt.grid(row=3, column=4, columnspan=2)

label_id_pret_retour.grid(row=4, column=4, padx=10, pady=10)
entry_id_pret_retour.grid(row=4, column=5, padx=10, pady=10)
bouton_enregistrer_retour.grid(row=5, column=4, columnspan=2, pady=10)
label_resultat_retour.grid(row=6, column=4, columnspan=2)

texte_retards.grid(row=7, column=4, columnspan=2, pady=10)

# ...

# Fonction pour afficher les prêts en cours
def afficher_prets_en_cours():
    prets_en_cours = recuperer_prets_en_cours()
    texte_prets_en_cours.delete(1.0, END)

    if prets_en_cours:
        texte_prets_en_cours.insert(END, "Prêts en cours :\n")
        for pret in prets_en_cours:
            texte_prets_en_cours.insert(END, f"ID Prêt: {pret[0]}, Livre: {pret[1]}, Emprunteur: {pret[2]} {pret[3]}, "
                                             f"Date prêt: {pret[4]}, Date retour prévue: {pret[5]}\n")
    else:
        texte_prets_en_cours.insert(END, "Aucun prêt en cours.\n")

# ...

# Interface pour la gestion des prêts et retours (suite)
texte_prets_en_cours = Text(root, height=10, width=50)

# ...

# Positionnement des éléments dans la fenêtre
texte_prets_en_cours.grid(row=8, column=4, columnspan=2, pady=10)

# Affiche les prêts en cours au lancement de l'application
afficher_prets_en_cours()

# ...

root.mainloop()


