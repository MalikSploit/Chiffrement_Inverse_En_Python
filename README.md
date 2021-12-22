# Chiffrement Inverse En Python3
Programme de chiffrement et de déchiffrement inverse d'un message en python3.

# Explication du chiffrement inverse avec complexité O(n)
1. La première fonction s’appelle chiffrement, elle prend en paramètre un message qui sera 
chiffré, la fonction commencera par prendre un Cipher qui est une chaine de caractère vide. 

2. Par la suite on utilisera un entier i qui prendra la taille du message, après on parcours lettre par 
lettre notre message et on donne à Cipher = Cipher + l’indice de la dernière case du message 
ensuite on lui rajoute l’avant dernière case et ainsi de suite jusqu’à avoir parcouru tout le 
message de la fin vers le début. 

3. Enfin on testera notre programme avec nos jeux d’essais,
on appellera deux fois la fonctions chiffrement pour coder notre message, le premier appel à 
chiffrement sera donné à msg_chiffré ensuite le deuxième chiffrement sera donné à 
msg_déchiffré qui déchiffrera notre message chiffré a chaque jeu d’essai.


# Execution
`python3 Chiffrement_Inverse.py`
