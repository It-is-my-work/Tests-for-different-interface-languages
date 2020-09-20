import time
from selenium.common.exceptions import NoSuchElementException

def test_guest_should_see_button_add_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    def test_check_button():
        try:
            browser.get(link)
            time.sleep(30)
            browser.find_element_by_css_selector(".btn-add-to-basket")
            return True
        except NoSuchElementException:
            return False
    assert test_check_button()==True, f"There is no 'Add to basket' button on the webpage {link}"
