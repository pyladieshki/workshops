from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://theoatmeal.com/quiz/got_character")
driver.implicitly_wait(10)

# start quiz
driver.find_element_by_link_text("Click here to begin").click()

answers = [3, 4, 5, 1, 1]

for i in range(0, len(answers)):

    # Wait for new answers to load

    # Find the radio buttons
    buttons = 

    # Click the answer specified
    answer = answers[i]
    buttons[answer-1].click()


