from scapy.all import *
from datetime import datetime
import query
from PySide6.QtWidgets import QMessageBox
#from Page_1 import firstpage

def start(d_name,vendour,mac,ip,a):
    now = datetime.now()
    dt_string = now.strftime("%b-%d-%Y%H:%M:%S")
    
    filter = "host "+ip
    packets = sniff(filter= filter,count = a)
   
    name = d_name+":_:"+dt_string+".pcapng"
    file = "/Users/divyaprabharajendran/Desktop/"+name
    open(file, "x")
    wrpcapng(file,packets)
    #sniff(offline="temp_1.pcap")
    print("here_4")
    query.insert(d_name,vendour,mac,ip,name)
    message()
    
    return packets

def message():
       
      message = QMessageBox()

      message.setText ("Capturing finished" )

      #message.setInformativeText ("Do you want to do something about it ?")

      #message.Icon(QMessageBox.critical)

      #message.setStandardButtons (MessageBox.Ok | MessageBox.Cancel)

      message.setDefaultButton(QMessageBox.Ok)

      ret = message. exec()

      



