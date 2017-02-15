import nv_statutes.lib


def test_finds_the_correct_number_of_titles():
    index_html = open("../nrs.html").read()
    titles = nv_statutes.lib.titles(index_html)
    assert len(titles) == 59


def test_titles_gets_the_first_titles_name():
    index_html = open("../nrs.html").read()
    titles = nv_statutes.lib.titles(index_html)
    assert titles[0].name == "STATE JUDICIAL DEPARTMENT"
