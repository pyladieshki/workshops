import time

import selenium.webdriver.common.keys as keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pause = 1.1

up = keys.Keys.ARROW_UP
down = keys.Keys.ARROW_DOWN
left = keys.Keys.ARROW_LEFT
right = keys.Keys.ARROW_RIGHT


driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

driver.get("http://s.cssdeck.com/labs/full/classic-snake-game-with-html5-canvas//noframe#dontkillanim")

element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Start")))

driver.find_element_by_link_text("Start").click()

controls = driver.find_element_by_id("canvas")

# Explicit wait
time.sleep(pause)

moves = [down, left, up, right]

i= 0

# Add some smarter logic here! 

while i < 5: 
    for move in moves:

        controls.send_keys(move)
        time.sleep(pause-0.25*i)
       

    i += 1
