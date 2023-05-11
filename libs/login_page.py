import time

from libs.driver_commands import BasicActions


class Login_page(BasicActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_page_text_Xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/h5"
        self.login_credentials_text_Xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div"
        self.username_textbox_Xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        self.password_textbox_Xpath= "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        self.login_button_Xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        self.orange_homepage_Xapth = "//*[@id='app']/div[1]/div[1]/aside/nav/div[1]/a/div[2]"

    def login_page(self):
        self.wait_element(12)
        self.element_is_displayed(self.login_page_text_Xpath)
        # assert status is True
        page_title = self.get_text_by_xpath(self.login_page_text_Xpath)
        print(page_title)

    def login_credentials_label(self):
        self.wait_element(12)
        self.element_is_displayed(self.login_credentials_text_Xpath)
        login_credentials_text = self.get_text_by_xpath(self.login_credentials_text_Xpath)
        print(login_credentials_text)

    def username_credentials(self):
        self.wait_element(10)
        self.type_by_xpath(self.username_textbox_Xpath, "Admin")

    def password_credentials(self):
        self.type_by_xpath(self.password_textbox_Xpath, "admin123")

    def login_button(self):
        self.click_by_xpath(self.login_button_Xpath)

    def orange_homepage(self):
        self.wait_element(12)
        self.element_is_displayed(self.orange_homepage_Xapth)


