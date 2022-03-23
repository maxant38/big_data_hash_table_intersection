from enum import auto
import random
import numpy as np
from collections import Counter
import Lecture_fichier
import math
import pandas as pd
import matplotlib.pyplot as plt
import sympy

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
