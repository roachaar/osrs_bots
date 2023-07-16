from time import sleep,time
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

def rsMoveClick(x,y,t,e):
    rsMoveTo(x,y,t,e)
    sleep(randint(12,234)/10000)
    pag.click()

def tithe_round():
    # make sure we are on runescape window
    rsMoveClick(1518,717,0.2,3)
    rsMoveClick(1364,590,0.2,3)
    sleep(2 + randint(123,234)/10000)
    # plant first 2 seeds
    rsMoveClick(1452, 760, 0.12, 2)
    rsMoveClick(1200,566, 0.12, 4)
    sleep(randint(24109,24444)/10000)
    rsMoveClick(1452, 760, 0.13, 2)
    rsMoveClick(1344,563, 0.14, 4)
    sleep(randint(24109,24444)/10000)

    #plant next 6 seeds
    for i in range(3):
        rsMoveClick(1452, 760, 0.14, 2)
        rsMoveClick(1169,639, 0.12, 4)
        sleep(randint(24203,24622)/10000)
        rsMoveClick(1452, 760, 0.12, 2)
        rsMoveClick(1344,563, 0.11, 4)
        sleep(randint(24103,24679)/10000)
    sleep(randint(24103,24679)/10000)
    # back to the top-left
    for j in range(4):
        rsMoveClick(1171,304,0.13, 3)
        sleep(randint(41969,42344)/10000)
        rsMoveClick(1326,525,0.14, 4)
        sleep(randint(30109,30344)/10000)
        for i in range(3):
            rsMoveClick(1171,625, 0.12, 4)
            sleep(randint(30109,30644)/10000)
            rsMoveClick(1335,550, 0.12, 4)
            sleep(randint(30109,30344)/10000)
        sleep(randint(30103,30679)/10000)
        if j == 0:
            sleep(2.4 + randint(1345,2695)/10000)
        if j == 1:
            sleep(25 + randint(6061,7069)/10000)
        if j == 2:
            sleep(28 + randint(123,234)/10000)

    # deposit finished plants
    rsMoveClick(1112,183,0.11,1)
    sleep(randint(54209,54633)/10000)
    # fill watering can
    rsMoveClick(1580,763,0.11,1)
    rsMoveClick(1221,586,0.11,1)
    sleep(randint(48109,48563)/10000)

def plant(x,y,t,e):
    rsMoveClick(1452,760,0.12,2)
    rsMoveClick(x,y,t,e)
    sleep(randint(18903,19422)/10000)

def water(x,y,t,e):
    rsMoveClick(x,y,t,e)
    sleep(randint(28959,29977)/10000)

def tithe_big_round():
    # get to starting point
    rsMoveClick(1361,223,0.15,1)
    sleep(randint(48509,50863)/10000)
    plant(1202,501,0.08,4)
    plant(1334,500,0.07,2)
    plant(1173,581,0.09,2)
    plant(1337,566,0.10,2)
    # plant the next 4 seeds
    for i in range(2):
        plant(1169,639, 0.09, 4)
        plant(1344,563, 0.08, 4)
    # move to southern patch
    plant(1174,721,0.13,1)
    sleep(randint(13103,14079)/10000)
    #plant1
    plant(1225,675,0.12,2)
    sleep(randint(6703,7479)/10000)
    for i in range(2):
        plant(1195,648,0.12,2)
    # go back up the the eastern side
    plant(1336,562,0.12,3)
    plant(1311,478,0.12,2)
    for i in range(2):
        plant(1314,413,0.12,2)
    
    for i in range(4):
        # begin watering plants/harvesting up
        # shift = (i == 3)*-30
        water(1171,61,0.28,1)
        sleep(randint(42709,43411)/10000)
        water(1334,504,0.06,1)
        water(1172,584,0.06,1)
        water(1334,545,0.06,1)
        for i in range(2):
            water(1170,642,0.06,1)
            water(1314,567,0.06,1)
        water(1176,725,0.08,3)
        sleep(randint(4133,6479)/10000)
        water(1230,671,0.07,2)
        sleep(randint(4107,6579)/10000)
        for i in range(2):
            water(1195,656,0.07,2)
        water(1343,551,0.08,2)
        water(1303,472,0.07,2)
        for i in range(2):
            water(1303,420,0.07,2)
    
    # deposit finished plants
    rsMoveClick(1111,391,0.20,1)
    sleep(randint(48109,48433)/10000)
    # fill watering can
    rsMoveClick(1580,763,0.08,1)
    rsMoveClick(1221,586,0.11,1)
    sleep(randint(154029,154963)/10000)



def main():
    start = time()
    for n in range(67):
        # tithe_round()
        tithe_big_round()
        loop_time = time()
        print(n+1, 'runs in', loop_time - start, \
              'seconds', '- AVG:', (loop_time - start)/(n+1), 'seconds')
        # sleep(15 + randint(1234,8765)/10000)

if __name__ == '__main__':
    main()