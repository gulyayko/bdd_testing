from tests.bdd.locators.home_page_locators import HomePageLocators
from tests.bdd.page_model.base_page import BasePage


class HomePage(BasePage):

    @property
    def url(self):
        return super(HomePage, self).base_url + '/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.BLOG_LINK)
