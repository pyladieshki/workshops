from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
 
meetup = "Helsinki-PyLadies" # meetup name from URL
event_id = "199185392" #event ID from URL


def list_members(xpath, label):
    #get a list of all members that have responded or attended
    members = driver.find_elements(By.XPATH, xpath)

    #output a label for this list including total guest count
    print "\n" + str(len(members)) + " " + label

    i = 0
    
    while i < len(members):
        #print name of all respondents
        print str(i+1)+". "+ members[i].text
        i += 1

driver = webdriver.Firefox()
driver.implicitly_wait(10)

#open the event page
driver.get("http://www.meetup.com/" + meetup + "/events/" + event_id + "/");



try:
    driver.find_element(By.ID, "rsvpBoxContainer")

    #this event has not yet occurred
    driver.find_element_by_link_text("see all").click()
    
    list_members("//*[@id='rsvp-list']/li/div/div/h5/a", "Yes")
    list_members("//*[@id='rsvp-list-no']/li/div/div/h5/a", "No")
except NoSuchElementException:
    #this event is in the past
    list_members("//*[@id='rsvp-list']/li/div/div/h5/a", "Attended")


# TODO: how would you improve the script to take into account "+1" attendants? 


