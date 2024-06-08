
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def username(self):
        #self.find_element(locator='#user-name')
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True


    def password(self):
        #self.find_element(locator='#user-name')
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True


    def equal_url(self):
        if self.get_url() == 'https://www.saucedemo.com/':
            return True
        else:
            return False
