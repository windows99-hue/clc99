#coding:utf-8
#Author:99
from colorama import  init,Fore,Back,Style
import platform
import time
import sys
from io import StringIO
from functools import wraps

initsystem = False

__version__ = "2.3.post1"

class FAILEDException(Exception):
    # This is a custom exception class for handling the err().
    pass

def err99(error_text="FAILED",text=""):
    """The err99 function in loading99 can interrupt function execution and output an error message similar to FAILED in the loading99 decorator.
    
    :param text: The error message to be displayed.
    :type text: str
    :param error_text:  The prefix for the error message. Default is "FAILED".
    :type error_text: str
    """
    errmessage = FAILEDException(error_text)
    errmessage.errortext = text #把错误信息存到属性里
    raise errmessage

#Main Functions
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

def print_status(*args, full=False, end="\n", file=None, sep=" "):
    """
    [*] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.BLUE + '[*]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.BLUE + '[*]' + Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_good(*args, full=False, end="\n", file=None, sep=" "):
    """
    [+] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.CYAN+'[+]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.CYAN+'[+]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_error(*args, full=False, end="\n", file=None, sep=" "):
    """
    [-] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.RED+'[-]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.RED+'[-]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_warning(*args, full=False, end="\n", file=None, sep=" "):
    """
    [!] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.YELLOW+'[!]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.YELLOW+'[!]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_finish(*args, full=False, end="\n", file=None, sep=" "):
    """
    [FINISH] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.GREEN+'[FINISH]', end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)
    else:
        print(Fore.GREEN+'[FINISH]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_os(*args, full=False, end="\n", file=None, sep=" "):
    """
    [$] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.CYAN+'[$]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.CYAN+'[$]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_notrun(*args, full=False, end="\n", file=None, sep=" "):
    """
    [#] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.MAGENTA+'[#]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.MAGENTA+'[#]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_e(*args, full=False, end="\n", file=None, sep=" "):
    """
    [ERROR] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.RED+'[ERROR]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.RED+'[ERROR]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_fileok(*args, full=False, end="\n", file=None, sep=" "):
    """
    [.] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.BLUE+'[.]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.BLUE+'[.]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_filerror(*args, full=False, end="\n", file=None, sep=" "):
    """
    [.] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.RED+'[.]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.RED+'[.]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_time(str='', timeformat="%Y-%m-%d %H:%M:%S", title='front', full=False, end="\n", file=None, sep=" "):
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
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        if title == 'front':
            print(Fore.CYAN+'[TIME]', end=' ', file=file)
            print(str+time.strftime(timeformat, time.localtime()) + Fore.RESET, file=file)
        if title == 'before':
            print(Fore.CYAN+'[TIME]', end=' ', file=file)
            print(time.strftime(timeformat, time.localtime())+str + Fore.RESET, file=file)
        if title == 'middle':
            print(Fore.CYAN+'[TIME]', end=' ', file=file)
            print(str+time.strftime(timeformat, time.localtime())+str + Fore.RESET, file=file)
    else:
        if title == 'front':
            print(Fore.CYAN+'[TIME]'+Fore.RESET, end=' ', file=file)
            print(str+time.strftime(timeformat, time.localtime()), file=file)
        if title == 'before':
            print(Fore.CYAN+'[TIME]'+Fore.RESET, end=' ', file=file)
            print(time.strftime(timeformat, time.localtime())+str, file=file)
        if title == 'middle':
            print(Fore.CYAN+'[TIME]'+Fore.RESET, end=' ', file=file)
            print(str+time.strftime(timeformat, time.localtime())+str, file=file)

def print_music(*args, full=False, end="\n", file=None, sep=" "):
    """
    [playmusic] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.GREEN+'[playmusic]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.GREEN+'[playmusic]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_video(*args, full=False, end="\n", file=None, sep=" "):
    """
    [playvideo] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.GREEN+'[playvideo]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.GREEN+'[playvideo]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_ok(*args, full=False, end="\n", file=None, sep=" "):
    """
    [OK] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.GREEN+'[OK]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.GREEN+'[OK]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_over(*args, full=False, end="\n", file=None, sep=" "):
    """
    [OVER] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.WHITE+'[OVER]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.WHITE+'[OVER]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_admin(*args, full=False, end="\n", file=None, sep=" "):
    """
    [Admin] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.CYAN+'[Admin]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.CYAN+'[Admin]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def input_str(str, full=False, file=None):
    """
    [input] please input your age:

    :param full: The color fill or not fill the string
    :type full: bool
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    """
    if full:
        inp = input('[input]'+str + Fore.RESET)
        return inp
    else:
        inp = input('[input]'+str)
        return inp

def print_dirok(*args, full=False, end="\n", file=None, sep=" "):
    """
    [/] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.GREEN+'[/]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.GREEN+'[/]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_direrror(*args, full=False, end="\n", file=None, sep=" "):
    """
    [/] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.RED+'[/]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.RED+'[/]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_comok(*args, full=False, end="\n", file=None, sep=" "):
    """
    [C] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.GREEN+'[C]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.GREEN+'[C]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_comerror(*args, full=False, end="\n", file=None, sep=" "):
    """
    [C] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.RED+'[C]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.RED+'[C]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_uquestion(*args, full=False, end="\n", file=None, sep=" "):
    """
    [?] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.YELLOW+'[?]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.YELLOW+'[?]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

def print_cquestion(*args, full=False, end="\n", file=None, sep=" "):
    """
    [?] hi!

    :param full: The color fill or not fill the string
    :type full: bool

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The separator between arguments, default is space
    :type sep: str
    """
    if full:
        print(Fore.RED+'[?]', end=' ', file=file)
        print(*args, Fore.RESET, end=end, file=file, sep=sep)
    else:
        print(Fore.RED+'[?]'+Fore.RESET, end=' ', file=file)
        print(*args, end=end, file=file, sep=sep)

if not platform.python_version() > "3.8":
    def user_color(title, color, full=False):
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
    def user_color(title: str, color: Literal['RED', 'BLACK', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE'], full: bool=False) -> str:
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
        
def __green(text):
    return Fore.GREEN + text + Fore.RESET

def __red(text):
    return Fore.RED + text + Fore.RESET

def __yellow(text):
    return Fore.YELLOW + text + Fore.RESET

def loading99(text="", success_text="OK", except_text="EXCEPT", suppress_output=True, output_success_text=True):
    """
    A decorator to display loading status and handle output suppression.
    
    Args:
        text (str): Loading display text, uses function name if empty
        success_text (str): Text to display on successful execution
        except_text (str): Text to display when exception occurs
        suppress_output (bool): Whether to suppress function's print output
        output_success_text (bool): Whether to display success text
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            display_text = text if text != "" else func.__name__
            
            if text == "":
                print("\"" + display_text + "\" is running......", end="", flush=True)
            else:
                print(display_text, end="", flush=True)
            
            if suppress_output:
                captured_output = StringIO()
                original_stdout = sys.stdout
                sys.stdout = captured_output
                
                try:
                    r = func(*args, **kwargs)
                except FAILEDException as e:
                    sys.stdout = original_stdout
                    eprofix = str(e)
                    emessage = getattr(e, 'errortext', '')
                    if emessage:
                        emessage = ": " + emessage
                    print(__red(eprofix+emessage), flush=True)
                    return
                except:
                    sys.stdout = original_stdout
                    print(__yellow(except_text), flush=True)
                    raise
                finally:
                    sys.stdout = original_stdout
            else:
                print("") # 填充换行
                try:
                    r = func(*args, **kwargs)
                except FAILEDException as e:
                    eprofix = str(e)
                    emessage = getattr(e, 'errortext', '')
                    if emessage:
                        emessage = ": " + emessage
                    print(__red(eprofix+emessage), flush=True)
                    return
                except:
                    print(__yellow("EXCEPTION OCCURRED!"), flush=True)
                    raise

            if output_success_text:
                print(__green(success_text), flush=True)
            
            return r
        return wrapper
    return decorator


if __name__ == "__main__":
    print_good(f"Welcome to clc99! Version:{__version__}")