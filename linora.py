import os
import sys
import subprocess
from ollama import ask_ollama  # Импорт функции Ollama
from colorama import Fore, Style, init

# Инициализация colorama для цветного текста
init(autoreset=True)

# ASCII-арт лисёнка Оры
ORRY_ART = rf"""
{Fore.YELLOW}   /\_/\      {Fore.CYAN}Welcome to {Fore.GREEN}Linora{Fore.CYAN}!
{Fore.YELLOW}  ( o.o )     {Fore.CYAN}Type {Fore.GREEN}'help'{Fore.CYAN} to start.
{Fore.YELLOW}   > ^ <      {Fore.CYAN}Version {Fore.GREEN}1.0.0
"""

def print_help():
    print(f"{Fore.CYAN}Available commands:")
    print(f"{Fore.GREEN}help{Fore.CYAN} - Show this help message")
    print(f"{Fore.GREEN}exit{Fore.CYAN} - Exit Linora")
    print(f"{Fore.GREEN}ollama <question>{Fore.CYAN} - Ask Ollama a question")
    print(f"{Fore.GREEN}linux <command>{Fore.CYAN} - Run Linux commands (via WSL)")
    print(f"{Fore.GREEN}explorer{Fore.CYAN} - Open Linora Explorer")
    print(f"{Fore.GREEN}lpm <install|uninstall> <package>{Fore.CYAN} - Manage packages")

def run_linux_command(command):
    try:
        result = subprocess.run(["wsl"] + command.split(), capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{Fore.CYAN}{result.stdout}")
        else:
            print(f"{Fore.RED}Error: {result.stderr}")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")

def main():
    print(ORRY_ART)
    while True:
        try:
            command = input(f"{Fore.GREEN}linora>{Style.RESET_ALL} ").strip()
            if command == "help":
                print_help()
            elif command == "exit":
                print(f"{Fore.CYAN}Goodbye!")
                break
            elif command.startswith("ollama"):
                question = command[len("ollama"):].strip()
                if question:
                    print(f"{Fore.CYAN}Ollama: {ask_ollama(question)}")
                else:
                    print(f"{Fore.RED}Error: Please ask a question.")
            elif command.startswith("linux"):
                linux_command = command[len("linux"):].strip()
                if linux_command:
                    run_linux_command(linux_command)
                else:
                    print(f"{Fore.RED}Error: Please enter a Linux command.")
            elif command == "explorer":
                os.system("python linora_explorer.py")
            elif command.startswith("lpm"):
                args = command[len("lpm"):].strip().split()
                if len(args) >= 2:
                    package = args[1]
                    if args[0] == "install":
                        print(f"{Fore.CYAN}Installing {package}...")
                        os.system(f"pip install {package}")
                    elif args[0] == "uninstall":
                        print(f"{Fore.CYAN}Uninstalling {package}...")
                        os.system(f"pip uninstall {package}")
                    else:
                        print(f"{Fore.RED}Error: Unknown lpm command.")
                else:
                    print(f"{Fore.RED}Error: Invalid lpm syntax.")
            else:
                print(f"{Fore.RED}Error: Command '{command}' not found.")
        except KeyboardInterrupt:
            print(f"\n{Fore.CYAN}Goodbye!")
            break

if __name__ == "__main__":
    main()