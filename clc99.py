#coding:utf-8
#作者:99
from colorama import  init,Fore,Back,Style
import platform
import time

initsystem = False

#创建主类
def initsystem():
    """
    A function to init the system.
    """
    v_system = platform.system()
    if v_system != 'Windows':
        #print('other')
        initsystem=True
    else:
        init(wrap=True)
        #print('Windows')
        initsystem = True

def print_status(*args, full=False, end="\n"):
    """
    [*] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.BLUE + '[*]', end=' ')
        print(*args, end=end)
    else:
        print(Fore.BLUE + '[*]' + Fore.RESET, end=' ')
        print(*args, end=end)

def print_good(*args,full=False,end="\n"):
    """
    [+] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.BLUE+'[+]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.BLUE+'[+]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_error(*args,full=False,end="\n"):
    """
    [-] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.RED+'[-]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.RED+'[-]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_warning(*args,full=False,end="\n"):
    """
    [!] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.YELLOW+'[!]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.YELLOW+'[!]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_finish(*args,full=False,end="\n"):
    """
    [√] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.GREEN+'[√]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.GREEN+'[√]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_os(*args,full=False,end="\n"):
    """
    [$] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.CYAN+'[$]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.CYAN+'[$]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_notrun(*args,full=False,end="\n"):
    """
    [#] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.MAGENTA+'[#]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.MAGENTA+'[#]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_e(*args,full=False,end="\n"):
    """
    [ERROR] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.RED+'[ERROR]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.RED+'[ERROR]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_fileok(*args,full=False,end="\n"):
    """
    [.] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.BLUE+'[.]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.BLUE+'[.]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_filerror(*args,full=False,end="\n"):
    """
    [.] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.RED+'[.]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.RED+'[.]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_time(str='',timeformat="%Y-%m-%d %H:%M:%S",title='front',full=False,end="\n"):
    """
    [TIME] 2025-03-08 11:11:11

    :param full: The color fill or not fill the string
    :type full: bool

    :param timeformat: The time format, same as module 'time'
    :type timeformat: str

    :param title: The position of the symbol, you can use front, before, middle
    :param title: str

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        if title == 'front':
            print(Fore.CYAN+'[TIME]',end=' ')
            print(str+time.strftime(timeformat, time.localtime()))
        if title == 'before':
            print(Fore.CYAN+'[TIME]',end=' ')
            print(time.strftime(timeformat, time.localtime())+str)
        if title == 'middle':
            print(Fore.CYAN+'[TIME]',end=' ')
            print(str+time.strftime(timeformat, time.localtime())+str)
    else:
        if title == 'front':
            print(Fore.CYAN+'[TIME]'+Fore.RESET,end=' ')
            print(str+time.strftime(timeformat, time.localtime()))
        if title == 'before':
            print(Fore.CYAN+'[TIME]'+Fore.RESET,end=' ')
            print(time.strftime(timeformat, time.localtime())+str)
        if title == 'middle':
            print(Fore.CYAN+'[TIME]'+Fore.RESET,end=' ')
            print(str+time.strftime(timeformat, time.localtime())+str)

def print_music(*args,full=False,end="\n"):
    """
    [playmusic] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.GREEN+'[playmusic]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.GREEN+'[playmusic]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_video(*args,full=False,end="\n"):
    """
    [playvideo] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.GREEN+'[playvideo]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.GREEN+'[playvideo]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_ok(*args,full=False,end="\n"):
    """
    [OK] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.GREEN+'[OK]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.GREEN+'[OK]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_over(*args,full=False,end="\n"):
    """
    [OVER] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.WHITE+'[OVER]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.WHITE+'[OVER]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_admin(*args,full=False,end="\n"):
    """
    [Admin] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.CYAN+'[Admin]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.CYAN+'[Admin]'+Fore.RESET,end=' ')
        print(*args, end=end)

def input_str(str,full=False):
    """
    [input] please input your age:

    :param full: The color fill or not fill the string
    :type full: bool
    """
    if full:
        inp = input('[input]'+str)
        return inp
    else:
        inp = input('[input]'+str)
        return inp
    
def print_dirok(*args,full=False,end="\n"):
    """
    [/] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.GREEN+'[/]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.GREEN+'[/]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_direrror(*args,full=False,end="\n"):
    """
    [/] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.RED+'[/]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.RED+'[/]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_comok(*args,full=False,end="\n"):
    """
    [C] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.GREEN+'[C]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.GREEN+'[C]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_comerror(*args,full=False,end="\n"):
    """
    [C] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.RED+'[C]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.RED+'[C]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_uquestion(*args,full=False,end="\n"):
    """
    [?] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.YELLOW+'[?]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.YELLOW+'[?]'+Fore.RESET,end=' ')
        print(*args, end=end)

def print_cquestion(*args,full=False,end="\n"):
    """
    [?] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    """
    if full:
        print(Fore.RED+'[?]',end=' ')
        print(*args, end=end)
    else:
        print(Fore.RED+'[?]'+Fore.RESET,end=' ')
        print(*args, end=end)

if not platform.python_version() > "3.8":
    def user_color(title,color,full=False):
        #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
        """
    [B] Custom Symbol \n
    Usage:\n
    def customcolor(str):
        user_c = clc99.user_color('[b]','YELLOW')
        print(user_c+str)\n
    customcolor('Custom symbols')

    :param title: The symbol you want to add
    :type full: str

    :param color: Which color do you wanna choose, you can choose 'RED', 'BLACK', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE'
    :type end: str

    :param full: The color fill or not fill the string
    :type full: bool
    """
        if color=='RED':
            colorinfo=Fore.RED
        elif color=='BLACK':
            colorinfo=Fore.BLACK
        elif color=='GREEN':
            colorinfo=Fore.GREEN
        elif color=='YELLOW':
            colorinfo=Fore.YELLOW
        elif color=='BLUE':
            colorinfo=Fore.BLUE
        elif color=='MAGENTA':
            colorinfo=Fore.MAGENTA
        elif color=='CYAN':
            colorinfo=Fore.CYAN
        elif color=='WHITE':
            colorinfo=Fore.WHITE
        else:
            raise ValueError(f'Could not find the color called {color}.')
        
        if full:
            return colorinfo+title
        else:
            return colorinfo+title+Fore.RESET
else:
    from typing import Literal
    def user_color(title: str,color: Literal['RED', 'BLACK', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE'],full: bool=False) -> str:
        #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
        """
    [B] Custom Symbol \n
    Usage:\n
    def customcolor(str):
        user_c = clc99.user_color('[b]','YELLOW')
        print(user_c+str)\n
    customcolor('Custom symbols')

    :param title: The symbol you want to add
    :type full: str

    :param color: Which color do you wanna choose, you can choose 'RED', 'BLACK', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE'
    :type end: str

    :param full: The color fill or not fill the string
    :type full: bool
    """
        if color=='RED':
            colorinfo=Fore.RED
        elif color=='BLACK':
            colorinfo=Fore.BLACK
        elif color=='GREEN':
            colorinfo=Fore.GREEN
        elif color=='YELLOW':
            colorinfo=Fore.YELLOW
        elif color=='BLUE':
            colorinfo=Fore.BLUE
        elif color=='MAGENTA':
            colorinfo=Fore.MAGENTA
        elif color=='CYAN':
            colorinfo=Fore.CYAN
        elif color=='WHITE':
            colorinfo=Fore.WHITE
        else:
            raise ValueError(f'Could not find the color called {color}.')
        
        if full:
            return colorinfo+title
        else:
            return colorinfo+title+Fore.RESET
    
if __name__ == "__main__":
    print_good("Welcome to clc99!")