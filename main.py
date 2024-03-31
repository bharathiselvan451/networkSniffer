from PySide6.QtWidgets import QApplication, QPushButton, QFrame
from Page_1 import firstpage
import sys



app = QApplication(sys.argv)

Window_1 = firstpage()

Window_1.show()

app.exec()