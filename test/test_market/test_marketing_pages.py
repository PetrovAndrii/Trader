# partnership pages
# Terms & Condition
# Risk and General Disclaimer
# Privacy Policy
# Community Guidelines
# About
# License Agreement


# partnership pages
def test_partnership_more_features_link(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_partnership_pages()
    new_url = app.marketing_pages.link_view_more_features()
    assert url + 'features/' == new_url


def test_partnership_affiliate_button(app):
    app.open_home_page()
    app.marketing_pages.open_partnership_pages()
    new_url = app.marketing_pages.button_become_an_affiliate()
    url = 'https://partner.smarttrader.com/signup/'
    assert url == new_url


def test_partnership_partner_button(app):
    app.open_home_page()
    app.marketing_pages.open_partnership_pages()
    url = app.wd.current_url
    new_url = app.marketing_pages.button_become_a_partner()
    assert url + '#partnerForm' == new_url


# Terms & Condition
def test_check_terms(app):
    app.open_home_page()
    app.marketing_pages.open_terms_pages()
    app.marketing_pages.check_subparagraphs_terms_text()


def test_privacy_policy_link(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_terms_pages()
    new_url = app.marketing_pages.privacy_policy_link()
    assert url + 'privacy-policy/' == new_url


def test_community_guidelines_link(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_terms_pages()
    new_url = app.marketing_pages.community_guidelines_link()
    assert url + 'community-guidelines/' == new_url


def test_risk_disclaime_link(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_terms_pages()
    new_url = app.marketing_pages.risk_disclaime_link()
    assert url + 'risk-disclaimer/' == new_url


def test_privacy_policy_link2(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_terms_pages()
    new_url = app.marketing_pages.privacy_policy_link2()
    assert url + 'privacy-policy/' == new_url


def test_terms_use_link(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_terms_pages()
    new_url = app.marketing_pages.terms_use_link()
    assert url + 'terms/' == new_url


def test_community_guidelines_link2(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_terms_pages()
    new_url = app.marketing_pages.community_guidelines_link2()
    assert url + 'community-guidelines/' == new_url


def test_privacy_policy_link3(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_terms_pages()
    new_url = app.marketing_pages.privacy_policy_link3()
    assert url + 'privacy-policy/' == new_url


def test_privacy_policy_link4(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_terms_pages()
    new_url = app.marketing_pages.privacy_policy_link4()
    assert url + 'privacy-policy/' == new_url


def test_community_guidelines_link4(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_terms_pages()
    new_url = app.marketing_pages.community_guidelines_link4()
    assert url + 'community-guidelines/' == new_url


# Risk and General Disclaimer
def test_check_risk_disclaimer(app):
    app.open_home_page()
    app.marketing_pages.open_risk_disclainer()
    app.marketing_pages.check_subparagraphs_risk_text()


# Privacy Policy
def test_check_privacy_policy(app):
    app.open_home_page()
    app.marketing_pages.open_privacy_policy()
    app.marketing_pages.check_subparagraphs_privacy_policy_text()


def test_nai_link(app):
    app.open_home_page()
    app.marketing_pages.open_privacy_policy()
    new_url = app.marketing_pages.nai_link()
    assert 'https://optout.networkadvertising.org/?c=1#!%2F' == new_url


def test_terms_of_use_link(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_privacy_policy()
    new_url = app.marketing_pages.terms_of_use_link()
    assert url + 'terms/' == new_url


# Community Guidelines
def test_check_community_guidlines(app):
    app.open_home_page()
    app.marketing_pages.open_community_guidelines()
    app.marketing_pages.check_subparagraphs_community_guidelines_text()


def test_ideas_link(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_community_guidelines()
    new_url = app.marketing_pages.ideas_link()
    assert url + 'ideas/' == new_url


def test_scripting_link(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_community_guidelines()
    new_url = app.marketing_pages.scripting_link()
    assert url + 'scripting/' == new_url


# About
def test_about(app):
    app.open_home_page()
    app.marketing_pages.open_about()
    app.marketing_pages.check_about_page()


def test_check_button(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_about()
    new_url = app.marketing_pages.learn_more_button()
    assert url + 'smart-hub' == new_url


# License Agreement
def test_license_agreement_text(app):
    app.open_home_page()
    app.marketing_pages.open_license_agreement()
    app.marketing_pages.check_license_agreement_page()


def test_eula_terms_use_link(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_license_agreement()
    new_url = app.marketing_pages.eula_terms_of_use_link()
    assert url + 'terms/' == new_url


def test_eula_privacy_policy_link(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_license_agreement()
    new_url = app.marketing_pages.eula_privacy_policy_link()
    assert url + 'privacy-policy/' == new_url


def test_eula_privacy_policy_link2(app):
    app.open_home_page()
    url = app.wd.current_url
    app.marketing_pages.open_license_agreement()
    new_url = app.marketing_pages.eula_privacy_policy_link2()
    assert url + 'privacy-policy/' == new_url
