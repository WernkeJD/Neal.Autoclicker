from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
import time
import threading
import press_xp_clicker
import chest_press
import duo_lingo
import stocks


import time

# Define custom User-Agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={user_agent}")

# Initialize the WebDriver with the custom options
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://neal.fun/stimulation-clicker/")

driver.implicitly_wait(0)

click_wait = 10
upgrade_clicks = 0

start_time = time.time()

#start concurrent threads here
press_xp_thread = threading.Thread(target=press_xp_clicker.click_xp_or_press, args=(driver,)) 
press_chest = threading.Thread(target=chest_press.chest_press, args=(driver,))
lingo_script = threading.Thread(target=duo_lingo.answer_lingo, args=(driver,))
stock_thread = threading.Thread(target=stocks.trade, args=(driver,))
press_xp_thread.daemon = True
press_chest.daemon = True
lingo_script.daemon = True
stock_thread.daemon = True
press_xp_thread.start()
press_chest.start()
lingo_script.start()
stock_thread.start()

while True:
    if time.time() - start_time < click_wait:
        try:            
            button = driver.find_element(By.CLASS_NAME, 'main-btn')
            button.click()
        except ElementClickInterceptedException:
            try:
                button = driver.find_element(By.CLASS_NAME, 'main-btn main-btn-pretty') 
                button.click()
            except NoSuchElementException:
                print("no button to click")

    else:
        try:
            # Attempt to find the element using CSS_SELECTOR
            upgrades = driver.find_elements(By.CLASS_NAME, 'upgrade')
            inner_start_time = time.time()
            for upgrade in upgrades:

                if upgrades.index(upgrade) == 0 and upgrade_clicks > 100:
                    continue
                
                if upgrades.index(upgrade) == 1 and upgrade_clicks > 30:
                    continue

                upgrade.click()
                if upgrade_clicks > 150:
                    pass
                else:
                    upgrade_clicks += 1

                if time.time() - inner_start_time > 2:
                    break

        except NoSuchElementException:
            # If the element is not found, continue to the next iteration
            print("Element not found, continuing...")
        except StaleElementReferenceException:
            # If the element reference is stale, try locating it again
            print("Stale element reference, retrying...")
            continue  # Retry the loop and re-locate the element
        except ElementClickInterceptedException:
            print("Element click intercepted, retrying...")

    
        start_time = time.time()
