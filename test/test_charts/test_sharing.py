

# share charts
def test_share_charts(app):
    app.open_charts_page()
    app.sharing.share_ideas_button()
    app.sharing.share_charts_button()
    app.sharing.make_snapshot_chart()
    current_datetime = app.common.get_current_date_time()
    app.sharing.write_idea_name(idea_name=current_datetime)
    app.sharing.write_description(description_text='test for sharing charts as idea')
    app.sharing.publish_idea()
    shared_check = app.sharing.check_shared_ideas(name_shared_ideas=current_datetime)
    assert current_datetime == shared_check


# share workspace
def test_share_workspace(app):
    app.open_charts_page()
    app.sharing.share_ideas_button()
    app.sharing.share_workspace_button()
    app.sharing.make_snapshot_workspace()
    current_datetime = app.common.get_current_date_time()
    app.sharing.write_idea_name(idea_name=current_datetime)
    app.sharing.write_description(description_text='test for sharing charts as idea')
    app.sharing.publish_idea()
    shared_check = app.sharing.check_shared_ideas(name_shared_ideas=current_datetime)
    assert current_datetime == shared_check


def test_share_active_workspace(app):
    app.open_charts_page()
    app.sharing.open_workspace_list()
    app.sharing.open_setting_active_workspaces()
    app.sharing.click_share_button_on_ws_settings()
    app.sharing.make_snapshot_workspace()
    current_datetime = app.common.get_current_date_time()
    app.sharing.write_idea_name(idea_name=current_datetime)
    app.sharing.write_description(description_text='test for sharing charts as idea')
    app.sharing.publish_idea()
    shared_check = app.sharing.check_shared_ideas(name_shared_ideas=current_datetime)
    assert current_datetime == shared_check


def test_share_private_workspace(app):
    app.open_charts_page()
    app.workspace_chart.button_add_workspace_chart()
    app.workspace_chart.manage_workspaces()
    app.workspace_chart.manage_workspaces_option()
    app.workspace_chart.share_private_workspace()
    app.sharing.make_snapshot_workspace()
    current_datetime = app.common.get_current_date_time()
    app.sharing.write_idea_name(idea_name=current_datetime)
    app.sharing.write_description(description_text='test for sharing charts as idea')
    app.sharing.publish_idea()
    shared_check = app.sharing.check_shared_ideas(name_shared_ideas=current_datetime)
    assert current_datetime == shared_check


# share scripts - CHECK THAT THE WORKSPACE IS NOT WITH PREMIUM CONTENT!
def test_share_scripts(app):
    app.open_charts_page()
    app.sharing.open_scripting_tab()
    app.sharing.open_user_smart_script()
    app.sharing.smart_script_share_button()
    app.sharing.make_snapshot_scripts()
    current_datetime = app.common.get_current_date_time()
    app.sharing.write_idea_name(idea_name=current_datetime)
    app.sharing.write_description(description_text='test for sharing charts as idea')
    app.sharing.publish_idea()
    shared_check = app.sharing.check_shared_ideas(name_shared_ideas=current_datetime)
    assert current_datetime == shared_check


# import as idea
def test_import_workspace_as_idea(app):
    app.open_charts_page()
    app.sharing.share_ideas_button()
    app.sharing.browse_ideas()
    name1 = app.sharing.import_random_workspace_button()
    name2 = app.sharing.return_imported_name()
    assert name1 == name2


def test_import_chart_as_idea(app):
    app.open_charts_page()
    app.sharing.share_ideas_button()
    app.sharing.browse_ideas()
    name1 = app.sharing.import_random_chart_button()
    name2 = app.sharing.return_imported_name()
    assert name1 == name2


# IMPORTANT! IT IS NECESSARY TO CHECK that you don't have any imported scripts (if you have - delete)
# import scripts
def test_import_scripts(app):
    app.open_charts_page()
    app.sharing.share_ideas_button()
    app.sharing.browse_scripts()
    script_name_to_import = app.sharing.import_random_scripts_button()
    imported_script_name = app.sharing.return_imported_script_name()
    assert script_name_to_import == imported_script_name


# share idea to social network
def test_share_to_social_footer_fb(app):
    app.open_charts_page()
    app.sharing.open_manage_shared_ideas_scripts()
    app.sharing.random_view_on_social_hub()
    app.sharing.button_share_into_social_on_footer()


# remove sharing ideas
def test_remove_sharing_ideas(app):
    app.open_charts_page()
    app.sharing.open_manage_shared_ideas_scripts()
    old_list = app.sharing.get_shared_ideas_scripts_list()
    app.sharing.remove_random_sharing_ideas()
    new_list = app.sharing.get_shared_ideas_scripts_list()
    assert len(old_list) - 1 == len(new_list)
