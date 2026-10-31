import sys
import random
import math
import time
import os
from termcolor import colored
from colorama import Fore, Back, Style, init

universe_logs = [
    {
        "universe_number": '4378 C',
        "date": "2023-07-28",
        "location": "16.642577, 65.531059",
        "entries": [
            {"timestamp": "08:00 AM", "message": "Jumping to Universe 4378 C..."},
            {"timestamp": "08:10 AM", "message": "Scanning International databases..."},
            {"timestamp": "09:14 AM", "message": "Detected presence of 'REDACTED' (Version 4378-C)."},
            {"timestamp": "09:15 AM", "message": "'REDACTED' (Version 4378-A) is a Warrior, born and raised in Temoria, identity: nA "},
            {"timestamp": "09:20 AM", "message": "Inflection point is found: 1300 years ago"},
        ],
    },
    {
        "universe_number": '7623 A',
        "date": "2023-08-12",
        "location": "37.947859, -53.450664",
        "entries": [
            {"timestamp": "09:00 AM", "message": "Jumping to Universe 7623 A..."},
            {"timestamp": "09:10 AM", "message": "Scanning International databases...."},
            {"timestamp": "14:37 PM", "message": "Discovered 'REDACTED' (Version 7623 A)."},
            {"timestamp": "14:37 PM", "message": "'REDACTED' (Version 7623 A) is an underworld hacker specializing in taking down Cybercrimnals. Identity: nA"},
            {"timestamp": "14:48 PM", "message": "Notable deviation: Humanity has reached Type-2 systems"},
        ],
    },
    {
        "universe_number": '9125 A',
        "date": "2023-08-17",
        "location": "86.294906, 176.604630",
        "entries": [
            {"timestamp": "10:00 AM", "message": "Jumping to Universe 9125 A..."},
            {"timestamp": "10:10 AM", "message": "Scanning International databases...."},
            {"timestamp": "10:33 AM", "message": " No such name exists: 'REDACTED' (Version 9125 A)."},
            {"timestamp": "10:58 AM", "message": "Looking for temporal abnormailities under Manual Override"},
            {"timestamp": "16:07 PM", "message": "'REDACTED' (Version 9125 A) has traveled through time. Destination: nA, Identity: nA"},
        ],
    },
    {
        "universe_number": '0712 B',
        "date": "2023-09-27",
        "location": "54.696540, -26.806521",
        "entries": [
            {"timestamp": "1:30 AM", "message": "Jumping to Universe 0712 B..."},
            {"timestamp": "1:40 AM", "message": "Scanning International databases...."},
            {"timestamp": "10:45 AM", "message": " No such name exists: 'REDACTED' (Version 0712 B)."},
            {"timestamp": "12:46 PM", "message": "Looking for Rupture Protocols under Manual Override"},
            {"timestamp": "16:07 PM", "message": "Rupture protocols exist in 0712 B, REDACTED' (Version 0712 B) Exists, Identity: nA"},
        ],
    },
    {
        "universe_number": '0712 A',
        "date": "2023-09-28",
        "location": "-1.028745, 76.277908",
        "entries": [
            {"timestamp": "18:25 PM", "message": "Jumping to Universe 0712 B..."},
            {"timestamp": "18:35 PM", "message": "Scanning International databases...."},
            {"timestamp": "22:37 PM", "message": "'REDACTED' (Version 0712 B) Existence confirmed."},
            {"timestamp": "07:21 AM", "message": "REDACTED has found and boarded the Ship on Manual Control"},
            {"timestamp": "14:22 PM", "message": "REDACTED gives the Captain a fleet of Ships, Identity: nA"},
        ],
    },
]

init(autoreset=True)

on = 3
x_val = 77
rec_val = 543
ov = False
shield = 60
thrust = 0
cloak = False
course = ''
tf = 1.0
overridden = set()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_typing(text, delay=0.03, color=None):
    for char in text:
        time.sleep(delay)
        if color:
            print(colored(char, color), end='', flush=True)
        else:
            print(char, end='', flush=True)
    print()

def main_2():
    global rec_val, x_val
    clear()
    print(colored(">> Accessing Ship Control Interface... Success!", "green"))

    uses = [
        "Main Ship Controls",
        "SPC Reactor Systems",
        "Log System",
        "Navisys Controls",
        "TempoMod Systems"
    ]

    print()
    for use in uses:
        if use in ('Log System', 'SPC Reactor Systems'):
            print_with_typing(f"   - {use} : Available", delay=0, color="green")
        elif ov:
            print_with_typing(f"   - {use} : Unlocked", delay=0, color="magenta")
        else:
            print_with_typing(f"   - {use} : Denied", delay=0, color="red")
        time.sleep(0.3)

    print_with_typing(f"   - Drone Controls : Available", delay=0, color="green")
    print()
    print_with_typing("\n> Ready for remote operations. Enter commands:", color="cyan")
    print("   - 'open <controls>' - Opens target Controls.")
    print("   - 'debug_rupture' - Run diagnostic on temporal subroutines.")
    print("\n> Type 'help' for command list, or 'exit' to terminate.")
    fin = input("\n>")

    if fin.strip().lower() == 'debug_rupture':
        clear()
        print_with_typing(">> Running Rupture Diagnostic Subroutine...", color="cyan")
        time.sleep(1)
        print(colored(">> ERROR AT MEMORY ADDRESS 0x0712-B", "red"))
        print(colored(">> INTRUDER SIGNATURE DETECTED: VURG-0", "yellow"))
        print(colored(">> DECRYPTION HASH GENERATED: 0x777-MRAK-SECURE", "green"))
        print_with_typing("\n> Use token '777-MRAK-SECURE' in Web Terminal to verify link.", color="cyan")
        input("\nPress Enter to return...")
        return

    if is_override(fin):
        run_override(fin)
        return

    if fin.upper() == 'OPEN SPC REACTOR SYSTEMS' or fin.upper() == 'OPEN SPC':
        clear()
        print(colored(">> Access granted to SPC Reactor Systems.", "green"))
        print(f"Current Reactor Temp: {rec_val}°C")
        print(f"Power Output: {x_val}%")
        cmd = input("\nEnter command (change_temperature / adjust_output): ")
        if cmd.upper() == 'CHANGE_TEMPERATURE':
            rec_val = float(input("> Enter new temperature (°C): "))
            if rec_val == 777:
                print(colored("\n>> SPECIAL SYNC ACHIEVED! Web Verification Token: 777-MRAK-SECURE", "green"))
            else:
                print(colored(f">> Reactor temperature adjusted to {rec_val}°C", "green"))
            time.sleep(2)
        elif cmd.upper() == 'ADJUST_OUTPUT':
            x_val = float(input("> Enter new output (%): "))
            print(colored(f">> Power output set to {x_val}%", "green"))
            time.sleep(2)

def is_override(s):
    return s.strip().lower().replace(' ', '').startswith('override=')

def run_override(s):
    global ov
    key = s.split('=', 1)[1].strip().strip('"\'\u201c\u201d')
    if key.lower() != 'xl554-mrak-jm':
        print(colored(">> Override signature rejected. Attempt logged.", "red"))
        time.sleep(1.5)
        return
    clear()
    print_with_typing("> Decrypting council key XL554...", color="cyan")
    for _ in range(4):
        print(colored("   " + ''.join(random.choice('0123456789ABCDEF') for _ in range(40)), "magenta"))
        time.sleep(0.2)
    print(colored(">> Mirakilin Council seal verified. Operator: MRAK-JM", "green"))
    ov = True
    time.sleep(0.8)
    print_with_typing("\n>> COUNCIL OVERRIDE ACTIVE. ALL SYSTEMS UNLOCKED.", color="yellow")
    input("\n> ")

def main():
    clear()
    print_with_typing("> Initializing D-COM v4.77...", color="cyan")
    time.sleep(0.5)
    print_with_typing("> Establishing TOR connection...\n", color="cyan")
    time.sleep(0.5)
    print(colored(">> Connection established with TOR Network <<\n", "green"))
    print_with_typing("> PV13 KEY Found", color="cyan")

    if on == 3:
        for _ in range(2):
            print(colored(">> No Connection found on RUPTURE address<<", "red"))
            time.sleep(1)
        print(colored(">> Secure link established with incoming vessel...", "green"))
        time.sleep(1)
        while True:
            main_2()

if __name__ == "__main__":
    main()