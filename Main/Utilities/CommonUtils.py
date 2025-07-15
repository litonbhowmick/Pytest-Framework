from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CommonUtils:

    def __init__(self,driver=WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_on_element(self,locator):
        try:
            self.wait.until(lambda x: x.execute_script("return document.readyState") == "complete")
            self.wait.until(expected_conditions.presence_of_element_located(locator)).click()
        except StaleElementReferenceException:
            self.click_on_element(locator)
        except Exception as e:
            print(e)

    def enter_text(self,locator,text):
        try:
            self.wait.until(lambda x: x.execute_script("return document.readyState") == "complete")
            self.wait.until(expected_conditions.presence_of_element_located(locator)).send_keys(text)
        except StaleElementReferenceException:
            self.enter_text(locator,text)
        except Exception as e:
            print(e)

    def count_elements_on_page_based_on_text(self,locator,text):
        elements = self.driver.find_elements(*locator)
        count = 0
        for ele in elements:
            if text in ele.text.lower():
                count += 1
                print(ele.text)
        if count > 1:
            return count
        else:
            print("No elements found on the page")
        return None

    def check_visibilty_of_element(self,locator):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
        except StaleElementReferenceException:
            self.check_visibilty_of_element(locator)
        except Exception as e:
            print(e)










