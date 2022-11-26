from selenium import webdriver

global driver

def start_browser():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("http://magento-demo.lexiconn.com/customer/account/create/")
    return driver
def close_browser():
    driver.quit()
