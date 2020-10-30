#!/usr/bin/env python3
''' Pagination '''
import csv
import math
from typing import Dict, List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' def get page '''
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        i = index_range(page, page_size)
        if i[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[i[0]:i[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        ''' Def get hyper '''
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        page = page
        total_pages = math.ceil(len(dataset) / page_size)
        page_size = len(data)
        next_page = None
        prev_page = None
        if page > 1:
            prev_page = page - 1
        if page < total_pages:
            next_page = page + 1

        P = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return p


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' Def index range '''
    index = page * page_size - page_size
    index_1 = index + page_size
    return (index, index_1)
