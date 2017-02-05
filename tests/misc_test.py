from nv_statutes.lib import title_count


def test_finds_the_correct_number_of_titles():
    index_html = open("../nrs.html").read()
    assert title_count(index_html) == 59
