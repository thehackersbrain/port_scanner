#!/usr/bin/python3
# port scanner
# Author : Gaurav Raj [HackersBrain]
# website : http://gauravraj.gq/
# Note : Don't Forget to give Credit before commiting changes...

# imports
import sys
import socket
import threading
import pyfiglet
from colorama import Fore, Style

hlp1 = " Usage :"
hlp2 = "\t python3 main.py <target> <start_port> <end_port>"
hlp3 = "\n\t   ex : python3 main.py 192.168.x.x 1 100\n"


def banner():
    bn = pyfiglet.figlet_format(" Port Scanner", font='slant')
    print(f"{Fore.GREEN}{bn}{Style.RESET_ALL}")
    print(f"\t\t\t[Author : {Fore.GREEN}HackersBrain{Style.RESET_ALL}]")
    print()


if len(sys.argv) != 4:
    banner()
    print(hlp1)
    print(hlp2)
    print(hlp3)
    sys.exit()

try:
    host = socket.gethostbyname(sys.argv[1])
except socket.gaierror as hst_err:
    print(" Unable to Get The Target..")
    sys.exit()


st_port = int(sys.argv[2])
end_port = int(sys.argv[3])

try:
    banner()
except ImportError as imp_err:
    print(" Failed to import Some Modules...")

print(f"\t Scanning Started... \tTarget : {Fore.GREEN}{host}{Style.RESET_ALL}\n")


def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((host, port))
    if not conn:
        print(f" Port {Fore.GREEN}{port}{Style.RESET_ALL} is OPEN")
    s.close()


for port in range(st_port, end_port+1):
    thrd = threading.Thread(target=port_scan, args=(port,))
    thrd.start()
