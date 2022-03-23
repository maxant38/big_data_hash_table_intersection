from enum import auto
import random
import numpy as np
from collections import Counter
import Lecture_fichier
import math
import pandas as pd
import matplotlib.pyplot as plt
import sympy
###Create a TAD of legnth M+1###

def create_TAD(M):
    X=np.zeros((M+1))
    return X
#-------------------------------------------------------------------

###Increment the ith cell of the TAD###

def put_in_TAD(X, i):
    X[i] += 1


#-------------------------------------------------------------------


###Evaluates the TAD, gives the min, max, mean and the occurence of each values###

def evaluate_TAD(X, M, graph):
    #print(graph)
    nb_acces = np.count_nonzero(X[0:M])
    labels, values = zip(*Counter(X[0:M]).items())
    ## A ORDONNER
    #print(labels)
    indexes = np.arange(len(labels))
    width = 1
    #print(indexes)
    #print(values)
    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    if (graph == 2):
        plt.tight_layout() ##auto scale
        plt.show()
    mean = np.ndarray.mean(X[0:M])
    min = np.ndarray.min(X[0:M])
    max = np.ndarray.max(X[0:M])
    #for i in range(int(max+1)):
        #print("there are: ", np.count_nonzero(X == i),i  )
    print("number access: ", nb_acces,"/", M, "|taux d'occupation", nb_acces/M*100,"%", "|mean: ", mean, "|min: ", min, "|max:", max)

#-------------------------------------------------------------------



###increment a random cell of the TAD and increment the counter

def use_TAD(X, M, R):
    for i in range(R):
        X[M] +=1
        j = random.randint(0, M-1)
        put_in_TAD(X, j)
    return X

#-------------------------------------------------------------------

#-------------------------------------------------------------------



###increment a random cell of the TAD and increment the counter

def use_hash(X, M, liste):
    for i in liste:
        X[M] +=1
        put_in_TAD(X, i)

#------------------------------------------------------------------


###gerenarte a Prime number close to M

def generate_prime_number(M):
    min = M
    max = M+ 0.20*M
    try:
        primeM = sympy.randprime(min, max)
    except ValueError:
        print("no prime number")
    print(primeM)
    return primeM

#-------------------------------------------------------------------

def hashage_ascii(mot):
    list_result = []
    position = 0
    modulo = 786307 # le M qui a été définie précédement
    base=256 # 256 valeurs possibles en ASCII
    longueur = len(mot)
    for lettre in mot:
        asciiLettre = ord(lettre)  # transforme la lettre en sa valeur ASCII : 0 à 255 sont les valeurs possibles
        position =+ 1
        list_result.append(asciiLettre*base**(longueur-position)) # on ajoute la valeur associée à la lettre dans le liste
    result = sum(list_result) # on fait la somme de l'ensemble des valeurs
    result = result % modulo # Afin d'éviter des débordements
    return result

#-------------------------------------------------------------------

def hash_justin_maxence_Jenkins(primeM, X_string):
    hash = 0
    for letter in X_string:
        #convert a letter in unicode
        letter = ord(letter)
        hash += letter
        hash += (hash << 10)
        hash ^= (hash >> 6)
    hash += (hash << 3)
    hash ^= (hash >> 11)
    hash += (hash << 15)
    hash %= primeM
    return hash

#-------------------------------------------------------------------


def hash_justin_maxence_multiplication(primeM, X_string):
    hash = 0
    ## Suggestion de D. Knuth
    A = (math.sqrt(5)-1)/2
    for letter in X_string:
        #convert a letter in unicode
        letter = ord(letter)
        hash += primeM * ((letter * A) % 1)
        hash = hash % primeM
        hash = int(hash)

    return hash

#-------------------------------------------------------------------
# A visualization of the data to see if our functions are uniforms

def data_viz(X,Y,Z,W):

    X_sample = [[],[]]
    Y_sample = [[],[]]
    Z_sample = [[],[]]
    W_sample = [[],[]]

# Nous prenons seulement des échantillons aléatoire des valeurs car sinon la visualisation prend trop de temps
    
    borneMoins = 150000 # Choisir l'intervalle sur lequel vous voulez la visualisation
    bornePlus = 152000  # Si vous prenez des intervalles > 10 000 le programme risque de planter

# Creation des échantillons

    i=0
    for i in range (borneMoins,bornePlus):
        X_sample[0].append(i)
        i =+ 1
        X_sample[1].append(X[i])

    i=0
    for i in range (borneMoins,bornePlus):
        Y_sample[0].append(i)
        i =+ 1
        Y_sample[1].append(Y[i])


    i=0
    for i in range (borneMoins,bornePlus):
        Z_sample[0].append(i)
        i =+ 1
        Z_sample[1].append(Z[i])



    i=0
    for i in range (borneMoins,bornePlus):
        W_sample[0].append(i)
        i =+ 1
        W_sample[1].append(W[i])


    
    fig, ax = plt.subplots(4) # On crée quatre figures pour les quatres histogrammes

    plt.suptitle('Comparaison de nos fonctions de hashages',fontsize=14, fontweight='bold')
    plt.ylabel("Nombre d'occurence", loc="center")
    plt.xlabel("Valeur")
 

    ax[0].bar(X_sample[0], X_sample[1],color="blue", label="Test TAD")
    ax[0].legend(loc="upper left")

    ax[1].bar(Y_sample[0], Y_sample[1],color="red", label="Hashage ASCII")
    ax[1].legend(loc="upper left")

    ax[2].bar(Z_sample[0], Z_sample[1],color="green", label="Hashage Jenkins")
    ax[2].legend(loc="upper left")

    ax[3].bar(W_sample[0], W_sample[1], color="black", label="Hashage Multiplication")
    ax[3].legend(loc="upper left")
    
    plt.show()

#-------------------------------------------------------------------

def creation_hash_table (length):
    none_column =np.full([length,1], None)  ## crée une matrice colone de longeur length que de None
    zero_column = np.zeros((length,1))      ## crée une matrice colone de longeur length que de 0
    hash_table = np.concatenate((none_column, zero_column), axis=1) ## crée notre table de hashage (None | 0)
    return hash_table

#-------------------------------------------------------------------

def hash_function(element,mod):
    return hash(element)%mod ##renvoie le hash de l'élément avec la fonction hash native à python modulo mod (nb max de mots)

#-------------------------------------------------------------------

def hash_file(filename, hash_table):
    mod = 786307
    f = open(filename, 'r')
    mots = f.readlines()
    for i in range(0, len(mots)):  # on parcout l'ensemble des mots du fichier

        mots[i] = mots[i][:-1]  # on enlève les caractères parasites
        index = hash_function(mots[i], mod)  # on détermine l'index où on va placer le mot avec la fonction de hashage
        k = True

        while k == True: ## on peut faire un while 1 puis break

            if hash_table[index][1] == 0:
                hash_table[index][0] = mots[i]  # on ajoute le mot à la table de hashage
                hash_table[index][1] += 1  # on augmente l'occurence
                k = False  # on sort de la boucle || break

            else:  # on gère le cas d'une colision
                if hash_table[index][0] == mots[i]:  # si on a le même mot
                    hash_table[index][1] += 1  # on augmente l'occurence
                    k = False  # on sort de la boucle
                else:  # si ce n'est pas le même mot
                    index += 1  # on augmente l'index pour tester la case suivante

            if index >= mod:  # Si l'index dépasse la dernière case de notre table on retourne au début de la table
                index = 0

    return hash_table

#-------------------------------------------------------------------


def common_word(hash_table):

    lst_common_words = [] ##crée une liste vide pour stocker les mots communs

    for i in range(0,len(hash_table)):
        if hash_table[i][1] > 1: ##si la valeur est 2 dans la seconde colone, on ajoute le mot car c'est un mot en commun
            lst_common_words.append(hash_table[i][0])
    return lst_common_words,len(lst_common_words)

#--------------------------------------------------------------------

def excutable(fileOne,fileTwo):

    return common_word(hash_file(fileOne,(hash_file(fileTwo,creation_hash_table(786307)))))