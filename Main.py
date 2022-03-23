import GUI
import TD
import sys
import numpy as np


def main(text1 = None, text2 = None):
    print(text1)
    if (text1 == None):
        GUI.main()
    common_words, length = TD.excutable(text1, text2)
    print(common_words)
    print(length)
    
def mainGUI(text1 = None, text2 = None):
    if (text1 == None):
        GUI.main()
    common_words, length = TD.excutable(text1, text2)
    print(common_words)
    print(length)

##without GUI
if __name__ == "__main__":
    main()

    
##launch GUI
if __name__ == "__main__":
    while True:
        yn = input("Try GUI now ? [Y/N] : ")
        if (yn == "Y"):
            break
        elif (yn == "N"):
            sys.exit()
        else:
            continue
    mainGUI()



