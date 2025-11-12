import string  # On importe le module string pour accéder aux caractères imprimables

def chiffre_de_cesar(message, decalage):
    
    
    
    alphabet = string.printable

    
    message_chiffre = ""

    
    for char in message:
        if char in alphabet:
            
            index = alphabet.index(char)
           
            index_chiffre = (index + decalage) % len(alphabet)
            
            message_chiffre += alphabet[index_chiffre]
        else:
        
            message_chiffre += char

    return message_chiffre



texte = "kaka !"    
cle = 5                     

resultat = chiffre_de_cesar(texte, cle)
print("Message original :", texte)
print("Message chiffré  :", resultat)


def chiffre_vigenere(message, cle):
    alphabet = string.printable
    message_chiffre = ""

    # position dans la clé
    position_cle = 0

    for char in message:
        if char in alphabet:
            
            # récupérer la lettre de la clé
            lettre_cle = cle[position_cle % len(cle)]
            
            # transformer la lettre de la clé en décalage
            decalage = alphabet.index(lettre_cle)
            
            # chiffrer le caractère
            message_chiffre += chiffre_de_cesar(char, decalage)

            # avancer dans la clé
            position_cle += 1
        else:
            message_chiffre += char

    return message_chiffre




def dechiffre_vigenere(message_chiffre, cle):
    alphabet = string.printable
    message_dechiffre = ""

    position_cle = 0

    for char in message_chiffre:
        if char in alphabet:
            lettre_cle = cle[position_cle % len(cle)]
            decalage = alphabet.index(lettre_cle)

            # ici on inverse le décalage (déchiffrement)
            message_dechiffre += chiffre_de_cesar(char, -decalage)

            position_cle += 1
        else:
            message_dechiffre += char

    return message_dechiffre


texte = "Cheickna"
cle_vigenere = "abc"

chiffre = chiffre_vigenere(texte, cle_vigenere)
dechiffre = dechiffre_vigenere(chiffre, cle_vigenere)

print("Message original :", texte)
print("Message chiffré  :", chiffre)
print("Message déchiffré:", dechiffre)

