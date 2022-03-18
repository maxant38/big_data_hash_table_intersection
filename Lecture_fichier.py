import TD


#--------------------------------------------------------------------------
def maxline():
    maxLine = 0
    #document in the same folder
    for doc in ['texte_Shakespeare.txt', 'corncob_lowercase.txt',
                'word2.txt']:  # pour compter le nombre de mot, on compte le nombre de ligne car il y a un mot par ligne
        f = open(doc, 'r')
        text = f.readlines()
        NumberOfLine = len(text)
        if maxLine < NumberOfLine:
            maxLine = NumberOfLine
    print(maxLine)
#--------------------------------------------------------------------------
# On obtient le résultat suivant : 235886
# On constate que le fichier qui contient le maximum de mots en contient 235 886. Sachant que l'on souhaite que la table de hachage soit occupée à environ 30% de sa capacité. 
# On va prendre une valeur proche de 235886/0.3=~ 786 287 .
# Afin d'avoir une fonction de hachage avec une bonne dispersion.Nous allons prendre un nombre premier proche de cette valeur.
# Nous avons donc grâce à la fonction generate_prime_number (contenue dans le fichier TD.py) déterminer le nombre premier que nous allons utilisé.
# Nous utiliserons donc le nombre premier M suivant : 786307

#--------------------------------------------------------------------------


def hashage_fichier_ascii(fichier):
    lst_fichier_hashe=[]
    f = open(fichier,'r')
    mots = f.readlines()
    for i in range (0,len(mots)):
        mots[i] = mots[i][:-1]
        lst_fichier_hashe.append(TD.hashage_ascii(mots[i]))
    return lst_fichier_hashe

def hashage_fichier_Jenkins(fichier):
    lst_fichier_hashe=[]
    f = open(fichier,'r')
    mots = f.readlines()
    for i in range (0,len(mots)):
        mots[i] = mots[i][:-1]
        lst_fichier_hashe.append(TD.hash_justin_maxence_Jenkins(786307, mots[i]))
    return lst_fichier_hashe

def hashage_fichier_multiplication(fichier):
    lst_fichier_hashe=[]
    f = open(fichier,'r')
    mots = f.readlines()
    for i in range (0,len(mots)):
        mots[i] = mots[i][:-1]
        lst_fichier_hashe.append(TD.hash_justin_maxence_multiplication(786307, mots[i]))
    return lst_fichier_hashe

