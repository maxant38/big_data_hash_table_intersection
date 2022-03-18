import GUI
import TD
import Lecture_fichier


def main(M=0, R=0, graph=0):
#--------------------------------------------------------------------------
##TAD
    if (M==0 & R==0):
        GUI.main()
    print(M, type(M), R, type(R))
    X = TD.create_TAD(M)
    TD.use_TAD(X,M,R)
    print("evaluate random TAD")
    #TD.evaluate_TAD(X,M, graph)
#--------------------------------------------------------------------------
## Test de la fonction de hash

##determine le max de ligne
 #   maxline = Lecture_fichier.maxline()

##genere un nombre premier proche de M pour taux occupation à 30%
    primeM = 786307
## met tous les mots dans une liste
    lst_word2 = Lecture_fichier.hashage_fichier_ascii("word2.txt")
    Y = TD.create_TAD(primeM)
    print(Y[0:100])
    TD.use_hash(Y, primeM, lst_word2)
    print("evaluate hash_ascii")
    TD.evaluate_TAD(Y, primeM, graph)
#--------------------------------------------------------------------------
    lst_word2 = Lecture_fichier.hashage_fichier_Jenkins("word2.txt")
    #print(lst_word2)
    Z = TD.create_TAD(primeM)
    TD.use_hash(Z, primeM, lst_word2)
    print("evaluate hash_Jenkins")
    TD.evaluate_TAD(Z, primeM, graph)
#--------------------------------------------------------------------------
    lst_word2 = Lecture_fichier.hashage_fichier_multiplication("word2.txt")
    W = TD.create_TAD(primeM)
    TD.use_hash(W, primeM, lst_word2)
    print("evaluate hash_multiplication")
    TD.evaluate_TAD(W, primeM, graph)

    print("la fonction hash_Jenkins est la meilleure")

#--------------------------------------------------------------------------
# On visualise comment sont répartit les valeurs. Cela permet de voir si nos fonctions de hachage sont uniformes.
    
    TD.data_viz(X,Y,Z,W)

#--------------------------------------------------------------------------

if __name__ == "__main__":
    main()




