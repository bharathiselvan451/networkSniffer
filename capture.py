from scapy.all import *
import Sniffer

def start(mac,ip,a):
    print("here_3")
    filter = "host "+ip
    packets = sniff(filter= filter,count = a)
    print("here_4.1ßß")
    file = "/Users/divyaprabharajendran/Desktop/device_"+mac+".pcapng"
    open(file, "x")
    wrpcapng(file,packets)
    #sniff(offline="temp_1.pcap")
    print("here_4")
    
    return packets

def store(packets):
    wrpcapng("temp_1.pcap",packets)