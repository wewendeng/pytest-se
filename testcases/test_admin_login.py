import pytest
from selenium import webdriver
from common import util
from pom import base_page, login_page


class TestAdminLogin:

    login_data = [
        ('admin', '123456', '666', '验证码不正确，请重新输入')
    ]

    def setup_class(self) -> None:
        self.login_url = 'http://localhost:8080/jpress/admin/login'
        self.logger = util.logger()
        # 初始化页面
        self.driver = webdriver.Chrome()
        self.base_page = base_page.BasePage(self.driver)
        self.login_page = login_page.LoginPage(self.driver)

    def teardown_class(self) -> None:
        self.driver.quit()

    @pytest.mark.parametrize('username, pwd, captcha, excepted', login_data)
    def test_admin_login_error(self, username, pwd, captcha, excepted):
        # 定位并输入测试数据
        self.login_page.goto_login_page(self.login_url)
        self.login_page.input_login_info(username, pwd)
        self.base_page.input_captcha(captcha)
        self.base_page.click_button()
        self.logger.info(f'admin登录case:username:{username}, pwd:{pwd}, captcha:{captcha}, expected:{excepted}')
        # 断言弹窗内容
        alert = self.base_page.get_alert()
        assert alert.text == excepted
        alert.accept()

    def test_admin_login_success(self):
        # 准备测试数据
        username = 'admin'
        pwd = '123456'
        excepted = 'JPress后台'

        # 刷新浏览器，保证页面干净
        self.driver.refresh()
        self.login_page.goto_login_page(self.login_url)
        self.login_page.input_login_info(username, pwd)
        self.base_page.input_captcha_from_thirdparty_admin()
        self.base_page.click_button()
        self.logger.info(f'admin登录case：username:{username}, pwd:{pwd}')
        self.base_page.wait_title_is(excepted)

        # 断言页面title
        assert self.driver.title == excepted
