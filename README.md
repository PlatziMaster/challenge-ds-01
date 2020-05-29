# Data manipulation and basic statistics

Given a books dataset, help us answer some basic questions.
1. Which book got more reviews?
2. Which book was better rated?
3. **X** Within the most rated books, which one got the best rating?

## How to submit your solution

* Add a directory named after your GitHub username under directory `solutions`, f.e: `solutions/pablotrinidad`.
* The directory must contain two files: `__init__.py` (empty) and `solution.py`
* `solution.py` must have the following class (feel free to add as many auxiliary methods as you want):

```python
from typing import Tuple


class Solution:

    def analyze_books(self, books_dataset: str) -> Tuple[int, int, int]:
        # WRITE YOUR SOLUTION HERE
```

* The method `analyze_books` must return a tuple of integers representing the book ID that answer each of the questions presented above, f.e: `(1, 10, 300)` means book with ID 1 was the most rated book, book 10 was the better rated and book 300 is **X**
* Include a Jupyter notebook explaining how you obtained your solution and using the functions `analyze_books`/
* The repository will run linting checks
* The repository will verify your solution is correct.
* When both linting and grading checks pass, someone from the team will review and merge your PR.
* Enjoy 💕.

**Notes:**

* Please make your code reusable and readable. Avoid leaving debugging instructions within your solution.