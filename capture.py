from scapy.all import *


def start(ip):
    filter = "host "+ip
    packets = sniff(filter= filter,count = 10)
    wrpcapng("temp_1.pcap",packets)
    return packets

