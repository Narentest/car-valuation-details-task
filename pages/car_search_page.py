from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import random

class CarSearchPage(BasePage):
    def __init__(self):
        self.accept_cookies = (By.ID, "onetrust-accept-btn-handler")
        self.vehicle_registration_number = (By.ID, "vehicleReg")
        self.mileage = (By.ID, "Mileage")
        self.valuation_button = (By.ID, "btn-go")
        self.error_details = (By.XPATH, "//*[@id=\"wbac-app-container\"]/div/div/vehicle-registration-check/section[1]/div/div[1]/div/div[1]/h1")

    def click_accept_link(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.accept_cookies)).click()

    def send_registration_num_and_random_mileage(self, number):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.mileage))
        self.driver.find_element(*self.vehicle_registration_number).send_keys(number)
        self.driver.find_element(*self.mileage).send_keys(str(random.randint(0, 10000)))
        self.driver.find_element(*self.valuation_button).click()
        from pages.your_details_page import YourDetailsPage  # Import here to avoid circular import
        return YourDetailsPage()