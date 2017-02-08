import bs4
from bs4 import BeautifulSoup


# from toolz.recipes import partitionby


def title_count(html_index: str) -> int:
    soup        = BeautifulSoup(html_index, 'html.parser')
    table       = soup.find_all('table')[1]
    rows        = table.find_all('tr')
    header_rows = list(filter(is_header_row, rows))
    return len(header_rows)


def titles(html_index: str):
    soup        = BeautifulSoup(html_index, 'html.parser')
    table       = soup.find_all('table')[1]
    rows        = table.find_all('tr')
    return []


def is_header_row(row: bs4.element.Tag) -> bool:
    columns = row.find_all('td')
    return len(columns) == 1
