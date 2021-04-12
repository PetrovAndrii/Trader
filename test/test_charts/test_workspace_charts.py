

def test_open_new_workspace(app):
    app.open_charts_page()
    old_list = app.workspace_chart.get_workspace_list()
    app.workspace_chart.close_workspace_list()
    app.workspace_chart.button_add_workspace_chart()
    app.workspace_chart.add_new_workspace()
    name = app.common.random_symbol('Work', 5) + app.common.random_symbol('Space', 5)
    app.workspace_chart.enter_workspace_name(workspace_name=name)
    app.workspace_chart.choose_random_forex_symbol_workspace()
    app.workspace_chart.add_new_ideas_button()
    new_list = app.workspace_chart.get_workspace_list()
    assert old_list + 1 == new_list


def test_open_new_chart(app):
    app.open_charts_page()
    old_list = app.workspace_chart.get_charts_list()
    app.workspace_chart.button_add_workspace_chart()
    app.workspace_chart.add_new_chart()
    app.workspace_chart.choose_random_forex_symbol_chart()
    app.workspace_chart.choose_random_bars()
    app.workspace_chart.add_new_ideas_button()
    new_list = app.workspace_chart.get_charts_list()
    assert old_list + 1 == new_list


def test_open_random_private_workspace(app):
    app.open_charts_page()
    app.workspace_chart.button_add_workspace_chart()
    app.workspace_chart.manage_workspaces()
    name = app.workspace_chart.open_random_private_workspaces()
    check_name = app.workspace_chart.return_imported_name()
    assert name == check_name


def test_private_workspace_import_button(app):
    app.open_charts_page()
    old_list = app.workspace_chart.get_workspace_list()
    app.workspace_chart.close_workspace_list()
    app.workspace_chart.button_add_workspace_chart()
    app.workspace_chart.manage_workspaces()
    app.workspace_chart.click_random_checkbox_in_manage_workspaces()
    app.workspace_chart.manage_workspaces_click_import_button()
    new_list = app.workspace_chart.get_workspace_list()
    assert old_list + 1 == new_list


def test_open_random_premium_workspace(app):
    app.open_charts_page()
    app.workspace_chart.button_add_workspace_chart()
    app.workspace_chart.manage_workspaces()
    app.workspace_chart.open_tab_premium_workspaces()
    name = app.workspace_chart.open_random_premium_workspaces()
    check_name = app.workspace_chart.return_imported_name()
    assert name == check_name


def test_premium_workspace_import_button(app):
    app.open_charts_page()
    old_list = app.workspace_chart.get_workspace_list()
    app.workspace_chart.close_workspace_list()
    app.workspace_chart.button_add_workspace_chart()
    app.workspace_chart.manage_workspaces()
    app.workspace_chart.open_tab_premium_workspaces()
    app.workspace_chart.click_random_checkbox_in_premium_manage_workspaces()
    app.workspace_chart.manage_workspaces_click_import_button()
    new_list = app.workspace_chart.get_workspace_list()
    assert old_list + 1 == new_list
