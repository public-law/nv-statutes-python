from collections import namedtuple
from typing import Iterable

import bs4
from bs4 import BeautifulSoup
from toolz.itertoolz import partition
from toolz.recipes import partitionby

Title   = namedtuple('Title', ['name', 'number', 'chapters'])
Chapter = namedtuple('Chapter', ['name', 'number', 'url'])


def title_count(html_index: str) -> int:
    rows        = contentRows(html_index)
    header_rows = list(filter(is_header_row, rows))
    return len(header_rows)


def titles(html_index: str) -> Iterable[Title]:
    tuples = rowTuples(contentRows(html_index))
    return list(map(newTitleFromTuple, tuples))


def newTitleFromTuple(aTuple) -> Title:
    titleRow = aTuple[0][0]
    name   = BeautifulSoup.getText(titleRow.find('b')).split('—')[1].strip()
    number = int(BeautifulSoup.getText(titleRow.find('b')).split('—')[0].strip().split()[1])
    return Title(name=name, number=number, chapters=[])


def contentRows(html_index: str):
    soup  = BeautifulSoup(html_index, 'html.parser')
    table = soup.find_all('table')[1]
    return table.find_all('tr')


def rowTuples(rows):
    result = list(partitionby(is_header_row, rows))
    return partition(2, result[1:])  # Skip Chapter 0


def is_header_row(row: bs4.element.Tag) -> bool:
    columns = row.find_all('td')
    return len(columns) == 1
