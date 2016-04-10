#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

# Scrape for the weather
def scrape_weather_website():
    page = urlopen('http://en.ilmatieteenlaitos.fi/local-weather')
    soup = bs(page.read(), "html.parser")

    return soup

# How does the weather feel right now in Helsinki?
def temp_feels_like():
    soup = crawl_weather_website()
    temps = soup.find_all('div', class_="apparent-temperature-value")

    return temps

# Weather right now in Helsinki
def temp_now():
    # let's select the first result, i.e. weather right now
    temperature_now = temp_feels_like()[0].text
    temp_celsius = int(temperature_now.replace('°', ''))

    return temp_celsius

# How's the feeling?
def how_does_it_feel(temp):
    # temp = temp_now()
    if temp < 0:
        return "Brrrr!"
    elif temp > 10:
        return "It's nice!"
    else:
        return "Doable"


# Weather in 3 hours in Helsinki
def temp_in_3_hours():
    """
    Function that returns a temperature
    value in 3 hours
    """

    # let's select the second result, i.e. weather in 3 hours
    temp_in_3 = temp_feels_like()[1].text

    return None


def how_will_temp_be_in_3_hours():
    """
    Function that returns a str
    saying whether the temperature
    will be colder, warmer or the same
    in 3 hours
    """

    return None
