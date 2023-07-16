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

def find_dhide():
    dhide_list = ['red_dhide.png','black_dhide.png','blue_dhide.png','green_dhide.png']
    if pag.locateCenterOnScreen('black_dhide_zero.png',region=(900,75,750,600)):
        dhide_list.remove('black_dhide.png')
    if pag.locateCenterOnScreen('blue_dhide_zero.png',region=(900,75,750,600)):
        dhide_list.remove('blue_dhide.png')
    for i in dhide_list:
        try:
            x,y = pag.locateCenterOnScreen(i, region=(900,75,750,600))
            if x:
                print('found', i)
                return x,y
        except:
            continue
    return None, None

def rsMoveClick(x,y,t,e):
    rsMoveTo(x,y,t,e)
    sleep(randint(12,234)/10000)
    pag.click()

def main():
    x,y = pag.locateCenterOnScreen('lunar_spellbook.png')
    if x:
        rsMoveClick(x,y,0.1,1)
    sleep(0.5)
    a,b = pag.locateCenterOnScreen('tan_leather_spell.png')
    if a:
        while True:
            rsMoveClick(1239,544,0.3,2) # bank!
            sleep(randint(234,1876)/10000)
            sleep(3 + randint(5234,6576)/10000)
            rsMoveClick(1536,762,0.11,2) # bank
            x,y = find_dhide()
            if x:
                rsMoveClick(x,y,0.11,2)
                sleep(randint(234,1876)/10000)
                rsMoveTo(1356,65,0.3,2) # bank
                pag.click()
                sleep(randint(1234,1876)/10000)
                rsMoveClick(a,b,0.2,2) # bank
                for i in range(4):
                    sleep(1 + randint(12234,12676)/10000)
                    pag.click()
                    sleep(randint(414,804)/10000)
                    pag.click()
                sleep(3 + randint(12036,12273)/10000)
            else:
                print('No more hides, all done')
                return None

if __name__ == '__main__':
    main()

# https://prices.runescape.wiki/osrs/item/1745
# https://prices.runescape.wiki/osrs/item/2505
# https://prices.runescape.wiki/osrs/item/2507
# https://prices.runescape.wiki/osrs/item/2509