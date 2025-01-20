import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException


def answer_lingo(driver):

    print("lingo started")

    while True:
        try:

            questions = driver.find_elements(By.CLASS_NAME, 'question-choice')

            answers = ["S", "E", "mt", "Hwyl far", "Death", "Mandarin", "Gemealez", "Shiin", "&", "Yurok", "Octopi or octopuses", "Half a mile", "Sneaked or snuck", "Jury", "Welsh", "Around 7,100", "Scottish", "Esperanto", "Seafood", "Polish", "Potate", "Nostalgic longing", "Vengence", "Undigested prey", "Witches", "Vertebrae", "A grumble", "Palindrome", "270 degrees", "Q", "German", "Dust"]

            for question in questions:
                question_text = question.text
                if question_text in answers:
                    question.click()

            
        except NoSuchElementException:
            print("bird not available yet")
        
        except ElementClickInterceptedException:
            print("element exception error")