from selenium import webdriver
import chromedriver_binary
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import pyperclip


def ExcelToList(file_path=None):
    my_list = None
    if(file_path is not None):
        try:
            df = pd.read_excel(file_path, keep_default_na=False)
            my_records = df.to_dict(orient='records')
            my_list = [
                row for row in my_records
                if row['Automation Status'] == 'Create'
                ]
        except KeyError:
            print("KeyError - No rows to import.")
        return my_list


def getKeyValue(item, key):
    value = ""
    if (key in item):
        value = item[key]
    else:
        value = None
    return value

# def getDuraction(num):
#     """
#     Provide duration in seconds (float/integer)
#     Returns dictionary with:
#         hr=hours,
#         min=minutes,
#         sec=seconds,
#         msg= formatted message; e.g 1hr, 2min, 30s
#     """
#     my_dict = {
#         'hr': 0,
#         'min': 0,
#         'sec': 0,
#         'msg': "",
#     }
#     pass

# def CSVtoJSONString(file_path=None):
#     if(file_path is not None):
#         my_list = []
#         with open(file_path, 'r' ) as theFile:
#             reader = csv.DictReader(theFile)
#             for line in reader:
#                 my_list.append(line)
#         return my_list


def clearTextBoxByID(driver, ele_identifier):
    waitForElement(driver, ele_identifier)
    ele = driver.find_element_by_id(ele_identifier)
    ele.clear()
    # driver.execute_script(
    #     """
    #     document.getElementById('"""+ ele_identifier +"""').value = '';
    #     """
    # )


def clickElement(driver, ele_identifier):
    waitForElement(driver, ele_identifier)
    ele = driver.find_element_by_id(ele_identifier)
    ele.click()
    time.sleep(1)


def initDriver():
    my_options = webdriver.ChromeOptions()
    # my_options.add_argument("headless") # Hide/Show browser
    driver = webdriver.Chrome(chrome_options=my_options)
    driver.set_window_size(1400, 1000)
    return driver


def setTextBoxFast(driver, ele_identifier, new_value=None):
    if new_value is not None:
        clearTextBoxByID(driver, ele_identifier)
        waitForElement(driver, ele_identifier)
        ele = driver.find_element_by_id(ele_identifier)
        pyperclip.copy(new_value)
        ele.click()
        ele.send_keys(Keys.CONTROL, 'v')
        time.sleep(0.5)


def getElementValue(driver, ele_identifier):
        waitForElement(driver, ele_identifier)
        ele = driver.find_element_by_id(ele_identifier)
        return str(ele.get_attribute('value'))


def setTextBox(driver, ele_identifier, new_value=None):
    if new_value is not None:
        clearTextBoxByID(driver, ele_identifier)
        waitForElement(driver, ele_identifier)
        ele = driver.find_element_by_id(ele_identifier)
        ele.send_keys(new_value)
        time.sleep(0.5)


def setDropDown(driver, ele_identifier, visible_text=None):
    if visible_text is not None and visible_text != "":
        waitForElement(driver, ele_identifier)
        ele = Select(driver.find_element_by_id(ele_identifier))
        try:
            ele.select_by_visible_text(visible_text)
            time.sleep(0.5)
        except NoSuchElementException:
            print("\nCould not locate visible text - " + visible_text)
            exit()


def setCheckBox(driver, ele_identifier, bool_value=None):
    if bool_value is not None:
        waitForElement(driver, ele_identifier)
        ele = driver.find_element_by_id(ele_identifier)
        ele_checked = ele.is_selected()  # ele.get_attribute("checked")
        # print("bool_value = " + str(bool_value) + "\n" +
        #     "ele_checked = " + str(ele_checked)
        # )
        if (ele_checked != bool_value):
            ele.click()
            time.sleep(2)


def openNewTabAndSwitch(driver, tab_number=1, time_sleep=1):
    driver.execute_script("window.open('');")
    time.sleep(time_sleep)
    driver.switch_to.window(driver.window_handles[tab_number])


def waitForElement(
        driver, ele_identifier,
        wait_duration=10, by_identifier=By.ID):
    element = None
    try:
        element = ui.WebDriverWait(driver, wait_duration).until(
            EC.presence_of_element_located((by_identifier, ele_identifier))
        )
        # print("Found element(s) " + ele_identifier)
    except:
        print("Unable to find element(s) " + ele_identifier)
    finally:
        if not element:
            # driver.quit()
            exit()


def waitForElement2(
        driver, ele_identifier,
        wait_duration=10, by_identifier=By.ID):
    element = None
    try:
        element = ui.WebDriverWait(driver, wait_duration).until(
            EC.presence_of_element_located((by_identifier, ele_identifier))
        )
        # print("Found element(s) " + ele_identifier)
    except:
        print("Unable to find element(s) " + ele_identifier)
    finally:
        if not element:
            # driver.quit()
            alert = driver.switch_to_alert()
            alert.accept()
