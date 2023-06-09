import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Payment_page(Base):

    url = 'https://www.21vek.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    """PRODUCT 1 - mascara"""
    delete_product_1 = "//*[@id='j-delete-8631523']"
    # confirm_the_order = "//button[@id='j-basket__confirm']"

    """PRODUCT 2 - headlamp"""
    delete_product_2 = "//*[@id='j-delete-6778132']"
    # confirm_the_order = "//button[@id='j-basket__confirm']"

    """PRODUCT 3 - filter for robot cleaner"""
    delete_product_3 = "//*[@id='j-delete-14464449']"
    # confirm_the_order = "//button[@id='j-basket__confirm']"

    # Getters
    """PRODUCT 1"""
    def get_delete_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_product_1)))

    # def get_confirm_the_order(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_the_order)))

    """PRODUCT 2"""
    def get_delete_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_product_2)))

    # def get_confirm_the_order(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_the_order)))

    """PRODUCT 3"""
    def get_delete_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_product_3)))

    # def get_confirm_the_order(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_the_order)))

    #Actions
    """PRODUCT 1"""
    def click_delete_product_1(self):
        self.get_delete_product_1().click()
        print("Click on button delete product 1")

    # def click_confirm_the_order(self):
    #     self.get_confirm_the_order().click()
    #     print("Click on button confirm the order")

    """PRODUCT 2"""
    def click_delete_product_2(self):
        self.get_delete_product_2().click()
        print("Click on button delete product 2")

    # def click_confirm_the_order(self):
    #     self.get_confirm_the_order().click()
    #     print("Click on button confirm the order")

    """PRODUCT 3"""
    def click_delete_product_3(self):
        self.get_delete_product_3().click()
        print("Click on button delete product 3")

    # def click_confirm_the_order(self):
    #     self.get_confirm_the_order().click()
    #     print("Click on button confirm the order")

    #Methods
    def payment_1(self):
        with allure.step("Payment of product  1 - mascara"):
            Logger.add_start_step(method="payment_1")
            self.driver.refresh()
            # self.get_current_url()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_delete_product_1())
            self.click_delete_product_1()
            self.get_screenshot()
            # self.driver.execute_script("arguments[0].scrollIntoView();", self.get_confirm_the_order())
            # self.click_confirm_the_order()
            Logger.add_end_step(url=self.driver.current_url, method="payment_1")

    def payment_2(self):
        with allure.step("Payment of product  2 - headlamp"):
            Logger.add_start_step(method="payment_2")
            self.driver.refresh()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_delete_product_2())
            self.click_delete_product_2()
            self.get_screenshot()
            # self.driver.execute_script("arguments[0].scrollIntoView();", self.get_confirm_the_order())
            # self.click_confirm_the_order()
            Logger.add_end_step(url=self.driver.current_url, method="payment_2")

    def payment_3(self):
        with allure.step("Payment of product 3 - filter robot cleaner"):
            Logger.add_start_step(method="payment_3")
            self.driver.refresh()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_delete_product_3())
            self.click_delete_product_3()
            self.get_screenshot()
            # self.driver.execute_script("arguments[0].scrollIntoView();", self.get_confirm_the_order())
            # self.click_confirm_the_order()
            Logger.add_end_step(url=self.driver.current_url, method="payment_3")

















