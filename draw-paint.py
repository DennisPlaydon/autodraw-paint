import pyautogui
import time

class Alphabet:
    def drawA(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.dragRel(0, 50)
        pyautogui.dragRel(-50, 0)
        pyautogui.moveRel(50, 0)
        pyautogui.dragRel(0, 50)

    def drawB(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(40, 0)
        pyautogui.dragRel(10, 10)
        pyautogui.dragRel(0, 40)
        pyautogui.dragRel(-50, 0)
        pyautogui.moveRel(50, 0)
        pyautogui.dragRel(0, 40)
        pyautogui.dragRel(-10, 10)
        pyautogui.dragRel(-40, 0)

    def drawC(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.moveRel(-50, 0)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(50, 0)

    def drawD(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(25, 0)
        pyautogui.dragRel(25, 25)
        pyautogui.dragRel(0, 50)
        pyautogui.dragRel(-25, 25)
        pyautogui.dragRel(-25, 0)
        pyautogui.dragRel(0, -100)

    def drawE(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.moveRel(-50, 0)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(50, 0)
        pyautogui.moveRel(-50, 0)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(50, 0)

    def drawF(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.moveRel(-50, 0)
        pyautogui.dragRel(0, 100)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(50, 0)

    def drawG(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.moveRel(-50, 0)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(50, 0)
        pyautogui.dragRel(0, -45)
        pyautogui.dragRel(-20, 0)

    def drawH(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(50, 0)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(0, 100)

    def drawI(self, startX, startY):
        pyautogui.moveTo(startX+25, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.moveRel(-30, 0)
        pyautogui.dragRel(60, 0)
        pyautogui.moveTo(startX+25, startY)
        pyautogui.moveRel(-30, 0)
        pyautogui.dragRel(60, 0)

    def drawJ(self, startX, startY):
        pyautogui.moveTo(startX+25, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(-25, 0)
        pyautogui.dragRel(0, -50)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(50, 0)

    def drawK(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.moveRel(0, -50)
        pyautogui.dragRel(50, -50)
        pyautogui.moveRel(-50, 50)
        pyautogui.dragRel(50, 50)

    def drawL(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(50, 0)

    def drawM(self, startX, startY):
        pyautogui.moveTo(startX, startY+100)
        pyautogui.dragRel(0, -100)
        pyautogui.dragRel(25, 50)
        pyautogui.dragRel(25, -50)
        pyautogui.dragRel(0, 100)

    def drawN(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 100)
        pyautogui.dragRel(0, -100)

    def drawO(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(-50, 0)
        pyautogui.dragRel(0, -100)

    def drawP(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.dragRel(0, 50)
        pyautogui.dragRel(-50, 0)

    def drawQ(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(10, 10)
        pyautogui.moveRel(-20, -20)
        pyautogui.dragRel(10, 10)
        pyautogui.dragRel(-50, 0)
        pyautogui.dragRel(0, -100)

    def drawR(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.dragRel(0, 50)
        pyautogui.dragRel(-50, 0)
        pyautogui.dragRel(50, 50)
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)

    def drawS(self, startX, startY):
        pyautogui.moveTo(startX+25, startY)
        pyautogui.dragRel(25, 25)
        pyautogui.dragRel(-10, 10)
        pyautogui.moveTo(startX+25, startY)
        pyautogui.dragRel(-25, 25)
        pyautogui.dragRel(50, 50)
        pyautogui.dragRel(-50, 25)
        pyautogui.dragRel(0, -25)

    def drawT(self, startX, startY):
        pyautogui.moveTo(startX+25, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.moveTo(startX+25, startY)
        pyautogui.moveRel(-30, 0)
        pyautogui.dragRel(60, 0)

    def drawU(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(50, 0)
        pyautogui.dragRel(0, 10)
        pyautogui.dragRel(0, -110)

    def drawV(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(25, 100)
        pyautogui.dragRel(25, -100)

    def drawW(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(0, 100)
        pyautogui.dragRel(30, -50)
        pyautogui.dragRel(30, 50)
        pyautogui.dragRel(0, -100)

    def drawX(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 100)
        pyautogui.moveTo(startX+50, startY)
        pyautogui.dragRel(-50, 100)

    def drawY(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(25, 50)
        pyautogui.moveTo(startX+50, startY)
        pyautogui.dragRel(-25, 50)
        pyautogui.dragRel(0, 50)

    def drawZ(self, startX, startY):
        pyautogui.moveTo(startX, startY)
        pyautogui.dragRel(50, 0)
        pyautogui.dragRel(-50, 100)
        pyautogui.dragRel(50, 0)

alphabet = Alphabet()
func = input('>')
sentence_array = list(func)
width, height = pyautogui.size()
# open paint
pyautogui.click(0, height, button='left')
pyautogui.click(0, height, button='left')
pyautogui.typewrite('paint')
time.sleep(1)
pyautogui.press('enter')

function_dict = {
    'A': alphabet.drawA,
    'B': alphabet.drawB,
    'C': alphabet.drawC,
    'D': alphabet.drawD,
    'E': alphabet.drawE,
    'F': alphabet.drawF,
    'G': alphabet.drawG,
    'H': alphabet.drawH,
    'I': alphabet.drawI,
    'J': alphabet.drawJ,
    'K': alphabet.drawK,
    'L': alphabet.drawL,
    'M': alphabet.drawM,
    'N': alphabet.drawN,
    'O': alphabet.drawO,
    'P': alphabet.drawP,
    'Q': alphabet.drawQ,
    'R': alphabet.drawR,
    'S': alphabet.drawS,
    'T': alphabet.drawT,
    'U': alphabet.drawU,
    'V': alphabet.drawV,
    'W': alphabet.drawW,
    'X': alphabet.drawX,
    'Y': alphabet.drawY,
    'Z': alphabet.drawZ
}

startX = 130
startY = 301
for i in sentence_array:
    i = i.upper()
    if i == " ":
        startX += 80
    try:
        function_dict[i](startX, startY)
        startX += 80
    except:
        continue