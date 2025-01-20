import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException

def chest_press(driver):
    while True:
        try:
            # Find all chest buttons
            chest_buttons = driver.find_elements(By.CLASS_NAME, 'loot-box-target')
            
            if not chest_buttons:
                print('No chests found')
                time.sleep(5)
                continue  # Wait and try again if no chests are found

            for chest_button in chest_buttons:
                try:
                    print("Clicking on chest")
                    
                    # Ensure the chest is in view and clickable
                    ActionChains(driver).move_to_element(chest_button).perform()

                    # Click on the chest
                    chest_button.click()
                    
                    # Optionally, wait a short period before the next click
                    time.sleep(2)

                except ElementClickInterceptedException:
                    print('Element is not clickable, retrying...')
                    time.sleep(1)  # Wait a bit and retry
                except ElementNotInteractableException:
                    print('Element not interactable, retrying...')
                    time.sleep(1)  # Wait a bit and retry

        except NoSuchElementException:
            print('no chests')
            time.sleep(5)

        time.sleep(2)