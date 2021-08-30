

def test_no_active_errors_on_the_page(app):
    app.login_form.open_login_page()
    app.registration.check_error_in_page()
