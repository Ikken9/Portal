# Portal

## Introduction
Portal is a basic port scanner console application written in Python3 using Scapy to manipulate packets. It also uses 
tqdm to display a progress bar that indicates the state of process while performing a scan and (approximately) the 
time that lefts to complete the task.

### Features
Portal can perform single and ranged port scans to a specified target. All scans can be made via TCP Connect, 
TCP SYN (Stealth), UDP and Xmas techniques.
The criteria used to determine the port state is the same as nmap.

It generates a progress bar in the output using tqdm, that indicates the scan progress.
The generated output format is very similar to the format that nmap uses, it shows the ports with their correspondant
state, the protocol, the actual time and (depending on the parameters) the open, closed and/or filtered ports count 
that aren't shown.

### Note
The main purpose of this project is just learn, this is not the fastest or powerful port scanner ever made, there's a 
bunch of other port scanners that works better.

## Installation
### Prerequisites
Install Python3 [latest version](https://www.python.org/downloads/), Scapy [latest version](https://scapy.readthedocs.io/en/latest/installation.html) (currently 2.5.0), 
and also install tqdm from the [official repo](https://github.com/tqdm/tqdm#installation).

## Usage
Run it as a normal python script: ./main.py <parameters...> <br>
Parameters:

    -H, --host <target-ip> (required)
    -P, --ports <port> or <smaller-port> - <largest-port> (optional, if empty a full range scan will be performed)
    -m, --mode <[sS, sT, sU, sX]> (required)
    -o, --open (optional)
    -c, --closed (optional)
    -f, --filtered (optional)

<br> -H: Target host ip.
<br> -P: Target port(s).
<br> -m: Operation mode, sS is  for TCP SYN (Stealth) scan, sT is for TCP Connect scan, sU is for UDP scan and sX is 
    for Xmas scan.
<br> -o: List open ports.
<br> -c: List closed ports.
<br> -f: List filtered ports.
<br> If all of these last three parameters are unset, both open and closed and filtered will be shown in the output.

## License
Portal is under [GNU GPL-3.0 License](LICENSE.md).

## Author
Portal was created by Ikken9.
