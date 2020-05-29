"""Grader entry point."""

from importlib import import_module
from typing import Any, List

import logging
import os
import sys
import pathlib

from grader import Grader # pylint: disable=E0611


SOLUTIONS_DIR = 'solutions'
SOLUTION_MODULE_NAME = 'solution'
SOLUTION_CLASS_NAME = 'Solution'


def get_solutions() -> List[Any]:
    """Returns a list of Solution classes found in the solutions package."""
    logger.info("Collecting solutions...")
    sys.path.append(str(pathlib.Path().absolute()))
    solutions = []
    for i in os.scandir(SOLUTIONS_DIR):
        if i.is_dir() and i.name != "__pycache__":
            module_name = f"{SOLUTIONS_DIR}.{i.name}.{SOLUTION_MODULE_NAME}"
            try:
                module = import_module(module_name)
            except ModuleNotFoundError:
                logger.error("Failed loading module %s", module_name)
                sys.exit(1)
            try:
                cls = getattr(module, SOLUTION_CLASS_NAME)
            except AttributeError:
                logger.error("Failed getting solution class %s", SOLUTION_CLASS_NAME)
                sys.exit(1)
            solutions.append(cls)
    return solutions


if __name__ == '__main__':
    logging.basicConfig(
        level=int(os.getenv("GRADER_LOG_LEVEL", default=logging.DEBUG)), # pylint: disable=W1508
        format='%(levelname)s: %(message)s'
    )
    logger = logging.getLogger()
    grader = Grader(get_solutions(), logger) # pylint: disable=E1102
    grader.run()
