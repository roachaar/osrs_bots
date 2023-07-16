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
    sleep(5)
    x,y = pag.position()
    return x,y

def main():
    sleep(5)
    for i in range(110):
        rsMoveTo(379,723,0.3,2) # bank
        pag.click()
        sleep(randint(51234,59876)/10000)
        rsMoveTo(1391,685,0.4,2) # deposit
        pag.click()
        sleep(randint(6789,9876)/10000)
        rsMoveTo(834,371,0.3,2) # withdraw
        pag.click()
        rsMoveTo(913,52,0.3,2) # close
        pag.click()
        sleep(randint(1234,2345)/10000)
        rsMoveTo(1160,377,0.4,2)
        pag.click()
        sleep(randint(51234,59876)/10000)
        pag.press('space')
        sleep(27*6 + randint(1234,9876)/10000)
        print('iteration', i+1, 'complete')

if __name__ == '__main__':
    main()