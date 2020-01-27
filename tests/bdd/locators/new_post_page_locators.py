from selenium.webdriver.common.by import By


class NewPostPageLocators:
    NEW_POST_FORM = By.ID, 'post-form'
    TITLE_FILELD = By.ID, 'title'
    CONTENT_FIELD = By.ID, 'content'
    CREATE_BUTTON = By.ID, 'create-post'
