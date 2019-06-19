import time

def test_add_to_cart_button_is_present(browser):
	browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
	time.sleep(3)
	assert browser.find_element_by_css_selector("button.btn-add-to-basket"), "No such button"
