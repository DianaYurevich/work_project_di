import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Client_information_page(Base):

    url = 'https://www.21vek.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    client_city = "//input[@name='data[city]']"
    choose_city = "//a[@class='ui-corner-all']"
    type_deliver = "//*[@id='delivery_self']"
    place_deliver = "//*[@id='j-offer_spots-list']/label[2]"
    client_number_phone = "//*[@id='j-phone']/div/div[2]/input"
    comment = "//*[@id='j-delivery-info']/label[2]/div/textarea"


    # Getters
    def get_client_city(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.client_city)))

    def get_choose_city(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.choose_city)))

    def get_type_deliver(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.type_deliver)))

    def get_place_deliver(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.place_deliver)))

    def get_client_number_phone(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.client_number_phone)))

    def get_comment(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.comment)))

    #Actions
    def input_client_city(self, client_city):
        self.get_client_city().send_keys(client_city)
        print("Input city of client")

    def click_choose_city(self):
        self.get_choose_city().click()
        print("Click on list of cities and will been choose city of client")

    def click_type_deliver(self):
        self.get_type_deliver().click()
        print("Click on type deliver button")

    def click_place_deliver(self):
        self.get_place_deliver().click()
        print("Click on place deliver button")

    def input_client_number_phone(self, client_number_phone):
        self.get_client_number_phone().send_keys(client_number_phone)
        print("Input number phone of client")

    def input_comment(self, comment):
        self.get_comment().send_keys(comment)
        print("Input comment")


    #Methods
    def input_information(self):
        with allure.step("Client information"):
            Logger.add_start_step(method="input_information")
            self.get_current_url()
            self.get_client_city().clear()
            self.input_client_city("г.Витебск")
            self.click_choose_city()
            self.click_type_deliver()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_client_number_phone())
            self.get_client_number_phone().clear()
            self.input_client_number_phone("+375291111111")
            self.input_comment("Will call when the goods arrived")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="input_information")



























