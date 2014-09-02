from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.reittiopas.fi/en/")
driver.implicitly_wait(10)

# enter the "from" and "to" addresses


# submit the form 


# click "Return route search"
