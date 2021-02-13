import pytest
from selenium import webdriver
from common import util
from pom import category_page, login_page, base_page


class TestCategary:

    category_data = [
        ('', 'python', 'test', '分类名称不能为空'),
        ('test', 'python', 'test', '')
    ]

    def setup_class(self):
        self.logger = util.logger()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # 初始化页面
        self.login_page = login_page.LoginPage(self.driver)
        self.category_page = category_page.CategaryPage(self.driver)
        self.base_page = base_page.BasePage(self.driver)
        self.login_page.login_with_admin()

    def teardown_class(self):
        self.driver.quit()

    # @pytest.mark.dependency(depends=["admin_login"], scope='module')
    @pytest.mark.parametrize('name, parent, slug, exceted', category_data)
    def test_add_category(self, name, parent, slug, exceted):

        self.login_page.goto_admin_page()
        self.category_page.add_category_info(name, parent, slug)

        if name:
            assert 1 == 1
        else:
            assert self.base_page.get_toast_text() == exceted
