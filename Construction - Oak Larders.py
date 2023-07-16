import pyautogui
import random
from time import sleep
import time
import os
os.chdir(r'C:\osrs\images')

def color_shower():
    posXY = pyautogui.position() 
    print(posXY, pyautogui.pixel(posXY[0], posXY[1]) )
    return pyautogui.pixel(posXY[0], posXY[1])

def useplank():
    location = pyautogui.locateCenterOnScreen('noted_plank.png',
                                              region=(1340,620, 120, 120), confidence = 0.80)
    print(location)
    pyautogui.moveTo(location[0] + random.randint(-3,1),
                     location[1] + random.randint(-3,1),
                     random.randint(1234,2345)/10000)
    pyautogui.click()
    
def onphial():
    while True:
        for x in range(705, 750, 44):
            for y in range(815, 865, 49):
                pyautogui.moveTo(x + random.randint(-1,1),
                y + random.randint(-1,1),
                random.randint(678,912)/10000)
                pyautogui.rightClick()
                sleep(0.15 + random.randint(765,1345)/10000)
                try:
                    x,y = pyautogui.locateCenterOnScreen('on_phials.png',
                                            region=(450,640,450,330), confidence = 0.80)
                    pyautogui.moveTo(x + random.randint(-3,1),y + random.randint(-3,1), random.randint(678,912)/10000)
                    pyautogui.click()
                    pyautogui.move(200,200, random.randint(123,345)/10000)
                    return None
                except:
                    pyautogui.move(200,80, random.randint(234,567)/10000)
                    continue
    
def exchangeall():
    pyautogui.press('3')

def enterhouse():
    for x in range(825, 865, 39):
        for y in range(275, 350, 24): #1275, 275, 125, 125
            pyautogui.moveTo(x + random.randint(-1,1),
            y + random.randint(-1,1),
            random.randint(678,912)/10000)
            pyautogui.rightClick()
            sleep(0.15 + random.randint(765,1345)/10000)
            try:
                x,y = pyautogui.locateCenterOnScreen('build_mode.png',
                                           region=(350,50,950,700), confidence = 0.80)
                pyautogui.moveTo(x + random.randint(-3,1),y + random.randint(-3,1), random.randint(678,912)/10000)
                pyautogui.click()
                pyautogui.move(200,200,1)
                return None
            except:
                pyautogui.move(200,80, random.randint(234,567)/10000)
                continue

def buildmode():
    x,y = pyautogui.locateCenterOnScreen('wrench_settings.png',
                                region=(1500,950,150,100))
    pyautogui.moveTo(x + random.randint(-3,1),y + random.randint(-3,1), random.randint(678,912)/10000)
    pyautogui.click()
    sleep(random.randint(2345,6789)/10000)
    x,y = pyautogui.locateCenterOnScreen('house_pic.png',
                                region=(1450,850,150,150))
    pyautogui.moveTo(x + random.randint(-3,1),y + random.randint(-3,1), random.randint(678,912)/10000)
    pyautogui.click()
    sleep(random.randint(8345,14789)/10000)
    x,y = pyautogui.locateCenterOnScreen('on_button.png',
                                region=(1500,750,150,150))
    pyautogui.moveTo(x + random.randint(-3,1),y + random.randint(-3,1), random.randint(678,912)/10000)
    pyautogui.click()
    sleep(3)
    pyautogui.press('esc')

def build_first_larder():
    pyautogui.moveTo(895 + random.randint(-4,3),423 + random.randint(-4,3), random.randint(2345,4567)/10000)
    sleep(random.randint(234,541)/10000)
    pyautogui.rightClick()
    sleep(0.15 + random.randint(765,1345)/10000)
    x,y = pyautogui.locateCenterOnScreen('build_larder.png',
                                region=(750,390,300,200), confidence = 0.80)
    pyautogui.moveTo(x + random.randint(-3,1),y + random.randint(-3,1), random.randint(678,912)/10000)
    pyautogui.click()
    sleep(random.randint(28345,31743)/10000)
    pyautogui.press('2')
    sleep(random.randint(12537,15143)/10000)
    pyautogui.moveTo(835 + random.randint(-5,6),500 + random.randint(-5,4))
    sleep(random.randint(1234,1541)/10000)
    pyautogui.rightClick()
    sleep(0.15 + random.randint(765,1345)/10000)
    x,y = pyautogui.locateCenterOnScreen('remove_larder.png',
                                region=(675,440,350,250), confidence = 0.80)
    pyautogui.moveTo(x + random.randint(-3,2),y + random.randint(-3,1), random.randint(678,912)/10000)
    pyautogui.click()
    sleep(random.randint(13345,15931)/10000)
    pyautogui.press('1')

def build_next_larder():
    pyautogui.moveTo(835 + random.randint(-5,6),500 + random.randint(-5,4))
    sleep(random.randint(234,541)/10000)
    pyautogui.rightClick()
    sleep(0.15 + random.randint(765,1345)/10000)
    x,y = pyautogui.locateCenterOnScreen('build_larder.png',
                                region=(675,440,350,250), confidence = 0.80)
    pyautogui.moveTo(x + random.randint(-3,2),y + random.randint(-3,1), random.randint(678,912)/10000)
    pyautogui.click()
    sleep(random.randint(9234,11541)/10000)
    pyautogui.press('2')
    sleep(random.randint(13537,15143)/10000)
    pyautogui.moveTo(835 + random.randint(-5,6),500 + random.randint(-5,4))
    sleep(random.randint(234,541)/10000)
    pyautogui.rightClick()
    sleep(0.15 + random.randint(765,1345)/10000)
    x,y = pyautogui.locateCenterOnScreen('remove_larder.png',
                                region=(675,440,350,250), confidence = 0.80)
    pyautogui.moveTo(x + random.randint(-3,2),y + random.randint(-3,1), random.randint(678,912)/10000)
    pyautogui.click()
    sleep(random.randint(13345,14841)/10000)
    pyautogui.press('1')

def leave_house():
    pyautogui.moveTo(735 + random.randint(-1,1),661 + random.randint(-5,5), random.randint(1234,2345)/10000)
    sleep(random.randint(1,587)/10000)
    pyautogui.click()
    sleep(2.15 + random.randint(-250,137)/10000)

sleep(5)
enterhouse()

sleep(4)
for i in range(350):
    useplank()
    sleep(0.3)
    onphial()
    sleep(3.6)
    exchangeall()
    sleep(1)
    enterhouse()
    sleep(4.7)
    #buildmode()
    #sleep(1.1)
    build_first_larder()
    sleep(1.8)
    build_next_larder()
    sleep(1.8)
    build_next_larder()
    sleep(1.8)
    leave_house()
    sleep(2.1)