from selenium.webdriver.common.by import By

from main_page import MainPage
from base_page import BasePage

class RegisterPage(BasePage):
    FIRSTNAME = (By.XPATH, '//*[@id="input-firstname"]')
    LASTNAME = (By.XPATH, '//*[@id="input-lastname"]')
    EMAIL = (By.XPATH, '//*[@id="input-email"]')
    PASSWORD = (By.XPATH, '//*[@id="input-password"]')
    PRIVACY_CHECKBOX = (By.XPATH, '//*[@id="form-register"]/div/div/input')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="form-register"]/div/button')

    def register_user(self, firstname, lastname, email, password):
        self.send_keys(self.FIRSTNAME, firstname)
        self.send_keys(self.LASTNAME, lastname)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.PRIVACY_CHECKBOX)
        self.click(self.CONTINUE_BUTTON)
        return MainPage(self.driver)  # Возвращаемся на главную страницу