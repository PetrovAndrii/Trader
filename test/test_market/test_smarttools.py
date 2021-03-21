


def test_button_get_start(app):
    app.open_home_page()
    url = app.wd.current_url
    app.smart_tools.open_smart_tools()
    new_url = app.smart_tools.button_get_started()
    assert url + 'plans/' == new_url


def test_smart_tools_marketplace(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    page = app.smart_tools.st_in_marketplace()
    assert 'Tools' == page


def test_smart_fib(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.s_fib()


def test_smart_waves(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.s_waves()
    page_2 = app.smart_tools.name_tools()
    assert 'Smart Waves Tool' == page_2


def test_smart_patterns(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.s_patterns()
    page_2 = app.smart_tools.name_tools()
    assert 'Smart Patterns Tool' == page_2


def test_smart_trend_lines(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.s_trend_lines()


def test_smart_analytics(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.s_analytics()
    page_2 = app.smart_tools.name_tools()
    assert 'Smart Analytics Tool' == page_2


def test_smart_gauge(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.s_gauge()
    page_2 = app.smart_tools.name_tools()
    assert 'Smart Gauge' == page_2


def test_smart_support(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.s_support()


def test_smart_resistance(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.s_resistance()


def test_smart_pivots(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.s_pivots()


def test_daily_encapsulation(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.daily_encapsulation()


def test_weekly_encapsulation(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.weekly_encapsulation()


def test_candlestick_overlay(app):
    app.open_home_page()
    app.smart_tools.open_smart_tools()
    app.smart_tools.candlestick_overlay()