"""Problem grader."""

import os
import sys

from base import BaseGrader # pylint: disable=E0611


class Grader(BaseGrader):
    """Problem grader."""

    evaluation_function_name = 'analyze_books'

    def get_solution_from_env(self, var_name):
        """Returns parsed solution from OS environment."""
        value = os.getenv(var_name)
        try:
            value = int(value)
        except TypeError:
            self.logger.error("Grader failed reading solution from environment variable %s.", var_name)
            sys.exit(1)
        return value

    def get_test_cases(self):
        """Returns the dataset file location and the solutions parsed from env vars."""
        return [(
            "books.csv",
            (
                self.get_solution_from_env("SOLUTION_QUESTION_1"),
                self.get_solution_from_env("SOLUTION_QUESTION_2"),
                self.get_solution_from_env("SOLUTION_QUESTION_3"),
            ),
        )]
