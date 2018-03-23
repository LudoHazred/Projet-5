# -*- coding: utf8 -*-

from tkinter import *

# fenetre racine de l'interface
window=Tk ()

#label de bienvenue
label_field = Label(window, text="Bienvenue sur le programme Pur Beurre")

# affiche le label dans la fenêtre
label_field.pack()

# Bouton pour quitter
button1 = Button(window, text="Quitter", command = window.destroy)
button1.pack(side=BOTTOM)

window.mainloop()