from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Finish_page(Base):

    url = 'https://www.21vek.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Methods
    def finish(self):
        self.get_current_url()
        # self.assert_url('')
        self.get_screenshot()























