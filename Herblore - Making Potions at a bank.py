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
box5 = object_locator()
box6 = object_locator()
box7 = object_locator()

def drop_inv():
    sleep(1)
    pag.keyDown('shift')
    for i in range(0,4):
        for j in range(0,7):
            rsMoveTo(box4[0] + 42*i, box4[1] +36*j, 0.10, 3)
            sleep(randint(123,456)/10000)
            pag.click()
    pag.keyUp('shift')

def main():
    sleep(2)
    for i in range(121):
        rsMoveTo(box1[0], box1[1], 0.15, 5)
        sleep(randint(123,678)/10000)
        pag.click()
        sleep(randint(7234,9654)/10000)
        rsMoveTo(box2[0], box2[1], 0.15, 5)
        sleep(randint(123,678)/10000)
        pag.click()
        sleep(randint(1430,3257)/10000)
        rsMoveTo(box3[0], box3[1], 0.15, 5)
        sleep(randint(123,678)/10000)
        pag.click()
        sleep(randint(2234,3154)/10000)
        rsMoveTo(box4[0], box4[1], 0.15, 5)
        sleep(randint(123,678)/10000)
        pag.click()
        sleep(randint(2034,3654)/10000)
        rsMoveTo(box5[0], box5[1], 0.3, 3)
        sleep(randint(123,678)/10000)
        pag.click()
        sleep(randint(6234,8357)/10000)
        rsMoveTo(box6[0], box6[1], 0.15, 5)
        sleep(randint(123,678)/10000)
        pag.click()
        sleep(randint(1719,4654)/10000)
        rsMoveTo(box7[0], box7[1], 0.15, 5)
        sleep(randint(123,678)/10000)
        pag.click()
        sleep(randint(8831,12650)/10000)
        pag.press('space')
        sleep(1.2*14 + randint(100,678)/10000)
        


if __name__ == '__main__':
    main()