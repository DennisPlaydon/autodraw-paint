import pyautogui
import time

class Alphabet:
    def drawE(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.moveRel(-50, 0)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(50, 0)
        pyautogui.moveRel(-50, 0)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(50, 0)
    def drawH(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(50, 0)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(0, 100)
    def drawL(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(50, 0)
    def drawO(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(-50, 0)
        pyautogui.dragRel(0, -100)

width, height = pyautogui.size()
# open paint
pyautogui.click(0, height, button='left')
pyautogui.click(0, height, button='left')
pyautogui.typewrite('paint')
time.sleep(1)
pyautogui.press('enter')

alphabet = Alphabet()
alphabet.drawH(130, 301)
alphabet.drawE(210, 301)
alphabet.drawL(290, 301)
alphabet.drawL(360, 301)
alphabet.drawO(440, 301)