import time
import clc99

print(clc99.__version__)

upload = clc99.make_printer("[UPLOAD]", color="cyan")

upload("foo.png")

@clc99.loading99(text="Loading test...",suppress_output=False)
def test():
    print("loading...")
    time.sleep(1)
    print("ok")

test()