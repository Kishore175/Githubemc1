##def dinner(func):
##    def outer(*args,**kwargs):
##        print('welcome')
##        func (*args,**kwargs)
##        print('thank you')
##    return outer
##print(outer())
##print(dinner())
##
##@dinner
##def name():
##    print('kishore like foodies')
##name()
import time
def outer(func):
    def inner(*args,**kwargs):
        start=time.time()
        tr=time.sleep(10)
        end=time.time()
        print('welcome',abs(start-end))
        func(*args,**kwargs)
        af=time.time()
        print('thank you',af)
    return inner

@outer
def name():
    print('kishore')
name()
