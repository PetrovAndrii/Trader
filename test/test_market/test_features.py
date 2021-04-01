

def test_button_open_tools(app):
    app.open_home_page()
    url = app.wd.current_url
    app.features.open_features_page()
    app.features.button_explore_smart_tools()
    new_url = app.wd.current_url
    assert url + 'smart-tools' == new_url


def test_button_get_start(app):
    app.open_home_page()
    url = app.wd.current_url
    app.features.open_features_page()
    new_url = app.features.button_get_started()
    assert url + 'plans/' == new_url


# Dashboard Customization
def test_custom_workspaces(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.custom_workspaces()


def test_variable_chart_monitoring(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.variable_chart_monitoring()


def test_access_to_realtime_data(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.access_to_realtime_data()


# Indicators
def test_popular_indicators(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.popular_indicators()


def test_active_alerts(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.active_alerts()


def test_custom_indicators(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.custom_indicators()


def test_premium_indicators(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.premium_indicators()


def test_open_marketplace_indicators(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.premium_indicators()
    app.features.premium_indicators_button()
    new_url = app.wd.current_url
    assert 'https://smarttrader.com/marketplace/products/indicators/' == new_url


# Connect & Trade
def test_easily_connect(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.easily_connect()


def test_choose_from_forex_brokers(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.choose_from_forex_brokers()


def test_connect_trading_accounts(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.connect_trading_accounts()


# Additional Features
def test_link_trading_rooms(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.trading_rooms()
    url = 'https://smarttrader.com/trading-rooms/'
    new_url = app.wd.current_url
    assert url == new_url


def test_link_trading_ideas(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.trading_ideas()
    url = 'https://smarttrader.com/ideas/'
    new_url = app.wd.current_url
    assert url == new_url


def test_link_marketplace(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.marketplace()
    url = 'https://smarttrader.com/marketplace/products/all/'
    new_url = app.wd.current_url
    assert url == new_url


def test_link_support(app):
    app.open_home_page()
    app.features.open_features_page()
    app.features.support()
    url = 'https://smarttrader.com/smart-hub/'
    new_url = app.wd.current_url
    assert url == new_url
