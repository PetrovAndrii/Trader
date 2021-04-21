

def test_add_general_indicators_on_chart(app):
    app.open_charts_page()
    old_list = app.indicators.get_indicators_list()
    app.indicators.click_add_indicators_button()
    app.indicators.click_general_indicators()
    app.indicators.add_random_general_indicator()
    new_list = app.indicators.get_indicators_list()
    assert old_list + 1 == new_list


def test_add_premium_indicators_on_chart(app):
    app.open_charts_page()
    old_list = app.indicators.get_indicators_list()
    app.indicators.click_add_indicators_button()
    app.indicators.click_premium_indicators()
    app.indicators.add_random_general_indicator()
    new_list = app.indicators.get_indicators_list()
    assert old_list + 1 == new_list


def test_add_my_indicators_on_chart(app):
    app.open_charts_page()
    old_list = app.indicators.get_indicators_list()
    app.indicators.click_add_indicators_button()
    app.indicators.click_my_indicators()
    app.indicators.add_random_general_indicator()
    new_list = app.indicators.get_indicators_list()
    assert old_list + 1 == new_list


def test_add_new_indicator_button_in_my_indicators(app):
    app.open_charts_page()
    app.indicators.click_add_indicators_button()
    app.indicators.click_my_indicators()
    app.indicators.click_button_add_indicator_on_my_indicators()
    name = app.indicators.choose_indicator_to_select_on_my_indicators()
    app.indicators.confirm_selected_indicator()
    current_datetime = app.common.get_current_date_time()
    app.indicators.fill_custom_indicator_name(indicator_name=current_datetime)
    app.indicators.fill_custom_indicator_description(description=name)
    app.indicators.button_save_as_custom_indicator()
    name_check = app.indicators.check_added_name()
    assert current_datetime == name_check
