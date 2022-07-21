
from time import sleep
import unittest
from pageobject.loginpage import Loginpage
from data.testdata import ReadWrite
from config.config import file,screenshot_path
from common.common import OpenBrowser
from log.log import logger
from parameterized import parameterized

class Login(unittest.TestCase,OpenBrowser):
    def setUp(self):
        # driver_path = Service(executable_path=driverpath)
        # self.Browser = webdriver.Edge(service=driver_path)
        # ##最大化窗体
        # self.Browser.maximize_window()
        # self.Browser.get(url)
        self.Browser=OpenBrowser().open_browser()
        self.Browser.implicitly_wait(15)
        self.loginobj=Loginpage(self.Browser)


    def tearDown(self):
        self.Browser.quit()


    def test_login_success(self):
        '''
        验证有效的用户名和密码成功登录系统
        '''
        users=ReadWrite(file,'user').read_data()
        username=users[0][0]
        password=users[0][1]
        self.loginobj.input_user(username)
        self.loginobj.input_pass(password)
        self.loginobj.click_login()
        sleep(1)
        # assert self.Browser.title=='我的地盘 - 禅道','fail'
        screenshot=screenshot_path+'test_login_success.png'
        self.Browser.get_screenshot_as_file(screenshot)
        logger.info(f"登录成功到{self.Browser.title}页面")


    def test_login_unsuccess(self):
        '''
        不存在的用户登录
        '''
        users = ReadWrite(file,'user').read_data()
        username = users[1][0]
        password = users[1][1]
        self.loginobj.input_user(username)
        self.loginobj.input_pass(password)
        self.loginobj.click_login()
        sleep(1)
        alert=self.Browser.switch_to.alert
        sleep(2)
        content=alert.text
        logger.info(content)
        alert.accept()
        assert content =='登录失败，请检查您的用户名或密码是否填写正确。' ,'fail'
        # screenshot = screenshot_path + 'test_login_unsuccess.png'
        # self.Browser.get_screenshot_as_file(screenshot)



