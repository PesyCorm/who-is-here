# from termcolor import colored
# import platform

# support = True
# if platform.system() == "Windows":
#     if int(platform.release()) >= 10:
#         if platform.version() >= "10.0.10586":
#             import ctypes

#             kernel32 = ctypes.windll.kernel32
#             kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
#         else:
#             support = False
#     else:
#         support = False
from colorama import init, Fore, Back, Style


init(autoreset=True)

def out_fore_red(text):
    return (Fore.RED + text)
def out_fore_blue(text):
    return (Fore.BLUE + text)
def out_fore_cyan(text):
    return (Fore.CYAN + text)
def out_fore_green(text):
    return (Fore.GREEN + text)
def out_back_red(text):
    return (Back.RED + text)
def out_back_blue(text):
    return (Back.BLUE + text)
def out_back_cyan(text):
    return (Back.CYAN + text)
def out_back_green(text):
    return (Back.GREEN + text)