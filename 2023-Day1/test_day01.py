"""
Advent of Code - Day 1: Trebuchet
Specification by Example test suite
"""
import pytest

# Part 1 Examples
PART1_EXAMPLES = [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77),
]

PART1_FULL_EXAMPLE = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]
PART1_EXPECTED_SUM = 142


# Part 2 Examples
PART2_EXAMPLES = [
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz", 13),
    ("xtwone3four", 24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
]
PART2_FULL_EXAMPLE = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

PART2_EXPECTED_SUM = 281

class TestPart1:
    """Part 1: Extract numeric digits only"""
    @pytest.mark.parametrize("line,expected", PART1_EXAMPLES)
    def test_individual_calibration_values(self, line, expected):
        """
        Given a line with mixed text and digits
        When we convert all numbers to their digit form and extract the first and last digit
        Then we get the correct two-digit calibration value
        """
        from day01 import get_calibration_value_part1
        assert get_calibration_value_part1(line) == expected

    def test_sum_of_calibration_values(self):
        """
        Given multiple calibration lines
        When we sum all calibration values
        Then we get the expected total
        """
        from day01 import solve_part1
        assert solve_part1(PART1_FULL_EXAMPLE) == PART1_EXPECTED_SUM

class TestPart2:
    """Part 2: Extract numeric and spelled-out digits"""
    @pytest.mark.parametrize("line,expected", PART2_EXAMPLES)
    def test_individual_calibration_values(self, line, expected):
        """
        Given a line with mixed text and digits (including spelled-out)
        When we extract the first and last digit
        Then we get the correct two-digit calibration value
        """
        from day01 import get_calibration_value_part2
        assert get_calibration_value_part2(line) == expected

    def test_sum_of_calibration_values(self):
        """
        Given multiple calibration lines with spelled-out digits
        When we sum all calibration values
        Then we get the expected total
        """
        from day01 import solve_part2
        assert solve_part2(PART2_FULL_EXAMPLE) == PART2_EXPECTED_SUM