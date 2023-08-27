#install the psutil, pyautogui, and opencv-python module in order to use this program.
#made by Eric Kim. This program is distributed under the GPLv2 license. This can be modified and distributed freely.
import psutil
from time import sleep
import pyautogui as pg
import cv2

def proc(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

while True:
    chrome_running = proc("chrome.exe")
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
delete = pg.locateOnScreen('delete.png', confidence=0.7)
x, y = pg.center(delete)
pg.click(x, y)
pg.hotkey('alt', 'f4')
