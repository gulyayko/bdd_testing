from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.bdd.locators.blog_page_locators import BlogPageLocators

use_step_matcher('re')


@given('Жду пока загрузятся записи')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located(BlogPageLocators.POSTS_SECTION))
