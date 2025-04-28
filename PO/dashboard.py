from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    pim_menu = (By.XPATH, "//span[text()='PIM']")
    user_dropdown = (By.XPATH, "//*[@class='oxd-userdropdown-tab']")
    logout_link = (By.LINK_TEXT, "Logout")

    def click_pim(self):
        pim_element = self.driver.find_element(*self.pim_menu)
        ActionChains(self.driver).move_to_element(pim_element).click().perform()
        WebDriverWait(self.driver,10).until(EC.url_contains("/pim/viewEmployeeList"))

    def logout(self):
        self.driver.find_element(*self.user_dropdown).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.logout_link))
        self.driver.find_element(*self.logout_link).click()

