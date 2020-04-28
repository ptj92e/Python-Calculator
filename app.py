# Importing sys to handle exit status of application.
import sys
# Import QApplication and all required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

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
        # Sets the central widget
        self._centralWdget = QWidget(self)
        self.setCentralWidget(self._centralWdget)

# Client code
def main():
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    #Show the calculator's GUI
    view=PyCalcUi()
    view.show()
    # Execute Calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == "__main__":
    main()