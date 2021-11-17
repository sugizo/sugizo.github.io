import pyautogui
import time
from pymongo import MongoClient

from ipot_vars import ipot, user, password, base_path
from ipot_kodebroker import kodebroker

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

"""
# settings > open workspace
pyautogui.click(10, 10)
pyautogui.press('o')

pyautogui.write(base_path + 'all_rg_value.dfw')
pyautogui.press('enter')

time.sleep(1)

# set date to today (tab for choose no)
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(1)
"""

# market analysis > activity summary broker -> stock
pyautogui.click(10, 10)
pyautogui.press('right')
pyautogui.press('a')

time.sleep(1)

start_time = time.time()

for broker in kodebroker:
    pyautogui.write(broker)
    pyautogui.press('enter')

    time.sleep(1)
    
    #pyautogui.hotkey('shiftleft', 'f10')
    pyautogui.click(500, 500, button = 'right')

    time.sleep(1)
    
    pyautogui.press('down')
    pyautogui.press('down') # Save To CSV
    pyautogui.press('down') # Save To XLS
    pyautogui.press('enter')

    time.sleep(1)
    
    pyautogui.write(base_path + 'all_rg_value\\' + broker + '.xls')
    pyautogui.press('enter')

    time.sleep(1)

duration = time.time() - start_time
print(duration)
