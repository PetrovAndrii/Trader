# chapter - chap
# video - v


def test_chap1_v1(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter1_video1()
    app.tutorial.chapter1_video1_1()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap1_v2(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter1_video2()
    app.tutorial.chapter1_video2_2()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap1_v3(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter1_video3()
    app.tutorial.chapter1_video3_3()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap1_v4(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter1_video4()
    app.tutorial.chapter1_video4_4()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 == name_2


def test_chap2_v1(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter2_video1()
    app.tutorial.chapter2_video1_1()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap2_v2(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter2_video2()
    app.tutorial.chapter2_video2_2()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap2_v3(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter2_video3()
    app.tutorial.chapter2_video3_3()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap2_v4(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter2_video4()
    app.tutorial.chapter2_video4_4()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap2_v5(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter2_video5()
    app.tutorial.chapter2_video5_5()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap2_v6(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter2_video6()
    app.tutorial.chapter2_video6_6()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap2_v7(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter2_video7()
    app.tutorial.chapter2_video7_7()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap3_v1(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter3_video1()
    app.tutorial.chapter3_video1_1()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap3_v2(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter3_video2()
    app.tutorial.chapter3_video2_2()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap3_v3(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter3_video3()
    app.tutorial.chapter3_video3_3()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap3_v4(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter3_video4()
    app.tutorial.chapter3_video4_4()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap4_v1(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter4_video1()
    app.tutorial.chapter4_video1_1()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


# "How Do I Use a Trendline Alert? | SmartTrader" but in page with video "How Do I Use a Trendline Alert | SmartTrader"
def test_chap4_v2(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter4_video2()
    app.tutorial.chapter4_video2_2()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap4_v3(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter4_video3()
    app.tutorial.chapter4_video3_3()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap4_v4(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter4_video4()
    app.tutorial.chapter4_video4_4()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2


def test_chap4_v5(app):
    app.open_home_page()
    app.tutorial.open_tutorial()
    name_1 = app.tutorial.chapter4_video5()
    app.tutorial.chapter4_video5_5()
    app.tutorial.check_fideo_form()
    name_2 = app.tutorial.copy_name_tutorial()
    assert name_1 + ' | SmartTrader' == name_2
