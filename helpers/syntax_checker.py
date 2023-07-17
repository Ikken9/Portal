import ipaddress
import sys


def check_host_syntax(host_ip):
    try:
        ipaddress.ip_address(host_ip)
        pass
    except:
        print("[!] Invalid port syntax")
        print("[!] Exiting...")
        sys.exit()


def check_port_syntax(port):
    port = str(port)
    try:
        ports_list = port.split('-')
    except:
        print("[!] Invalid port syntax")
        print("[!] Exiting...")
        sys.exit()

    if len(ports_list) > 2:
        print("[!] Invalid port syntax")
        print("[!] Exiting...")
        sys.exit()

    if len(ports_list) > 1:
        try:
            int(ports_list[0])
            int(ports_list[1])
        except:
            print("[!] Invalid port syntax")
            print("[!] Exiting...")
            sys.exit()

        if int(ports_list[0]) < int(ports_list[1]):
            for ports in ports_list:
                if int(ports) <= 0 or int(ports) > 65535:
                    print("[!] Invalid port syntax")
                    print("[!] Port must be an integer between 1 and 65535, both included")
                    print("[!] Exiting...")
                    sys.exit()
        else:
            pass
