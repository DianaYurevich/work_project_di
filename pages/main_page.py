import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    url = 'https://www.21vek.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    """First product - mascara"""
    all_categories = "//button[@class='styles_catalogButton__1K6kI']"
    beauty_category = "//a[@href='/beauty/']"
    make_up_type_category = "//*[@id='content']/div[1]/div[6]/h2/a"
    mascara = "//*[@id='content']/div[1]/div/div[1]/div[2]/a"
    price_start_1 = "//*[@id='j-filter__form']/div[1]/dl/dd/label[1]/span/input"
    price_finish_1 = "//*[@id='j-filter__form']/div[1]/dl/dd/label[2]/span/input"
    filter_show_all = "//*[@id='j-filter__form']/div[3]/dl/dd"
    filter_choose_brand = "//label[@title='Max Factor']"
    button_show_products = "//*[@id='j-filter__btn']"

    add_product_1 = "//*[@id='j-result-page-1']/li[3]/dl/div[2]/form/button"
    account_shopping_cart = "//*[@id='header']/div/div[3]/div/div[4]/a"

    """Second product - headlamp"""
    search_2 = "//input[@id='catalogSearch']"
    mode = "//*[@id='j-filter__form']/div[3]/dl[3]/dt/span"
    button_4 = "//label[@title='4']"
    range = "//*[@id='j-filter__form']/div[3]/dl[21]/dt/span"
    show_filter_range = "//*[@id='j-filter__form']/div[3]/dl[21]/dd"
    button_50 = "//*[@id='j-filter__form']/div[3]/dl[21]/div/dd[56]/label"
    leds = "//*[@id='j-filter__form']/div[3]/dl[24]/dt/span"
    show_filter_leds = "//*[@id='j-filter__form']/div[3]/dl[24]/dd/span"
    button_25 = "//label[@title='25']"
    button_show_product_2 = "//*[@id='j-filter__btn']"
    add_product_2 = "//*[@id='j-result-page-1']/div/div/ul/li[1]/dl/dd/div/form/button"

    """Third product - filter for robot cleaner"""
    search_3 = "//input[@id='catalogSearch']"
    price_filter_start = "//input[@name='filter[price][from]']"
    price_filter_finish = "//input[@name='filter[price][to]']"
    model = "//label[@title='Xiaomi']"
    amount_product = "//*[@id='j-filter__form']/div[3]/dl[2]/dt"
    button_2 = "//*[@id='j-filter__form']/div[3]/dl[2]/div/dd/label"
    button_show_product_3 = "//*[@id='j-filter__btn']"
    add_product_3 = "//*[@id='j-result-page-1']/div/div/ul/li[1]/dl/dd/div/form/button"


    """For second test - information about delivery from this internet shop"""
    button_services_yet = "//*[@id='header']/div/div[1]/div/div/ul[1]/li[3]/div/div/button"
    button_delivery = "//*[@id='navMenu']/ul/li[2]/a"


    # Getters
    """First product"""
    def get_all_categories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_categories)))

    def get_beauty_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.beauty_category)))

    def get_make_up_type_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.make_up_type_category)))

    def get_mascara(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mascara)))

    def get_price_start_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_start_1)))

    def get_price_finish_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_finish_1)))

    def get_filter_show_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_show_all)))

    def get_filter_choose_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_choose_brand)))

    def get_button_show_products(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_show_products)))

    def get_add_product_1(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.add_product_1)))

    def get_account_shopping_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.account_shopping_cart)))


    """Second product"""
    def get_search_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_2)))

    def get_mode(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.mode)))

    def get_button_4(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_4)))

    def get_range(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.range)))

    def get_show_filter_range(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.show_filter_range)))

    def get_button_50(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_50)))

    def get_leds(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.leds)))

    def get_show_filter_leds(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.show_filter_leds)))

    def get_button_25(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_25)))

    def get_button_show_product_2(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_show_product_2)))

    def get_add_product_2(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.add_product_2)))

    """Third product"""
    def get_search_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_3)))

    def get_price_filter_start(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter_start)))

    def get_price_filter_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter_finish)))

    def get_model(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.model)))

    def get_amount_product(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.amount_product)))

    def get_button_2(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_2)))

    def get_button_show_product_3(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_show_product_3)))

    def get_add_product_3(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.add_product_3)))

    """For second test"""
    def get_button_services_yet(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_services_yet)))

    def get_button_delivery(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_delivery)))


    #Actions
    """First product"""
    def click_all_categories(self):
        self.get_all_categories().click()
        print("Click on button all categories")

    def click_beauty_category(self):
        self.get_beauty_category().click()
        print("Click on button and choose category of beauty")

    def click_make_up_type_category(self):
        self.get_make_up_type_category().click()
        print("Click on button and choose category of make-up")

    def click_mascara(self):
        self.get_mascara().click()
        print("Click on button mascara")

    def input_price_start_1(self, price_start_1):
        self.get_price_start_1().send_keys(price_start_1)
        print("Input text 39 - it is will be minimum price")

    def input_price_finish_1(self, price_finish_1):
        self.get_price_finish_1().send_keys(price_finish_1)
        print("Input text 40 - it is will be maximum price")

    def click_filter_show_all(self):
        self.get_filter_show_all().click()
        print("Click on button filter show all names of brand")

    def click_filter_choose_brand(self):
        self.get_filter_choose_brand().click()
        print("Click on button choose brand")

    def click_button_show_products(self):
        self.get_button_show_products().click()
        print("Click on button show products with selected options")

    def click_add_product_1(self):
        self.get_add_product_1().click()
        print("Click on button add product to shopping cart")

    def click_account_shopping_cart(self):
        self.get_account_shopping_cart().click()
        print("Click on button account shopping cart")



    """Second product"""

    def input_search_2(self, search):
        self.get_search_2().send_keys(search)
        print("Input text for search second the goods")

    def click_mode(self):
        self.get_mode().click()
        print("Click on button model")

    def click_button_4(self):
        self.get_button_4().click()
        print("Click on button 4 mode")

    def click_range(self):
        self.get_range().click()
        print("Click on button range")

    def click_show_filter_range(self):
        self.get_show_filter_range().click()
        print("Click on button show filter range")

    def click_button_50(self):
        self.get_button_50().click()
        print("Click on button 50 meters range")

    def click_leds(self):
        self.get_leds().click()
        print("Click on button leds")

    def click_show_filter_leds(self):
        self.get_show_filter_leds().click()
        print("Click on button show filter  amount of leds")

    def click_button_25(self):
        self.get_button_25().click()
        print("Click on button 25 leds")

    def click_button_show_product_2(self):
        self.get_button_show_product_2().click()
        print("Click on button show product 2")

    def click_add_product_2(self):
        self.get_add_product_2().click()
        print("Click on button add product 2")

    """Third product"""
    def input_search_3(self, search_3):
        self.get_search_3().send_keys(search_3)
        print("Input text for search third the goods")

    def input_price_filter_start(self, price_filter_start):
        self.get_price_filter_start().send_keys(price_filter_start)
        print("Input numbers of price minimum")

    def input_price_filter_finish(self, price_filter_finish):
        self.get_price_filter_finish().send_keys(price_filter_finish)
        print("Input numbers of price maximum")

    def click_model(self):
        self.get_model().click()
        print("Click on button model")

    def click_amount_product(self):
        self.get_amount_product().click()
        print("Click on button amount product")

    def click_button_2(self):
        self.get_button_2().click()
        print("Click on button 2 products")

    def click_button_show_product_3(self):
        self.get_button_show_product_3().click()
        print("Click on button show product 3")

    def click_add_product_3(self):
        self.get_add_product_3().click()
        print("Click on button add product 3")


    """For second test"""
    def click_button_services_yet(self):
        self.get_button_services_yet().click()
        print("Click on button Services")

    def click_button_delivery(self):
        self.get_button_delivery().click()
        print("Click on button Delivery")



    #Methods
    """First product"""
    def select_product_1(self):
        with allure.step("Select_product_1"):
            Logger.add_start_step(method="select_product_1")
            self.get_current_url()
            self.click_all_categories()
            self.click_beauty_category()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_make_up_type_category())
            self.click_make_up_type_category()
            self.click_mascara()
            self.input_price_start_1('39')
            self.input_price_finish_1('40')
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_filter_show_all())
            self.click_filter_show_all()
            self.driver.execute_script("arguments[0].click()", self.get_filter_choose_brand())
            self.click_filter_choose_brand()
            self.click_filter_choose_brand()
            self.click_button_show_products()
            self.get_current_url()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_add_product_1())
            self.click_add_product_1()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_account_shopping_cart())
            self.click_account_shopping_cart()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_1")

    """Second product"""
    def select_product_2(self):
        with allure.step("Select_product_2"):
            Logger.add_start_step(method="select_product_2")
            self.get_current_url()
            self.input_search_2('лобный фонарик Navigator')
            self.get_search_2().send_keys(Keys.ENTER)
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_mode())
            self.driver.execute_script("arguments[0].click()", self.get_mode())
            self.click_mode()
            self.click_mode()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_button_4())
            self.driver.execute_script("arguments[0].click()", self.get_button_4())
            self.click_button_4()
            self.click_button_4()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_range())
            self.driver.execute_script("arguments[0].click()", self.get_range())
            self.click_range()
            self.click_range()
            self.click_show_filter_range()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_button_50())
            self.driver.execute_script("arguments[0].click()", self.get_button_50())
            self.click_button_50()
            self.click_button_50()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_leds())
            self.driver.execute_script("arguments[0].click()", self.get_leds())
            self.click_leds()
            self.click_leds()
            self.click_show_filter_leds()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_button_25())
            self.driver.execute_script("arguments[0].click()", self.get_button_25())
            self.click_button_25()
            self.click_button_25()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_button_show_product_2())
            self.click_button_show_product_2()
            self.click_add_product_2()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_account_shopping_cart())
            self.click_account_shopping_cart()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_2")

    """Third product"""
    def select_product_3(self):
        with allure.step("Select_product_3"):
            Logger.add_start_step(method="select_product_3")
            self.get_current_url()
            self.input_search_3('фильтер для роботов-пылесосов')
            self.get_search_2().send_keys(Keys.ENTER)
            self.input_price_filter_start('30')
            self.input_price_filter_finish('40')
            self.click_model()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_amount_product())
            self.click_amount_product()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_button_2())
            self.driver.execute_script("arguments[0].click()", self.get_button_2())
            self.click_button_2()
            self.click_button_2()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_button_show_product_3())
            self.click_button_show_product_3()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_add_product_3())
            self.click_add_product_3()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.get_account_shopping_cart())
            self.click_account_shopping_cart()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_3")

    """For second test"""
    def select_menu_services(self):
        with allure.step("Select_menu_services"):
            Logger.add_start_step(method="select_menu_services")
            self.get_current_url()
            self.click_button_services_yet()
            self.click_button_delivery()
            self.assert_url('https://www.21vek.by/services/delivery.html')
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_services")






















