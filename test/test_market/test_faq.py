

def test_show_all(app):
    app.open_home_page()
    app.FAQ.open_faq()
    old_list = app.FAQ.get_faq_list()
    app.FAQ.show_all()
    new_list = app.FAQ.get_faq_list()
    assert old_list + 6 == new_list


def test_hide_all(app):
    app.open_home_page()
    app.FAQ.open_faq()
    old_list = app.FAQ.get_faq_list()
    app.FAQ.hide_all()
    new_list = app.FAQ.get_faq_list()
    assert old_list - 1 == new_list


def test_id_rate(app):
    app.open_home_page()
    app.FAQ.open_faq()
    app.FAQ.id_rate()
    app.FAQ.rate_link_plans()


def test_id_create(app):
    app.open_home_page()
    app.FAQ.open_faq()
    app.FAQ.id_create()
    app.FAQ.check_link_at_create()


def test_fb_group_in_support(app):
    app.open_home_page()
    app.FAQ.open_faq()
    app.FAQ.id_support()
    url_test = app.FAQ.fb_url()
    url_site = 'https://www.facebook.com/groups/417015495332176/'
    assert url_site == url_test


def test_feedback_portal_in_support(app):
    app.open_home_page()
    app.FAQ.open_faq()
    app.FAQ.id_support()
    url_test = app.FAQ.feedback_portal_url()
    url_site = 'https://ucpro.ideas.aha.io/'
    assert url_site == url_test


def test_release_notes_in_support(app):
    app.open_home_page()
    app.FAQ.open_faq()
    app.FAQ.id_support()
    url_test = app.FAQ.release_notes_url()
    url_site = 'https://docs.google.com/document/d/1cbMYxWzdwsgvdJ9R4SX8h06s93R6RSJCQ_U3PscpRXw/edit'
    assert url_site == url_test 


def test_learn_more_in_brokers(app):
    app.open_home_page()
    app.FAQ.open_faq()
    app.FAQ.id_brokers()
    url_test = app.FAQ.learn_more_url()
    url_site = 'https://blog.smarttrader.com/smarttrader-broker-name-service/'
    assert url_site == url_test


def test_help_finding_a_broker(app):
    app.open_home_page()
    app.FAQ.open_faq()
    app.FAQ.id_brokers()
    url_test = app.FAQ.help_finding_url()
    url_site = 'https://smarttrader.com/trading/'
    assert url_site == url_test


def test_open_multiple(app):
    app.open_home_page()
    app.FAQ.open_faq()
    app.FAQ.id_multiple()


def test_blog_post_in_connect(app):
    app.open_home_page()
    app.FAQ.open_faq()
    app.FAQ.id_connect()
    url_test = app.FAQ.follow_help_url()
    url_site = 'https://blog.smarttrader.com/how-to-integrate-your-forex-broker-account-to-easily-execute-trades/'
    assert url_site == url_test


def test_open_change_plans(app):
    app.open_home_page()
    app.FAQ.open_faq()
    app.FAQ.id_change_plans()