from nv_statutes.lib import title_count, titles


def test_finds_the_correct_number_of_titles():
    index_html = open("../nrs.html").read()
    assert title_count(index_html) == 59


def test_titles_gets_the_first_titles_name():
    index_html = open("../nrs.html").read()
    assert titles(index_html)[0].name == "STATE JUDICIAL DEPARTMENT"
