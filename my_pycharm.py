"""
Tutoriel PyCharm : https://youtu.be/hc50ALh_x5g?t=5739

Pour la présaisie des données : kite pour pycharm, sublimetext...
lien : https://www.kite.com/

PyCharm est un IDE (environnement de développement intégré)

Pour accéder directement aux packages installés -> aller en bas à droite et cliquer sur 'Python 3.9' puis sélectionner
'Interpreter Settings'

Installer un assistant de présentation pour obtenir des touches raccourcis :
-> Aller sur 'Interpreter Settings'
-> Sélectionner Plugins
-> Sélectionner MarketPlace
-> Sélectionner Presentation Assistant puis Installer

Changer le thème :
-> Aller sur 'Interpreter Settings'
-> Sélectionner Appearance & Behavior puis Appearance et Theme : Darcula
Puis, sélectionner la couleur des écritures :
-> Aller sur 'Interpreter Settings'
-> Editor -> Color Scheme

Instructions à faire (TODO) :
-> appuyer sur la touche CTRL + la touche /
-> saisir 'TODO:'
-> sélectionner l'icône en bas de la fenêtre où il est inscrit TODO pour accéder aux endroits où on a des instructions à
faire

Appel d'une fonction d'un autre fichier :
-> Saisir le nom de la fonction
-> Aller sur le point d'exclamation rouge et sélectionner 'Import this name' et sélectionner la fonction précédée du nom
du fichier où elle se situe (donc idem pour les modules car un module est un fichier)

Trouver les fichiers qui font appel à la fonction :
-> Se positionner sur le nom de l'en-tête de la fonction
-> Aller dans le menu Edit -> Find Usages -> Find Usages

Terminal :
Avec le Terminal situé en bas de la fenêtre, on peut exécuter d'autres programmes que celui ouvert, il suffit d'ajouter
un autre onglet 'Local', se situer sur un fichier .py et saisir l'instruction suivante : python nomFichier.py

Raccourcis de clavier :
-> Afficher la fenêtre à gauche 'Project' : ALT + 1 (Projet)
-> Afficher le terminal en bas de la fenêtre : ALT + 4 (Run)
-> Afficher les variables et fonctions déclarées à gauche de la fenêtre : ALT + 7 (Structure)
-> Récupérer les fonctions récurrentes puis ACTIVATION automatique de ces fonctions par la suite : CTRL + ESPACE
-> Récupérer les méthodes spéciales telles que le super constructeur : aller dans la classe puis touches CTRL + O
-> Coller : CTRL + V
-> Coller un des éléments conservés dans le presse-papier : CTRL + SHIFT + V
-> Rechercher dans un fichier : CTRL + F
-> Rechercher dans tous les fichiers : CTRL + SHIFT + F
-> Rechercher et remplacer : CTRL + R
-> Rechercher et remplacer dans tous les fichiers : CTRL + SHIFT + R
-> Sélection d'un mot à plusieurs mots jusqu'à sélectionner la ligne voire un paragraphe et plus : CTRL + W
-> Réduire la sélection faite avec CTRL + W : appuyer sur les touches CTRL + SHIFT + W
-> Mettre en majuscule/minuscule : CTRL + SHIFT + U
-> Dupliquer l'instruction à peine saisie : CTRL + D (duplicate)
-> Supprimer une ligne : CTRL + Y
-> Déplacer une ligne : CTRL + SHIFT + touches directionnelles
-> Ajouter une ligne au-dessus de la ligne sélectionnée : CTRL + ALT + ENTREE
-> Mettre fin à l'erreur affichée sur la ligne en cours de saisie : CTRL + SHIFT + ENTREE
-> Ouvrir une fenêtre la liste des fichiers récents : CTRL + E
-> Ouvrir une fenêtre avec un historique des derniers travaux effectués sur les fichiers récents : CTRL + SHIFT + E
-> Recherches diverses et aller d'un fichier à un autre fichier dans le même projet : SHIFT + SHIFT
-> Renommer un fichier : sélectionner le fichier puis : SHIFT + F6
-> GIT & Github : https://youtu.be/hc50ALh_x5g?t=7369 :
    . aller dans le menu VCS -> Enable Version Controle Integration... et appuyer sur OK : les fichiers sont en rouge
    . pour faire un commit, sélectionner les fichiers concernés dans la fenêtre de gauche 'projects', puis clique droit
    et aller sur Git puis Add : les fichiers sont en vert
    . quand les fichiers sont modifiés ils sont en bleu

Éditeur : Laurent REYNAUD
Date : 10-02-2021
"""

name = "John"
name2 = "GERALD"


def hello():
    print(f"Hello M. {name} {name2} !")


"""Autre possibilité pour exécuter le programme que d'appuyer sur l'icône de la flêche verte en haut à droite, en
saisissant uniquement 'main' puis touche TAB"""
if __name__ == '__main__':
    print('Hello World!!!')
    print(f"Name : {name}")
    print('PYCHARM IS AWESOME!')
    hello()
