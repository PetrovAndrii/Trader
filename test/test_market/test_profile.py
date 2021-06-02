import string
import random


def random_pass(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_log_in(app):
    app.session.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")


def test_change_pass(app):
    app.open_home_page()
    app.session.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
    app.profile.my_profile()
    app.profile.button_change_passw0rd()
    password = random_pass("P@ssw0r", 5)
    app.profile.current_password(curr_pass='P@ssw0rd')
    app.profile.change_pass(new_pass=password)
    app.profile.save_new_pass()
    print('')
    print(password)
    # return password back because we don't want change for next run test
    app.profile.button_change_passw0rd()
    app.profile.current_password(curr_pass=password)
    app.profile.change_pass(new_pass='P@ssw0rd')
    app.profile.save_new_pass()


def test_change_photo(app):
    app.open_home_page()
    app.session.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
    app.profile.my_profile()
    app.profile.user_image()
    app.profile.upload_new_photo(path_foto="\\Change_Profile_Image.png")
    app.profile.save_photo()


def test_change_phone(app):
    app.open_home_page()
    app.session.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
    app.profile.my_profile()
    app.profile.new_phone_number()
    app.profile.save_new_phone()


def test_log_out(app):
    app.session.log_out_from_homepage()
