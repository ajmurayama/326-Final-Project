"""modules designed for GUI related scripting
TimBlackwell final project INST326"""
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
)

class Window(QMainWindow):
    """Main Window/screen. needed for GUI creation"""
    def __init__(self, parent):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Contacts")
        self.resize(xvalue,yvalue)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
import sys

from PyQt5.QtWidgets import QApplication

from **previousfile** import Window

def main():
    """main function to initialize window as mandatory argument."""
    # application created
    app = QApplication(sys.argv)
    # window initialized
    win = Window()
    win.show()
    sys.exit(app.exec())
    
    
    if __name__ == "__main__":
    main()

#Code for building GUI and database will be below this


