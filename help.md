# clc99 Help

> For the full tutorial see the **[wiki](https://github.com/windows99-hue/clc99/wiki)**, this page is a quick reference kept in the repository.

## Installation

clc99 needs **Python 3.7 or newer** (it depends on `colorama>=0.4.6`).

~~~bash
pip install clc99
~~~

## Import

~~~python
import clc99          # keeps the namespace, call clc99.print_status(...)
from clc99 import *   # call print_status(...) directly
~~~

clc99 runs colorama's `just_fix_windows_console()` automatically when it is imported, so no manual initialisation is needed (`initsystem()` was removed in 2.4.0).

## Default output functions

~~~python
clc99.print_status('[*] status')
clc99.print_good('[+] good')
clc99.print_error('[-] error')
clc99.print_warning('[!] warning')
clc99.print_finish('[FINISH] finish')
clc99.print_os('[$] os')
clc99.print_notrun('[#] comment')
clc99.print_e('[ERROR] error')
clc99.print_fileok('[.] file ok')
clc99.print_filerror('[.] file error')
clc99.print_music('[playmusic] play music')
clc99.print_video('[playvideo] play video')
clc99.print_ok('[OK] ok')
clc99.print_over('[OVER] over')
clc99.print_admin('[Admin] admin')
clc99.print_dirok('[/] dir ok')
clc99.print_direrror('[/] dir error')
clc99.print_comok('[C] device ok')
clc99.print_comerror('[C] device error')
clc99.print_uquestion('[?] user question')
clc99.print_cquestion('[?] code question')
~~~

They all take the same parameters:

Parameter | Type | Default | Description
-- | -- | -- | --
args | any | none | What to output, just like `print`, any number of values of any type
full | bool | False | Whether the color fills the whole line
end | str | "\n" | Same as `print(end=)`
file | file | None | Same as `print(file=)`
sep | str | " " | Same as `print(sep=)`

## Special output functions

### print_time

Inserts the current time into your output:

~~~python
print_time()                               # [TIME] 2026-09-27 21:00:00
print_time("TIME: ", position="front")     # [TIME] TIME: 2026-09-27 21:00:00
print_time(" <- now", position="before")   # [TIME] 2026-09-27 21:00:00 <- now
print_time("-", position="middle")         # [TIME] -2026-09-27 21:00:00-
~~~

Parameters: `text`, `timeformat` (same format as the `time` module), `position` (`front` / `before` / `middle`, default `front`), `full`, `end`, `file`, `sep`.

> **Changed in 2.4.0**: `text` used to be called `str` and `position` used to be called `title`, both old names still work. An unknown `position` now raises `ValueError` (it used to print nothing at all). `end` used to be ignored and works now (`sep` has no effect for `print_time`, because it only prints one piece of text).

### input_str

A wrapper around `input`:

~~~python
name = input_str("Please enter your name: ")
~~~

### make_printer (new in 2.4.0)

Build your own symbol output function:

~~~python
upload = clc99.make_printer("[UPLOAD]", color="cyan")
upload("foo.png")             # [UPLOAD] foo.png
upload("bar.png", full=True)  # the color fills the whole line
~~~

The returned function works just like `print_status`, `full` / `end` / `file` / `sep` are all supported.

### user_color

Create your own symbol:

~~~python
user_c = clc99.user_color('[b]', 'YELLOW')
print(user_c + 'custom symbol')
~~~

`make_printer` and `user_color` share the same color syntax: the eight basic colors `BLACK` `RED` `GREEN` `YELLOW` `BLUE` `MAGENTA` `CYAN` `WHITE`, the light ones like `LIGHTRED`, `RESET`, or a raw colorama escape code such as `Fore.RED`. Case and `_`/`-` do not matter, and an unknown color name raises `ValueError`.

## loading99 decorator

~~~python
@loading99(text="Working...", success_text="OK")
def work():
    print("this line is hidden")
    return 1

work()
~~~

Parameter | Type | Default | Description
-- | -- | -- | --
text | str | "" | Loading text, uses the function name + "is running" when empty
success_text | str | "OK" | Text shown after the function succeeds
except_text | str | "EXCEPTION OCCURRED!" | Text shown when the function raises
suppress_output | bool | True | Whether to hide the print output of the function
output_success_text | bool | True | Whether to show the success text

Use `err99()` to stop the function anywhere and print a message:

~~~python
@loading99()
def check(age):
    if age < 18:
        err99("too young")                 # prints FAILED: too young
    if age > 100:
        err99("INVALID_AGE", "not real")   # prints INVALID_AGE: not real
~~~

`err99(error_text="FAILED", text="")` raises a `FAILEDException`, which `loading99` catches and displays, so your program does not crash.

## Changes in 2.4.0

* Added `make_printer()`.
* `print_time`: `str` is now `text` and `title` is now `position` (old names still work), a wrong position raises `ValueError` instead of printing nothing, `end` works now.
* `user_color`: colors are case insensitive and also accept the light ones, `RESET` and `Fore.*` escape codes.
* `loading99`: the default of `except_text` is `"EXCEPTION OCCURRED!"` and it now works with both values of `suppress_output`.
* Removed `initsystem()`, the terminal is fixed automatically on import.
* Minimum supported Python is 3.7 (because of `colorama>=0.4.6`).
