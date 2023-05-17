#!/usr/bin/env python3
"""
Defines the Server class which pulls paginates a database of popular baby
names.
"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the appropriate page of the dataset.
        """
        assert isinstance(page, int) and isinstance(page_size, int),\
            'Arguments must be positive integers'
        assert page > 0 and page_size > 0,\
            'Arguments must be positive integers'

        self.dataset()
        start, end = index_range(page, page_size)

        num_pages = math.ceil((len(self.__dataset) / page_size))
        next_page = page + 1 if page < num_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': self.__dataset[start:end] if start < len(self.__dataset)
            and end <= len(self.__dataset) else [],
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': num_pages
        }
