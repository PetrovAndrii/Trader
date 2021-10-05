from model.registration_model import Group
import string
import random


def random_symbol(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_no_active_errors_on_the_login_page(app):
    app.registration.registration_button()
    app.registration.show_password_is_inactive()
    app.registration.checkbox_not_selected()


def test_show_password_do_inactive(app):
    app.registration.registration_button()
    app.registration.click_do_active_show_password()
    app.registration.click_do_inactive_show_password()


def test_registration_get_started_button(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    email = random_symbol("test", 7) + random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
    print('')
    print('Email: ', email)
    app.registration.registration_fields(Group(full_name='Test Test', email=email, password='P@ssw0rd',
                                               phone='+380930000000'))
    app.registration.agree_terms_conditions_license()
    app.registration.button_create_my_account()
    app.registration.check_confirmation_registration()
    app.session.log_out_from_homepage()


def test_registration_at_login_form(app):
    app.registration.registration_button()
    app.registration.login_button()
    app.registration.check_error_in_page()
    app.registration.link_create_an_account_at_login_form()
    email = random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
    print('')
    print('Email: ', email)
    app.registration.registration_fields(Group(full_name='Test Test', email=email, password='P@ssw0rd',
                                               phone='+380930000000'))
    app.registration.agree_terms_conditions_license()
    app.registration.button_create_my_account()
    app.registration.check_confirmation_registration()
    app.session.log_out_from_homepage()


def test_registration_null_phone(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    email = random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
    print('')
    print('Email: ', email)
    app.registration.registration_fields(Group(full_name='Test Test', email=email, password='P@ssw0rd',
                                               phone=' '))
    app.registration.agree_terms_conditions_license()
    app.registration.button_create_my_account()
    app.registration.check_confirmation_registration()
    app.session.log_out_from_homepage()
