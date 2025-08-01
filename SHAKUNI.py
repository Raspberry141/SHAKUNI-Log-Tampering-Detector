from pyfiglet import figlet_format
from colorama import Fore, Style

print(Fore.MAGENTA + figlet_format("SHAKUNI"))
print(Fore.RED + "[*] Created by Vizz\n" + Style.RESET_ALL)

def detect_log_tampering(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        if lines[i] < lines[i-1]:
            print(Fore.RED + f"[!] Suspicious entry disorder at line {i+1}" + Style.RESET_ALL)

    print(Fore.GREEN + "[+] Log integrity check complete" + Style.RESET_ALL)

detect_log_tampering("eventlog.txt")