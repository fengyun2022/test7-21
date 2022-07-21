from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import driverpath,url

class OpenBrowser:
    def open_browser(self):
        driver_path = Service(executable_path=driverpath)
        self.Browser = webdriver.Chrome(service=driver_path)
        ##最大化窗体
        self.Browser.maximize_window()
        self.Browser.get(url)
        return self.Browser


