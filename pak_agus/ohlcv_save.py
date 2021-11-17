import pyautogui
import time
from pymongo import MongoClient
import datetime

from ipot_vars import ipot, user, password, base_path
from ipot_listsaham_excel import listsaham

"""
db_url = 'mongodb://ks:37nVhMz2Ae8XAPZR@51.79.196.193'
client = MongoClient(db_url, 27017)
db = client.kawan_saham
"""

pyautogui.hotkey('winleft', 'r')

time.sleep(1)

pyautogui.write(ipot)
pyautogui.press('enter')

time.sleep(1)

pyautogui.hotkey('ctrlleft', 'i')

time.sleep(1)

pyautogui.write(user)
pyautogui.press('tab')
pyautogui.write(password)
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(1)

#pyautogui.press('enter')

#time.sleep(1)

# settings > open workspace
pyautogui.click(10, 10)
pyautogui.press('o')

pyautogui.write(base_path + 'ohlcv.dfw')
pyautogui.press('enter')

time.sleep(9)

"""
# market analysis > stock summary > selected
pyautogui.click(10, 10)
pyautogui.press('right')
pyautogui.press('s')
pyautogui.press('right')
pyautogui.press('enter')

time.sleep(1)
"""

start_time = time.time()

while True:
    pyautogui.click(300, 300, button = 'right')

    time.sleep(1)

    pyautogui.press('up') # Save To XLS
    pyautogui.press('enter')

    time.sleep(1)

    now = datetime.datetime.now()

    pyautogui.write(base_path + 'ohlcv\\ohlcv_save_' + str(now) + '.xls')
    pyautogui.press('enter')

    time.sleep(58)

duration = time.time() - start_time
print(duration)
