import pytest

import nv_statutes.lib


@pytest.fixture(scope="module")
def titles():
    index_html = open("../nrs.html").read()
    return nv_statutes.lib.titles(index_html)


def test_finds_the_correct_number_of_titles(titles):
    assert len(titles) == 59


def test_titles_gets_the_first_titles_name(titles):
    assert titles[0].name == "STATE JUDICIAL DEPARTMENT"
