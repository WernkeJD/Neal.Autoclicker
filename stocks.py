from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
import re


#check stock profit element instead of just the stock price when determining buy or sell orders.
def trade(driver):
    start_time = time.time()

    while True:
        try:

            dropdown = driver.find_element(By.CLASS_NAME, 'stock-select')
            dropdown.click()

            select = Select(dropdown)
            select.select_by_value('Bitcoin')
            time.sleep(2)

            buy_clicks = 0

            while True:
                try:
                    price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'last-price')))
                    print(f"Price found: {price.text}")
                except NoSuchElementException:
                    print("Price element not found on the page.")
                    continue  # Try again if element isn't found

                try:
                    buy = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[4]/div[4]/div[2]/button[1]')

                except NoSuchElementException:
                    print("cant buy")
                    try:
                        buy = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[6]/div[4]/div[2]/button[1]')
                    except NoSuchElementException:
                        print("still can't find buy")

            
                try:
                    sell = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[4]/div[4]/div[2]/button[2]')
                except NoSuchElementException:
                    print("Cant find sell button")
                    try:
                        sell = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[6]/div[4]/div[2]/button[2]')
                    except NoSuchElementException:
                        print("still cant find sell")

                except ElementNotInteractableException:
                    print("can't interact with sell button")

                price_text = price.text
                clean_price = re.sub(r"[$,xX2]", "", price_text)
                print("cleaned price: ", clean_price)


                if int(clean_price) < 5000:
                    print('buying')
                    for i in range(3):
                        buy.click()
                        i += 1
                        buy_clicks += 1
                elif int(clean_price) > 25000 and buy_clicks != 0:
                    print("selling")
                    for i in range(buy_clicks):
                        sell.click()
                        i += 1
                        buy_clicks -= 1
                else:
                    break

        except NoSuchElementException:
            print("no such element")
            time.sleep(2)
        except ElementClickInterceptedException:
            print("click intercepted")
    
        if time.time() - start_time > 2:
            break