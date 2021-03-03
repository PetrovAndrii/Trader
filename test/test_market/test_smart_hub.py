


def test_open_tutorials(app):
    app.open_home_page()
    url = app.wd.current_url
    app.smart_hub.open_smart_hub()
    app.smart_hub.click_tutorials()
    new_url = app.wd.current_url
    assert url + 'tutorials' == new_url


def test_open_blog(app):
    app.open_home_page()
    app.smart_hub.open_smart_hub()
    app.smart_hub.click_blog()
    url = 'https://blog.smarttrader.com/'
    new_url = app.wd.current_url
    assert url == new_url


def test_open_knowledge_base(app):
    app.open_home_page()
    app.smart_hub.open_smart_hub()
    app.smart_hub.click_knowledge_base()
    url = 'https://help.smarttrader.com/s/'
    new_url = app.wd.current_url
    assert url == new_url


def test_open_ideas_community(app):
    app.open_home_page()
    url = app.wd.current_url
    app.smart_hub.open_smart_hub()
    app.smart_hub.click_ideas_community()
    new_url = app.wd.current_url
    assert url + 'ideas/' == new_url


def test_open_trading_rooms(app):
    app.open_home_page()
    url = app.wd.current_url
    app.smart_hub.open_smart_hub()
    app.smart_hub.click_trading_rooms()
    new_url = app.wd.current_url
    assert url + 'trading-rooms' == new_url


def test_open_marketplace(app):
    app.open_home_page()
    url = app.wd.current_url
    app.smart_hub.open_smart_hub()
    app.smart_hub.click_marketplace()
    new_url = app.wd.current_url
    assert url + 'marketplace/products/all/' == new_url