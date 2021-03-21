

def test_tab_360pro_button_not_login(app):
    app.session.log_out()
    app.plans.open_plans_360pro()
    app.plans.click_access_button()
    cost1 = app.plans.check_cost()
    assert '199.95/' == cost1
    app.plans.fill_fields()
    cost2 = app.plans.checkout_plan_cost()
    cost3 = app.plans.checkout_total_price()
    assert '$' + cost1 == "$" + cost2 + '/' == cost3 + '/'


def test_tab_360pro_button_login(app):
    app.session.log_in(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
    app.plans.open_plans_360pro()
    app.plans.click_access_button()
    cost1 = app.plans.checkout_plan_cost()
    cost2 = app.plans.checkout_total_price()
    assert "$" + cost1 == cost2


def test_button_only_differencec(app):
    app.open_home_page()
    app.plans.open_plans_all()
    old_list = app.plans.get_row_list()
    app.plans.put_only_differences()
    new_list = app.plans.get_row_list()
    assert old_list + 20 == new_list
