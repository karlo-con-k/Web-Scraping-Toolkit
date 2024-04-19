from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from .statBrowser import startDriver



# driver = webdriver.Chrome()

def logInOctafx(driver: webdriver, user: str, password: str):
    '''
        We need to be in https://my.octafx.com/ for log in, and we will need
        to enter to gmail and get the mail code
    '''
    time.sleep(1)
    #* cin the user and the password, after click log in button
    input_user   = driver.find_element(By.CLASS_NAME, "poJmJ") 
    input_user.send_keys(user)
    input_pass   = driver.find_element(By.CLASS_NAME, "poJmJ.etfPv")
    input_pass.send_keys(password) 
    driver.find_element(By.CLASS_NAME, "NYZcr").click()


    #* Load in gmail for get the code for login, we will need to wait for the code
    time.sleep(20) 
    gmailDriver =  startDriver("https://www.google.com/gmail/about/")
    logInGmail(gmailDriver, user, password)
    print("Enter to gmail successfully")

    #* Get the html id of the fist mail
    time.sleep(1)
    mails    = gmailDriver.find_elements(By.XPATH, "//div/div/div/table/tbody/tr")
    fistMail = mails[1]
    tr_id = fistMail.get_attribute("id")

    #* Click in the  fist mail, and get the code in the mail title
    gmailDriver.find_element(By.ID, tr_id).click()
    heder_mail = gmailDriver.find_element(By.CLASS_NAME, "hP")
    code = heder_mail.text[-4:]
    print("The mail code is ", code)

    #* Put the code in the text boxes of the oxtafx page, after click enter.
    input_code = driver.find_element(By.CLASS_NAME, "base-form__field")
    input_code.send_keys(code)
    driver.find_element(By.CLASS_NAME, "device-validate__button.styled-btn-v2._primary._normal").click()



def logInGmail(driver: webdriver, user: str, password: str):
    '''
        We need to be in https://www.google.com/gmail/about/ for log in
    '''
    time.sleep(1)
    #* click in Sign on the top page.
    driver.find_element(By.LINK_TEXT, "Sign in").click() 

    #* Enter the gmail user, and click next
    input_user = driver.find_element(By.ID, "identifierId") 
    input_user.send_keys(user)
    driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.BqKGqe.Jskylb.TrZEUc.lw1w4b").click()
    
    #* Wait to the pase load the user text box
    time.sleep(5) #* we could need to wait more than 5 (depends of the wifi sped)

    #* Send the gmail password
    input_password = driver.find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
    input_password.send_keys(password)
    driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.BqKGqe.Jskylb.TrZEUc.lw1w4b").click()





