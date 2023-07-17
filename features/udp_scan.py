from logging import getLogger, ERROR
from scapy.all import *
from scapy.layers.inet import IP, UDP, ICMP
from tqdm import tqdm

getLogger("scapy.runtime").setLevel(ERROR)


def scan(host, port_min, port_max):
    result = []
    try:
        for port in tqdm(range(port_min, port_max + 1)):
            UDP_pkt = IP(dst=host) / UDP(sport=RandShort(), dport=port)
            res = sr1(UDP_pkt, timeout=0.05)
            if res is None:
                result.append([port, "UDP", "open|filtered"])
            elif res.haslayer(UDP):
                result.append([port, "UDP", "open"])
            elif int(res.getlayer(ICMP).type) == 3 and int(res.getlayer(ICMP).code) in [1, 2, 9, 10, 13]:
                result.append([port, "UDP", "filtered"])
            elif int(res.getlayer(ICMP).type) == 3 and int(res.getlayer(ICMP).code) == 3:
                result.append([port, "UDP", "closed"])
    except KeyboardInterrupt:
        print("\n[*] User Requested Shutdown...")
        print("[*] Exiting...")
        sys.exit()
    return result


