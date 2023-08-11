#install the psutil and pyautogui module in order to use this program.
#made by Eric Kim. This program is distributed under the GPLv2 license. This can be modified and distributed freely.
import psutil
from time import sleep
import pyautogui as pg

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

while True:
    chrome_running = is_process_running("chrome.exe")
    if chrome_running:
        print("Chrome is still running.")
        sleep(1)
    else:
        print("Chrome has terminated.")
        break
pg.hotkey('win','r')
pg.write('chrome')
pg.press('enter')
sleep(1)
pg.hotkey('ctrl', 'shift', 'delete')
sleep(1)
delete = pg.locateOnScreen('delete.png')
x, y = pg.center(delete)
pg.click(x, y)