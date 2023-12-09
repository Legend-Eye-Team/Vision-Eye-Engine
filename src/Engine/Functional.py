PRIVATE_MODULE_FUNCTIONAL = {
    "Module":"Functional",
    "Coder":["QuangDeNhi"],
    "Target":"Create short Method for Local"
}

import threading
import time


start_id = 0
def CreateID():
    global start_id
    start_id += 1
    return start_id - 1

start_id_gui = 0
def CreateGuiID():
    global start_id_gui
    start_id_gui -= 1
    return start_id_gui

def ConvertBoolean(value):
    return not value

def WaitThread(wait_time,todo,exit_do=None):
    
    def f(wt):
        time.sleep(wt)
        todo()
    thread = threading.Thread(target=f,args=(wait_time,))
    thread.start()
    if exit_do != None: exit_do()