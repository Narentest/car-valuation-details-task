from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import configparser

class BasePage:
    driver = None
    config = configparser.ConfigParser()
    config.read('config.properties')

    @classmethod
    def initialize_browser(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(20)
        cls.driver.get(cls.config['DEFAULT']['url'])

    @classmethod
    def close_browser(cls):
        cls.driver.quit()