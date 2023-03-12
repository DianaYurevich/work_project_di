import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_site_services():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\Diana\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)

    print("Start test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_services()

    print("Finish test")
