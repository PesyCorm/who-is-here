import shutil
# import platform

support = True
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


def return_output(text, fill_sep):
    if support:
        columns, lines = shutil.get_terminal_size()
        string = "{:{fill}{align}{width}}"
        return string.format(f' {text} ', fill=fill_sep, align='^', width=columns)
    else:
        return fill_sep * 7 + f' {text} ' + fill_sep * 7