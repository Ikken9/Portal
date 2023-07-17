from tabulate import tabulate
from helpers.argument_parser import LIST_OPEN_PORTS, LIST_CLOSED_PORTS, LIST_FILTERED_PORTS


def make_report(data):
    output = []

    ports_open_count = 0
    ports_closed_count = 0
    ports_filtered_count = 0

    for port in data:
        port_number = port[0]
        port_protocol = port[1]
        port_state = port[2]

        if port_state == ("open" or "open|filtered"):
            ports_open_count += 1
            if LIST_OPEN_PORTS:
                output.append([port_number, port_protocol, port_state])

        if port_state == ("closed" or "closed|filtered"):
            ports_closed_count += 1
            if LIST_CLOSED_PORTS:
                output.append([port_number, port_protocol, port_state])

        if port_state == ("filtered" or "open|filtered" or "closed|filtered"):
            ports_filtered_count += 1
            if LIST_FILTERED_PORTS:
                output.append([port_number, port_protocol, port_state])

    if not LIST_OPEN_PORTS or not LIST_CLOSED_PORTS or not LIST_FILTERED_PORTS:
        not_shown = "Not shown: "
        if not LIST_OPEN_PORTS:
            not_shown += f"{ports_open_count} open ports, "
        if not LIST_CLOSED_PORTS:
            not_shown += f"{ports_closed_count} closed ports, "
        if not LIST_FILTERED_PORTS:
            not_shown += f"{ports_filtered_count} filtered ports, "
        not_shown = not_shown[:-2]
        print(f"\n{not_shown}")
    print("\n")
    print(tabulate(output, headers=["PORT", "PROTOCOL", "STATE"]))