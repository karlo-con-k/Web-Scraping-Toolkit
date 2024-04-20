from selenium.webdriver.common.by import By
from datetime import datetime
import time
import csv
import re



def prepareWebPageOctafx(driver):
    '''
        We need to be in the start page of Octafx, and we will move to the live time value of BTCUSD
    '''

    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "styled-btn-v2._small-on-desktop._secondary").click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])




def getDataOCtafx(driver, time_between_gets = 5, sizeTimeSerie = 10):
    '''
        Get the value of the BTCUSD every time_between_gets, and save in a vector with the current time.
            We need to be in https://my.octafx.com/octatrader/
    '''

    #* To ensure that we are where we need to be
    driver.refresh() 
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "Button_button__fGgzW.secondary.small.ChipButton_chip__WFRKd").click()
    BTCUSD_div = driver.find_element(By.XPATH, "//div[@class='SymbolInfo_quotes__zO_ns']")

    timeSerie = []
    for _ in range(sizeTimeSerie):

        time.sleep(time_between_gets)
        data = BTCUSD_div.text #* Get the current BTCUSD value

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


def getDataOCtafx_and_save_in_CSV(driver, time_between_gets = 5, sizeTimeSerie = 10):
    '''
        Get the value of the BTCUSD every time_between_gets, and save in a vector with the current time.
            We need to be in https://my.octafx.com/octatrader/
    '''
    #* To ensure that we are where we need to be
    driver.refresh() 
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "Button_button__fGgzW.secondary.small.ChipButton_chip__WFRKd").click()
    BTCUSD_div = driver.find_element(By.XPATH, "//div[@class='SymbolInfo_quotes__zO_ns']")

    #* Open the CSV file for write
    with open('timePriceOf_BTCUSA.csv', mode = 'w', newline = '') as file:
        
        writer = csv.writer(file)
        writer.writerow(['cost', 'time'])

        for _ in range(sizeTimeSerie):
            time.sleep(time_between_gets)

            #* Get the current BTCUSD value, and the current time.
            data    = BTCUSD_div.text 
            pattern = r'[-+]?\d*\.\d+|\d+'
            matches = re.findall(pattern, data)
            current_time = datetime.now()

            #* Save the BTCUSD value, and the current time in the CSV
            if matches:
                cost = float(matches[0])
                writer.writerow([cost, current_time])
            else:
                print("No data cost found.")

        print(f"Data saved to {'timePriceOf_BTCUSA.csv'}")





