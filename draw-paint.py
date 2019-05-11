import pyautogui
import time

width, height = pyautogui.size()
# open paint
pyautogui.click(0, height, button='left')
pyautogui.click(0, height, button='left')
pyautogui.typewrite('paint')
time.sleep(1)
pyautogui.press('enter')