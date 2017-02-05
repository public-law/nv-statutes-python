import bs4
from bs4 import BeautifulSoup
from toolz.recipes import partitionby


def title_count(html_index: str) -> int:
    soup        = BeautifulSoup(html_index, 'html.parser')
    tables      = soup.find_all('table')
    main_table  = tables[1]
    rows        = main_table.find_all('tr')
    header_rows = list(filter(is_header_row, rows))
    return len(header_rows)


def is_header_row(row: bs4.element.Tag) -> bool:
    columns = row.find_all('td')
    return len(columns) == 1
