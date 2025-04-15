from selenium.webdriver.common.by import By

from base_page import BasePage

class ProductPage(BasePage):
    WISHLIST_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/form/div/button[1]')
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="button-cart"]')
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    REVIEW_TAB = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/p/a[2]')
    REVIEW_NAME = (By.ID, 'input-name')
    REVIEW_TEXT = (By.ID, 'input-text')
    REVIEW_RATING_5 = (By.XPATH, '//*[@id="input-rating"]/input[5]')
    REVIEW_SUBMIT_BUTTON = (By.ID, 'button-review')
    REVIEW_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

    def open_reviews_tab(self):
        self.click(self.REVIEW_TAB)
        return self

    def submit_review(self, name, text):
        self.send_keys(self.REVIEW_NAME, name)
        self.send_keys(self.REVIEW_TEXT, text)
        self.click(self.REVIEW_RATING_5)
        self.click(self.REVIEW_SUBMIT_BUTTON)
        return self

    def is_review_submitted(self):
        return "Thank you for your review" in self.get_alert_text()

    def add_to_wishlist(self):
        self.click(self.WISHLIST_BUTTON)
        assert "Success" in self.is_visible(self.SUCCESS_ALERT).text
        return self

    def get_alert_text(self):
        return self.is_visible(self.SUCCESS_ALERT).text

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        return self

    def get_alert_text(self):
        return self.is_visible(self.SUCCESS_ALERT).text