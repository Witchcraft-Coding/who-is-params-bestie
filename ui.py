from PySide6 import QtCore, QtWidgets

from functions import is_params_bestie

class WhoIsParamsBestie(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.bestie = 'Medha'
        self.bestie_surname = 'Tripathi'

        self.button = QtWidgets.QPushButton("Am I Param's bestie?")
        self.text = QtWidgets.QLabel("Enter your name below to check if you are Param's bestie.",
                                     alignment=QtCore.Qt.AlignCenter)
        self.input = QtWidgets.QLineEdit()
        self.input.setPlaceholderText('Enter your name here')

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.check)
        self.input.returnPressed.connect(self.check)

    @QtCore.Slot()
    def check(self):
        name = self.input.text()
        output = is_params_bestie(name, self.bestie, self.bestie_surname)
        self.text.setText(output)