from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class YourDetailsPage(BasePage):
    def __init__(self):
        self.registration_number = (By.XPATH, "/html/body/div[1]/wbac-app/div[1]/div/div/vehicle-questions/div/section[1]/div/div[1]/div/div[3]/div/vehicle-details/div[3]/div[1]/div[2]")
        self.make = (By.XPATH, "//*[@id=\"wbac-app-container\"]/div/div/vehicle-questions/div/section[1]/div/div[1]/div/div[3]/div/vehicle-details/div[3]/div[2]/div[1]/div[2]")
        self.model = (By.XPATH, "//*[@id=\"wbac-app-container\"]/div/div/vehicle-questions/div/section[1]/div/div[1]/div/div[3]/div/vehicle-details/div[3]/div[2]/div[2]/div[2]")
        self.year = (By.XPATH, "//*[@id=\"wbac-app-container\"]/div/div/vehicle-questions/div/section[1]/div/div[1]/div/div[3]/div/vehicle-details/div[3]/div[2]/div[3]/div[2]")

    def get_registration_number(self):
        return self.driver.find_element(*self.registration_number).text

    def get_make(self):
        return self.driver.find_element(*self.make).text

    def get_model(self):
        return self.driver.find_element(*self.model).text

    def get_year(self):
        return self.driver.find_element(*self.year).text

    def click_back_button_to_search_page(self):
        self.driver.back()
        self.driver.refresh()
        from pages.car_search_page import CarSearchPage  # Import here to avoid circular import
        return CarSearchPage()