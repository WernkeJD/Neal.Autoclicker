import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException

def egg_press(driver):

    try:

        #logic to collect the tomogachi eggs
        eggs = driver.find_elements(By.CLASS_NAME, 'egg')

        if len(eggs) > 0:
            print("here is the eggs: ", eggs)

        try:

            for egg in eggs:
                print("clicking eggs")
                ActionChains(driver).move_to_element(egg).perform()
                egg.click()

            try:
                feed = driver.find_element(By.CLASS_NAME, 'action-btn')
                feed.click()

            except NoSuchElementException:
                print("no need to feed")

        except ElementClickInterceptedException:
            print("no eggs to collect")
        except ElementNotInteractableException:
            print("Can't interact with eggs collect")

        

    except NoSuchElementException:
        print("No pop-ups found, breaking loop")