from clc99 import *
import time

@loading99(text="123...")
def test():
    print_status("loading......")
    time.sleep(0.5)
    try:
        r = 1/0
    except ZeroDivisionError:
        r = 1
        # raise ZeroDivisionError("除零错误")
    return r

@loading99(suppress_output=False)
def test02():
    time.sleep(1)
    print_error("ok")

@loading99()
def test03():
    time.sleep(1)
    err99()

r = test()
test02()
test03()    
print_status("all done.")