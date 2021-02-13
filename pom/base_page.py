from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common import util


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.element_captcha = (By.NAME, 'captcha')
        self.element_button = (By.CLASS_NAME, 'btn')
        self.element_category_toast = (By.CLASS_NAME, 'toast-message')

    def get_alert(self):
        """
        显式等待alert出现在页面
        Returns
        - 等待时间内出现alert，则返回一个alter对象
        - 反之，则返回TimeoutException
        """
        try:
            WebDriverWait(self.driver, 5).until(ec.alert_is_present())
            return self.driver.switch_to.alert
        except TimeoutException:
            return 'TimeoutException'

    def wait_title_is(self, excepted):
        """
        显式等待页面title是否为预期值
        Parameters
        - excepted：title预期值
        Returns
        - 等待时间内title==excepted，则返回True
        - 反之，则返回TimeoutException
        """
        try:
            WebDriverWait(self.driver, 5).until(ec.title_is(excepted))
            return True
        except TimeoutException:
            return 'TimeoutException'

    def get_toast_text(self):
        """
        获取toast弹窗
        Returns
        - 等待时间内返回toast弹窗的文本信息
        - 反之，则返回TimeoutException
        """
        # 抓取弹窗
        try:
            WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.element_category_toast))

            return self.driver.find_element(*self.element_category_toast).text
        except TimeoutException:
            return 'TimeoutException'

    def input_captcha(self, captcha):
        """
        验证码输入
        Parameters
        captcha：验证码
        Returns：None
        """
        self.driver.find_element(*self.element_captcha).send_keys(captcha)

    def input_captcha_from_thirdparty(self):
        """
        从第三方接口识别图片验证码
        """
        self.input_captcha(util.get_authcode(self.driver, 'captchaimg'))

    def input_captcha_from_thirdparty_admin(self):
        """
        从第三方接口识别图片验证码
        """
        self.input_captcha(util.get_authcode(self.driver, 'captchaImg'))

    def click_button(self):
        """
        通用button确定按钮
        """
        self.driver.find_element(*self.element_button).click()