from pytest_bdd import *
from libs.login_page import Login_page

scenarios('../feature/login.feature')


@given("the user navigates to login page")
@when("user should view the login credentials in the login page")
def login_homepage(browser):
    login_pages = Login_page(browser)
    login_pages.login_page()


@then("verify the login credentials presences in the login page")
def login_credentials_label(browser):
    login_pages = Login_page(browser)
    login_pages.login_credentials_label()


@when("the user fills the user name in the login page")
def username_textbox(browser):
    login_pages = Login_page(browser)
    login_pages.username_credentials()


@when("the user fills the password in the login page")
def password_textbox(browser):
    login_pages = Login_page(browser)
    login_pages.password_credentials()


@when("click on the login Button")
def login_button(browser):
    login_pages = Login_page(browser)
    login_pages.login_button()


@then("home page is loaded")
def home_page(browser):
    login_pages = Login_page(browser)
    login_pages.orange_homepage()
