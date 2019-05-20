#standard packages
import time
from selenium.webdriver.common.by import By
import re

#my packages
from csod_models import setTextBox, setDropDown, setCheckBox, setTextBoxFast
from csod_models import getKeyValue, getElementValue, waitForElement, waitForElement2
from csod_models import clickElement, openNewTabAndSwitch
from csod_import_excel import write_to_excel, writeToExcel
from getDuration import getDuration
from csod_CONSTANTS import MY_PORTAL_URL
from selenium.webdriver.common.keys import Keys

def myDictionary(x):
    return {
        'edit_online_class': "ddProviders_lnkSearch",
        'search_video': "ctl00_ContentPlaceHolder1_ucProviderDropDown_csSelectProvider_txtValue",
    }[x]


def editProvider(driver, action_type, provider_name="Prototype Provider"):
    edit_window = driver.window_handles[1]
    clickElement(driver, myDictionary(action_type))
    new_window = driver.window_handles[2]
    driver.switch_to_window(new_window)
    setTextBox(driver, "SearchTextBox", provider_name)
    clickElement(driver, "SearchButton")
    waitForElement(driver, "ProvidersList_ctl01_ProviderName")

    # set mg_provider_id
    driver.execute_script("""
        var my_child = document.getElementById("ProvidersList_ctl01_ProviderName");
        var my_parent = my_child.parentElement.parentElement.querySelector("td a");
        my_parent.setAttribute("id", "mg_provider_id");
    """)
    clickElement(driver, "mg_provider_id")
    time.sleep(1)
    driver.switch_to_window(edit_window) # back to edit page


def searchVideo(driver, video_title, provider_name):
    driver.get("https://nice.csod.com/LMS/Video/Admin/VideoAdminList.aspx")
    setTextBox(
        driver,
        'ctl00_ContentPlaceHolder1_txtVideoTitle',
        video_title
    )
    editProvider(driver, "search_video")
    clickElement(driver, "ctl00_ContentPlaceHolder1_btnSearch")

def doProcess(openNewTab=True, **kwargs):
    """
    openNewTab=True,
    kwargs = {
        driver = ChromeDriver to use
        my_list,
        full_file_path (Excel file path)
        sheet_name
        myProcess (function to execute, must return True/False)
    }
    """
    if (kwargs["full_file_path"] is None):
        msg_no_file_path = "Did not provide file path."
        print(msg_no_file_path)
        exit()
    
    if (kwargs["openNewTab"]):
        openNewTabAndSwitch(kwargs["driver"])

    my_len = len(kwargs["my_list"])
    for key, item in enumerate(kwargs["my_list"]):
        t1 = time.time()
        msg_status = f"Processing ({key + 1} of {my_len}) ID: {item['ID']}"
        print(msg_status)

        #execute proces
        completed_process = kwargs["myProcess"](
            file_full_path=kwargs["file_fullpath"],
            sheet_name=kwargs["sheet_name"],
            my_data = item # {header1: value1, header2: value2}
        )

        #done processing
        time.sleep(1)

        if completed_process:
            t2 = time.time()        
            diff = round(t2-t1, 1)
            msg_success = f"Successfully processed in ({diff} seconds)\n"
            print(msg_success)
        else:
            msg_failed = "Failed to process."
            print(msg_failed)
            exit()

    return True

def processFindAndReplace(driver, my_list, full_file_path):
    openNewTabAndSwitch(driver)
    my_len = len(my_list)
    for idx, lo in enumerate(my_list):
        t1 = time.time()
        print("(" + str(idx + 1) + " of " + str(my_len) +") ID: " + str(lo['ID']))

        url_edit = getKeyValue(lo, 'Training Object ID')
        if (url_edit is not None):
            str_url = f"https://nice.csod.com/LMS/Admin/ManageTrainingEditCombined.aspx?lo_id={url_edit}&permissionOpID=6"
            driver.get(str_url)
        else:
            print("Training Object ID column does not exist.")
            return False
        
        time.sleep(2)
        waitForElement(driver, "tbLocalTitle")

        find_string = getKeyValue(lo, 'Find string')
        replace_with = getKeyValue(lo, 'Replace with')
        
        new_description = getElementValue(driver, "txtLoDescription")
        old_length = len(new_description)
        re_str = re.search(find_string, new_description)
        new_description = new_description.replace(re_str.group(0), replace_with)

        setTextBoxFast(
            driver,
            "txtLoDescription",
            new_description
        )

        new_description = getElementValue(driver, "txtLoDescription")
        new_length = len(new_description)

        if (new_length != old_length):
            return

        # save / cancel
        #waitForElement(driver, "btnBack")
        #btn_cancel = driver.find_element_by_id("btnBack")
        #btn_cancel.click()
        waitForElement(driver, "SubmitButton")
        btn_save = driver.find_element_by_id("SubmitButton")
        
        btn_save.click()
        time.sleep(1)
        waitForElement(driver, "ctl00_ContentPlaceHolder1_widgetLayout_mainDivRenderedWidgets")
        written_successfully = write_to_excel(
            full_file_path,
            'ID',
            getKeyValue(lo, 'ID'),
            'Automation Status',
            'Completed'
        )

        if written_successfully is not True:
            print("Could not write to Excel file.")
            exit()

        t2 = time.time()        
        diff = round(t2-t1, 1)
        print("Processed in (%s seconds)\n" % diff)


    return True


def processCatalogEditLO(driver, my_list, full_file_path):
    openNewTabAndSwitch(driver)
    my_len = len(my_list)
    sum_seconds = 0
    for idx, lo in enumerate(my_list):
        print(f"({idx + 1} of {my_len}) ID: {lo['ID']})")
        t1 = time.time()

        training_object_id = getKeyValue(lo, 'Training Object ID')
        if (training_object_id is not None):
            str_url = f"{MY_PORTAL_URL}/LMS/Admin/ManageTrainingEditCombined.aspx?lo_id={training_object_id}&permissionOpID=6"
            driver.get(str_url)
        else:
            msg_err = f"Training Object ID column doesn't exist."
            print(msg_err)
            return False
        
        time.sleep(2)
        waitForElement(driver, "tbLocalTitle")
        
        # provider
        #editProvider(driver, 'edit_online_class')
        
        # new title
        setTextBoxFast(
            driver,
            "tbLocalTitle",
            getKeyValue(lo, 'New Title')
        )

        # keywords
        # setTextBox(
        #     driver,
        #     "txtKeywords",
        #     getKeyValue(lo, 'New Keywords')
        # )
        setTextBoxFast(
            driver,
            "txtKeywords",
            getKeyValue(lo, 'New Keywords')
        )


        # description textarea
        setTextBoxFast(
            driver,
            "txtLoDescription",
            getKeyValue(lo, 'New Description')
        )

        # old title textarea
        setTextBoxFast(
            driver,
            "CustomFieldControl_dtlCustomField_ctl00_customFieldWrapper_ctl00_txtValue",
            getKeyValue(lo, 'Old Title')
        )

        # SOLUTION_TOP_DIVISION select
        setDropDown(
            driver,
            "CustomFieldControl_dtlCustomField_ctl00_customFieldWrapper_ctl00_lstControl",
            getKeyValue(lo, 'SOLUTION_TOP_DIVISION')
        )

        # SOLUTION_NAME select
        setDropDown(
            driver,
            "CustomFieldControl_dtlCustomField_ctl01_customFieldWrapper_ctl00_lstControl",
            getKeyValue(lo, 'SOLUTION_NAME')
        )

        # SOLUTION_VERSION select
        setDropDown(
            driver,
            "CustomFieldControl_dtlCustomField_ctl02_customFieldWrapper_ctl00_lstControl",
            getKeyValue(lo, 'SOLUTION_VERSION')
        )

        # Content Type select
        setDropDown(
            driver,
            "CustomFieldControl_dtlCustomField_ctl04_customFieldWrapper_ctl00_lstControl",
            getKeyValue(lo, 'Content Type')
        )

        # Direct Link textarea
        setTextBoxFast(
            driver,
            "CustomFieldControl_dtlCustomField_ctl05_customFieldWrapper_ctl00_txtValue",
            getKeyValue(lo, 'Direct Link')
        )

        # Recommended Prerequisites textarea
        setTextBoxFast(
            driver,
            "CustomFieldControl_dtlCustomField_ctl06_customFieldWrapper_ctl00_txtValue",
            getKeyValue(lo, 'Recommended Prerequisites')
        )

        # Target Audience textarea
        setTextBoxFast(
            driver,
            "CustomFieldControl_dtlCustomField_ctl07_customFieldWrapper_ctl00_txtValue",
            getKeyValue(lo, 'Target Audience')
        )

        # Content Created By textbox
        setTextBoxFast(
            driver,
            "CustomFieldControl_dtlCustomField_ctl10_customFieldWrapper_ctl00_txtValue",
            getKeyValue(lo, 'Content Created By')
        )

        # Exclude from Course Recommendations checkbox
        setCheckBox(
            driver,
            "cbHideFromRecommendation",
            getKeyValue(lo, 'Exclude From Recommendations')
        )

        # Active checkbox
        setCheckBox(
            driver,
            "ActiveCheck",
            getKeyValue(lo, 'Training Active')
        )

        # Compatibility Mode select
        # value = IE=EmulateIE10, index = 4 , last one
        # setDropDown(
        #     driver,
        #     "ddlCompatibilityMode",
        #     "IE10 Compatibility"
        # )

        # Enable Completion page checkbox
        setCheckBox(
            driver,
            "chkEnableCompletionPage",
            getKeyValue(lo, 'Enable Completion Page')
        )

        # save / cancel
        #waitForElement(driver, "btnBack")
        #btn_cancel = driver.find_element_by_id("btnBack")
        #btn_cancel.click()
        waitForElement(driver, "SubmitButton")
        btn_save = driver.find_element_by_id("SubmitButton")
        btn_save.click()
        time.sleep(1)
        waitForElement(driver, "ctl00_ContentPlaceHolder1_widgetLayout_mainDivRenderedWidgets")
        written_successfully = write_to_excel(
            full_file_path,
            'ID',
            getKeyValue(lo, 'ID'),
            'Automation Status',
            'Completed'
        )

        if written_successfully is not True:
            print("Could not write to Excel file.")
            exit()

        t2 = time.time()        
        diff = round(t2-t1, 1)
        sum_seconds += diff
        dur = getDuration(sum_seconds)
        print(f"Processed in ({diff} seconds)\nTime elapsed: {dur['short_msg']}\n")
    return True

def processEditSession(driver, my_list, full_file_path):
    openNewTabAndSwitch(driver)
    my_len = len(my_list)
    sum_seconds = 0
    for idx, lo in enumerate(my_list):
        print(f"({idx + 1} of {my_len}) ID: {lo['ID']})")
        t1 = time.time()

        training_locator_number = getKeyValue(lo, 'training locator number')
        if (training_locator_number is not None):
            str_url = f"{MY_PORTAL_URL}/LMS/ILT/event_sessions_list_main.aspx?locator={training_locator_number}"
            driver.get(str_url)
        else:
            msg_err = f"Training Locator Number doesn't exist."
            print(msg_err)
            return False
        
        time.sleep(2)
        waitForElement(driver, "SessionList_ctl00_EditSessionButton")
        btn_edit = driver.find_element_by_id("SessionList_ctl00_EditSessionButton")
        btn_edit.click()
        time.sleep(2)

        waitForElement(driver, "ctl00_ctl00_ContentPlaceHolder1_StepsControl_rpSteps_ctl01_lnkStep")
        btn_details = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder1_StepsControl_rpSteps_ctl01_lnkStep")
        btn_details.click()

        waitForElement2(driver, "ctl00_ctl00_ContentPlaceHolder1_SessionDetailContent_SessionCustomFieldControl_dtlCustomField_ctl14_customFieldWrapper_ctl00_txtValue")
        #time.sleep(2)
        #waitForElement(driver, "ctl00_ctl00_ContentPlaceHolder1_SessionDetailContent_SessionCustomFieldControl_dtlCustomField_ctl12_customFieldWrapper_ctl00_txtValue")
        
            

        # Content Created By textbox
        setTextBoxFast(
            driver,
            "ctl00_ctl00_ContentPlaceHolder1_SessionDetailContent_SessionCustomFieldControl_dtlCustomField_ctl14_customFieldWrapper_ctl00_txtValue",
            getKeyValue(lo, 'Content Created By')
        )

        


        # Compatibility Mode select
        # value = IE=EmulateIE10, index = 4 , last one
        # setDropDown(
        #     driver,
        #     "ddlCompatibilityMode",
        #     "IE10 Compatibility"
        # )

        

        # save / cancel
        #waitForElement(driver, "btnBack")
        #btn_cancel = driver.find_element_by_id("btnBack")
        #btn_cancel.click()
        waitForElement(driver, "ctl00_ctl00_ContentPlaceHolder1_SaveButton")
        btn_savesession = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder1_SaveButton")
        btn_savesession.click()
        time.sleep(1)
        written_successfully = write_to_excel(
            full_file_path,
            'ID',
            getKeyValue(lo, 'ID'),
            'Automation Status',
            'Completed'
        )

        if written_successfully is not True:
            print("Could not write to Excel file.")
            exit()

        t2 = time.time()        
        diff = round(t2-t1, 1)
        sum_seconds += diff
        dur = getDuration(sum_seconds)
        print(f"Processed in ({diff} seconds)\nTime elapsed: {dur['short_msg']}\n")
    return True