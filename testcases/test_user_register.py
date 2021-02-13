import pytest
from selenium import webdriver
from common import util
from pom import base_page, register_page


class TestUserRegister:

    register_data = [
        (util.gen_random_str(), util.gen_random_email(), '123456', '123456', '666', '验证码不正确'),
        (util.gen_random_str(), util.gen_random_email(), '123456', '123456', '', '注册成功，点击确定进行登录。')
    ]

    @classmethod
    def setup_class(cls) -> None:
        cls.register_url = 'http://localhost:8080/jpress/user/register'
        cls.logger = util.logger()
        # 初始化浏览器和注册页面
        cls.driver = webdriver.Chrome()
        cls.register_page = register_page.RegisterPage(cls.driver)
        cls.base_page = base_page.BasePage(cls.driver)

    @classmethod
    def teardown_class(cls) -> None:
        cls.driver.quit()

    @pytest.mark.parametrize('username, email, password, confirmpwd, captcha, expected', register_data)
    def test_user_register(self, username, email, password, confirmpwd, captcha, expected):

        self.driver.refresh()

        # 定位并输入测试数据
        self.register_page.goto_register_page(self.register_url)
        self.register_page.register_info(username, email, password, confirmpwd)

        if captcha:
            self.base_page.input_captcha(captcha)
            self.logger.debug(f'账号注册信息case：username:{username},password:{email}, password:{password},'
                              f'captcha:{captcha}, expected:{expected}')
        else:
            authcode = self.base_page.input_captcha_from_thirdparty()
            self.logger.debug(f'账号注册信息case：username:{username},password:{email}, password:{password},'
                              f'captcha:{authcode}, expected:{expected}')

        self.base_page.click_button()
        alert = self.base_page.get_alert()
        self.logger.info('alert弹窗信息：' + alert.text)
        # 断言弹窗内容
        assert alert.text == expected
        # 关闭弹窗
        alert.accept()
