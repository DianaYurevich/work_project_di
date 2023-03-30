import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page
# from selenium.webdriver import Keys

@pytest.mark.run(order=1)
@allure.description("Test buy product 1")
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\Diana\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    # driver.find_element().send_keys(Keys.ENTER)
    driver.delete_all_cookies()


    print("Start shopping product 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_1()

    cp = Cart_page(driver)
    cp.click_checkout_product()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment_1()

    f = Finish_page(driver)
    f.finish()

    print("Finish shopping product 1")

@pytest.mark.run(order=2)
@allure.description("Test buy product 2")
def test_buy_product_2(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\Diana\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    # driver.find_element().send_keys(Keys.ENTER)
    driver.delete_all_cookies()

    print("Start shopping product 2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_2()

    cp = Cart_page(driver)
    cp.click_checkout_product()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment_2()

    f = Finish_page(driver)
    f.finish()

    print("Finish shopping product 2")

@pytest.mark.run(order=3)
@allure.description("Test buy product 3")
def test_buy_product_3(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\Diana\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    # driver.find_element().send_keys(Keys.ENTER)
    driver.delete_all_cookies()


    print("Start shopping product 3")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_3()

    cp = Cart_page(driver)
    cp.click_checkout_product()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment_3()

    f = Finish_page(driver)
    f.finish()

    print("Finish shopping product 3")
