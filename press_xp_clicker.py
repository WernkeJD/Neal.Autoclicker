import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException

def click_xp_or_press(driver):
    while True:
        try:
            xp_button = driver.find_element(By.CLASS_NAME, 'reward')
            xp_button_collect = driver.find_element(By.CLASS_NAME, 'collect') 

            
            #xp button handling
            try:
                ActionChains(driver).move_to_element(xp_button).perform()
                xp_button.click()
                print("xp_button clicked")
            except ElementClickInterceptedException:
                print("No xp popup")
                time.sleep(5) 
            except ElementNotInteractableException:
                print("Can't interact with xp")
                time.sleep(5)  
            except StaleElementReferenceException:
                print("Can't interact with xp")
                time.sleep(5)

            try:
                ActionChains(driver).move_to_element(xp_button_collect).perform()
                xp_button_collect.click() 
                print("xp_collect clicked")
            except ElementClickInterceptedException:
                print("No xp popup")
                time.sleep(5) 
            except ElementNotInteractableException:
                print("Can't interact with xp")
                time.sleep(5)
            except StaleElementReferenceException:
                print("Can't interact with xp")
                time.sleep(5)  
            
            #hydrolic press handling (does not work currently)

            hydrolic_press_start = driver.find_element(By.CLASS_NAME, 'hydrolic-press')  
            collect_press = driver.find_element(By.CLASS_NAME, 'press-collect press-collect-hide')

            try:                
                ActionChains(driver).move_to_element(hydrolic_press_start).perform()
                hydrolic_press_start.click()
                print("press clicked")
            except ElementClickInterceptedException:
                print("no press start")
                time.sleep(5)
            except ElementNotInteractableException:
                print("Can't interact with press")
                time.sleep(5)  

            try:
                ActionChains(driver).move_to_element(collect_press).perform()
                collect_press.click()
                print("press collected")
            except ElementClickInterceptedException:
                print("no press collect")
                time.sleep(5)
            except ElementNotInteractableException:
                print("Can't interact with press collect")
                time.sleep(5)

            #logic to collect the tomogachi eggs
            eggs = driver.find_elements(By.CLASS_NAME, 'egg-part egg-to')

            try:
                for egg in eggs:
                    egg.click()

            except ElementClickInterceptedException:
                print("no eggs to collect")
                time.sleep(5)
            except ElementNotInteractableException:
                print("Can't interact with eggs collect")
                time.sleep(5)
    
            

        except NoSuchElementException:
            print("No pop-ups found, continuing...")

        time.sleep(2)  