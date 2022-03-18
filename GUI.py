import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator

import Main
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QCheckBox, QPushButton, \
    QDialog
from PyQt5 import QtCore

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
        self.setWindowTitle("Integer Inputs")
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
        hlayout = QHBoxLayout()
        h2layoout = QHBoxLayout()

        self.Mdiv = LabelledIntField('TAD length', 786307)
        self.Rdiv = LabelledIntField('Number of use', 235886)
        self.checkBoxA = QCheckBox("Show graph")


        hlayout.addWidget(self.Mdiv)
        hlayout.addWidget(self.Rdiv)
        h2layoout.addWidget(self.checkBoxA)
        hlayout.addStretch()
        h2layoout.addStretch()
        parentLayout.addLayout(hlayout)
        parentLayout.addLayout(h2layoout)
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


    def buttonOkAction(self):
        plt.close()
        print(self.Mdiv.getValue())
        print(self.Rdiv.getValue())
        print(self.checkBoxA.checkState())
        Main.main(self.Mdiv.getValue(), self.Rdiv.getValue(), self.checkBoxA.checkState())

#--------------------------------------------------------------------
    def buttonCloseAction(self):
        self.close()
        sys.exit()
    #--------------------------------------------------------------------

# ========================================================
def main():
    # Create the Qt Application
    print("loading GUI")
    app = QApplication(sys.argv)
    window = Demo() # <<-- Create an instance
    window.setWindowTitle("Caille_Courtois_TAD")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()