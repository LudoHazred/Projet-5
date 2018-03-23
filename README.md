# PROJET 5 OC
GROS Ludovic

L'id�e de *Pur Beurre* est de cr�er un programme interagissant avec la base Open Food Facts.
Ce programme permet de r�cup�rer les aliments de la base de donn�e d'Open Food Facts, les comparer et proposer � l'utilisateur un substitut plus sain � l'aliment qui lui fait envie.

## Description

Sur le terminal, l'utilisateur se voit proposer plusieurs choix :
* 1-Quel aliment souhaitez-vous remplacer ?
* 2-Retrouver les aliments substitu�s.

Si l'utilisateur s�lectionne 1. Le programme pose les questions suivantes � l'utilisateur et ce dernier s�lectionne les r�ponses :
* S�lectionnez la cat�gorie. [Plusieurs propositions associ�es � un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entr�e]
* S�lectionnez l'aliment. [Plusieurs propositions associ�es � un chiffre. L'utilisateur entre le chiffre correspondant � l'aliment choisi et appuie sur entr�e]
* Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas �ch�ant) et un lien vers la page d'Open Food Facts concernant cet aliment.
* L'utilisateur a alors la possibilit� d'enregistrer le r�sultat dans la base de donn�es.

Si l'utilisateur s�lectionne 2, le programme affiche le r�sultat des recherchez d�j� effectu�s permettant ainsi d'�viter de refaire une recherche dans la base de donn�e.

## Fonctionnalit�s
* Recherche d'aliments dans la base Open Food Facts.
* Le programme propose substitut, description, magasin ou l'acheter et un lien vers la page d'Open Food Facts.
* L'utilisateur interagit avec le programme dans le terminal (potentiellement une interface graphique).
* Si l'utilisateur entre un caract�re qui n'est pas un chiffre, le programme lui r�p�te la question.
* La recherche s'effectue sur une base MySQL.