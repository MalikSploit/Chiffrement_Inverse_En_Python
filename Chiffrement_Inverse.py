# -*- coding: utf-8 -*-
"""
Malik Makkes
"""

def Chiffrement(message): #Notre fonction de chiffrement
  Cipher = '' 
  i = len(message) - 1 #Parcours de la fin vers le début.
  while i >= 0: #Continuer tant que i >=0
    Cipher = Cipher + message[i] 
    i = i - 1
  return Cipher


message1 = 'Malik' #jeu d'essai 1 à chiffrer
message2 = 'M4l1k'#jeu d'essai 2 à chiffrer
message3 = 'Un t3st 4v3ec pl3!in de ch@rchteres sp3c !aux'#jeu d'essai 3 à chiffrer
msg_chiffré1 = Chiffrement(message1) #On chiffre notre message1
msg_chiffré2 = Chiffrement(message2) #On chiffre notre message2
msg_chiffré3 = Chiffrement(message3) #On chiffre notre message3
msg_déchiffré1 = Chiffrement(msg_chiffré1) #On dechiffre msg_chiffré 1
msg_déchiffré2 = Chiffrement(msg_chiffré2) #On dechiffre msg_chiffré 2
msg_déchiffré3 = Chiffrement(msg_chiffré3) #On dechiffre msg_chiffré 3
print("Le message chiffré 1 est : \n", msg_chiffré1 ) #On affiche msg_chiffré 1
print("Le message déchiffré 1 est : \n", msg_déchiffré1) #On affiche msg_déchiffré 1
print("Le message chiffré 2 est : \n", msg_chiffré2 ) #On affiche msg_chiffré 2
print("Le message déchiffré 2 est : \n", msg_déchiffré2) #On affiche msg_déchiffré 2
print("Le message chiffré 3 est : \n", msg_chiffré3 ) #On affiche msg_chiffré 3
print("Le message déchiffré 3 est : \n", msg_déchiffré3) #On affiche msg_déchiffré 3

