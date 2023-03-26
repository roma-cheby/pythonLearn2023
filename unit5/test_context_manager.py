import unittest
from block_errors import BlockErrors

class TestManager(unittest.TestCase):
    def test_ignore_errors(self):
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            a=1 / 0

    def test_errors_spend_higher_processed(self):
        def func():
            outer_err_types = {ZeroDivisionError}
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'

        self.assertRaises(TypeError, func)

    def test_ignore_errors_spend_higher_processed(self):
        outer_err_types = {TypeError}
        with BlockErrors(outer_err_types):
            inner_err_types = {ZeroDivisionError}
            with BlockErrors(inner_err_types):
                a = 1 / '0'

    def test_ignore_child_errors(self):
        err_types = {Exception}
        with BlockErrors(err_types):
            a=1 / '0'


