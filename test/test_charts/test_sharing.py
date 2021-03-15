import time


def test_share_charts(app):
    app.open_charts_page()
    app.sharing.share_ideas_button()
    app.sharing.share_charts_button()
    app.sharing.make_snapshot_chart()
    current_datetime = app.sharing.get_current_datetime()
    app.sharing.write_idea_name(idea_name=current_datetime)
    app.sharing.write_description(description_text='test for sharing charts as idea')
    app.sharing.publish_idea()
    shared_check = app.sharing.check_shared_ideas()
    assert current_datetime == shared_check


def test_share_workspace(app):
    app.open_charts_page()
    app.sharing.share_ideas_button()
    app.sharing.share_workspace_button()
    app.sharing.make_snapshot_workspace()
    current_datetime = app.sharing.get_current_datetime()
    app.sharing.write_idea_name(idea_name=current_datetime)
    app.sharing.write_description(description_text='test for sharing charts as idea')
    app.sharing.publish_idea()
    shared_check = app.sharing.check_shared_ideas()
    assert current_datetime == shared_check


def test_import_workspase_as_idea(app):
    app.open_charts_page()
    app.sharing.share_ideas_button()
    app.sharing.browse_ideas()
    app.sharing.import_random_workspace_button()


def test_import_chart_as_idea(app):
    app.open_charts_page()
    app.sharing.share_ideas_button()
    app.sharing.browse_ideas()
    app.sharing.import_random_chart_button()