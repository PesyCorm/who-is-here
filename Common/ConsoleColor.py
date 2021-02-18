from termcolor import colored
import platform
support = True
if platform.system() == "Windows":
    if platform.version() >= "10.0.10586":
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    else:
        support = False


def out_red(text):
    if support:
        return colored(text, 'red')
    else:
        return text
def out_blue(text):
    if support:
        return colored(text, 'blue')
    else:
        return text
def out_cyan(text):
    if support:
        return colored(text, 'cyan')
    else:
        return text
def out_green(text):
    if support:
        return colored(text, 'green')
    else:
        return text
def out_blue_underline(text):
    if support:
        return colored(text, 'blue', attrs=['underline'])
    else:
        return text