from PySide6.QtWidgets import QApplication, QPushButton, QFrame, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import Qt, QSize
import Scan
import Sniffer

class firstpage(QWidget):
    button_layout = QVBoxLayout()
    line = ""
    devices = {}
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network Scanner")
        self.setGeometry(600, 600, 600, 600)
        button1 = QPushButton("Scan the network")
        button1.setStyleSheet("background-color : green; border-width: 15px; border-color: beige;")
        button1.clicked.connect(self.Find_devices)
        #button1.setGeometry(100, 100, 600, 400)
        #sbutton1.setFixedSize(QSize(100, 50))
        #Sub_layout1 = QHBoxLayout()
        self.button_layout.addWidget(button1)
        #self.button_layout.addStretch(5)
        self.button_layout.setAlignment(button1,Qt.AlignCenter)
        #Sub_layout1.setAlignment(button1,Qt.AlignVCenter)
        #self.button_layout.addLayout(button_layout)
        
        button2 = QPushButton("Device History")
        button2.clicked.connect(self.Previous_devices)
        button2.setStyleSheet("background-color : green; border-width: 15px; border-color: beige;")
        button2.adjustSize()
        #sbutton1.setFixedSize(QSize(100, 50))
        #Sub_layout1 = QHBoxLayout()
        self.button_layout.addWidget(button2)
        #self.button_layout.addStretch(5)
        self.button_layout.setAlignment(button2,Qt.AlignCenter)
        

        self.setLayout(self.button_layout)

    def Find_devices(self):
        dict = Scan.scanner()
        self.devices = dict
        print(self.devices)
        sub_layout2 = QHBoxLayout()
        label = QLabel("Enter the number of packets to capture :")
        label.setStyleSheet("color : green")
        self.line = QLineEdit()
        self.line.setStyleSheet("background-color : green; border-width: 15px; border-color: beige;")
        self.button_layout.addWidget(label)
        self.button_layout.addWidget(self.line)
        self.button_layout.setAlignment(label,Qt.AlignCenter)
        self.button_layout.setAlignment(self.line,Qt.AlignCenter)
        #self.setGeometry(600, 600, 600, 600)
        #self.button_layout.addStretch(1)
        for key, value in dict.items():
           Button = QPushButton(str(value[1])+" "+str(key))
           Button.setStyleSheet("background-color : green; border-width: 15px; border-color: beige;")
           Button.pressed.connect(lambda val=str(key): self.modo(val))
           sub_layout2.addWidget(Button)
           Button.setGeometry(20, 15, 10, 40) 
           #self.button_layout.setAlignment(Button,Qt.AlignBottom)
           sub_layout2.setAlignment(Button,Qt.AlignVCenter)
        
        self.button_layout.addLayout(sub_layout2)
        #dict.clear()

    def modo(self,mac):
       ip = self.devices[mac][1]
       print(ip)
       try:
           a = int(self.line.text())
           if(a>0):
              print(a)
              Sniffer.algo(mac,ip,a)
           else:
             return
       except Exception as e:
          print(e)

    def Previous_devices(self):
        self.wid = QWidget()
        self.wid.resize(250, 150)
        self.wid.setWindowTitle('Devices')
        self.wid.show()
           
    