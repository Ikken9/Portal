from scapy.all import *
from scapy.layers.inet import IP, TCP
from tqdm import tqdm


def scan(host, port_min, port_max):
    SYNACK = 0x12
    result = []
    try:
        for port in tqdm(range(port_min, port_max + 1)):
            sport = RandShort()
            pkt = IP(dst=host) / TCP(sport=sport, dport=port, flags="S")
            ACK_pkt = IP(dst=host) / TCP(sport=sport, dport=port, flags="A")
            RST_pkt = IP(dst=host) / TCP(sport=RandShort(), dport=port, flags="R")
            res = sr1(pkt, timeout=1, verbose=0)
            if res is not None and res.haslayer(TCP) and res.getlayer(TCP).flags == SYNACK:
                result.append([port, "TCP", "open"])
                send(ACK_pkt, timeout=0.01, verbose=0)
                send(RST_pkt, timeout=0.01, verbose=0)
            else:
                result.append([port, "TCP", "closed|filtered"])
    except KeyboardInterrupt:
        print("\n[*] User Requested Shutdown...")
        print("[*] Exiting...")
        sys.exit()
    return result
