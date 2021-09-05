

def test_no_active_errors_on_the_login_page(app):
    app.login_form.open_login_page()
    app.login_form.check_error_in_page()
    app.login_form.show_password_is_inactive()


def test_do_active_show_password(app):
    app.login_form.open_login_page()
    app.login_form.click_do_active_show_password()


def test_do_inactive_show_password(app):
    app.login_form.open_login_page()
    app.login_form.click_do_active_show_password()
    app.login_form.click_do_inactive_show_password()


def test_error_if_not_fill_fields(app):
    app.login_form.open_login_page()
    app.login_form.fill_email(mail_login="")
    app.login_form.fill_password(pass_login="")
    app.login_form.click_log_in_button()
    email_error = app.login_form.check_error_if_email_empty()
    password_error = app.login_form.check_error_if_password_empty()
    assert email_error == password_error == 'This field is required!'


def test_error_if_only_email_empty(app):
    app.login_form.open_login_page()
    app.login_form.fill_password(pass_login="P@ssw0rd")
    app.login_form.click_log_in_button()
    app.login_form.check_no_error_in_password_field()
    email_error = app.login_form.check_error_if_email_empty()
    assert email_error == 'This field is required!'


def test_error_if_only_password_empty(app):
    app.login_form.open_login_page()
    app.login_form.fill_email(mail_login="test@yopmail.com")
    app.login_form.click_log_in_button()
    app.login_form.check_no_error_in_email_field()
    password_error = app.login_form.check_error_if_password_empty()
    assert password_error == 'This field is required!'


def test_click_link_create_an_account_at_login_form(app):
    app.login_form.open_login_page()
    app.login_form.link_create_an_account_at_login_form()


def test_link_forgot_password(app):
    app.login_form.open_login_page()
    app.login_form.click_link_forgot_password()


# forgot/reset password page
def test_no_active_errors_on_the_reset_password_page(app):
    app.login_form.open_login_page()
    app.login_form.click_link_forgot_password()
    app.login_form.check_error_in_page()


def test_error_if_email_field_empty_on_the_reset_password_page(app):
    app.login_form.open_login_page()
    app.login_form.click_link_forgot_password()
    app.login_form.click_reset_password_button()
    email_error = app.login_form.check_error_in_email_field_on_reset_page()
    assert email_error == 'This field is required!'


def test_error_on_the_reset_password_page_account_does_not_exist(app):
    app.login_form.open_login_page()
    app.login_form.click_link_forgot_password()
    app.login_form.fill_email(mail_login="@yopmail.com")
    app.login_form.click_reset_password_button()
    email_error = app.login_form.check_massage_on_reset_page_if_account_not_exist()
    assert email_error == 'Account does not exist. Create an Account'


def test_link_create_an_account_on_the_reset_password_page(app):
    app.login_form.open_login_page()
    app.login_form.click_link_forgot_password()
    app.login_form.fill_email(mail_login="@yopmail.com")
    app.login_form.click_reset_password_button()
    app.login_form.click_link_create_an_account_on_reset_page()


def test_link_back_to_login_from_reset_password_page(app):
    app.login_form.open_login_page()
    app.login_form.click_link_forgot_password()
    app.login_form.click_link_back_to_login_at_reset_form()
