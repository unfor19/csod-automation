from csod_login import processLogin
from csod_models import openNewTabAndSwitch, initDriver, ExcelToList, waitForElement2
from csod_edit_lo import processCatalogEditLO, processFindAndReplace, processEditSession

from tkinter import filedialog, Tk
"""
# from tkinter import *
my_list = [
    lo_id=934d7ee2-95f2-4d96-a0d5-5a83b93e9513&permissionOpID=6",
]
"""

"""
import csv or excel file

excel
choose sheet

login to CSOD process

process each row, when done, set "Complete" in row

write back to csv/excel file

"""

# Step 0
# full_file_path = R"C:\Users\meirg\Desktop\SOLUTION fields mapping.xlsx"

DEBUG = False

if DEBUG:
    full_file_path = R"C:\Users\yuvalgro\Desktop\testing yuval.xlsx"
else:
    root = Tk()
    full_file_path = filedialog.askopenfilename(
        title="Select file", filetypes=[("Excel files", "*.xlsx *.xls")]
        )
    root.destroy()

print(f"Selected file full path: {full_file_path}")
print("\nImporting Excel...")
my_list = []
try:
    my_list = ExcelToList(full_file_path)
    if len(my_list) > 0:
        print (f"Successfully imported Excel.\n{len(my_list)} rows were imported.\n")
    else:
        print("Error - No rows to import.")
        press_any_key = input("\nPress any key to close terminal...")
        exit()
        
except FileNotFoundError:
    print ("\nFailed to import Excel.")
    press_any_key = input("\nPress any key to close terminal...")
    exit()

print ("Opening browser...")
driver = initDriver()

# Step 1
print ("Starting login process...")
step1 = processLogin(driver)
step2 = None
# Step 2
if step1:
    #step2 = processCatalogEditLO(driver, my_list, full_file_path)
    #step2 = processFindAndReplace(driver, my_list, full_file_path)
    step2 = processEditSession(driver, my_list, full_file_path)
else:
    print(f"Step1 = {step1}")
# Step 3
if step2 is not None:
    print("Finished")
else:
    print("Step1 was not completed.")