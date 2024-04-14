from PySide6.QtWidgets import QApplication, QPushButton, QFrame
from PySide6.QtCore import Qt
from Page_1 import firstpage
import sys



app = QApplication(sys.argv)

Window_1 = firstpage()

Window_1.setAttribute(Qt.WA_StyledBackground, True)
Window_1.setStyleSheet('background-color: white;')

Window_1.show()

app.exec()