from logging import getLogger, ERROR
from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP
from tqdm import tqdm

getLogger("scapy.runtime").setLevel(ERROR)


def scan(host, port_min, port_max):
    SYNACK = 0x12
    ACKRST = 0x14
    result = []
    RST_pkt = None
    try:
        for port in tqdm(range(port_min, port_max + 1)):
            sport = RandShort()
            RST_pkt = IP(dst=host) / TCP(sport=sport, dport=port, flags="R")
            SYN_pkt = IP(dst=host) / TCP(sport=sport, dport=port, flags="S")
            res = sr1(SYN_pkt, timeout=0.01)
            if res is None:
                result.append([port, "TCP", "filtered"])
                send(RST_pkt)
            elif res.haslayer(TCP):
                if res[TCP].flags == SYNACK:
                    result.append([port, "TCP", "open"])
                    send(RST_pkt)
                elif res[TCP].flags == ACKRST:
                    result.append([port, "TCP", "closed"])
                    send(RST_pkt)
                elif int(res.getlayer(ICMP).type) == 3 and int(res.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                    result.append([port, "TCP", "filtered"])
                    send(RST_pkt)
    except KeyboardInterrupt:
        send(RST_pkt)
        print("\n[*] User Requested Shutdown...")
        print("[*] Exiting...")
    return result
