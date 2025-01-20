from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
import re

def trade(driver):
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
                    buy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div/div[4]/div[4]/div[2]/button[1]')))
                except NoSuchElementException:
                    print("cant get buy button")
            
                try:
                    sell = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[4]/div[4]/div[2]/button[2]')
                except NoSuchElementException:
                    print("Cant find sell button")
                except ElementNotInteractableException:
                    print("can't interact with sell button")

                price_text = price.text
                clean_price = re.sub(r"[$,]", "", price_text)
                print("cleaned price: ", clean_price)


                if int(clean_price) < 5000:
                    print('buying')
                    for i in range(3):
                        buy.click()
                        i += 1
                        buy_clicks += 1
                elif int(clean_price) > 40000 and buy_clicks != 0:
                    print("selling")
                    for i in range(buy_clicks):
                        sell.click()
                        i += 1
                        buy_clicks -= 1
                else:
                    time.sleep(5)
                    continue

        except NoSuchElementException:
            print("no such element")
            time.sleep(30)
        except ElementClickInterceptedException:
            print("click intercepted")