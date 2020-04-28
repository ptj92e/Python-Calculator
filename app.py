# Importing sys to handle exit status of application.
import sys
# Import QApplication and all required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from functools import partial

ERROR_MSG = "ERROR"

__version__ = "0.1"
__author__ = "Phillip Jones"
# Set a subclass of QMainWindow to setup GUI
class PyCalcUi(QMainWindow):
    # Python Calculator's View
    def __init__(self):
        # View Initilizer
        super().__init__()
        # Sets the window's properties
        self.setWindowTitle("Python Calculator")
        self.setFixedSize(235, 235)
        # Sets the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWdget = QWidget(self)
        self._centralWdget.setLayout(self.generalLayout)
        self.setCentralWidget(self._centralWdget)
        # Create display and the buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        # Create display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        # Create the buttons
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Dictionary of button text and coordinate of the grid
        buttons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 4)
        }
        # Loop over buttons to add them to the layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
            # Add buttons layout to general layout
            self.generalLayout.addLayout(buttonsLayout)
    # Sets and Updates the display's text
    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()
    # Getter method the returns the display's current text
    def displayText(self):
        return self.display.text()
    # Resets the display text back to an empty string
    def clearDisplay(self):
        self.setDisplayText("")

class PyCalcCtrl:
    def __init__(self, view):
        self._view = view
        # Connect Signals and Slots
        self._connectSignals()

    def _buildExpression(self, sub_exp):
        # Build the expression
        expression = self._view.displayText() + sub_exp
        # Calling the setDisplayText method to change the display text
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        # Connect signals and slots
        for btnText, btn in self._view.buttons.items():
            if btnText not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)

# Client code
def main():
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    #Show the calculator's GUI
    view=PyCalcUi()
    view.show()
    # Create instances of the model and the controller 
    PyCalcCtrl(view=view)
    # Execute Calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == "__main__":
    main()