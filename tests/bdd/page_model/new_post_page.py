from selenium.webdriver.common.by import By
from tests.bdd.page_model.base_page import BasePage
from tests.bdd.locators.new_post_page_locators import NewPostPageLocators


class NewPostPage(BasePage):

    @property
    def url(self):
        return super(NewPostPage, self).base_url + '/post'

    @property
    def form(self):
        return self.driver.find_element(*NewPostPageLocators.NEW_POST_FORM)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)

    @property
    def create_button(self):
        return self.driver.find_element(*NewPostPageLocators.CREATE_BUTTON)
