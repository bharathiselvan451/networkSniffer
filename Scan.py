import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from PySide6.QtWidgets import QApplication, QPushButton, QFrame
from scapy.all import ARP, Ether, srp, wrpcap
#import spoof
import dr

def scanner():
    target_ip = dr.range()+".0/24"

    arp = ARP(pdst=target_ip)

    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp
    result = srp(packet, timeout=5, verbose=0)[0]

    clients = []
    for sent, received in result:
     clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    dict = {}

    Device_name = ""

    i = 1
    for client in clients:
     device = "device_"+str(i)
     dict[client['mac']] = device , client['ip']
     i = i+1

    return(dict)


   



#spoof.algo()


