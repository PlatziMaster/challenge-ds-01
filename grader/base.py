"""Base module contains the abstract classes that control the grader execution."""

import sys
from typing import Any, List, Tuple

IOPair = Tuple[Any, Any]


class BaseGrader:
    """BaseGrader contains the utilities and execution management rules for the main grader."""

    # Evaluation function name in solution module.
    evaluation_function_name: str

    _MAX_ENTRY_LENGTH = 10**3

    def __init__(self, solutions, logger):
        self.solutions = solutions
        self.logger = logger
        self.failed = False
        self.errors = 0

        # Solution entry point, used for evaluation of test cases.
        self.f = None # pylint: disable = C0103
        # Solution instance at any given evaluation.
        self.sol = None

    def run(self):
        """Runs the grader."""
        if not self.evaluation_function_name:
            self.logger.error("Grader is missing `evaluation_function_name` attribute",)
            sys.exit(1)

        for sol in self.solutions:
            errors, passed = 0, 0
            # Test cases are generated for each solution to avoid mutation between solutions
            test_cases = self.get_test_cases()
            for test in test_cases:
                self.setup(sol)
                if self.eval_solution(test):
                    errors += 1
                    self.errors += 1
                else:
                    passed += 1

            if errors > 0:
                # Log failed status
                self.failed = True
            else:
                self.logger.info(
                    "%s finished: %d passed, %d failed",
                    self.__get_solution_full_name(sol), passed, errors
                )

        if self.failed:
            self.logger.error("Grader finished with %d errors", self.errors)
            sys.exit(1)

    def setup(self, solution):
        """Creates a new solution instance."""
        self.sol = solution()
        try:
            self.f = getattr(self.sol, self.evaluation_function_name) # pylint: disable = C0103
        except AttributeError:
            self.logger.error(
                "Cannot find function %s in %s", self.evaluation_function_name, self.__get_solution_full_name(solution)
            )
            sys.exit(1)

    def get_test_cases(self) -> List[IOPair]:
        """Generate the test cases used against each solution."""
        raise NotImplementedError

    def eval_solution(self, test_case: IOPair) -> bool:
        """Evaluates solution against the given test case."""
        input_data, want = test_case
        if isinstance(input_data, tuple):
            got = self.f(*input_data)
        else:
            got = self.f(input_data)
        results_differ = self.compare_results(got, want)
        if results_differ:
            self.log_execution_results(got, test_case, failed=True)
        return results_differ

    def compare_results(self, got, want) -> bool:
        """Compares evaluation result with expected result. Returns true if results differ."""
        return want != got

    def log_execution_results(self, got, test_case, failed=False):
        """Logs the result of the evaluation function that differed from expected result."""
        input_data, want = test_case
        reps = []
        for value in [input_data, got, want]:
            if type(value) in {list, str, tuple}:
                reps.append(self._truncate_value(value))
            else:
                reps.append(str(value))

        execution_string = "{}\n\tinput:\t\t{}\n\toutput: \t{}\n\texpected:\t{}".format(
            self.__get_solution_full_name(self.f),
            *reps
        )
        if failed:
            self.logger.error(execution_string)
        else:
            self.logger.info(execution_string)

    def _truncate_value(self, value):
        """Returns the truncated string representation of the given interable."""
        return ', '.join([str(x) for x in value[:self._MAX_ENTRY_LENGTH]])

    def __get_solution_full_name(self, sol_cls):
        """Return solution full name."""
        return f"{sol_cls.__module__}.{sol_cls.__name__}"
