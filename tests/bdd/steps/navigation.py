from behave import *
from selenium import webdriver

from tests.bdd.page_model.blog_page import BlogPage
from tests.bdd.page_model.home_page import HomePage
from tests.bdd.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@given('Я на главной странице')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('Я на странице блога')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@given('Я на странице создания записи')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = NewPostPage(context.driver)
    context.driver.get(page.url)


@then('Открылся блог')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert expected_url == context.driver.current_url


@then('Открылась главная страница')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert expected_url == context.driver.current_url
