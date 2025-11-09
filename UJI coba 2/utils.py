import os
from colorama import Fore, Style, init
init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(text):
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + text.center(60))
    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)

def info(msg):
    print(Fore.GREEN + msg + Style.RESET_ALL)

def warning(msg):
    print(Fore.RED + msg + Style.RESET_ALL)

def prompt(msg):
    return Fore.MAGENTA + msg + Style.RESET_ALL
