#!/usr/bin/python3
# port scanner
# Author : Gaurav Raj [HackersBrain]
# website : http://gauravraj.gq/
# Note : Don't Forget to give Credit before committing changes...

# imports
try:
    import sys
    import socket
    import threading
    import pyfiglet
    import argparse
    from colorama import Fore, Style
except ImportError as imp_err:
    print(f"\n {Fore.RED}Failed Importing Some Modules{Style.RESET_ALL}\n\t{imp_err}")

# Defined Functions


def banner():
    """ Figlet Banner """
    bn = pyfiglet.figlet_format(" Port Scanner", font='slant')
    print(f"{Fore.GREEN}{bn}{Style.RESET_ALL}")
    print(f"\t\t\t[Author : {Fore.GREEN}HackersBrain{Style.RESET_ALL}]")
    print()


def hlp():
    """ Uses Details """
    banner()
    print(" Usage :")
    print("\t python3 main.py <target> <start_port> <end_port>")
    print("\n\t   ex : python3 main.py 192.168.x.x 1 100\n")


def port_scan(port):
    """ Trying to connecting to ports using socket module """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((host, port))
    if not conn:
        print(f" Port {Fore.GREEN}{port}{Style.RESET_ALL} is OPEN")
    s.close()


# Functions

if len(sys.argv) != 4:
    hlp()
    sys.exit()

args = argparse.ArgumentParser()
args.add_argument("t", help="target")
args.add_argument("sp", help="starting_port", type=int)
args.add_argument("ep", help="ending_port", type=int)
act = args.parse_args()

if __name__ == '__main__':

    try:
        host = socket.gethostbyname(act.t)
    except socket.gaierror as hst_err:
        print(" Unable to Get The Target..")
        sys.exit()

    banner()
    print(f"\t Scanning Started... \tTarget : {Fore.GREEN}{host}{Style.RESET_ALL}\n")

    for port in range(act.sp, act.ep+1):
        thrd = threading.Thread(target=port_scan, args=(port,))
        thrd.start()
