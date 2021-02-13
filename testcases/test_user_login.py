import pytest
from selenium import webdriver
from common import util
from pom import base_page, login_page


class TestUserLogin:

    login_data = [
        ('', '123456', '账号不能为空'),
        ('admin', '123456', '用户中心')
    ]

    def setup_class(self) -> None:
        self.login_url = 'http://localhost:8080/jpress/user/login'
        self.logger = util.logger()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_page = base_page.BasePage(self.driver)
        self.login_page = login_page.LoginPage(self.driver)

    def teardown_class(self) -> None:
        self.driver.quit()

    @pytest.mark.parametrize('username, pwd, excepted', login_data)
    def test_user_login(self, username, pwd, excepted):
        # 清除输入框内容
        self.driver.refresh()
        # 定位并输入测试数据
        self.login_page.goto_login_page(self.login_url)
        self.login_page.input_login_info(username, pwd)
        self.base_page.click_button()
        self.logger.info(f'用户登录case：username:{username}, password:{pwd}')

        if username:
            # 等待页面title
            self.base_page.wait_title_is(excepted)
            # 断言页面title
            assert self.driver.title == excepted
        else:
            # 获取弹窗
            alert = self.base_page.get_alert()
            # 断言弹窗内容
            assert alert.text == excepted
            alert.accept()
