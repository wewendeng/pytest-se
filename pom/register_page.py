from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

        self.element_username = (By.NAME, 'username')
        self.element_email = (By.NAME, 'email')
        self.element_pwd = (By.NAME, 'pwd')
        self.element_confirmpwd = (By.NAME, 'confirmPwd')

    def goto_register_page(self, url):
        # 打开注册页面
        self.driver.get(url)

    def register_info(self, username, email, password, confirmpwd):
        """
        输入注册账户信息
        Args:
            url: 页面url
            username: 用户名
            email: 用户email
            password: 用户密码
            confirmpwd: 密码确认

        Returns: None
        """
        self.driver.find_element(*self.element_username).send_keys(username)
        self.driver.find_element(*self.element_email).send_keys(email)

        self.driver.find_element(*self.element_pwd).send_keys(password)
        self.driver.find_element(*self.element_confirmpwd).send_keys(confirmpwd)

