

# general tab
# bug https://markettradersinstitute.atlassian.net/browse/KYIV-9783
def test_change_font_size(app):
    app.open_charts_page()
    app.global_settings.open_general_global_settings()
    size_before = app.global_settings.choose_random_font_size()
    app.global_settings.click_save_button()
    size_after = app.global_settings.check_font_size()
    assert size_before == size_after


def test_select_light_appearance(app):
    app.open_charts_page()
    app.global_settings.open_general_global_settings()
    app.global_settings.select_light_theme()
    app.global_settings.click_save_button()
    background_color = app.global_settings.check_background_color()
    assert background_color == '#ffffff'


def test_select_dark_appearance(app):
    app.open_charts_page()
    app.global_settings.open_general_global_settings()
    app.global_settings.select_dark_theme()
    app.global_settings.click_save_button()
    background_color = app.global_settings.check_background_color()
    assert background_color == '#26272e'


# charts tab
def test_change_chart_candle_color(app):
    app.open_charts_page()
    app.global_settings.open_charts_global_setting()
    before_line_mountain_color = app.global_settings.change_charts_line_mountain_color()
    before_up_candle_color = app.global_settings.change_charts_up_candle_color()
    before_up_candle_wick_color = app.global_settings.change_charts_up_candle_wick_color()
    before_up_candle_outline_color = app.global_settings.change_charts_up_candle_outline_color()
    before_down_candle_color = app.global_settings.change_charts_down_candle_color()
    before_down_candle_wick_color = app.global_settings.change_charts_down_candle_wick_color()
    before_down_candle_outline_color = app.global_settings.change_charts_down_candle_outline_color()
    before_mpd_ssl_line_color = app.global_settings.change_charts_mpd_ssl_line_color()
    before_bullish_formation_color = app.global_settings.change_charts_bullish_formation_color()
    before_bearish_formation_color = app.global_settings.change_charts_bearish_formation_color()
    before_text_color = app.global_settings.change_charts_text_color()
    before_gradient1_color = app.global_settings.change_charts_gradient_color1()
    before_gradient2_color = app.global_settings.change_charts_gradient_color2()
    before_grid_style_color = app.global_settings.change_charts_grid_style_color()
    app.global_settings.click_save_button()
    app.global_settings.open_charts_global_setting()
    after_line_mountain_color = app.global_settings.check_charts_line_mountain_color()
    after_up_candle_color = app.global_settings.check_charts_up_candle_color()
    after_up_candle_wick_color = app.global_settings.check_charts_up_candle_wick_color()
    after_up_candle_outline_color = app.global_settings.check_charts_up_candle_outline_color()
    after_down_candle_color = app.global_settings.check_charts_down_candle_color()
    after_down_candle_wick_color = app.global_settings.check_charts_down_candle_wick_color()
    after_down_candle_outline_color = app.global_settings.check_charts_down_candle_outline_color()
    after_mpd_ssl_line_color = app.global_settings.check_charts_mpd_ssl_line_color()
    after_bullish_formation_color = app.global_settings.check_charts_bullish_formation_color()
    after_bearish_formation_color = app.global_settings.check_charts_bearish_formation_color()
    after_text_color = app.global_settings.check_charts_text_color()
    after_gradient1_color = app.global_settings.check_charts_gradient_color1()
    after_gradient2_color = app.global_settings.check_charts_gradient_color2()
    after_grid_style_color = app.global_settings.check_charts_grid_style_color()
    assert before_line_mountain_color == after_line_mountain_color
    assert before_up_candle_color == after_up_candle_color
    assert before_up_candle_wick_color == after_up_candle_wick_color
    assert before_up_candle_outline_color == after_up_candle_outline_color
    assert before_down_candle_color == after_down_candle_color
    assert before_down_candle_wick_color == after_down_candle_wick_color
    assert before_down_candle_outline_color == after_down_candle_outline_color
    assert before_mpd_ssl_line_color == after_mpd_ssl_line_color
    assert before_bullish_formation_color == after_bullish_formation_color
    assert before_bearish_formation_color == after_bearish_formation_color
    assert before_text_color == after_text_color
    assert before_gradient1_color == after_gradient1_color
    assert before_gradient2_color == after_gradient2_color
    assert before_grid_style_color == after_grid_style_color


# bug https://markettradersinstitute.atlassian.net/browse/KYIV-9783
def test_change_show_watermark_switcher(app):
    app.open_charts_page()
    app.global_settings.open_charts_global_setting()
    state1 = app.global_settings.click_watermark_switcher()
    app.global_settings.click_save_button()
    app.global_settings.open_charts_global_setting()
    state2 = app.global_settings.check__watermark_switcher()
    assert state1 == state2


def test_change_charts_grid_style(app):
    app.open_charts_page()
    app.global_settings.open_charts_global_setting()
    app.global_settings.change_grid_style()
    style_type_before = app.global_settings.check_grid_style_type()
    app.global_settings.click_save_button()
    app.global_settings.open_charts_global_setting()
    style_type_after = app.global_settings.check_grid_style_type()
    assert style_type_before == style_type_after


def test_change_chart_font(app):
    app.open_charts_page()
    app.global_settings.open_charts_global_setting()
    app.global_settings.change_chart_font()
    chart_font_before = app.global_settings.check_chart_font()
    app.global_settings.click_save_button()
    app.global_settings.open_charts_global_setting()
    chart_font_after = app.global_settings.check_chart_font()
    assert chart_font_before == chart_font_after


def test_change_chart_text_size(app):
    app.open_charts_page()
    app.global_settings.open_charts_global_setting()
    app.global_settings.change_chart_text_size()
    chart_text_size_before = app.global_settings.check_chart_text_size()
    app.global_settings.click_save_button()
    app.global_settings.open_charts_global_setting()
    chart_text_size_after = app.global_settings.check_chart_text_size()
    assert chart_text_size_before == chart_text_size_after


# trading tab
def test_change_trading_switchers_state(app):
    app.open_charts_page()
    app.global_settings.open_trading_global_setting()
    app.global_settings.change_switcher_show_open_orders_state()
    switcher_show_open_orders_state1 = app.global_settings.check_switcher_show_open_orders_state()
    app.global_settings.change_switcher_show_pending_orders_state()
    switcher_show_pending_orders_state1 = app.global_settings.check_switcher_show_pending_orders_state()
    app.global_settings.change_switcher_show_markers_state()
    switcher_show_markers_state1 = app.global_settings.check_switcher_show_markers_state()
    switcher_one_click_trades_state1 = app.global_settings.change_switcher_one_click_trades_state
    app.global_settings.click_save_button()
    app.global_settings.open_trading_global_setting()
    switcher_show_open_orders_state2 = app.global_settings.check_switcher_show_open_orders_state()
    switcher_show_pending_orders_state2 = app.global_settings.check_switcher_show_pending_orders_state()
    switcher_show_markers_state2 = app.global_settings.check_switcher_show_markers_state()
    switcher_one_click_trades_state2 = app.global_settings.check_switcher_one_click_trades_state()
    assert switcher_show_open_orders_state1 == switcher_show_open_orders_state2
    assert switcher_show_pending_orders_state1 == switcher_show_pending_orders_state2
    assert switcher_show_markers_state1 == switcher_show_markers_state2
    assert switcher_one_click_trades_state1 == switcher_one_click_trades_state2


def test_change_color_in_trading_tab(app):
    app.open_charts_page()
    app.global_settings.open_trading_global_setting()
    app.global_settings.change_trading_buy_marker_style_color()
    app.global_settings.change_trading_sell_marker_style_color()
    app.global_settings.change_trading_close_marker_style_color()
    app.global_settings.change_trading_market_buy_line_color()
    app.global_settings.change_trading_market_sell_line_color()
    app.global_settings.change_trading_pending_orders_color()
    app.global_settings.change_trading_stop_loss_color()
    app.global_settings.change_trading_take_profit_color()
    app.global_settings.change_trading_price_alert_color()
    before_buy_market_style_color = app.global_settings.check_trading_buy_market_style_color()
    before_sell_market_style_color = app.global_settings.check_trading_sell_market_style_color()
    before_close_market_style_color = app.global_settings.check_trading_close_market_style_color()
    before_market_buy_line_color = app.global_settings.check_trading_market_buy_line_color()
    before_market_sell_line_color = app.global_settings.check_trading_market_sell_line_color()
    before_pending_orders_color = app.global_settings.check_trading_pending_orders_color()
    before_stop_loss_color = app.global_settings.check_trading_stop_loss_color()
    before_take_profit_color = app.global_settings.check_trading_take_profit_color()
    before_price_alert_color = app.global_settings.check_trading_price_alert_color()
    app.global_settings.click_save_button()
    app.global_settings.open_trading_global_setting()
    after_buy_market_style_color = app.global_settings.check_trading_buy_market_style_color()
    after_sell_market_style_color = app.global_settings.check_trading_sell_market_style_color()
    after_close_market_style_color = app.global_settings.check_trading_close_market_style_color()
    after_market_buy_line_color = app.global_settings.check_trading_market_buy_line_color()
    after_market_sell_line_color = app.global_settings.check_trading_market_sell_line_color()
    after_pending_orders_color = app.global_settings.check_trading_pending_orders_color()
    after_stop_loss_color = app.global_settings.check_trading_stop_loss_color()
    after_take_profit_color = app.global_settings.check_trading_take_profit_color()
    after_price_alert_color = app.global_settings.check_trading_price_alert_color()
    assert before_buy_market_style_color == after_buy_market_style_color
    assert before_sell_market_style_color == after_sell_market_style_color
    assert before_close_market_style_color == after_close_market_style_color
    assert before_market_buy_line_color == after_market_buy_line_color
    assert before_market_sell_line_color == after_market_sell_line_color
    assert before_pending_orders_color == after_pending_orders_color
    assert before_stop_loss_color == after_stop_loss_color
    assert before_take_profit_color == after_take_profit_color
    assert before_price_alert_color == after_price_alert_color


def test_line_style_for_trading_tab(app):
    app.open_charts_page()
    app.global_settings.open_trading_global_setting()
    app.global_settings.change_trading_buy_market_style_size()
    app.global_settings.change_trading_sell_market_style_size()
    app.global_settings.change_trading_close_market_style_size()
    app.global_settings.change_trading_market_buy_line_line_view()
    app.global_settings.change_trading_market_sell_line_line_view()
    app.global_settings.change_trading_pending_orders_line_view()
    app.global_settings.change_trading_stop_loss_line_view()
    app.global_settings.change_trading_take_profit_line_view()
    app.global_settings.change_trading_price_alert_line_view()
    before_buy_market_style_line_size = app.global_settings.check_trading_buy_market_style_size()
    before_sell_market_style_line_size = app.global_settings.check_trading_sell_market_style_size()
    before_close_market_style_line_size = app.global_settings.check_trading_close_market_style_size()
    before_market_buy_line_line_view = app.global_settings.check_trading_market_buy_line_line_view()
    before_market_sell_line_line_view = app.global_settings.check_trading_market_sell_line_line_view()
    before_pending_orders_line_view = app.global_settings.check_trading_pending_orders_line_view()
    before_stop_loss_line_view = app.global_settings.check_trading_stop_loss_line_view()
    before_take_profit_line_view = app.global_settings.check_trading_take_profit_line_view()
    before_price_alert_line_view = app.global_settings.check_trading_price_alert_line_view()
    app.global_settings.click_save_button()
    app.global_settings.open_trading_global_setting()
    after_buy_market_style_line_size = app.global_settings.check_trading_buy_market_style_size()
    after_sell_market_style_line_size = app.global_settings.check_trading_sell_market_style_size()
    after_close_market_style_line_size = app.global_settings.check_trading_close_market_style_size()
    after_market_buy_line_line_view = app.global_settings.check_trading_market_buy_line_line_view()
    after_market_sell_line_line_view = app.global_settings.check_trading_market_sell_line_line_view()
    after_pending_orders_line_view = app.global_settings.check_trading_pending_orders_line_view()
    after_stop_loss_line_view = app.global_settings.check_trading_stop_loss_line_view()
    after_take_profit_line_view = app.global_settings.check_trading_take_profit_line_view()
    after_price_alert_line_view = app.global_settings.check_trading_price_alert_line_view()
    assert before_buy_market_style_line_size == after_buy_market_style_line_size
    assert before_sell_market_style_line_size == after_sell_market_style_line_size
    assert before_close_market_style_line_size == after_close_market_style_line_size
    assert before_market_buy_line_line_view == after_market_buy_line_line_view
    assert before_market_sell_line_line_view == after_market_sell_line_line_view
    assert before_pending_orders_line_view == after_pending_orders_line_view
    assert before_stop_loss_line_view == after_stop_loss_line_view
    assert before_take_profit_line_view == after_take_profit_line_view
    assert before_price_alert_line_view == after_price_alert_line_view


# scripting tab
def test_change_scripting_font_size(app):
    app.open_charts_page()
    app.global_settings.open_scripting_global_setting()
    size_before = app.global_settings.change_scripting_font_size()
    app.global_settings.click_save_button()
    size_after = app.global_settings.check_font_size_in_scripting_tab()
    assert size_before == size_after


def test_change_run_on_state(app):
    app.open_charts_page()
    app.global_settings.open_scripting_global_setting()
    run_on_before = app.global_settings.change_run_on_state()
    app.global_settings.click_save_button()
    app.global_settings.open_scripting_global_setting()
    run_on_after = app.global_settings.return_selected_run_on()
    assert run_on_before == run_on_after


def test_automatic_logs_download_switcher(app):
    app.open_charts_page()
    app.global_settings.open_scripting_global_setting()
    switcher_show_open_orders_state1 = app.global_settings.check_automatic_logs_download_switcher_state()
    app.global_settings.click_save_button()
    app.global_settings.open_scripting_global_setting()
    switcher_show_open_orders_state2 = app.global_settings.check_switcher_automatic_logs_download_state()
    assert switcher_show_open_orders_state1 == switcher_show_open_orders_state2


def test_change_scripting_theme(app):
    app.open_charts_page()
    app.global_settings.open_scripting_global_setting()
    scripting_theme_new = app.global_settings.change_scripting_theme()
    app.global_settings.click_save_button()
    check_scripting_theme = app.global_settings.check_scripting_theme()
    assert scripting_theme_new == check_scripting_theme

