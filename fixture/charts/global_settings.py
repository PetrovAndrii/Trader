import random
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

from constants.charts import ChartsConstants
from constants.global_settings import GlobalSettingsConstants
from constants.scripting import ScriptingConstants


class GlobalSettingsHelper:

    def __init__(self, app):
        self.app = app

    def open_global_Settings(self):
        wd = self.app.wd
        wd.find_element(By.ID, ChartsConstants.PROFILE_BUTTON_ID).click()
        wd.find_element(By.CSS_SELECTOR, GlobalSettingsConstants.GLOBAL_SETTINGS_BUTTON_CSS_SELECTOR).click()

    def open_general_global_settings(self):
        wd = self.app.wd
        try:
            wd.find_element(By.ID, GlobalSettingsConstants.GENERAL_TAB_ID).click()
        except:
            self.open_global_Settings()

    def open_charts_global_setting(self):
        wd = self.app.wd
        try:
            wd.find_element(By.ID, GlobalSettingsConstants.CHART_TAB_ID).click()
        except:
            self.open_global_Settings()
            wd.find_element(By.ID, GlobalSettingsConstants.CHART_TAB_ID).click()

    def open_trading_global_setting(self):
        wd = self.app.wd
        try:
            wd.find_element(By.ID, GlobalSettingsConstants.TRADING_TAB_ID).click()
        except:
            self.open_global_Settings()
            wd.find_element(By.ID, GlobalSettingsConstants.TRADING_TAB_ID).click()

    def open_scripting_global_setting(self):
        wd = self.app.wd
        try:
            wd.find_element(By.ID, GlobalSettingsConstants.SCRIPTING_TAB_ID).click()
        except:
            self.open_global_Settings()
            wd.find_element(By.ID, GlobalSettingsConstants.SCRIPTING_TAB_ID).click()

    def click_save_button(self):
        wd = self.app.wd
        time.sleep(1)
        wd.find_element(By.ID, GlobalSettingsConstants.SAVE_BUTTON_ID).click()
        time.sleep(1)

    def click_close_button(self):
        wd = self.app.wd
        wd.find_element(By.ID, GlobalSettingsConstants.CLOSE_BUTTON_ID).click()

    def choose_random_font_size(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.APP_FONT_SIZE_XPATH).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.FONT_SIZE_LIST_XPATH)
        selected_size = wd.find_element(By.XPATH, GlobalSettingsConstants.APP_FONT_SIZE_XPATH)
        # return size and delete all symbols except numbers
        return re.sub("[^0-9]", "", selected_size.text)

    def check_font_size(self):
        wd = self.app.wd
        self.open_global_Settings()
        time.sleep(2)
        size = wd.find_element(By.ID, GlobalSettingsConstants.APP_FONT_SIZE_TEXT_ID).value_of_css_property('font-size')
        if size == '11.998px':
            return '14'
        else:
            if size == '12.855px':
                return '15'
            else:
                if size == '13.712px':
                    return '16'
                else:
                    if size == '14.569px':
                        return '17'
                    else:
                        if size == '15.426px':
                            return '18'

    def select_light_theme(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.LIGHT_THEME_OPTION_XPATH).click()

    def select_dark_theme(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.DARK_THEME_OPTION_XPATH).click()

    def check_background_color(self):
        wd = self.app.wd
        self.open_global_Settings()
        color = wd.find_element(By.CSS_SELECTOR, GlobalSettingsConstants.MODAL_SETTINGS_WINDOW_CSS_SELECTOR) \
            .value_of_css_property("background-color")
        return Color.from_string(color).hex

    def change_charts_line_mountain_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.LINE_MOUNTAIN_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW1_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.LINE_MOUNTAIN_COLOR_XPATH)

    def change_charts_up_candle_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.UP_CANDLE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW2_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.UP_CANDLE_COLOR_XPATH)

    def change_charts_up_candle_wick_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.UP_CANDLE_WICK_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW3_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.UP_CANDLE_WICK_COLOR_XPATH)

    def change_charts_up_candle_outline_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.UP_CANDLE_OUTLINE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW4_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.UP_CANDLE_OUTLINE_COLOR_XPATH)

    def change_charts_down_candle_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.DOWN_CANDLE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW5_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.DOWN_CANDLE_COLOR_XPATH)

    def change_charts_down_candle_wick_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.DOWN_CANDLE_WICK_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW6_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.DOWN_CANDLE_WICK_COLOR_XPATH)

    def change_charts_down_candle_outline_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.DOWN_CANDLE_OUTLINE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW7_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.DOWN_CANDLE_OUTLINE_COLOR_XPATH)

    def change_charts_mpd_ssl_line_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.MPD_SSL_LINE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW8_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.MPD_SSL_LINE_COLOR_XPATH)

    def change_charts_bullish_formation_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.BULLISH_FORMATION_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW9_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.BULLISH_FORMATION_COLOR_XPATH)

    def change_charts_bearish_formation_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.BEARISH_FORMATION_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW1_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.BEARISH_FORMATION_COLOR_XPATH)

    def change_charts_text_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.TEXT_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW2_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.TEXT_COLOR_XPATH)

    def change_charts_gradient_color1(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.GRADIENT_COLOR1_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW3_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.GRADIENT_COLOR1_XPATH)

    def change_charts_gradient_color2(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.GRADIENT_COLOR2_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW4_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.GRADIENT_COLOR2_XPATH)

    def change_charts_grid_style_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.GRID_STYLE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW5_XPATH)
        return self.return_color(By.XPATH, GlobalSettingsConstants.GRID_STYLE_COLOR_XPATH)

    def random_color(self, by, value):
        wd = self.app.wd
        # find all elements
        elements = wd.find_elements(by, value)
        # create a list of indexes of all active elements
        active_color = [index for index, element in enumerate(elements) if element.is_enabled()]
        # choose a random index from the list
        random_color = random.choice(active_color)
        # click on the element with the selected index
        elements[random_color].click()

    def return_color(self, by, value):
        wd = self.app.wd
        color = wd.find_element(by, value).value_of_css_property("background-color")
        # return the color that was chosen randomly
        # if you want to return color in hex format you can use -> return print(Color.from_string(color).hex)
        return color

    def check_charts_line_mountain_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.LINE_MOUNTAIN_COLOR_XPATH)

    def check_charts_up_candle_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.UP_CANDLE_COLOR_XPATH)

    def check_charts_up_candle_wick_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.UP_CANDLE_WICK_COLOR_XPATH)

    def check_charts_up_candle_outline_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.UP_CANDLE_OUTLINE_COLOR_XPATH)

    def check_charts_down_candle_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.DOWN_CANDLE_COLOR_XPATH)

    def check_charts_down_candle_wick_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.DOWN_CANDLE_WICK_COLOR_XPATH)

    def check_charts_down_candle_outline_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.DOWN_CANDLE_OUTLINE_COLOR_XPATH)

    def check_charts_mpd_ssl_line_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.MPD_SSL_LINE_COLOR_XPATH)

    def check_charts_bullish_formation_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.BULLISH_FORMATION_COLOR_XPATH)

    def check_charts_bearish_formation_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.BEARISH_FORMATION_COLOR_XPATH)

    def check_charts_text_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.TEXT_COLOR_XPATH)

    def check_charts_gradient_color1(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.GRADIENT_COLOR1_XPATH)

    def check_charts_gradient_color2(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.GRADIENT_COLOR2_XPATH)

    def check_charts_grid_style_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.GRID_STYLE_COLOR_XPATH)

    def click_watermark_switcher(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, GlobalSettingsConstants.WATERMARK_SWITCHER_XPATH)
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        if wd.find_elements(By.XPATH, GlobalSettingsConstants.SHOW_WATERMARK_LABEL_XPATH):
            return 'disabled'
        else:
            return 'enabled'

    def check__watermark_switcher(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, GlobalSettingsConstants.WATERMARK_SWITCHER_XPATH)
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        if wd.find_elements(By.XPATH, GlobalSettingsConstants.SHOW_WATERMARK_LABEL_XPATH):
            return 'disabled'
        else:
            return 'enabled'

    def return_field_value(self, by, value):
        wd = self.app.wd
        data_value = wd.find_element(by, value).get_attribute("data-selectvalue")
        return data_value

    def change_grid_style(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.GRID_STYLE_DROPDOWN_XPATH).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.GRID_STYLE_DROPDOWN_LIST_XPATH)

    def check_grid_style_type(self):
        return self.return_field_value(By.XPATH, GlobalSettingsConstants.GRID_STYLE_DROPDOWN_XPATH)

    def change_chart_font(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.CHART_FONT_XPATH).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.CHART_FONT_LIST_XPATH)

    def check_chart_font(self):
        return self.return_field_value(By.XPATH, GlobalSettingsConstants.CHART_FONT_XPATH)

    def change_chart_text_size(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.CHART_TEXT_SIZE_XPATH).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.CHART_TEXT_SIZE_LIST_XPATH)

    def check_chart_text_size(self):
        return self.return_field_value(By.XPATH, GlobalSettingsConstants.CHART_TEXT_SIZE_XPATH)

    def change_switcher_show_open_orders_state(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.SHOW_OPEN_ORDERS_SWITCHER_XPATH).click()

    def check_switcher_show_open_orders_state(self):
        return self.check_trading_switchers_state(By.XPATH, GlobalSettingsConstants.SHOW_OPEN_ORDERS_SWITCHER_XPATH)

    def change_switcher_show_pending_orders_state(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.SHOW_PENDING_ORDERS_SWITCHER_XPATH).click()

    def check_switcher_show_pending_orders_state(self):
        return self.check_trading_switchers_state(By.XPATH, GlobalSettingsConstants.SHOW_PENDING_ORDERS_SWITCHER_XPATH)

    def change_switcher_show_markers_state(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.SHOW_MAKERS_SWITCHER_XPATH).click()

    def check_switcher_show_markers_state(self):
        return self.check_trading_switchers_state(By.XPATH, GlobalSettingsConstants.SHOW_MAKERS_SWITCHER_XPATH)

    def change_switcher_one_click_trades_state(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.ONE_CLICK_TRADES_SWITCHER_XPATH).click()

    def check_switcher_one_click_trades_state(self):
        return self.check_trading_switchers_state(By.XPATH, GlobalSettingsConstants.ONE_CLICK_TRADES_SWITCHER_XPATH)

    def check_trading_switchers_state(self, by, value):
        wd = self.app.wd
        element = wd.find_element(by, value).get_attribute("style")
        if element == 'left: 18px; transition: left 0.2s ease 0s;':
            return 'enabled'
        else:
            return 'disabled'

    def change_trading_buy_marker_style_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.BUY_MARKER_STYLE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW1_XPATH)

    def change_trading_sell_marker_style_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.SELL_MARKER_STYLE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW2_XPATH)

    def change_trading_close_marker_style_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.CLOSE_MARKER_STYLE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW3_XPATH)

    def change_trading_market_buy_line_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.MARKET_BUY_LINE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW4_XPATH)

    def change_trading_market_sell_line_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.MARKET_SELL_LINE_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW5_XPATH)

    def change_trading_pending_orders_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.PENDING_ORDERS_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW6_XPATH)

    def change_trading_stop_loss_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.STOP_LOSS_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW7_XPATH)

    def change_trading_take_profit_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.TAKE_PROFIT_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW8_XPATH)

    def change_trading_price_alert_color(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.PRICE_ALERTS_COLOR_XPATH).click()
        self.random_color(By.XPATH, GlobalSettingsConstants.COLOR_WINDOW9_XPATH)

    def check_trading_buy_market_style_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.BUY_MARKER_STYLE_COLOR_XPATH)

    def check_trading_sell_market_style_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.SELL_MARKER_STYLE_COLOR_XPATH)

    def check_trading_close_market_style_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.CLOSE_MARKER_STYLE_COLOR_XPATH)

    def check_trading_market_buy_line_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.MARKET_BUY_LINE_COLOR_XPATH)

    def check_trading_market_sell_line_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.MARKET_SELL_LINE_COLOR_XPATH)

    def check_trading_pending_orders_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.PENDING_ORDERS_COLOR_XPATH)

    def check_trading_stop_loss_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.STOP_LOSS_COLOR_XPATH)

    def check_trading_take_profit_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.TAKE_PROFIT_COLOR_XPATH)

    def check_trading_price_alert_color(self):
        return self.return_color(By.XPATH, GlobalSettingsConstants.PRICE_ALERTS_COLOR_XPATH)

    def change_trading_buy_market_style_size(self):
        wd = self.app.wd
        wd.find_element(By.ID, GlobalSettingsConstants.BUY_MARKER_STYLE_SIZE_ID).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.BUY_MARKER_STYLE_SIZE_LIST_XPATH)

    def change_trading_sell_market_style_size(self):
        wd = self.app.wd
        wd.find_element(By.ID, GlobalSettingsConstants.SELL_MARKER_STYLE_SIZE_ID).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.SELL_MARKER_STYLE_SIZE_LIST_XPATH)

    def change_trading_close_market_style_size(self):
        wd = self.app.wd
        wd.find_element(By.ID, GlobalSettingsConstants.CLOSE_MARKER_STYLE_SIZE_ID).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.CLOSE_MARKER_STYLE_SIZE_LIST_XPATH)

    def change_trading_market_buy_line_line_view(self):
        wd = self.app.wd
        wd.find_element(By.ID, GlobalSettingsConstants.MARKET_BUY_LINE_LINE_VIEW_ID).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.MARKET_BUY_LINE_LINE_VIEW_LIST_XPATH)

    def change_trading_market_sell_line_line_view(self):
        wd = self.app.wd
        wd.find_element(By.ID, GlobalSettingsConstants.MARKET_SELL_LINE_LINE_VIEW_ID).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.MARKET_SELL_LINE_LINE_VIEW_LIST_XPATH)

    def change_trading_pending_orders_line_view(self):
        wd = self.app.wd
        wd.find_element(By.ID, GlobalSettingsConstants.PENDING_ORDERS_LINE_VIEW_ID).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.PENDING_ORDERS_LINE_VIEW_LIST_XPATH)

    def change_trading_stop_loss_line_view(self):
        wd = self.app.wd
        wd.find_element(By.ID, GlobalSettingsConstants.STOP_LOSS_LINE_VIEW_ID).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.STOP_LOSS_LINE_VIEW_LIST_XPATH)

    def change_trading_take_profit_line_view(self):
        wd = self.app.wd
        wd.find_element(By.ID, GlobalSettingsConstants.TAKE_PROFIT_LINE_VIEW_ID).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.TAKE_PROFIT_LINE_VIEW_LIST_XPATH)

    def change_trading_price_alert_line_view(self):
        wd = self.app.wd
        wd.find_element(By.ID, GlobalSettingsConstants.PRICE_ALERTS_LINE_VIEW_ID).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.PRICE_ALERTS_LINE_VIEW_LIST_XPATH)

    def return_fields_value_in_trading_tab(self, by, value):
        wd = self.app.wd
        element = wd.find_element(by, value).get_attribute("value")
        return element

    def check_trading_buy_market_style_size(self):
        return self.return_fields_value_in_trading_tab(By.ID, GlobalSettingsConstants.BUY_MARKER_STYLE_SIZE_ID)

    def check_trading_sell_market_style_size(self):
        return self.return_fields_value_in_trading_tab(By.ID, GlobalSettingsConstants.SELL_MARKER_STYLE_SIZE_ID)

    def check_trading_close_market_style_size(self):
        return self.return_fields_value_in_trading_tab(By.ID, GlobalSettingsConstants.CLOSE_MARKER_STYLE_SIZE_ID)

    def check_trading_market_buy_line_line_view(self):
        return self.return_fields_value_in_trading_tab(By.ID, GlobalSettingsConstants.MARKET_BUY_LINE_LINE_VIEW_ID)

    def check_trading_market_sell_line_line_view(self):
        return self.return_fields_value_in_trading_tab(By.ID, GlobalSettingsConstants.MARKET_SELL_LINE_LINE_VIEW_ID)

    def check_trading_pending_orders_line_view(self):
        return self.return_fields_value_in_trading_tab(By.ID, GlobalSettingsConstants.PENDING_ORDERS_LINE_VIEW_ID)

    def check_trading_stop_loss_line_view(self):
        return self.return_fields_value_in_trading_tab(By.ID, GlobalSettingsConstants.STOP_LOSS_LINE_VIEW_ID)

    def check_trading_take_profit_line_view(self):
        return self.return_fields_value_in_trading_tab(By.ID, GlobalSettingsConstants.TAKE_PROFIT_LINE_VIEW_ID)

    def check_trading_price_alert_line_view(self):
        return self.return_fields_value_in_trading_tab(By.ID, GlobalSettingsConstants.PRICE_ALERTS_LINE_VIEW_ID)

    def change_scripting_font_size(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.SCRIPTING_FONT_SIZE_XPATH).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.FONT_SIZE_LIST_XPATH)
        selected_size = wd.find_element(By.XPATH, GlobalSettingsConstants.SCRIPTING_FONT_SIZE_XPATH)
        # return size and delete all symbols except numbers
        return selected_size.text

    def check_font_size_in_scripting_tab(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, ScriptingConstants.SCRIPTING_TAB2_XPATH)
        if element.is_displayed():
            pass
        else:
            self.app.common.open_trading_panel()
        element.click()
        size = wd.find_element(By.CSS_SELECTOR, ScriptingConstants.FIRST_LINE_IN_SCRIPT_CODE_CSS_SELECTOR). \
            value_of_css_property('font-size')
        return re.sub("[^0-9]", "", size)

    def change_run_on_state(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.RUN_ON_XPATH).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.RUN_ON_LIST_XPATH)
        return self.return_field_text(By.XPATH, GlobalSettingsConstants.RUN_ON_XPATH)

    def return_selected_run_on(self):
        return self.return_field_text(By.XPATH, GlobalSettingsConstants.RUN_ON_XPATH)

    def return_field_text(self, by, value):
        wd = self.app.wd
        select_element = wd.find_element(by, value)
        return select_element.text

    def check_automatic_logs_download_switcher_state(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.AUTOMATIC_LOGS_DOWNLOAD_XPATH).click()
        return self.check_trading_switchers_state(By.XPATH, GlobalSettingsConstants.AUTOMATIC_LOGS_DOWNLOAD_XPATH)

    def check_switcher_automatic_logs_download_state(self):
        return self.check_trading_switchers_state(By.XPATH, GlobalSettingsConstants.AUTOMATIC_LOGS_DOWNLOAD_XPATH)

    def change_scripting_theme(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, GlobalSettingsConstants.SCRIPTING_THEME_XPATH).click()
        self.app.common.click_random_element(By.XPATH, GlobalSettingsConstants.SCRIPTING_THEME_LIST_XPATH)
        return self.return_field_text(By.XPATH, GlobalSettingsConstants.SCRIPTING_THEME_XPATH)

    def check_scripting_theme(self):
        wd = self.app.wd
        # open scripting tab
        element = wd.find_element(By.XPATH, ScriptingConstants.SCRIPTING_TAB2_XPATH)
        if element.is_displayed():
            pass
        else:
            self.app.common.open_trading_panel()
        element.click()
        # return theme color
        self.app.wait_element_located(By.CSS_SELECTOR, ScriptingConstants.FIRST_LINE_IN_SCRIPT_CODE_CSS_SELECTOR)
        returned_theme = self.return_color(By.CSS_SELECTOR, ScriptingConstants.FIRST_LINE_IN_SCRIPT_CODE_CSS_SELECTOR)
        theme_color = Color.from_string(returned_theme).hex
        if theme_color == '#e8f2ff':
            return 'Default'
        else:
            if theme_color == '#ffffff':
                self.open_scripting_global_setting()
                return self.return_field_text(By.XPATH, GlobalSettingsConstants.SCRIPTING_THEME_XPATH)
            else:
                if theme_color == '#373831':
                    return 'Dark Gray'
