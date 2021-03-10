def decbin(d,nb=0):
    """dec2bin(d,nb=0): conversion nombre entier positif ou nul -> chaîne binaire (si nb>0, complète à gauche par des zéros)"""
    if d==0:
        b="0"
    else:
        b=""
        while d!=0:
            b="01"[d&1]+b
            d=d>>1
    return b.zfill(nb)

#msg initial que l'on doit crypté
nbr = "F"
print("le msg à décrypter est:",nbr)

print("-"*20)

#pr convertir le char en val deci
msg =ord(nbr)
print("msg en décimal:",msg)

#clé en binaire
clé = 0b00000110
print("la clé en décimal:", clé)

resultat = msg ^ clé
print("voici le résultat:",resultat)

print("-"*20)
ASCII = chr(resultat)
print("le msg crypté est:",ASCII)


print("le msg crypté en binaire:", decbin(resultat,8))

print("-"*20)
#le decryptage:
resultat = resultat ^ clé

#resultat decrypter (resultat final)
ASCII = chr(resultat)
print("le msg de base est :",ASCII)



















