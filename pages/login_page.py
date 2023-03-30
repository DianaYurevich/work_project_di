import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    url = 'https://www.21vek.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    cookie_button = "//*[@id='modal-cookie']/div/div[2]/div/button[2]"
    account_button = "//button[@class='styles_userToolsToggler__imcSl']"
    button_entrance = "//button[@data-testid='loginButton']"

    user_name = "//input[@id='login-email']"
    password = "//input[@id='login-password']"
    loggin_button = "//button[@data-testid='loginSubmit']"

    main_word = "//h6[@class='SpecialOffersList_header__1dh7S']"



    # Getters
    def get_cookie_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookie_button)))

    def get_account_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_button)))

    def get_button_entrance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_entrance)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_loggin_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loggin_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    #Actions
    def click_cookie_button(self):
        self.get_cookie_button().click()
        print("Click on cookie button")

    def click_account_button(self):
        self.get_account_button().click()
        print("Click on account button")

    def click_button_entrance(self):
        self.get_button_entrance().click()
        print("Click on button entrance")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_loggin_button(self):
        self.get_loggin_button().click()
        print("Click on loggin button")


    #Methods
    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_cookie_button()
            self.click_account_button()
            self.click_button_entrance()
            self.input_user_name("gojaryn@rambler.ru")
            self.input_password("sunnyday")
            self.click_loggin_button()
            self.assert_word(self.get_main_word(),'Все акции')
            Logger.add_end_step(url=self.driver.current_url, method="authorization")






















