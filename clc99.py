#coding:utf-8
#Author:99
from colorama import just_fix_windows_console, Fore, Back, Style
import time
from io import StringIO
from functools import wraps
from contextlib import redirect_stdout, ExitStack

just_fix_windows_console()

__version__ = "2.4.0"

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
def _print_message(args, symbol, color, full=False, end="\n", file=None, sep=" ",
                   reset_full=True, reset_as_arg=True, message_factory=None):
    print(color + symbol + ("" if full else Fore.RESET), end=" ", file=file)
    if message_factory is not None:
        args = (message_factory(),)
    if full and reset_full:
        if reset_as_arg:
            args = (*args, Fore.RESET)
        else:
            args = (args[0] + Fore.RESET,)
    print(*args, end=end, file=file, sep=sep)


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
    _print_message(args, '[*]', Fore.BLUE, full, end, file, sep)

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
    _print_message(args, '[+]', Fore.CYAN, full, end, file, sep)

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
    _print_message(args, '[-]', Fore.RED, full, end, file, sep)

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
    _print_message(args, '[!]', Fore.YELLOW, full, end, file, sep)

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
    _print_message(args, '[FINISH]', Fore.GREEN, full, end, file, sep, reset_full=False)

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
    _print_message(args, '[$]', Fore.CYAN, full, end, file, sep)

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
    _print_message(args, '[#]', Fore.MAGENTA, full, end, file, sep)

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
    _print_message(args, '[ERROR]', Fore.RED, full, end, file, sep)

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
    _print_message(args, '[.]', Fore.BLUE, full, end, file, sep)

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
    _print_message(args, '[.]', Fore.RED, full, end, file, sep)

def print_time(text='', timeformat="%Y-%m-%d %H:%M:%S", title=None, full=False, end="\n", file=None, sep=" ",
               position=None, **old_names):
    """
    [TIME] 2025-03-08 11:11:11

    :param text: The text with the time, it was called 'str' before, that old name still works
    :type text: str

    :param full: The color fill or not fill the string
    :type full: bool

    :param timeformat: The time format, same as module 'time'
    :type timeformat: str

    :param position: The position of the time, you can use 'front', 'before' or 'middle'. It was called 'title' before, both names work.
    :type position: str

    :param end: The same as print(end="")
    :type end: str
    
    :param file: The output file, default is sys.stdout
    :type file: file object
    
    :param sep: The same as print(sep=""). print_time only prints one message, so it joins nothing and changes nothing.
    :type sep: str
    """
    if 'str' in old_names: # the old name of 'text'
        old_text = old_names.pop('str')
        if text != '' and text != old_text:
            raise TypeError("print_time() got both 'text' and the old 'str', please pass only one of them")
        text = old_text
    if old_names:
        raise TypeError(f"print_time() got an unexpected keyword argument '{list(old_names)[0]}', "
                        "the arguments are: text, timeformat, title, full, end, file, sep, position")

    if position is None: # 'title' is the old name of 'position'
        position = 'front' if title is None else title
    elif title is not None and title != position:
        raise ValueError("'position' and 'title' are the same argument, please pass only one of them")

    if position == 'front':
        message_factory = lambda: text + time.strftime(timeformat, time.localtime())
    elif position == 'before':
        message_factory = lambda: time.strftime(timeformat, time.localtime()) + text
    elif position == 'middle':
        message_factory = lambda: text + time.strftime(timeformat, time.localtime()) + text
    else:
        raise ValueError(f"position (title) must be 'front', 'before' or 'middle', not {position!r}")

    _print_message((), '[TIME]', Fore.CYAN, full, end=end, file=file, sep=sep,
                   reset_as_arg=False, message_factory=message_factory)

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
    _print_message(args, '[playmusic]', Fore.GREEN, full, end, file, sep)

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
    _print_message(args, '[playvideo]', Fore.GREEN, full, end, file, sep)

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
    _print_message(args, '[OK]', Fore.GREEN, full, end, file, sep)

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
    _print_message(args, '[OVER]', Fore.WHITE, full, end, file, sep)

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
    _print_message(args, '[Admin]', Fore.CYAN, full, end, file, sep)

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
    _print_message(args, '[/]', Fore.GREEN, full, end, file, sep)

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
    _print_message(args, '[/]', Fore.RED, full, end, file, sep)

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
    _print_message(args, '[C]', Fore.GREEN, full, end, file, sep)

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
    _print_message(args, '[C]', Fore.RED, full, end, file, sep)

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
    _print_message(args, '[?]', Fore.YELLOW, full, end, file, sep)

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
    _print_message(args, '[?]', Fore.RED, full, end, file, sep)

_COLOR_CODES = {
    'BLACK': Fore.BLACK,
    'RED': Fore.RED,
    'GREEN': Fore.GREEN,
    'YELLOW': Fore.YELLOW,
    'BLUE': Fore.BLUE,
    'MAGENTA': Fore.MAGENTA,
    'CYAN': Fore.CYAN,
    'WHITE': Fore.WHITE,
    'RESET': Fore.RESET,
    'LIGHTBLACK': Fore.LIGHTBLACK_EX,
    'LIGHTRED': Fore.LIGHTRED_EX,
    'LIGHTGREEN': Fore.LIGHTGREEN_EX,
    'LIGHTYELLOW': Fore.LIGHTYELLOW_EX,
    'LIGHTBLUE': Fore.LIGHTBLUE_EX,
    'LIGHTMAGENTA': Fore.LIGHTMAGENTA_EX,
    'LIGHTCYAN': Fore.LIGHTCYAN_EX,
    'LIGHTWHITE': Fore.LIGHTWHITE_EX,
}

def _color_code(color):
    """Turn a color name like 'cyan' into the code of colorama.

    :param color: The color name, it doesn't matter that you use 'cyan', 'CYAN' or 'Cyan'
    :type color: str

    :return: The code of colorama, it can also be a code like Fore.CYAN
    :rtype: str
    """
    if isinstance(color, str):
        if color in _COLOR_CODES:
            return _COLOR_CODES[color]
        if color.startswith("\x1b"): # A code of colorama, like Fore.CYAN
            return color
        name = color.strip().upper().replace("_", "").replace("-", "").replace(" ", "")
        if name in _COLOR_CODES:
            return _COLOR_CODES[name]
    raise ValueError(f'Could not find the color called {color}.')

def make_printer(symbol, color="cyan"):
    """
    Make a printer with your own symbol and color, then use it just like print_status. \n
    Usage:\n
    upload = clc99.make_printer("[UPLOAD]", color="cyan")
    upload("foo.png")\n
    [UPLOAD] foo.png

    :param symbol: The symbol of the printer, e.g. "[UPLOAD]"
    :type symbol: str

    :param color: The color of the symbol, you can choose 'BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE', and the light ones like 'LIGHTRED'. The default is 'cyan'.
    :type color: str

    :return: A printer function, it has the same args as print_status
    :rtype: function
    """
    colorinfo = _color_code(color)

    def printer(*args, full=False, end="\n", file=None, sep=" "):
        """
        [SYMBOL] hi!

        :param full: The color fill or not fill the string
        :type full: bool

        :param end: The same as print(end="")
        :type end: str

        :param file: The output file, default is sys.stdout
        :type file: file object

        :param sep: The separator between arguments, default is space
        :type sep: str
        """
        _print_message(args, symbol, colorinfo, full, end, file, sep)

    return printer

def user_color(title, color, full=False):
    """
    [B] Custom Symbol \n
    Usage:\n
    def customcolor(str):
        user_c = clc99.user_color('[b]','YELLOW')
        print(user_c+str)\n
    customcolor('Custom symbols')

    :param title: The symbol you want to add
    :type title: str

    :param color: Which color do you wanna choose, you can choose 'BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE' and the light ones like 'LIGHTRED'. The case doesn't matter, so 'cyan' and 'CYAN' are both ok.
    :type color: str

    :param full: The color fill or not fill the string
    :type full: bool
    """
    colorinfo = _color_code(color)
    return colorinfo + title + ("" if full else Fore.RESET)

def __green(text):
    return Fore.GREEN + text + Fore.RESET

def __red(text):
    return Fore.RED + text + Fore.RESET

def __yellow(text):
    return Fore.YELLOW + text + Fore.RESET

def loading99(text="", success_text="OK", except_text="EXCEPTION OCCURRED!", suppress_output=True, output_success_text=True):
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
                capture = redirect_stdout(StringIO())
            else:
                print("") # 填充换行
                capture = ExitStack() #什么都不做，只是让两种模式共用下面同一个 try

            try:
                with capture:
                    r = func(*args, **kwargs)
            except FAILEDException as e:
                # 已经出了 with，sys.stdout 恢复了，这里的 print 不会被吞掉
                eprofix = str(e)
                emessage = getattr(e, 'errortext', '')
                if emessage:
                    emessage = ": " + emessage
                print(__red(eprofix+emessage), flush=True)
                return
            except BaseException:
                print(__yellow(except_text), flush=True)
                raise

            if output_success_text:
                print(__green(success_text), flush=True)
            
            return r
        return wrapper
    return decorator


if __name__ == "__main__":
    print_good(f"Welcome to clc99! Version:{__version__}")
