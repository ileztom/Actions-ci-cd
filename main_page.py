from selenium.webdriver.common.by import By
from base_page import BasePage

class MainPage(BasePage):
    ACCOUNT_MENU = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/a/span')
    REGISTER_LINK = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[1]/a')
    LOGO = (By.XPATH, '//*[@id="logo"]/a/img')
    FIRST_PRODUCT = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[1]/a/img')
    CAMERA_PRODUCT = (By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[1]/a/img')
    CATALOG_MENU_TABLETS = (By.XPATH, '//*[@id="narbar-menu"]/ul/li[4]/a')
    FIRST_TABLET_IN_LIST = (By.XPATH, '//*[@id="product-list"]/div/div/div[1]/a/img')

    def open_tablets_catalog(self):
        self.click(self.CATALOG_MENU_TABLETS)
        return self

    def open_first_tablet(self):
        self.click(self.FIRST_TABLET_IN_LIST)
        from product_page import ProductPage
        return ProductPage(self.driver)

    def open_camera_product(self):
        self.click(self.CAMERA_PRODUCT)
        from product_page import ProductPage
        return ProductPage(self.driver)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        return self

    def open_account_menu(self):
        self.click(self.ACCOUNT_MENU)
        return self

    def click_register(self):
        self.click(self.REGISTER_LINK)
        from register_page import RegisterPage
        return RegisterPage(self.driver)

    def go_to_home(self):
        self.click(self.LOGO)
        return self

    def open_first_product(self):
        self.click(self.FIRST_PRODUCT)
        from product_page import ProductPage
        return ProductPage(self.driver)