from collections import namedtuple

import bs4
from bs4 import BeautifulSoup
from toolz.recipes import partitionby

Title   = namedtuple('Title', ['name', 'number', 'chapters'])
Chapter = namedtuple('Chapter', ['name', 'number', 'url'])


def title_count(html_index: str) -> int:
    rows        = contentRows(html_index)
    header_rows = list(filter(is_header_row, rows))
    return len(header_rows)


def titles(html_index: str):
    tuples      = rowTuples(contentRows(html_index))
    return []


def contentRows(html_index: str):
    soup  = BeautifulSoup(html_index, 'html.parser')
    table = soup.find_all('table')[1]
    return table.find_all('tr')


def rowTuples(rows):
    list(partitionby(is_header_row, rows))


def is_header_row(row: bs4.element.Tag) -> bool:
    columns = row.find_all('td')
    return len(columns) == 1
