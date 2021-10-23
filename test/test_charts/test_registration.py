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
    app.registration.registration_fields(full_name='Test Test', email=email, password='P@ssw0rd', phone='+380930000000')
    app.registration.agree_terms_conditions_license()
    app.registration.click_button_create_my_account()
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
    app.registration.registration_fields(full_name='Test Test', email=email, password='P@ssw0rd', phone='+380930000000')
    app.registration.agree_terms_conditions_license()
    app.registration.click_button_create_my_account()
    app.registration.check_confirmation_registration()
    app.session.log_out_from_homepage()


def test_registration_without_phone(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    email = random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
    print('')
    print('Email: ', email)
    app.registration.registration_fields(full_name='Test Test', email=email, password='P@ssw0rd', phone='')
    app.registration.agree_terms_conditions_license()
    app.registration.click_button_create_my_account()
    app.registration.check_confirmation_registration()
    app.session.log_out_from_homepage()


def test_error_if_full_name_empty(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    email = random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
    print('')
    print('Email: ', email)
    app.registration.registration_fields(full_name='', email=email, password='P@ssw0rd', phone='')
    app.registration.agree_terms_conditions_license()
    app.registration.click_button_create_my_account()
    full_name_error = app.registration.name_field_error()
    assert full_name_error == 'This field is required!'


def test_error_if_email_empty(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    app.registration.registration_fields(full_name='Test Test', email='', password='P@ssw0rd', phone='')
    app.registration.agree_terms_conditions_license()
    app.registration.click_button_create_my_account()
    email_error = app.registration.email_field_error()
    assert email_error == 'This field is required!'


def test_error_if_password_empty(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    email = random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
    print('')
    print('Email: ', email)
    app.registration.registration_fields(full_name='Test Test', email=email, password='', phone=' ')
    app.registration.agree_terms_conditions_license()
    app.registration.click_button_create_my_account()
    color = app.registration.password_field_empty()
    assert color == '#ff0000'


def test_error_if_agree_checkbox_not_selected(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    email = random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
    print('')
    print('Email: ', email)
    app.registration.registration_fields(full_name='Test Test', email=email, password='P@ssw0rd', phone=' ')
    app.registration.click_button_create_my_account()
    agree_error = app.registration.text_if_agree_checkbox_not_selected()
    assert agree_error == 'You must agree with terms and conditions'


def test_check_terms_link(app):
    app.registration.registration_button()
    url = app.base_url
    new_url = app.registration.terms_link()
    assert url + 'terms/' == new_url


def test_check_license_link(app):
    app.registration.registration_button()
    url = app.base_url
    new_url = app.registration.license_link()
    assert url + 'eula/' == new_url


def test_error_if_incorrect_email(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    app.registration.click_button_create_my_account()
    app.registration.fill_email(email='te..st@yopmail.com')
    email_error1 = app.registration.email_field_error()
    assert email_error1 == 'Please enter valid email address'
    app.registration.fill_email(email='.test@yopmail.com')
    email_error2 = app.registration.email_field_error()
    assert email_error2 == 'Please enter valid email address'
    app.registration.fill_email(email='test@yopmailcom')
    email_error3 = app.registration.email_field_error()
    assert email_error3 == 'Please enter valid email address'
    app.registration.fill_email(email='testyopmail.com')
    email_error4 = app.registration.email_field_error()
    assert email_error4 == 'Please enter valid email address'
    app.registration.fill_email(email='te st@yopmail.com')
    email_error5 = app.registration.email_field_error()
    assert email_error5 == 'Please enter valid email address'
    app.registration.fill_email(email='test@yopma il.com')
    email_error6 = app.registration.email_field_error()
    assert email_error6 == 'Please enter valid email address'
    app.registration.fill_email(email='@yopmail.com')
    email_error7 = app.registration.email_field_error()
    assert email_error7 == 'Please enter valid email address'
    app.registration.fill_email(email='test@yopmailcom')
    email_error8 = app.registration.email_field_error()
    assert email_error8 == 'Please enter valid email address'
    app.registration.fill_email(email='te[st@yopmail.com')
    email_error9 = app.registration.email_field_error()
    assert email_error9 == 'Please enter valid email address'


def test_check_login_button(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    app.registration.link_login_at_registration_form()


def test_check_character_count_in_the_password_field(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    # positive cases: 8 and 30
    app.registration.fill_password(password='12345678')
    app.registration.character_count_no_error()
    app.registration.fill_password(password='1234567890test0987654321test30')
    app.registration.character_count_no_error()
    # less than 8 characters
    app.registration.fill_password(password='1')
    app.registration.active_character_count_error()
    # more than 30 characters
    app.registration.fill_password(password='1234567890test23test1234233P@ssw0rd')
    app.registration.active_character_count_error()


def test_check_special_character_in_the_password_field(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    # positive cases
    app.registration.fill_password(password='@#$-:\№')
    app.registration.special_character_no_error()
    # negative cases
    app.registration.fill_password(password='!')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='%')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='^')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='&')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='*')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='(')
    app.registration.active_special_character_error()
    app.registration.fill_password(password=')')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='_')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='+')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='=')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='/')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='[')
    app.registration.active_special_character_error()
    app.registration.fill_password(password=']')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='{')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='}')
    app.registration.active_special_character_error()
    app.registration.fill_password(password=';')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='|')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='?')
    app.registration.active_special_character_error()
    app.registration.fill_password(password=',')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='.')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='<')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='>')
    app.registration.active_special_character_error()
    app.registration.fill_password(password='"')
    app.registration.active_special_character_error()
    app.registration.fill_password(password="'")
    app.registration.active_special_character_error()


def test_check_number_in_the_password_field(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    # positive cases
    app.registration.fill_password(password='test')
    app.registration.active_number_error()
    # negative cases
    app.registration.fill_password(password='1')
    app.registration.number_no_error()


def test_check_capital_letter_in_the_password_field(app):
    app.registration.registration_button()
    app.registration.check_error_in_page()
    # positive cases
    app.registration.fill_password(password='a')
    app.registration.active_capital_letter_error()
    # negative cases
    app.registration.fill_password(password='A')
    app.registration.capital_letter_no_error()
