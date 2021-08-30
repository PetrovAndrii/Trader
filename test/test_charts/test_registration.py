from model.registration_model import Group
import string
import random


def random_symbol(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_registration_get_started_button(app):
    app.open_home_page()
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
    app.open_home_page()
    app.registration.login_button()
    app.registration.check_error_in_page()
    app.registration.join_for_free_at_login_form()
    email = random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
    print('')
    print('Email: ', email)
    app.registration.registration_fields(Group(full_name='Test Test', email=email, password='P@ssw0rd',
                                               phone='+380930000000'))
    app.registration.agree_terms_conditions_license()
    app.registration.button_create_my_account()
    app.registration.check_confirmation_registration()
    app.session.log_out_from_homepage()


# def test_registration_error_mail(app):
#     app.open_home_page()
#     app.registration.registration_button()
#     app.registration.cookies_agree()
#     app.registration.registration_fields(Group(full_name='Test Test', email='not_valid_mail', password='P@ssw0rd',
#                                                phone='+380930000000'))
#     app.registration.agree_terms_conditions_license()
#     app.registration.button_create_my_account()
#     app.registration.error_email()
#
#
# def test_registration_error_pass(app):
#     app.open_home_page()
#     app.registration.registration_button()
#     app.registration.cookies_agree()
#     app.registration.registration_fields(Group(full_name='Test Test', email='test@yopmail.com', password=' ',
#                                                phone='+380930000000'))
#     app.registration.agree_terms_conditions_license()
#     app.registration.button_create_my_account()
#     app.registration.error_pass()
#
#
# def test_registration_null_phone(app):
#     app.open_home_page()
#     app.registration.registration_button()
#     app.registration.cookies_agree()
#     email = random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
#     print('')
#     print('Email: ', email)
#     app.registration.registration_fields(Group(full_name='Test Test', email=email, password='P@ssw0rd',
#                                                phone=' '))
#     app.registration.agree_terms_conditions_license()
#     app.registration.button_create_my_account()
#     app.registration.check_confirmation_registration()
#     app.session.log_out_from_homepage()
#
#
# def test_registration_error_agree(app):
#     app.open_home_page()
#     app.registration.registration_button()
#     app.registration.cookies_agree()
#     app.registration.registration_fields(Group(full_name='Test Test', email='test@yopmail.com',
#                                                password='P@ssw0rd', phone=' '))
#     app.registration.button_create_my_account()
#     app.registration.error_agree()
#
#
# def test_registration_exist_email(app):
#     app.open_home_page()
#     app.registration.registration_button()
#     app.registration.cookies_agree()
#     app.registration.registration_fields(Group(full_name='Test Test', email='test12421@yopmail.com',
#                                                password='P@ssw0rd', phone=' '))
#     app.registration.agree_terms_conditions_license()
#     app.registration.button_create_my_account()
#     web_error = app.registration.exist_account()
#     error = 'Account already exists, please sign in.'
#     assert web_error == error
