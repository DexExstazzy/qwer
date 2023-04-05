from selenium.webdriver.common.by import By
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page1 = MainPage(driver, link )
    page1.open()
    page1.go_to_login_page()
