from selenium.webdriver.common.by import By
from pom import base_page


class LoginPage:

    def __init__(self, driver):
        self.base_page = base_page.BasePage(driver)
        self.driver = driver
        self.driver.maximize_window()
        self.element_username = (By.NAME, 'user')
        self.element_pwd = (By.NAME, 'pwd')

    def goto_login_page(self, url):
        """
        打开login页面
        Args:
            url: login地址
        Returns:None
        """
        self.driver.get(url)

    def input_login_info(self, username, pwd):
        """
        打开登录页面，并输入登录账号信息
        Returns:None
        """

        self.driver.find_element(*self.element_username).send_keys(username)
        self.driver.find_element(*self.element_pwd).send_keys(pwd)

    def login_with_admin(self):
        """
        登录admin后台
        Returns:None
        """
        self.goto_login_page('http://localhost:8080/jpress/admin/login')
        self.input_login_info('admin', '123456')
        self.base_page.input_captcha_from_thirdparty_admin()
        self.base_page.click_button()

    def goto_admin_page(self):
        self.driver.get('http://localhost:8080/jpress/admin')