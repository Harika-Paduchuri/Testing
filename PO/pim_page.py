from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PimPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_employee(self):
        add_employee_button = self.driver.find_element(By.LINK_TEXT, "Add Employee")
        add_employee_button.click()

    def add_employee(self, first_name, middle_name,last_name):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
        self.driver.find_element(By.NAME, "middleName").send_keys(middle_name)
        self.driver.find_element(By.NAME, "lastName").send_keys(last_name)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)  # wait to save the data

    def go_to_employee_list(self):
        employee_list_menu = self.driver.find_element(By.LINK_TEXT, "Employee List")
        employee_list_menu.click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("pim/viewEmployeeList"))

    def verify_employee(self, first_name, middle_name, last_name):
        full_name = f"{first_name} {middle_name} {last_name}".strip()
        time.sleep(3)  # Let list load
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        self.driver.execute_script("window.scrollBy(0, 1000);")
        if full_name in body_text:
            print(f"Name Verified: {full_name}")
        else:
            print(f"Name Not Found: {full_name}")
