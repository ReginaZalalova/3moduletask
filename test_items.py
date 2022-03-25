import time

from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_korzina(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_elements(By.XPATH,'//button[@class="btn btn-lg btn-primary btn-add-to-basket"]'),\
        "корзинка не найдена"

