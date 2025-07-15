from selenium.webdriver.common.by import By
from Main.Pagefactory.Courses_Page import Courses_Page
from Main.Utilities.CommonUtils import CommonUtils


class LoginPage(CommonUtils):

    # object attributes
    login_button = (By.CLASS_NAME, "login-btn")
    login_text = (By.XPATH, "//a[text()='Log in']")
    login_password_link = (By.ID, "login-with-password-link")
    submit_button = (By.XPATH, "//input[@type='submit']")
    email= (By.ID, "email")
    password = (By.ID, "password")

    #constructor for driver initilization
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    # function to login
    def logintopage(self,username,password):
        self.click_on_element(self.login_button)
        self.click_on_element(self.login_text)
        self.click_on_element(self.login_password_link)
        self.check_visibilty_of_element(self.submit_button)
        self.enter_text(self.email,username)
        self.enter_text(self.password, password)
        self.click_on_element(self.submit_button)
        return Courses_Page(self.driver)