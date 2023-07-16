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

def drop_bg():
    x,y = pag.locateCenterOnScreen('blue_gill_inv.png', confidence = 0.97)
    rsMoveTo(x,y,0.1,2)
    sleep(randint(12,123)/10000)
    pag.keyDown('shift')
    pag.click()
    pag.keyUp('shift')

def fish_bg():
    x,y = pag.locateCenterOnScreen('blue_gill.png', confidence = 0.8)
    rsMoveTo(x+3,y+3,0.06,2)
    sleep(randint(12,77)/10000)
    pag.click()
    sleep(2.4 + randint(123,2345)/10000)

def loc_kingworm():
    x,y = pag.locateCenterOnScreen('highlighted_kingworm.png', confidence = 0.7)
    rsMoveTo(x,y,0.12, 1)
    sleep(randint(11,185)/10000)
    pag.click()

def old_main():
    for j in range(10):
        for i in range(46):
            try:
                fish_bg()
            except:
                rsMoveTo(1247, 722, 0.1, 20)
                pag.click()
            try:
                drop_bg()
            except:
                    print('no fish to drop')
            print(i)
        for i in range(12):
            loc_kingworm()
            if i < 1:
                sleep(randint(36123,42444)/10000)
            else:
                rsMoveTo(1000,500,0.7,150)

def cut_fish():
    rsMoveTo(1452, 792, 0.1, 2)
    sleep(randint(11,185)/10000)
    pag.click()
    try:
        x,y = pag.locateCenterOnScreen('blue_gill_inv.png', confidence = 0.97)
        rsMoveTo(x,y,0.1,2)
        sleep(randint(12,123)/10000)
        pag.click()
    except:
        x,y = pag.locateCenterOnScreen('common_tench_inv.png', confidence = 0.97)
        rsMoveTo(x,y,0.1,2)
        sleep(randint(12,123)/10000)
        pag.click()
    sleep(randint(240895, 248201)/10000)

def drop_ct():
    x,y = pag.locateCenterOnScreen('common_tench_inv.png', confidence = 0.97)
    rsMoveTo(x,y,0.1,2)
    sleep(randint(12,123)/10000)
    pag.keyDown('shift')
    pag.click()
    pag.keyUp('shift')

def drop_inv():
    sleep(1)
    pag.keyDown('shift')
    for i in range(0,4):
        for j in range(2,7):
            rsMoveTo(box2[0] + 42*i, box2[1] +36*j, 0.10, 3)
            sleep(randint(123,456)/10000)
            pag.click()
    pag.keyUp('shift')

def main():
    for j in range(50):
        for i in range(1,22):
            if i%5 == 0:
                print(j, '-', i)
            try:
                fish_bg()
            except:
                rsMoveTo(1247, 722, 0.1, 20)
                pag.click()
        if j%3 == 0:
            try:
                cut_fish()
            except:
                print('no fish to cut')
        else:
            drop_inv()

if __name__ == '__main__':
    main()