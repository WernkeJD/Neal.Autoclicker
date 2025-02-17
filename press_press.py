import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException

def hydrolic_press(driver):
    while True:

        try:
            hydrolic_press_start = driver.find_element(By.CSS_SELECTOR, '#__layout > div > div > div.hydraulic-press > button.press-btn')  
            if hydrolic_press_start:
                print("found hydrolic press button")
            collect_press = driver.find_element(By.CLASS_NAME, 'press-collect')

            
            #hydrolic press handling (does not work currently)

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


        except NoSuchElementException:
            print("No pop-ups found, breaking loop")
            time.sleep(5)