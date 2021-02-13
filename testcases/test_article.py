import time
import pytest
from selenium import webdriver
from common import util
from pom import base_page, article_page, login_page


class TestArticle:

    article_data = [
        ('我的文章', '我的文章内容', '文章保存成功。'),
        ('你的文章', '你的文章内容', '文章保存成功。'),
        ('他的文章', '他的文章内容', '文章保存成功。'),
        ('', '文章内容', '标题不能为空')
    ]

    def setup_class(self):
        self.logger = util.logger()
        self.driver = webdriver.Chrome()
        self.base_page = base_page.BasePage(self.driver)
        self.login_page = login_page.LoginPage(self.driver)
        self.article_page = article_page.ArticlePage(self.driver)
        self.login_page.login_with_admin()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('title, content, expected', article_data)
    def test_add_article(self, title, content, expected):

        time.sleep(1)
        self.article_page.goto_article_page()
        self.article_page.add_article(title, content)

        assert self.base_page.get_toast_text() == expected

    def test_delete_one_article(self):

        self.login_page.goto_admin_page()
        self.article_page.goto_article_page()
        delete_before_num = self.article_page.get_article_nums()
        self.article_page.delete_one_article()
        delete_after_mun = self.article_page.get_article_nums()

        assert delete_before_num == delete_after_mun + 1

    def test_delete_all_article(self):

        self.login_page.goto_admin_page()
        self.article_page.goto_article_page()
        delete_before_num = self.article_page.get_article_nums()
        if delete_before_num == 0:
            assert 1 == 1
        self.article_page.delete_all_article()
        delete_after_num = self.article_page.get_article_nums()

        assert delete_after_num == 0
