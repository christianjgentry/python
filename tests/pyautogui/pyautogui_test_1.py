'''
import os
import shutil
src = "/Users/christian.gentry/Desktop/_from"
dest = "/Users/christian.gentry/Desktop/_to"
src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, dest)
'''

import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print(pyautogui.size())



pyautogui.typewrite("safari", .3)

pyautogui.press('enter')

pyautogui.typewrite("huckabee architects")

pyautogui.press('enter')

pyautogui.moveTo(297, 246, .5)

pyautogui.click()
