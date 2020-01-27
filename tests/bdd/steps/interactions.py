from behave import *
from tests.bdd.page_model.base_page import BasePage
from tests.bdd.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@when('Я кликаю на ссылку "(.*)"')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation
    matched_links = [link for link in links if link.text == link_text]
    if len(matched_links) > 0:
        matched_links[0].click()
    else:
        raise RuntimeError()


@when('Я ввожу "(.*)" в поле "(.*)"')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('Я кликаю кнопку "Create"')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.create_button.click()
