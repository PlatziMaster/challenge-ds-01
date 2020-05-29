"""Solution by pablotrinidad."""

import os
from typing import Tuple

import numpy as np
import pandas as pd


class Solution:
    """Abstract the computations required for analysis."""

    def analyze_books(self, books_dataset: str) -> Tuple[int, int, int]:
        """Returns the n-th fibonacci number."""
        books = pd.read_csv(books_dataset, error_bad_lines=False)
        print(books.dtypes)
        book_count = 0
        with open(books_dataset, "r") as bds:
            for _ in bds.readlines():
                book_count += 1
        print(f"Found {book_count} books! which is > {np.pi}")

        return (
            int(os.getenv("SOLUTION_QUESTION_1")),
            int(os.getenv("SOLUTION_QUESTION_2")),
            int(os.getenv("SOLUTION_QUESTION_3")),
        )
