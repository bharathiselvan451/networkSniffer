from PySide6.QtWidgets import QApplication, QPushButton, QFrame, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import Qt, QSize
import Scan
import Sniffer
import query

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
           device = query.search_device(key)
           Button = ""
           if(device==None):
               Button = QPushButton(str(value[1])+" "+str(key))
           else:
               Button = QPushButton(device.Device_name)
               
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

     
           a = int(self.line.text())
           
           if(query.search(mac)):
              self.user_input_1(mac,ip,a)
           else:
              device = query.search_device(mac)
              Sniffer.algo(device.Device_name,device.vendour,mac,ip,a)
       
            #print(e)

       
       
      
       

    def Previous_devices(self):
        devices = query.all()
        Layout = QVBoxLayout()
        for device in devices:
            #Label = QLabel(device.Device_name+" "+device.MAC_address+" "+device.IP_address+" "+device.File_name+" "+device.vendour)
            Label = QLabel("Device name: "+device.Device_name+" Mac Address: "+device.MAC_address+" IP address: "+device.IP_address+" Vendour: "+device.vendour+" Files: "+device.File_name)
            Layout.addWidget(Label)
        self.wid = QWidget()
        self.wid.resize(250, 150)
        self.wid.setWindowTitle('Devices')
        self.wid.setLayout(Layout)
        self.wid.show()

    def user_input_1(self,mac,ip,a):
        label = QLabel("Provide details about the device")
        label_1 = QLabel("name")
        Device_name = QLineEdit()
        label_2 = QLabel("vendour")
        vendour = QLineEdit()
        button = QPushButton("Continue")
        
        button.clicked.connect(lambda: self.First_Start(vendour,Device_name,self.wid_1,mac,ip,a))

        label.setStyleSheet("color : green")
        label_1.setStyleSheet("color : green")
        Device_name.setStyleSheet("background-color : green; border-width: 15px; border-color: beige;")
        label_2.setStyleSheet("color : green")
        vendour.setStyleSheet("background-color : green; border-width: 15px; border-color: beige;")
        button.setStyleSheet("background-color : green; border-width: 15px; border-color: beige;")

        Layout = QVBoxLayout()
        Layout.addWidget(label)
        Layout.addWidget(label_1)
        Layout.addWidget(Device_name)
        Layout.addWidget(label_2)
        Layout.addWidget(vendour)
        Layout.addWidget(button)

        

        Layout.setAlignment(label,Qt.AlignCenter)
        Layout.setAlignment(label_1,Qt.AlignCenter)
        Layout.setAlignment(Device_name,Qt.AlignCenter)
        Layout.setAlignment(label_2,Qt.AlignCenter)
        Layout.setAlignment(vendour,Qt.AlignCenter)
        Layout.setAlignment(button,Qt.AlignCenter)

        self.wid_1 = QWidget()
        self.wid_1.setStyleSheet('background-color: white;')
        self.wid_1.resize(250, 150)
        self.wid_1.setWindowTitle('Provide details')
        self.wid_1.setLayout(Layout)
        self.wid_1.show()

   
    
    def First_Start(self,vendour,name,wid,mac,ip,a):
        
            print(str(vendour.text()))
            print(str(name.text()))
            print(mac)
            print(ip)
            print(a)
            wid.close()
            Sniffer.algo(name.text(),vendour.text(),mac,ip,a)
        
