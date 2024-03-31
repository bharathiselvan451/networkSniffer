from PySide6.QtWidgets import QApplication, QPushButton, QFrame, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt
import Scan
import Sniffer

class firstpage(QWidget):
    button_layout = QHBoxLayout()
    devices = {}
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network Scanner")
        self.setGeometry(600, 600, 600, 600)
        button1 = QPushButton("Scan the network")
        button1.clicked.connect(self.Find_devices)
        Sub_layout1 = QHBoxLayout()
        Sub_layout1.addWidget(button1)
        Sub_layout1.addStretch(5)
        #Sub_layout1.setAlignment(button1,Qt.AlignVCenter)
        #Sub_layout1.setAlignment(button1,Qt.AlignHCenter)
        self.button_layout.addLayout(Sub_layout1)
       
        

        self.setLayout(self.button_layout)

    def Find_devices(self):
        dict = Scan.scanner()
        self.devices = dict
        sub_layout2 = QHBoxLayout()
        self.setGeometry(600, 600, 600, 600)
        sub_layout2.addStretch(1)
        for key, value in dict.items():
           Button = QPushButton(str(value[1]))
           sub_layout2.addWidget(Button)
           Button.pressed.connect(lambda val=str(value[1]): self.modo(val))
           sub_layout2.setAlignment(Button,Qt.AlignVCenter)
           sub_layout2.setAlignment(Button,Qt.AlignHCenter)
        self.button_layout.addLayout(sub_layout2)

    def modo(self,ip):
        Sniffer.algo(ip)