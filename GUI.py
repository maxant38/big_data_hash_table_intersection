import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator
import Main
import sys
from importlib import reload
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QCheckBox, QPushButton, \
    QDialog, QComboBox


class LabelledIntField(QWidget):
    def __init__(self, title, initial_value=None):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel()
        self.label.setText(title)
        self.label.setFixedWidth(150)
        self.label.setFont(QFont("Arial",weight=QFont.Bold))
        layout.addWidget(self.label)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFixedWidth(100)
        self.lineEdit.setValidator(QIntValidator())
        if initial_value != None:
            self.lineEdit.setText(str(initial_value))
        layout.addWidget(self.lineEdit)
        layout.addStretch()

    def setLabelWidth(self, width):
        self.label.setFixedWidth(width)

    def setInputWidth(self, width):
        self.lineEdit.setFixedWidth(width)

    def getValue(self):
        return int(self.lineEdit.text())

    def getValueCheckbox(self, state):
        return bool(self.state)
#-------------------------------------------------------------------


class Demo(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        # Ensure our window stays in front and give it a title
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Select txt files")
        self.setFixedSize(400, 200)

        # Create and assign the main (vertical) layout.
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)

        self.addIntInputsPanel(vlayout)
        vlayout.addStretch()
        self.addButtonPanel(vlayout)
        self.show()
    #--------------------------------------------------------------------
    def addIntInputsPanel(self, parentLayout):
        h1layout = QHBoxLayout()
        h2layout = QHBoxLayout()


        #la longueur correspond à celle de notre table, et le number of use au nombre de mots
        self.label1 = QLabel("first text : ")
        self.cb1 = QComboBox()
        self.cb1.addItems(["corncob_lowercase.txt", "texte_Shakespeare.txt", "word2.txt"])
        self.label2 = QLabel("Second text : ")
        self.cb2 = QComboBox()
        self.cb2.addItems(["corncob_lowercase.txt", "texte_Shakespeare.txt", "word2.txt"])


        h1layout.addWidget(self.label1)
        h1layout.addWidget(self.cb1)
        h2layout.addWidget(self.label2)
        h2layout.addWidget(self.cb2)

        h1layout.addStretch()
        h2layout.addStretch()
        parentLayout.addLayout(h1layout)
        parentLayout.addLayout(h2layout)

    #--------------------------------------------------------------------
    def addButtonPanel(self, parentLayout):
        self.button = QPushButton("OK")
        self.CloseButton = QPushButton("Close")
        self.button.clicked.connect(self.buttonOkAction)
        self.CloseButton.clicked.connect(self.buttonCloseAction)
        hlayout = QHBoxLayout()
        hlayout.addStretch()
        hlayout.addWidget(self.button)
        hlayout.addWidget(self.CloseButton)
        parentLayout.addLayout(hlayout)
    #--------------------------------------------------------------------

    #renvoie les valeurs d'inputs et des cases cochées en main
    def buttonOkAction(self):
        plt.close()
        print(self.cb1.currentText())
        print(self.cb2.currentText())
        if (self.cb1.currentText() == self.cb2.currentText()):
            print("select two different texts")
            self.close()
        text1, text2 = self.cb1.currentText(), self.cb2.currentText()
        self.close()
        Main.main(text1, text2)

#--------------------------------------------------------------------
    #quitte le programme
    def buttonCloseAction(self):
        self.close()
        sys.exit()
    #--------------------------------------------------------------------

# ========================================================
def main():
    # Create the Qt Application
    app = QApplication(sys.argv)
    window = Demo() # <<-- Create an instance
    window.setWindowTitle("Caille_Courtois_TAD")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

