from behave import *

from tests.bdd.page_model.base_page import BasePage
from tests.bdd.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('У страницы есть заголовок')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@step('Заголовок страницы "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content


@then('На странице отображается раздел записей')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()


@then('Я вижу пост с заголовком "(.*)"')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]
    assert len(posts_with_title) > 0
    assert all(post.is_displayed() for post in posts_with_title)
