import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
import getpass
import re
import time
from csod_models import openNewTabAndSwitch, waitForElement, setTextBox, clickElement
import csod_msgs
from csod_CONSTANTS import *

def cleanCredentials(driver):
    driver.execute_script(open("./edit_lo_login_page.js").read()) # clean fields      

def processLogin(driver):
    driver.get(MY_PORTAL_URL)  # navigate to
    while (MY_PORTAL_URL in driver.current_url):
        if not MY_USERNAME:
            my_username = input("Username: ")
        else:
            my_username = MY_USERNAME
        if not MY_PASSWORD:                                    
            my_password = getpass.getpass('Password (hidden):')
        else:
            my_password = MY_PASSWORD
        setTextBox(driver, "userNameBox", my_username)
        setTextBox(driver, "passWordBox", my_password)
        clickElement(driver, "LoginBtn")
        is_welcome_page = "Welcome.aspx" in driver.current_url

        if (is_welcome_page):
            print(csod_msgs.welcome)
            # GoTo Next step ...
            return True
        else:
            waitForElement(driver, "error", by_identifier=By.CLASS_NAME)
            err = driver.find_element_by_class_name("error")
            err_text = err.get_attribute('innerText').rstrip()
            print("Error: " + err_text + "\n" +
            "Error current_url = " + driver.current_url)
            return False