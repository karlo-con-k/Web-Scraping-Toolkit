from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

def logInOctafx(driver, user, password):
    '''
        We need to be in https://my.octafx.com/ for log in
    '''

    #* cin the user and the password
    input_user   = driver.find_element(By.CLASS_NAME, "poJmJ") 
    input_user.send_keys(user)
    input_pass   = driver.find_element(By.CLASS_NAME, "poJmJ.etfPv")
    input_pass.send_keys(password) 

    #* click in log in button
    driver.find_element(By.CLASS_NAME, "NYZcr").click()





