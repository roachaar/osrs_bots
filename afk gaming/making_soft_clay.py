import pyautogui as pag
from random import randint
from time import sleep
import os
os.chdir(r'C:\osrs\afk gaming')

def click_bank():
    pag.moveTo(799 + randint(-2,2), 552 + randint(-2,2), randint(2376, 4344)/10000)
    sleep(randint(0,2341)/10000)
    pag.click()
    sleep(0.5 + randint(7658,9010)/10000)

def deposit_soft_clay():
    try:
        x,y = pag.locateCenterOnScreen('soft_clay_inv.png', region=(1300,600,600,450), confidence = 0.90)
        pag.moveTo(x + randint(-2,2),y + randint(-2,2), randint(2376, 4344)/10000)
        sleep(randint(0,2341)/10000)
        pag.click()
        return True
    except:
        return False

def withdraw_clay():
    try:
        x,y = pag.locateCenterOnScreen('clay_bank.png', region=(300,30,600,300), confidence = 0.95)
        pag.moveTo(x + randint(-2,2),y + randint(-2,2), randint(2376, 4344)/10000)
        sleep(randint(0,2341)/10000)
        pag.click()
        return True
    except:
        return False

def close_bank():
    try:
        x,y = pag.locateCenterOnScreen('close_bank.png', region=(850,20,200,150), confidence = 0.90)
        pag.moveTo(x + randint(-2,2),y + randint(-2,2), randint(2376, 4344)/10000)
        sleep(randint(0,2341)/10000)
        pag.click()
        sleep(randint(7658,9010)/10000)
        return True
    except:
        return False

def cast_humidify():
    try:
        x,y = pag.locateCenterOnScreen('humidify_spell.png', region=(1300,600,600,450), confidence = 0.90)
        pag.moveTo(x + randint(-2,2),y + randint(-2,2), randint(2376, 4344)/10000)
        sleep(randint(0,2341)/10000)
        pag.click()
        sleep(2 + randint(4658,7311)/10000)
        return True
    except:
        return False

object_locator()
for i in range(2000):
    click_bank()
    if not deposit_soft_clay():
        print('failed to deposit soft clay')
        break
    if not withdraw_clay():
        print('failed to withdraw clay')
        break
    if not close_bank():
        print('failed to close bank')
        break
    if not cast_humidify():
        print('failed to cast humidify')
        break
