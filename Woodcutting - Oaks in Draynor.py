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

box1 = object_locator()
box2 = object_locator()
box3 = object_locator()
box4 = object_locator()
box_list = list(box1,box2,box3,box4)
def main():
    inv_full = 0
    sleep(2)
    for i in range(2275):
        rsMoveTo(box1[0],box1[1]-2,0.3,2) # bank
        sleep(randint(234,3876)/10000)
        pag.click()
        sleep(3.5 + randint(1234,12345)/10000)
        rsMoveTo(box2[0],box2[1],0.3,2) # bank
        sleep(randint(234,3876)/10000)
        pag.click()
        rsMoveTo(box3[0],box3[1],0.3,2) # bank
        sleep(randint(234,3876)/10000)
        pag.click()
        sleep(4 + randint(1234,6789)/10000)
        rsMoveTo(box4[0],box4[1],0.3,2) # bank
        sleep(randint(234,3876)/10000)
        pag.click()
        sleep(3.1 + randint(345,13459)/10000)
        while not inv_full:
            rsMoveTo(box4[0]-15,box4[1]-15,0.3,2) # bank
            sleep(randint(234,3876)/10000)
            pag.click()
            sleep(2 + randint(2345,32345)/10000)
            test = pag.locateCenterOnScreen('full_inv_logs.png')
            if test:
                inv_full = 1
        inv_full = 0


if __name__ == '__main__':
    main()