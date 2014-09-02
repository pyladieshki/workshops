from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
driver.implicitly_wait(10)

# go to the English wikipedia home page
driver.get()

i = 0

links = []

while i < 20:

    # click the random article link

    # get all wiki links inside the article content


    # count the links
    links.append(len(link_list))

    i += 1


#calcute average number of links found in a random wikipedia article
print sum(links)/float(len(links))
