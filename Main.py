import GUI
import TD
import Lecture_fichier
import numpy as np


def main(text1 = None, text2 = None):
    print(text1)
    if (text1 == None):
        GUI.main()
    common_words, length = TD.excutable(text1, text2)
    print(common_words)
    print(length)

if __name__ == "__main__":
    main()




