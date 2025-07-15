import time
from selenium.webdriver.common.by import By
from Main.Utilities.CommonUtils import CommonUtils


class Courses_Page(CommonUtils):

    # object attributes
    clear_filter = (By.XPATH, "//a[@data-sentry-element='Button']")
    courses_titles = (By.XPATH, "//h2[@data-sentry-element='CardTitle']")
    product_search = (By.ID, "heap_product-search")

    #constructor for driver initilization
    def __init__(self, driver):
        super().__init__(driver)

    # function to login
    def courses_count(self, course_name):
        self.click_on_element(self.clear_filter)
        time.sleep(5)
        self.enter_text(self.product_search,course_name)
        time.sleep(8)
        return self.count_elements_on_page_based_on_text(self.courses_titles,course_name)