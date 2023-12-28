import sys
import time
import os
import time
from termcolor import colored
import time
from colorama import Fore, Back, Style, init

# Initialize colorama for colored text
init(autoreset=True)

on=3
universe_logs = [
    {
        "universe_number": '4378 C',
        "date": "2023-07-28",
        "location": "16.642577, 65.531059",
        "entries": [
            {
                "timestamp": "08:00 AM",
                "message": "Jumping to Universe 4378 C...",
            },
            {
                "timestamp": "08:10 AM",
                "message": "Scanning International databases...",
            },
            {
                "timestamp": "09:14 AM",
                "message": "Detected presence of 'James Mirakilin' (Version 4378-C).",
            },
            {
                "timestamp": "09:15 AM",
                "message": "'James Mirakilin' (Version 4378-A) is a Warrior, born and raised in Temoria, identity: nA ",
            },
            {
                "timestamp": "09:20 AM",
                "message": "Inflection point is found: 1300 years ago",
            },
        ],
    },
    {
        "universe_number": '7623 A',
        "date": "2023-08-12",
        "location": "37.947859, -53.450664",
        "entries": [
            {
                "timestamp": "09:00 AM",
                "message": "Jumping to Universe 7623 A...",
            },
            {
                "timestamp": "09:10 AM",
                "message": "Scanning International databases....",
            },
            {
                "timestamp": "14:37 PM",
                "message": "Discovered 'James Mirakilin' (Version 7623 A).",
            },
            {
                "timestamp": "14:37 PM",
                "message": "'James Mirakilin' (Version 7623 A) is an underworld hacker specializing in taking down Cybercrimnals. Identity: nA",
            },
            {
                "timestamp": "14:48 PM",
                "message": "Notable deviation: Humanity has reached Type-2 systems",
            },
        ],
    },
    {
        "universe_number": '9125 A',
        "date": "2023-08-17",
        "location": "86.294906, 176.604630",
        "entries": [
            {
                "timestamp": "10:00 AM",
                "message": "Jumping to Universe 9125 A...",
            },
            {
                "timestamp": "10:10 AM",
                "message": "Scanning International databases....",
            },
            {
                "timestamp": "10:33 AM",
                "message": " No such name exists: 'James Mirakilin' (Version 9125 A).",
            },
            {
                "timestamp": "10:58 AM",
                "message": "Looking for temporal abnormailities under Manual Override",
            },
            {
                "timestamp": "16:07 PM",
                "message": "'James Mirakilin' (Version 9125 A) has traveled through time. Destination: nA, Identity: nA",
            },
        ],
    },
    {
        "universe_number": '0712 B',
        "date": "2023-09-27",
        "location": "54.696540, -26.806521",
        "entries": [
            {
                "timestamp": "1:30 AM",
                "message": "Jumping to Universe 0712 B...",
            },
            {
                "timestamp": "1:40 AM",
                "message": "Scanning International databases....",
            },
            {
                "timestamp": "10:45 AM",
                "message": " No such name exists: 'James Mirakilin' (Version 0712 B).",
            },
            {
                "timestamp": "12:46 PM",
                "message": "Looking for Rupture Protocols under Manual Override",
            },
            {
                "timestamp": "16:07 PM",
                "message": "Rupture protocols exist in 0712 B, James Mirakilin' (Version 0712 B) Exists, Identity: nA",
            },
        ],
    },
    {
        "universe_number": '0712 A',
        "date": "2023-09-28",
        "location": "-1.028745, 76.277908",
        "entries": [
            {
                "timestamp": "18:25 PM",
                "message": "Jumping to Universe 0712 B...",
            },
            {
                "timestamp": "18:35 PM",
                "message": "Scanning International databases....",
            },
            {
                "timestamp": "22:37 PM",
                "message": "'James Mirakilin' (Version 0712 B) Existence confirmed.",
            },
            {
                "timestamp": "07:21 AM",
                "message": "James Mirakilin has found and boarded the Ship on Manual Control",
            },
            {
                "timestamp": "14:22 PM",
                "message": "James Mirakilin gives the Captain a fleet of Ships, Identity: nA",
            },
        ],
    },
]

def clear():
    os.system( 'cls' )

def print_with_typing(text, delay=0.04, color=None):
    for char in text:
        time.sleep(delay)
        if color:
            print(colored(char, color), end='', flush=True)
        else:
            print(char, end='', flush=True)
    print()

def main_2():
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
        if use=='Log System':
            print_with_typing(f"   - {use} : Available", delay=0,color="green")
            time.sleep(0.7)
        else:
            print_with_typing(f"   - {use} : Denied", delay=0,color="red")
            time.sleep(0.7)

    print_with_typing(f"   - Drone Controls : Available", delay=0, color="green")
    print()
    print_with_typing("\n> Ready for remote operations. Enter commands:", color="cyan")
    print("   - 'scan_area <coordinates>' - Perform reconnaissance.")
    print("   - 'capture_data <target>' - Collect data.")
    print("   - 'open <controls>' - Opens target Controls.")
    print("   - 'engage_target <target>' - Engage specified target.")
    print("   - 'select <target>' - Use target program.")
    print("   - 'return_home <target>' - Return to base.")
    print("\n> Type 'help' for command list, or 'exit' to terminate.")
    fin=input("\n>")

    if fin.upper()=='OPEN DRONE CONTROLS':

        print(colored(">> Scanning for available drones...\n", "green"))

        time.sleep(1)

        print(colored(">> 5 drones detected in proximity:", "green"))
        print()
        time.sleep(1)

        drones = [
            "Drone ID: DRN-875",
            "Drone ID: DRN-934",
            "Drone ID: DRN-177",
            "Drone ID: DRN-591",
            "Drone ID: DRN-054",
        ]

        for drone in drones:
            print_with_typing(f"   - {drone}", color="green")

        print_with_typing("\n> Ready for remote operations. Enter commands:", color="cyan")
        print("   - 'scan_area <drone Number>' - Target Drone Performs surrounding area reconnaissance.")
        print("   - 'capture_data <drone Number>' - Target Drone Collect data on Ship exterior.")
        print("   - 'override <drone Number>' - Overrides target Drone.")
        print("   - 'engage_target <drone Number> <target>' - Target Drone Engage specified target.")
        print("   - 'destroy <drone number>' - Destroys specified Drone.")
        print("   - 'return_home <drone number>' - Target Drone Return to base.")
        print("\n> Type 'help' for command list, or 'exit' to terminate.")
        sen=input("\n>")
        l=sen.split()
        cmd=l[0]
        dno=int(l[1])
        extra=''
        try:
            extra=l[2]
        except:
            print()
    
        if cmd.upper()=='SCAN_AREA':
            time.sleep(1)
            print(colored(">> Initiating area scan...", "green"))
            print(colored(">> Scanning in progress...", "green"))
            time.sleep(1)

            print_with_typing(f"   - Drone ID: DRN-{drone}: Scan complete. Results stored.", color="green")
            time.sleep(0.5)

            print_with_typing("\n> Scanning results available. Enter 'show_results' to display.", color="cyan")
            time.sleep(1)
            thre=input("\n>")
            if thre.upper()=='SHOW_RESULTS':
                scan_results = {
                    f"DRN-{dno}": {
                    "Environmental Data": "Clear skies, High Humidity, Moderate temperature.",
                    "Life forms Detected": "High Concentrations of aquatic lifeforms",}}
                for drone, data in scan_results.items():
                    print_with_typing(f"   - {drone}:", color="green")
                    for key, value in data.items():
                        print_with_typing(f"     - {key}: {value}", color="green")
                    time.sleep(0.5)

            print("\n> Scan results displayed. Enter any Key to return to HOME INTERFACE")
            input("\n>_")
        elif cmd.upper()=='CAPTURE_DATA':
            print(colored(">> Initiating data capture on the ship exterior...", "green"))
            print(colored(">> Data capture in progress...", "green"))
            time.sleep(3)

            print_with_typing(f"   - Drone ID: DRN-{dno}: Data capture complete.", color="green")
            time.sleep(0.5)

            print_with_typing("\n> Data capture results available. Enter 'analyze_data' to process data.", color="cyan")
            time.sleep(1)

            thre=input("\n>")
            print()
            time.sleep(1)
            print(colored(f">> Analyzing DRN-{dno}:captured data...", "green"))
            time.sleep(2)

            print("\n> Data analysis complete. Displaying results:")
            print("\n[Ship Exterior Data Analysis]")
            print(" - Hull Integrity: 95%")
            print(" - Cloaking Signature: Normal")
            print(" - External Temperature: 25°C")
            print(" - Radiation Levels: Backgorund")

            print("\n> Analysis results displayed. Further actions can be taken as needed.")
            input("\n>")
            
            emer='''
            ===================================================================================
            WARNING! SPC Reactor and TempoMod Systems have been activated! JUMP IMMINENT!   
            ===================================================================================

                    DATA:
                        Depart Time: 18:23 CEST 
                        Depart Location: Otherworld 0712-B

                        Arrival Destination: Otherworld 0712-A

                        SPC Reactor Temperature: 543°C
                        TempMod system capacity: 83%

            ===================================================================================
                    ALL REMOTE CAPABILITIES WILL TURN OFF IN 5 SECONDS!
            ===================================================================================
            '''

            print_with_typing(emer,delay=0,color='red')
        elif cmd.upper()=='OVERRIDE':
            print()
        elif cmd.upper()=='ENGAGE_TARGET':
            print()         

    elif fin.upper()=='OPEN LOG SYSTEM':
        logs(universe_logs)

    

def main():
    clear()
    time.sleep(1)
    print_with_typing("> Initializing D-COM v4.77...", color="cyan")
    time.sleep(0.8)
    print_with_typing("> Establishing secure TOR connection...\n", color="cyan")
    time.sleep(1)

    print(colored(">> Connection established with TOR Network <<\n", "green"))
    
    print_with_typing("> PV13 KEY Found", color="cyan")
    print_with_typing("> Establishing Connection with RUPTURE KEY PV13...\n", color="cyan")

    if on==1:
        time.sleep(2)
        print(colored(">> Connection established K.S Network <<\n", "green"))

        print('Initialization required')
        t=input("> ")
        if not t.upper()=='INITIALIZE':
            print_with_typing('>> ERROR!',delay=0,color='red')
            sys.exit()
        print_with_typing("> Initiating Ship Control Interface...", color="cyan")
        time.sleep(0.7)

        while True:
            main_2()

    elif on==2:
       time.sleep(2)
       while True:
        print(colored(">> No Connection found on RUPTURE address<<", "red")) 
        print(colored("> Retrying in 5 seconds......."))
        print()
        time.sleep(5)

    elif on==3:
        time.sleep(2)

        for k in range(4):
            print(colored(">> No Connection found on RUPTURE address<<", "red")) 
            print(colored("> Retrying in 5 seconds......."))
            print()
            time.sleep(5)

        print(colored(">> Unauthorized incoming connection detected! Attempting to find source...", "red"))
        time.sleep(2)

        print(colored(">> Source of connection: Unknown", "red"))
        print(colored(">> Establishing secure link with incoming vessel...", "green"))
        time.sleep(2)

        print(colored(">> Secure link established"))
        print()

        print(colored("> Unknown Swarm of Ships Detected:", "red"))
        print()
        time.sleep(1)

        unknown_ships = [
            "Ship ID: Unidentified Vessel 001",
            "Ship ID: Unidentified Vessel 002",
            "Ship ID: Unidentified Vessel 003",
            "Ship ID: Unidentified Vessel 004",
            "Ship ID: Unidentified Vessel 005",
        ]

        for ship in unknown_ships:
            print_with_typing(f"   - {ship}", color="cyan")
            time.sleep(0.5)

        print_with_typing("\n> Analyzing incoming data...", color="cyan")
        time.sleep(1)

        print(colored(">> Data packets received from Unknown Fleet:", "yellow"))
        print(colored("   - Decrypting data...", "yellow"))
        time.sleep(1)
        print(colored("   - Analyzing data...", "yellow"))
        time.sleep(2)

        print(colored("[Data Analysis]", "yellow"))
        print(colored(" - Source: Unknown", "yellow"))
        print(colored(" - Content: Unknown", "yellow"))


        print_with_typing("\n> Ready for operations. Enter commands:", color="cyan")
        print("   - 'trasnmit_inquiry' - Transmits a message to the unkonwn Fleet.")
        print("   - 'return_home' - Returns back to D-COM home")
        print("\n> Type 'help' for command list, or 'exit' to terminate.")
        sen=input("\n>")

        if sen.upper()=='TRANSMIT_INQUIRY':
            print_with_typing("\n> Transmitting a secure inquiry...", color="cyan")
            time.sleep(1)

            print(colored("> Secure communication channel established", "cyan"))
            print()
            print(colored(">> Attention, Unknown Fleet. This is James Mirakilin of the 6 Mirakilin Council"))
            print(colored(">> Please identify yourselves and state your intentions on this world."))
            print()
            print(colored("> Awaiting response from the Unknown Fleet...", "green"))
            print()
            print(colored(">> COMMUNICATIONS HAVE BEEN SWITCHED OFF IN THE UNKOWN FLEET! <<", color='red'))

            time.sleep(2)

            input("\n> ")

    else:
        print(colored(">> NO CONNECTIONS FOUND! <<", "red"))
        input('\n> ')
        sys.exit()

    '''
            print_with_typing("\n> Selecting target drones for connection...", color="cyan")
            time.sleep(1)

            for drone in drones:
                print(colored(f">> Connecting to {drone}... Success!", "green"))
                time.sleep(0.5)

            print(colored("\n> Establishing command link...", "cyan"))
            time.sleep(1)

            print(colored(">> Command link established with all target drones <<", "green"))
            print()

            print_with_typing("> Hacking drone systems...", color="cyan")
            time.sleep(1)

            for drone in drones:
                print(colored(f">> Overriding security protocols for {drone}... Success!", "green"))
                time.sleep(0.5)

            print(colored("\n> Drone Control Panel:", "cyan"))
            time.sleep(1)

            for drone in drones:
                print_with_typing(f"   - {drone}: Online", color="green")
                time.sleep(0.5)

            print_with_typing("\n> Ready for remote operations. Enter commands:", color="cyan")
            print("   - 'scan_area <coordinates>' - Perform reconnaissance.")
            print("   - 'capture_data <target>' - Collect data.")
            print("   - 'engage_target <target>' - Engage specified target.")
            print("   - 'return_home <target>' - Return to base.")
            print("\n> Type 'help' for command list, or 'exit' to terminate.")
            print("\n>_")
            '''

def format_log_entry(timestamp, message):
    return f"{Fore.CYAN}[{timestamp}] {Fore.RESET}{message}"

def logs(logs):
    clear()
    for log in logs:
        print(f"{Fore.YELLOW}========================================{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}LOG OF THE CRYSTAL SHIP 065 {Fore.RESET}")
        print(f"{Fore.YELLOW}========================================{Fore.RESET}\n")

        print(f"{Fore.LIGHTWHITE_EX}Universe Log - Universe {log['universe_number']}{Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}----------------------------------------{Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}Date: {log['date']}{Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}Location: {log['location']}{Fore.RESET}\n")

        for entry in log['entries']:
            print(format_log_entry(entry['timestamp'], entry['message']))
            time.sleep(1)  # Pause for dramatic effect
            print()

        print(f"{Fore.LIGHTWHITE_EX}End of Log{Fore.RESET}")
        print(f"{Fore.YELLOW}========================================{Fore.RESET}\n")
    input('> ')
    clear()

if __name__ == "__main__":
    main()
