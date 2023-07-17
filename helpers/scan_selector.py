from features import tcp_syn_scan
from features import tcp_connect_scan
from features import udp_scan
from features import xmas_scan


def scan_selector(host, ports_list, scan_mode):
    result = [None, None, None]

    if scan_mode == "sT" and len(ports_list) == 1:
        result = tcp_connect_scan.scan(host, int(ports_list[0]), int(ports_list[0]))
    elif scan_mode == "sT" and len(ports_list) == 2:
        result = tcp_connect_scan.scan(host, int(ports_list[0]), int(ports_list[1]))
    elif scan_mode == "sS" and len(ports_list) == 1:
        result = tcp_syn_scan.scan(host, int(ports_list[0]), int(ports_list[0]))
    elif scan_mode == "sS" and len(ports_list) == 2:
        result = tcp_syn_scan.scan(host, int(ports_list[0]), int(ports_list[1]))
    elif scan_mode == "sU" and len(ports_list) == 1:
        result = udp_scan.scan(host, int(ports_list[0]), int(ports_list[0]))
    elif scan_mode == "sU" and len(ports_list) == 2:
        result = udp_scan.scan(host, int(ports_list[0]), int(ports_list[1]))
    elif scan_mode == "sX" and len(ports_list) == 1:
        result = xmas_scan.scan(host, int(ports_list[0]), int(ports_list[0]))
    elif scan_mode == "sX" and len(ports_list) == 2:
        result = xmas_scan.scan(host, int(ports_list[0]), int(ports_list[1]))

    return result
