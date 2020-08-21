# -*- coding: utf-8 -*-
"""
#Created on Thu Jul 23 09:47:24 2020
#
#@author: josep
#"""

# WARNING: This script is coded for josep, hence in order to make this work,
# we need to add the inputs for the login, the feature will be added later.

from time import sleep

import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import threading

import pyautogui as pg



def pageupper():
    while True:
        pg.press(Keys.PAGE_DOWN)

def whole_script():
    ''' START '''
    
    ''' This is the URL for the first page for the link-finding '''
    
    init_page = 'https://www.instagram.com/p/CCxGqrehScX/?hl=en'
    
    options = Options()
        
    options.add_argument("--disable-extensions")
    
    options.add_argument("user-data-dir=selenium") 
    
        
    driver = webdriver.Chrome(options=options)
    
    
    driver.get(init_page)
    
    comment_xpath = '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea'
    commentbtn_xpath = '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button/div/svg'
    

    comment_box = driver.find_element_by_xpath(comment_xpath)
    post_xpath = '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button'
    
    
    
    while True:
        
        sleep(3)
        randy = random.uniform(1,4)
        
        mini_randy = random.uniform(0.5,1.8)
        
        
        for i in range(1,40):
            
            pg.keyDown(Keys.PAGE_UP)
        
            sleep(1 + randy)
            usernames = ['@erikuka478 ', '@sxponte ', '@segunpausini ', '@sebaoliver15 ' , '@floreria_pipo ',
                         '@sxponte.makeup ', '@kukarachaa ', '@el_vaso_del_conejo ', '@janetmvega ']
            random.shuffle(usernames)
            
            usernames.pop(0)
            usernames.pop(0)
            usernames.pop(0)
            usernames.pop(0)
            usernames.pop(0)
            
            stringy = ''
            
            for username in usernames:
                stringy += str(username)
                
            pg.moveTo(1666,987)
            
            pg.click() # comment field click
            
        
                      
            pg.typewrite(stringy)
            
            driver.execute_script("window.scrollTo(0, 0)") 
            
            
            
            sleep(0.5 + mini_randy)
            pg.moveTo(1839,987)
            sleep(1 + mini_randy)
            
            pg.click()
            
            checker = 2
            
            while(checker != 0):
                try:
                    
    
                    errbox = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p")
                    
                    if errbox.is_displayed():
                        print("sleeping for 60")
                        sleep(60 + randy)
                    else:
                        break
                        
                except:
                    checker -= 1
                    print("Not there!")
        #    post = driver.find_element_by_xpath(post_xpath)
        #    post.click()
        
        
    
        driver.refresh() 
        sleep(1.5 + mini_randy)
            
            
''' MAIN '''

thread1 = threading.Thread(target = whole_script)
thread2 = threading.Thread(target = pageupper)

thread1.start()
thread2.start()

thread1.join()
thread2.join()