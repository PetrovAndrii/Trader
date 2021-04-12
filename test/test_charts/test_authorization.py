

def test_log_in_from_homepage(browser):
    browser.session.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")


def test_log_in_from_marketplace(browser):
    browser.session.log_in_from_marketplace(mail_login="test@yopmail.com", pass_login="P@ssw0rd")


def test_log_in_from_charts_page(browser):
    browser.session.log_in_from_charts_page(mail_login="test@yopmail.com", pass_login="P@ssw0rd")


def test_check_automatically_log_in(browser):
    browser.session.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
    browser.authorization.open_google()
    browser.open_home_page()
    browser.authorization.check_log_in_profile()


def test_log_out_from_homepage(browser):
    browser.session.log_out_from_homepage()
