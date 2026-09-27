## 2021/8/31
Today, I uploaded colorconsole99 on GitHub for the first time, version 1.0.0 .
This is my first self-made library, but it is not ready to be released on pypi  :)

You can copy the master file directly to the python Library Directory.

## 2021/9/1
Today, I canceled the complex colors class, which can be called directly without executing "colorconsole99. Colors. [XXX]"

This is only a beta version

## 2021/9/5

Today, I released the colorconsole99 Python library to pypi. You can directly pip install colorconsole99, which is very simple!

## 2021/9/10

Today,update README.md

## 2021/9/12
Today is an exciting day. Just yesterday, I used my own library, but I found that I couldn't install it because there was a major bug in my program. 

Today, I fixed it and everything was normal! You can use pip to install. It also has a new version number: 1.0.1.1

## 2024/12/15

Today, I have made up my mind to refactor colorconsole99. I have changed the name of this library to clc99, which is more convenient. I have also removed unnecessary libraries and simplified the program structure. I will also upload it again, not only on GitHub, but clc99 will also work on Pypi!

## 2024/12/19

Today, I added the 'end' parameter to clc99 and also refactored the code structure of the library

## 2025/3/8

Today, I fixed some bugs, and remake a few of functions, add the tips of add functions.
Fixed the bug of `full`

## 2025/3/9

Today, I changed the color of the `print_good` function.


## 2025/11/12

Today, I added the parameter `sep` and `file` to every function.
Modified the symbol of `print_finish`

## 2025/11/15

Today, I made the `loading99` which im very like!

## 2025/11/21

Today, I fixed a bug that cause `text` arg error when a same function is invoked.

## 2026/9/27

Today, I added the `make_printer` function. Now you can make your own printer with a symbol and a color you like, and it works just like `print_status`:

~~~python
upload = clc99.make_printer("[UPLOAD]", color="cyan")
upload("foo.png")
~~~

I also fixed the python version check in `user_color`. It was `not platform.python_version() > "3.8"`, but comparing version strings is wrong: `"3.14.4" > "3.8"` is `False` because it compares `'1'` with `'8'`. So every python newer than 3.9 used the old branch without `typing.Literal`. Now it's `sys.version_info < (3, 8)`.

Then I removed the duplicated color code. `user_color` used to have its own `if color=='RED': ... elif ...` chain, and it was written twice, one copy for python < 3.8 and one copy for python 3.8+. Now it just calls `_color_code()`, the same helper `make_printer` uses, so all the color APIs accept the same names. Two more good things came with it: no more version branch at all, and `user_color` now also understands 'cyan', 'light-red' and a raw `Fore` code. 74 lines gone.

Then I cleaned up `loading99`. It used to do `original_stdout = sys.stdout` / `sys.stdout = captured_output` by hand, and it had two almost identical `try/except` blocks, one for `suppress_output=True` and one for `False`. Now it uses `contextlib.redirect_stdout`, and both modes share a single `try/except`. The `print` in the handlers stays outside the `with`, so the error message is not swallowed by the redirect.

That also fixed a small bug: in the non suppress mode the exception message was hardcoded to `EXCEPTION OCCURRED!`, so the `except_text` parameter only worked when `suppress_output=True`. Now both modes use `except_text`, and the default of `except_text` is `EXCEPTION OCCURRED!`. So the non suppress mode keeps its old text, and the suppress mode now says `EXCEPTION OCCURRED!` instead of `EXCEPT` when you don't pass `except_text`. If you want the short one, pass `except_text="EXCEPT"`.

`import sys` is not used any more, so I removed it too.

By the way, `redirect_stdout` does not make `loading99` thread safe by itself, swapping `sys.stdout` is still global state. It only makes the save/restore correct (exceptions, nesting, no forgotten restore).