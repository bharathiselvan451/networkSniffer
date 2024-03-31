from scapy.all import *


def router():
    p = sr1(IP(dst="www.google.com", ttl = 0)/ICMP())
    return p.src

def range():
    p = sr1(IP(dst="www.google.com", ttl = 0)/ICMP())
    source = p.src.split(".", 4)
    
    return source[0]+"."+source[1]+"."+source[2]