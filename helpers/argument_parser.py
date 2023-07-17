import argparse

LIST_OPEN_PORTS = False
LIST_CLOSED_PORTS = False
LIST_FILTERED_PORTS = False


def argument_parser():
    global LIST_OPEN_PORTS
    global LIST_CLOSED_PORTS
    global LIST_FILTERED_PORTS
    parser = argparse.ArgumentParser(
        prog="Portal",
        description="Port Scanner")
    parser.add_argument("-H", "--host",
                        help="Target IP",
                        required=True)
    parser.add_argument("-P", "--ports",
                        help="Target Port(s), if not specified, a full range port scan will be performed\n" +
                        "Syntax: <smaller_port> - <largest_port>\n" +
                        "Port must be an integer between 1 and 65535, both included",
                        required=False)
    parser.add_argument("-m", "--mode",
                        help="Operation Mode, it can be:\n"
                             "1. sS (TCP SYN Stealth Scan)\n"
                             "2. sT (TCP Connect Scan)\n"
                             "3. sU (UDP Scan)\n"
                             "4. sX (Xmas Scan)\n",
                        required=True,
                        choices=["sS", "sT", "sU", "sX"],
                        type=str)
    parser.add_argument("-o", "--open",
                        help="List open ports",
                        required=False,
                        action="store_true")
    parser.add_argument("-c", "--closed",
                        help="List closed ports",
                        required=False,
                        action="store_true")
    parser.add_argument("-f", "--filtered",
                        help="List filtered ports",
                        required=False,
                        action="store_true")

    parsed_args = parser.parse_args()
    if parsed_args.ports is None:
        parsed_args.ports = "1-65535"
    return parsed_args


args = argument_parser()
if args.open:
    LIST_OPEN_PORTS = True
if args.closed:
    LIST_CLOSED_PORTS = True
if args.filtered:
    LIST_FILTERED_PORTS = True

if not args.open and not args.closed and not args.filtered:
    LIST_OPEN_PORTS = True
    LIST_CLOSED_PORTS = True
    LIST_FILTERED_PORTS = True

