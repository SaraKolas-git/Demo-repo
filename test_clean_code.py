"""Unit tests for clean_code module."""
import unittest
from clean_code import add_numbers, subtract_numbers


class TestCleanCode(unittest.TestCase):
    """Tests for clean_code functions."""

    def test_add(self):
        """Test add_numbers function."""
        assert add_numbers(2, 3) == 5

    def test_subtract(self):
        """Test subtract_numbers function."""
        assert subtract_numbers(5, 3) == 2
"""Final Test"""