import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print(pyautogui.size())


pyautogui.hotkey('command', 'space')

pyautogui.typewrite("chrome", .3)

pyautogui.press('enter')

pyautogui.moveTo(334, 77)

pyautogui.PAUSE = 2

pyautogui.click()

pyautogui.PAUSE = .5

pyautogui.typewrite("http://orteil.dashnet.org/cookieclicker/")

pyautogui.press('enter')

pyautogui.moveTo(123, 432)

count = True
pyautogui.PAUSE = .2

while count == True:
    pyautogui.tripleClick()
    
