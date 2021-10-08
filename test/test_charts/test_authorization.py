

def test_log_in_from_homepage(browser):
    browser.session.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")


def test_log_in_from_footer_on_marketplace(browser):
    browser.session.log_in_from_footer_on_marketplace(mail_login="test@yopmail.com", pass_login="P@ssw0rd")


def test_log_in_from_wish_list_on_marketplace(browser):
    browser.session.log_in_from_wish_list_on_marketplace(mail_login="test@yopmail.com", pass_login="P@ssw0rd")


def test_log_in_from_shopping_cart_on_marketplace(browser):
    browser.session.log_in_from_shopping_cart_on_marketplace(mail_login="test@yopmail.com", pass_login="P@ssw0rd")


def test_log_in_from_charts_page(browser):
    browser.session.log_in_from_charts_page(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
    browser.session.check_authorization_on_chart()


def test_log_in_from_modal_window_on_charts(browser):
    browser.session.log_in_from_modal_window_on_charts(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
    browser.session.check_authorization_on_chart()


def test_check_automatically_log_in(browser):
    browser.session.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
    browser.session.open_google()
    browser.open_home_page()
    browser.session.check_log_in_profile()


def test_log_out_from_homepage(browser):
    browser.session.log_out_from_homepage()
