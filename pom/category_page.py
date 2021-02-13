from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CategaryPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.element_article = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]')
        self.element_category = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a')
        self.element_category_title_input = (By.NAME, 'category.title')
        self.element_category_choice = (By.NAME, 'category.pid')
        self.element_category_slug_input = (By.NAME, 'category.slug')
        self.element_category_add = (By.XPATH, '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button')

    def goto_category_page(self):
        """
        打开添加分类页面
        """
        # 点击文章
        self.driver.find_element(*self.element_article).click()
        # 点击分类
        self.driver.find_element(*self.element_category).click()

    def add_category_info(self, name, parent, slug):
        """
        新增分类
        Args:
            name: 分类名称
            parent: 分类的父类
            slug: slug
        """
        self.goto_category_page()
        # 输入分类名称
        self.driver.find_element(*self.element_category_title_input).send_keys(name)
        # 选择分类
        parent_category_ele = self.driver.find_element(*self.element_category_choice)
        Select(parent_category_ele).select_by_visible_text(parent)
        # 输入slug
        self.driver.find_element(*self.element_category_slug_input).send_keys(slug)
        # 点击添加
        self.driver.find_element(*self.element_category_add).click()
