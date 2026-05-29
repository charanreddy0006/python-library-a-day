from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

print(Fore.GREEN + "Success: Program executed successfully!")

print(Fore.RED + "Error: Something went wrong!")

print(Fore.YELLOW + "Warning: Check your input.")

print(Fore.CYAN + "Info: Loading data...")

print(Back.BLUE + Fore.WHITE + "Python Colorama Example")

print(Style.BRIGHT + Fore.MAGENTA + "Bright Colored Text")