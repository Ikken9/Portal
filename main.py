#!/usr/bin/python3

from time import strftime
from helpers.argument_parser import *
from features.ping import *
from helpers.syntax_checker import *
from helpers.scan_selector import *
from helpers.scan_result import *


def main():
    parsed_args = argument_parser()
    host = parsed_args.host
    check_host_syntax(host)

    ports = str(parsed_args.ports).strip()
    port_list = ports.split('-')
    print("[*] Checking if target is online...")
    ping(host)

    print("[*] Scanning Started at " + strftime("%H:%M:%S") + "\n")
    start_clock = datetime.now()

    scan_result = scan_selector(host, port_list, parsed_args.mode)
    make_report(scan_result)

    stop_clock = datetime.now()
    total_time = stop_clock - start_clock
    print("\n[*] Scanning Finished!")
    print("[*] Total Scan Duration: " + str(total_time))


if __name__ == '__main__':
    main()
