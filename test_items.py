from selenium.common.exceptions import NoSuchElementException


def test_add_to_basket_button(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        browser.find_element_by_css_selector("button.btn-add-to-basket")
    except NoSuchElementException:
        assert False, "Button 'Add to basket' not found"
