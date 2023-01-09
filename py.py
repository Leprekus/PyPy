import sys
from PyQt5.QtWidgets import ( 
    QApplication, 
    QMainWindow,
    QPushButton
    )

class MainWindow(QMainWindow):
    #avoids referring to main class
    #helps with inheritance 
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')
        button = QPushButton('Press Me')
        self.setCentralWidget(button)

#if no cli arguments will be used an empty list can be pased
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
