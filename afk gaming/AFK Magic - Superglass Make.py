# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:31:23 2021

@author: Aaron Roach
"""


import pyautogui
import random
from time import sleep
import time
import os
os.chdir('D:\\Python Programs\\magic')

bankx = 1277
banky = 648

depositx = 1494
deposity = 870

#rightclick
#click deposit all

w1x = 1246
w1y = 144 # click 6 times

w2x = 1292
w2y = 141 # click once

closex = 1354
closey = 66

supermakex = 1437
supermakey = 858

start_time = time.time()
for j in range(2500):
    pyautogui.moveTo(bankx + random.randint(-3,3),
                     banky + random.randint(-3,3),
                     random.randint(1063,3066)/10000)
    sleep(random.randint(123,876)/10000)
    pyautogui.click()
    sleep(random.randint(1861,2453)/10000)
    pyautogui.moveTo(depositx 
                     + random.randint(-2,3),
                     deposity
                     + random.randint(-2,2),
                     random.randint(4069,6861)/10000)
    sleep(random.randint(1239,1633)/10000)
    pyautogui.rightClick()
    attempt_number_deposit = 1
    while True:
        try:
            x,y = pyautogui.locateCenterOnScreen('deposit_all.png', \
                region = (1375, 689, 350, 375))
            print(attempt_number_deposit)
            break
        except:
            if attempt_number_deposit > 5:
                break
            time.sleep(random.randint(234,678)/10000)
            attempt_number_deposit += 1
    x,y = pyautogui.locateCenterOnScreen('deposit_all.png', 
        region = (1375, 689, 350, 375))
    pyautogui.moveTo(x + random.randint(-3,5),
                     y + random.randint(-1,1),
                     random.randint(334,756)/10000)
    sleep(random.randint(345,1379)/10000)
    pyautogui.click()
    sleep(random.randint(307,833)/10000)
    pyautogui.moveTo(w1x
                     + random.randint(-2,2),
                     w1y
                     + random.randint(-3,2),
                     random.randint(769,1866)/10000)
    for i in range(6):
        sleep(random.randint(706,1033)/10000)
        pyautogui.click()
    attempt_number = 1
    pyautogui.moveTo(w2x
                     + random.randint(-2,2),
                     w2y
                     + random.randint(-3,2),
                     random.randint(449,1366)/10000)
    sleep(random.randint(406,733)/10000)
    pyautogui.click()
    sleep(random.randint(102,498)/10000)
    while True:
        try:
            a,b = pyautogui.locateCenterOnScreen('correct_inv.png', \
                region = (1300, 650, 400, 400))
            print(attempt_number)
            break
        except:
            if attempt_number > 5:
                print(attempt_number)
                break
            time.sleep(random.randint(2434,2778)/10000)
            attempt_number += 1
    a,b = pyautogui.locateCenterOnScreen('correct_inv.png', \
        region = (1300, 650, 400, 400))
    pyautogui.moveTo(closex
                     + random.randint(-2,3),
                     closey
                     + random.randint(-2,2),
                     random.randint(2041,4266)/10000)
    sleep(random.randint(0,745)/10000)
    pyautogui.click()
    sleep(random.randint(0,334)/10000)
    pyautogui.moveTo(supermakex + random.randint(-4,3),
                     supermakey + random.randint(-3,3),
                     random.randint(1648,2534)/10000)
    sleep(random.randint(0,733)/10000)
    pyautogui.click()
    sleep(random.randint(24382,27645)/10000)
    print(j, time.time() - start_time)