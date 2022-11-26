from selenium import webdriver
import time

from BASE.Intiate_Browser import start_browser,close_browser


def test_openbrowser():
    driver = start_browser()
    #driver = webdriver.Chrome(executable_path="C:\\Users\ABBU RAM REDDY\PycharmProjects\First\E2E_Project\TEST CASES\chromedriver.exe")
    #driver.get("http://magento-demo.lexiconn.com/customer/account/create/")
    driver.maximize_window()
    time.sleep(2)

