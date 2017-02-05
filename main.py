from bs4 import BeautifulSoup
from toolz.recipes import partitionby
import ipdb


def main():
    html_file = open("../nrs.html").read()
    soup = BeautifulSoup(html_file, 'html.parser')
    ipdb.set_trace()

    shallow_tree = tuple(partitionby(isHeader, [0, 10, 20, 30, 1, 99, 99, 99]))
    print(shallow_tree)


def isHeader(row):
    row < 10


if __name__ == "__main__":
    main()
