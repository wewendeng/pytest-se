import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pom import base_page


class ArticlePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = base_page.BasePage(self.driver)
        self.ele_article = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]')
        self.ele_article_manage = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a')
        self.ele_add_article = (By.XPATH, '/html/body/div/div/section[3]/div/div/div/div[1]/div/div/a')
        self.ele_input_article_title = (By.ID, 'article-title')
        self.ele_content_iframe = (By.XPATH, '//*[@id="cke_1_contents"]/iframe')
        self.ele_content = (By.XPATH, '/html/body')
        self.ele_article_issue = (By.XPATH, '//*[@id="form"]/div/div[2]/div[1]/div/button[1]')
        self.ele_article_nums = (By.CLASS_NAME, 'jp-actiontr')
        self.ele_title_mouse_hover = (By.XPATH, '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/strong/a')
        self.ele_delete_one_option = (By.XPATH, '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/a[3]')
        self.ele_delete_batch_option = (By.ID, 'batchDel')
        self.ele_checkbox = (By.NAME, 'dataItem')

    def goto_article_page(self):
        # 打开文章管理页面
        self.driver.find_element(*self.ele_article).click()
        self.driver.find_element(*self.ele_article_manage).click()

    def add_article(self, title, content):
        """
        新增文章
        Args:
            title: 文章标题
            content: 文章内容
        """
        # 点击新建-输入文章标题-输入文章内容-点击发布
        self.driver.find_element(*self.ele_add_article).click()
        time.sleep(1)
        self.driver.find_element(*self.ele_input_article_title).send_keys(title)
        # 切入文章内容输入框，输入内容后，再切出iframe
        frame1 = self.driver.find_element(*self.ele_content_iframe)
        self.driver.switch_to.frame(frame1)
        time.sleep(1)
        self.driver.find_element(*self.ele_content).send_keys(content)
        self.driver.switch_to.default_content()

        self.driver.find_element(*self.ele_article_issue).click()

    def delete_one_article(self):
        """
        删除一篇文章
        """
        # 鼠标悬浮到文章标题-点击垃圾箱
        link = self.driver.find_element(*self.ele_title_mouse_hover)
        ActionChains(self.driver).move_to_element(link).perform()
        time.sleep(1)
        self.driver.find_element(*self.ele_delete_one_option).click()

    def delete_all_article(self):
        """
        删除所有文章
        """
        # 获取标题复选框-点击批量检查
        self.driver.find_element(*self.ele_checkbox).click()
        self.driver.find_element(*self.ele_delete_batch_option).click()

        # 获取弹窗并关闭弹窗
        alert = self.base_page.get_alert()
        alert.accept()

    def get_article_nums(self):
        """
        获取文章数量
        """
        time.sleep(1)
        return len(self.driver.find_elements(*self.ele_article_nums))