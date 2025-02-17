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
            except ElementNotInteractableException:
                print("Can't interact with xp")
            except StaleElementReferenceException:
                print("Can't interact with xp")

            try:
                ActionChains(driver).move_to_element(xp_button_collect).perform()
                xp_button_collect.click() 
                print("xp_collect clicked")
            except ElementClickInterceptedException:
                print("No xp popup")
            except ElementNotInteractableException:
                print("Can't interact with xp")
            except StaleElementReferenceException:
                print("Can't interact with xp")
    
        except NoSuchElementException:
            print("No pop-ups found, breaking loop")
            break