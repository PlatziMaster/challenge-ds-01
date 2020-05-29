"""Solution by pablotrinidad."""

from typing import Tuple


class Solution:
    """Abstract the computations required for analysis."""

    def analyze_books(self, books_dataset: str) -> Tuple[int, int, int]:
        """Returns the n-th fibonacci number."""
        with open(books_dataset, "r") as bds:
            for line in bds.readlines():
                print(line)
        return (1, 2, 3)
