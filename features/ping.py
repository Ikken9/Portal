from scapy.all import *
from scapy.layers.inet import IP, ICMP


def ping(host):
    conf.verb = 0
    icmp = sr(IP(dst=host) / ICMP(), timeout=1)
    if icmp is not None:
        pass
    elif icmp is None:
        print("[!] Target isn't up")
        print("[!] Exiting...")
        sys.exit()
