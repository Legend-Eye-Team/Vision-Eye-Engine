import threading
import time

def ConvertBoolean(value):
    return not value

def WaitThread(wait_time,todo,exit_do=None):
    
    def f(wt):
        time.sleep(wt)
        todo()
    thread = threading.Thread(target=f,args=(wait_time,))
    thread.start()
    if exit_do != None: exit_do()