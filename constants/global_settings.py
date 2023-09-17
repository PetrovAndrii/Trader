class GlobalSettingsConstants:
    GLOBAL_SETTINGS_BUTTON_CSS_SELECTOR = 'div.v-dropdown.ProfileMenu__dropdown > ul:nth-child(5) > li:nth-child(3) > a'
    SAVE_BUTTON_ID = 'scxThemeDialog_btn_save'
    CLOSE_BUTTON_ID = 'scxThemeDialog_btn_close'
    APP_FONT_SIZE_XPATH = '//*[@data-id="scxThemeDialog_input_appFontSize"]'
    FONT_SIZE_LIST_XPATH = '//*[@class="btn-group bootstrap-select scxDropdown open"]/div/ul/li'
    APP_FONT_SIZE_TEXT_ID = 'scxThemeDialog_label_appFontSize'
    LIGHT_THEME_OPTION_XPATH = '//*[@data-value="scxThemeLight"]'
    DARK_THEME_OPTION_XPATH = '//*[@data-value="scxThemeDark"]'
    MODAL_SETTINGS_WINDOW_CSS_SELECTOR = '.modal-content.modal-content--with-tabs.ui-draggable'
    GENERAL_TAB_ID = 'generalTab'
    CHART_TAB_ID = 'chartTab'
    TRADING_TAB_ID = 'tradingTab'
    SCRIPTING_TAB_ID = 'scriptingTab'
    LINE_MOUNTAIN_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[1]/td[2]/div/div[1]/div'
    UP_CANDLE_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[2]/td[2]/div/div[1]/div'
    UP_CANDLE_WICK_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[3]/td[2]/div/div[1]/div'
    UP_CANDLE_OUTLINE_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[4]/td[2]/div/div[1]/div'
    DOWN_CANDLE_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[5]/td[2]/div/div[1]/div'
    DOWN_CANDLE_WICK_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[6]/td[2]/div/div[1]/div'
    DOWN_CANDLE_OUTLINE_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[7]/td[2]/div/div[1]/div'
    MPD_SSL_LINE_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[8]/td[2]/div/div[1]/div'
    BULLISH_FORMATION_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[9]/td[2]/div/div[1]/div'
    BEARISH_FORMATION_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[10]/td[2]/div/div[1]/div'
    TEXT_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[2]/tbody/tr[3]/td[2]/div/div[1]/div'
    GRADIENT_COLOR1_XPATH = '//*[@id="tab_chartSettings"]/table[2]/tbody/tr[4]/td[2]/div/div[1]/div'
    GRADIENT_COLOR2_XPATH = '//*[@id="tab_chartSettings"]/table[2]/tbody/tr[5]/td[2]/div/div[1]/div'
    GRID_STYLE_COLOR_XPATH = '//*[@id="tab_chartSettings"]/table[2]/tbody/tr[6]/td[3]/div/div[1]/div'
    COLOR_WINDOW1_XPATH = "//*[@class='scxSpectrum sp-container sp-light sp-input-disabled sp-palette-only']" \
                          "/div[1]/div[1]/div[1]/span"
    COLOR_WINDOW2_XPATH = "//*[@class='scxSpectrum sp-container sp-light sp-input-disabled sp-palette-only']" \
                          "/div[1]/div[1]/div[2]/span"
    COLOR_WINDOW3_XPATH = "//*[@class='scxSpectrum sp-container sp-light sp-input-disabled sp-palette-only']" \
                          "/div[1]/div[1]/div[3]/span"
    COLOR_WINDOW4_XPATH = "//*[@class='scxSpectrum sp-container sp-light sp-input-disabled sp-palette-only']" \
                          "/div[1]/div[1]/div[4]/span"
    COLOR_WINDOW5_XPATH = "//*[@class='scxSpectrum sp-container sp-light sp-input-disabled sp-palette-only']" \
                          "/div[1]/div[1]/div[5]/span"
    COLOR_WINDOW6_XPATH = "//*[@class='scxSpectrum sp-container sp-light sp-input-disabled sp-palette-only']" \
                          "/div[1]/div[1]/div[6]/span"
    COLOR_WINDOW7_XPATH = "//*[@class='scxSpectrum sp-container sp-light sp-input-disabled sp-palette-only']" \
                          "/div[1]/div[1]/div[7]/span"
    COLOR_WINDOW8_XPATH = "//*[@class='scxSpectrum sp-container sp-light sp-input-disabled sp-palette-only']" \
                          "/div[1]/div[1]/div[8]/span"
    COLOR_WINDOW9_XPATH = "//*[@class='scxSpectrum sp-container sp-light sp-input-disabled sp-palette-only']" \
                          "/div[1]/div[1]/div[9]/span"
    WATERMARK_SWITCHER_XPATH = '//*[@id="tab_chartSettings"]/table[1]/tbody/tr[11]/td[2]/span/small'
    SHOW_WATERMARK_LABEL_XPATH = "//*[@id='scxThemeDialog_label_showWatermark' and @class='disabled']"
    GRID_STYLE_DROPDOWN_XPATH = "//*[@data-id='scxThemeDialog_input_gridStyle']"
    GRID_STYLE_DROPDOWN_LIST_XPATH = '//*[@class="btn-group bootstrap-select scxGridStyleSelector ' \
                                     'scxLineStyleSelector open"]/div/ul/li '
    CHART_FONT_XPATH = '//*[@id="tab_chartSettings"]/table[2]/tbody/tr[1]/td[2]/div/button'
    CHART_FONT_LIST_XPATH = '//*[@class="btn-group bootstrap-select scxDropdown scxFontDropdown themeDialogElement ' \
                            'open"]/div/ul/li '
    CHART_TEXT_SIZE_XPATH = "//*[@data-id='scxThemeDialog_input_textSize']"
    CHART_TEXT_SIZE_LIST_XPATH = '//*[@class="btn-group bootstrap-select scxDropdown themeDialogElement open"]' \
                                 '/div/ul/li '
    SHOW_OPEN_ORDERS_SWITCHER_XPATH = '//*[@id="tab_tradingSettings"]/table[1]/tbody/tr[1]/td[2]/span/small'
    SHOW_PENDING_ORDERS_SWITCHER_XPATH = '//*[@id="tab_tradingSettings"]/table[1]/tbody/tr[2]/td[2]/span/small'
    SHOW_MAKERS_SWITCHER_XPATH = '//*[@id="tab_tradingSettings"]/table[1]/tbody/tr[3]/td[2]/span/small'
    ONE_CLICK_TRADES_SWITCHER_XPATH = '//*[@class="oneClickTradesContainer"]/table/tbody/tr/td[2]/span/small'
    BUY_MARKER_STYLE_COLOR_XPATH = '//*[@id="tab_tradingSettings"]/table[1]/tbody/tr[4]/td[2]/div/div[1]/div'
    SELL_MARKER_STYLE_COLOR_XPATH = '//*[@id="tab_tradingSettings"]/table[1]/tbody/tr[5]/td[2]/div/div[1]/div'
    CLOSE_MARKER_STYLE_COLOR_XPATH = '//*[@id="tab_tradingSettings"]/table[1]/tbody/tr[6]/td[2]/div/div[1]/div'
    MARKET_BUY_LINE_COLOR_XPATH = '//*[@id="tab_tradingSettings"]/table[2]/tbody/tr[1]/td[2]/div/div[1]/div'
    MARKET_SELL_LINE_COLOR_XPATH = '//*[@id="tab_tradingSettings"]/table[2]/tbody/tr[2]/td[2]/div/div[1]/div'
    PENDING_ORDERS_COLOR_XPATH = '//*[@id="tab_tradingSettings"]/table[2]/tbody/tr[3]/td[2]/div/div[1]/div'
    STOP_LOSS_COLOR_XPATH = '//*[@id="tab_tradingSettings"]/table[2]/tbody/tr[4]/td[2]/div/div[1]/div'
    TAKE_PROFIT_COLOR_XPATH = '//*[@id="tab_tradingSettings"]/table[2]/tbody/tr[5]/td[2]/div/div[1]/div'
    PRICE_ALERTS_COLOR_XPATH = '//*[@id="tab_tradingSettings"]/table[2]/tbody/tr[6]/td[2]/div/div[1]/div'
    BUY_MARKER_STYLE_SIZE_ID = 'scxThemeDialog_trading_buy_marker_size'
    SELL_MARKER_STYLE_SIZE_ID = 'scxThemeDialog_trading_sell_marker_size'
    CLOSE_MARKER_STYLE_SIZE_ID = 'scxThemeDialog_trading_close_marker_size'
    MARKET_BUY_LINE_LINE_VIEW_ID = 'scxThemeDialog_trading_lines_buy'
    MARKET_SELL_LINE_LINE_VIEW_ID = 'scxThemeDialog_trading_lines_sell'
    PENDING_ORDERS_LINE_VIEW_ID = 'scxThemeDialog_trading_lines_pending'
    STOP_LOSS_LINE_VIEW_ID = 'scxThemeDialog_trading_lines_stopLoss'
    TAKE_PROFIT_LINE_VIEW_ID = 'scxThemeDialog_trading_lines_takeProfit'
    PRICE_ALERTS_LINE_VIEW_ID = 'scxThemeDialog_trading_lines_priceAlerts'
    BUY_MARKER_STYLE_SIZE_LIST_XPATH = '//*[@id="scxThemeDialog_trading_buy_marker_size"]/option'
    SELL_MARKER_STYLE_SIZE_LIST_XPATH = '//*[@id="scxThemeDialog_trading_sell_marker_size"]/option'
    CLOSE_MARKER_STYLE_SIZE_LIST_XPATH = '//*[@id="scxThemeDialog_trading_close_marker_size"]/option'
    MARKET_BUY_LINE_LINE_VIEW_LIST_XPATH = '//*[@id="scxThemeDialog_trading_lines_buy"]/option'
    MARKET_SELL_LINE_LINE_VIEW_LIST_XPATH = '//*[@id="scxThemeDialog_trading_lines_sell"]/option'
    PENDING_ORDERS_LINE_VIEW_LIST_XPATH = '//*[@id="scxThemeDialog_trading_lines_pending"]/option'
    STOP_LOSS_LINE_VIEW_LIST_XPATH = '//*[@id="scxThemeDialog_trading_lines_stopLoss"]/option'
    TAKE_PROFIT_LINE_VIEW_LIST_XPATH = '//*[@id="scxThemeDialog_trading_lines_takeProfit"]/option'
    PRICE_ALERTS_LINE_VIEW_LIST_XPATH = '//*[@id="scxThemeDialog_trading_lines_priceAlerts"]/option'
    SCRIPTING_FONT_SIZE_XPATH = '//*[@data-id="scxThemeDialog_input_codeEditorFontSize"]/span'
    RUN_ON_XPATH = '//*[@id="tab_scriptingSetting"]/table[2]/tbody/tr[1]/td[2]/div/button/span[1]'
    RUN_ON_LIST_XPATH = '//*[@class="btn-group bootstrap-select scriptingDropdown scxDropdown open"]/div/ul/li'
    AUTOMATIC_LOGS_DOWNLOAD_XPATH = '//*[@id="autoLogsDownload"]/td[2]/span/small'
    SCRIPTING_THEME_XPATH = '//*[@data-id="scxThemeDialog_input_codeEditorTheme"]/span'
    SCRIPTING_THEME_LIST_XPATH = '//*[@class="btn-group bootstrap-select scriptingDropdown scxDropdown open"]/div/ul/li'
