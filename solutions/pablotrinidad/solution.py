"""Solution by pablotrinidad."""

from typing import Tuple


class Solution:
    """Abstract the computations required for analysis."""

    def analyze_books(self, books_dataset: str) -> Tuple[int, int, int]:
        """Returns the n-th fibonacci number."""
        books_count = 0
        with open(books_dataset, "r") as bds:
            for _ in bds.readlines():
                books_count += 1
        return (1, 2, books_count)
