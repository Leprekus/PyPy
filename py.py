from PyQt5.QtWidgets import QApplication, QWidget
import sys

#if no cli arguments will be used an empty list can be pased
app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec_()
print(sys.version)