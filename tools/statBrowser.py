from selenium import webdriver
import os

URL_ScrapeMaster = os.environ['URL_ScrapeMaster']


def startDriver(URL_to_open = URL_ScrapeMaster):

    #* Open Chrome, and go to URL_ScrapeMaster
    driver = webdriver.Chrome()
    driver.get(URL_ScrapeMaster)    
    return driver


