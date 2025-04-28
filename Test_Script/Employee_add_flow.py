import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from PO.Login import LoginPage
from PO.dashboard import DashboardPage
from PO.pim_page import PimPage
import time


def test_orangehrm_flow():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    # Login
    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login_button()
    time.sleep(3)

    # Navigate to PIM
    dashboard = DashboardPage(driver)
    dashboard.click_pim()
    time.sleep(3)

    # Add Employees
    pim = PimPage(driver)
    employees = [("Harika","", "Paduchuri"), ("Rupsa","", "B"), ("Clera","crasta","M"), ("nick", "joseph","K")]

    for first,middle,last in employees:
        pim.click_add_employee()
        pim.add_employee(first,middle,last)


    # Verify Employees
    #   pim.go_to_employee_list()
    # for first,middle,last in employees:
        #     full_name = f"{first} {middle} {last}".strip() # to clear extra spaces
    #    pim.verify_employee(full_name)
    pim.verify_employee(first,middle,last)

    dashboard.logout()

    driver.quit()

if __name__ == "__main__":
    test_orangehrm_flow()
