import pyautogui
import time

class Alphabet:
    def drawH(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(50, 0)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(0, 100)

width, height = pyautogui.size()
# open paint
pyautogui.click(0, height, button='left')
pyautogui.click(0, height, button='left')
pyautogui.typewrite('paint')
time.sleep(1)
pyautogui.press('enter')

alphabet = Alphabet()
alphabet.drawH(130, 301)