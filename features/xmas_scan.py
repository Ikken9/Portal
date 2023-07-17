from logging import getLogger, ERROR
from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP
from tqdm import tqdm

getLogger("scapy.runtime").setLevel(ERROR)


def scan(host, port_min, port_max):
    RST = 0x04
    result = []
    try:
        for port in tqdm(range(port_min, port_max + 1)):
            pkt = IP(dst=host) / TCP(sport=RandShort(), dport=port, flags="FPU")
            res = sr1(pkt, timeout=0.01)
            if res is None:
                result.append([port, "TCP", "open|filtered"])
            elif res.haslayer(TCP) and res[TCP].flags == RST:
                result.append([port, "TCP", "closed"])
            elif int(res.getlayer(ICMP).type) == 3 and int(res.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                result.append([port, "TCP", "filtered"])
    except KeyboardInterrupt:
        print("\n[*] User Requested Shutdown...")
        print("[*] Exiting...")
    return result