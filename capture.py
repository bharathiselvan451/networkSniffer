from scapy.all import *
from datetime import datetime
import query

def start(mac,ip,a):
    now = datetime.now()
    dt_string = now.strftime("%b-%d-%Y%H:%M:%S")
    print("here_3")
    filter = "host "+ip
    packets = sniff(filter= filter,count = a)
    print("here_4.1ßß")
    name = "device_"+mac+":_:"+dt_string+".pcapng"
    file = "/Users/divyaprabharajendran/Desktop/"+name
    open(file, "x")
    wrpcapng(file,packets)
    #sniff(offline="temp_1.pcap")
    print("here_4")
    query.insert(mac,ip,name)
    
    return packets

def store(packets):
    wrpcapng("temp_1.pcap",packets)