from time import sleep
import pyautogui as pag
from random import randint
import os

os.chdir(r'C:\osrs\images')

def rsMoveTo(x,y,t,e): # x, y, time, error
    pag.moveTo(x + randint(-e,e),\
        y + randint(-e,e), 
        (t + 0.25*t*randint(-4321,3456)/10000))
    sleep(0.15*(t + 0.75*t*randint(-4321,3456)/10000))

def rsLogin(user, pw):
    x,y = pag.locateCenterOnScreen('existing_user.png')
    rsMoveTo(x, y, 0.2, 3)
    pag.click()
    for char in user:
        pag.write(char, 0.0625 + randint(-345,345)/10000)
    pag.press('tab')
    for char in pw:
        pag.write(char, 0.0625 + randint(-345,345)/10000)
    pag.press('enter')
    sleep(12)
    x,y = pag.locateCenterOnScreen('click_to_play.png')
    rsMoveTo(x,y,0.1,4)
    pag.click()

def object_locator():
    sleep(0.25)
    x,y = pag.position()
    return x,y

def main():
    sleep(2)
    for i in range(400):
        rsMoveTo(899,704,0.3,2) # bank
        sleep(randint(234,1876)/10000)
        pag.click()
        sleep(2 + randint(57234,65876)/10000)
        rsMoveTo(1493,760,0.3,2) # bank
        sleep(randint(234,1876)/10000)
        pag.click()
        rsMoveTo(1004,211,0.3,2) # bank
        sleep(randint(234,1876)/10000)
        pag.click()
        sleep(randint(234,1876)/10000)
        rsMoveTo(1050,212,0.3,2) # bank
        sleep(randint(1034,1876)/10000)
        pag.click()
        sleep(randint(1234,1876)/10000)
        rsMoveTo(1588,397,0.3,2) # bank
        sleep(randint(234,1876)/10000)
        pag.click()
        sleep(3 + randint(51234,68876)/10000)
        rsMoveTo(1032,437,0.3,2) # bank
        sleep(randint(234,1876)/10000)
        pag.click()
        sleep(23 + randint(8234,13376)/10000)
        # rsMoveTo(447,211,0.3,2) # bank
        # sleep(randint(234,1876)/10000)
        # pag.click()
        # sleep(1.5 + randint(1234,9876)/10000)

if __name__ == '__main__':
    main()