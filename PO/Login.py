from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element(By.NAME, "username")
        self.password_field = driver.find_element(By.NAME, "password")
        self.login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        self.error_message = (By.XPATH, "//*[contains(text(), 'Invalid credentials')]")

    def enter_username(self, username):
        self.username_field.send_keys(username)

    def enter_password(self, password):
        self.password_field.send_keys(password)

    def click_login_button(self):
        self.login_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("index.php/dashboard/index"))

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
