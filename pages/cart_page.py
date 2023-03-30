import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):
    url = 'https://www.21vek.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    checkout_product = "//button[@id='j-basket__ok']"

    # Getters
    def get_checkout_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_product)))

    #Actions
    def click_checkout_product(self):
        self.get_checkout_product().click()
        print("Click on button of checkout product")

    #Methods
    def product_confirmation_1(self):
        with allure.step("Product_confirmation_1"):
            Logger.add_start_step(method="product_confirmation_1")
            self.get_current_url()
            self.get_screenshot()
            self.click_checkout_product()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation_1")
























