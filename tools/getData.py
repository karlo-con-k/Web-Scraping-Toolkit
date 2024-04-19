import time
import re
from datetime import datetime
from selenium.webdriver.common.by import By



def prepareWebPageOctafx(driver):
    '''
        We need to be in the start page of Octafx, and we will move to the live time value of BTCUSD
    '''

    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "styled-btn-v2._small-on-desktop._secondary").click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "Button_button__fGgzW.secondary.small.ChipButton_chip__WFRKd").click()



def getDataOCtafx(driver, time_to_get = 5):
    '''
        Get the value of the BTCUSD every time_to_get, and save in a vector with the current time.
            We need to be in https://my.octafx.com/octatrader/
    '''

    #* To ensure that we are where we need to be
    driver.refresh() 
    time.sleep(5)

    BTCUSD_div = driver.find_element(By.XPATH, "//div[@class='SymbolInfo_quotes__zO_ns']")
    timeSerie = []

    for _ in range(10):

        time.sleep(time_to_get)
        data = BTCUSD_div.text #* Save the current BTCUSD value

        #* Get all float matches with the regular expression and save the first one
        pattern = r'[-+]?\d*\.\d+|\d+'
        matches = re.findall(pattern, data)
        current_time = datetime.now()

        if matches:
            timeSerie.append((float(matches[0]), current_time))
        else:
            print("No float found.")
            break

    return timeSerie

