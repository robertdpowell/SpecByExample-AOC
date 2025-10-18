"""
Advent of Code - Day 2: Cube Conundrum
Specification by Example test suite
"""
import pytest

# Test constants
valid = True
invalid = False

# Game constraints: Maximum cubes available
# As specified in the problem: 12 red cubes, 13 green cubes, and 14 blue cubes
MAX_CUBES = {'red': 12, 'green': 13, 'blue': 14}

# Part 1 Examples
PART1_EXAMPLES = [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", valid),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", valid),
    ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", invalid),
    ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", invalid),
    ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", valid)
]

# Derive the full example list from PART1_EXAMPLES (DRY principle)
PART1_FULL_EXAMPLE = [game for game, _ in PART1_EXAMPLES]

# Expected sum: Game 1 (valid) + Game 2 (valid) + Game 5 (valid) = 1 + 2 + 5 = 8
PART1_EXPECTED_SUM = 8

class TestPart1:
    """Part 1: Determine valid games with cube constraints"""
    @pytest.mark.parametrize("line,expected", PART1_EXAMPLES)
    def test_individual_calibration_values(self, line, expected):
        """
        **Given** a record of a game and a max number of cubes available for the game
        **When** we determine if the game is viable by comparing the game record with the max number of cubes
        **Then** we mark the game as valid/invalid
        
        Max cubes: 12 red, 13 green, 14 blue
        """
        from day02 import get_valid_game_part1
        assert get_valid_game_part1(line, MAX_CUBES) == expected

    def test_sum_of_valid_games(self):
        """
        Given multiple game records
        When we sum all valid games (respecting max cubes: 12 red, 13 green, 14 blue)
        Then we get the expected total
        """
        from day02 import solve_part1
        assert solve_part1(PART1_FULL_EXAMPLE, MAX_CUBES) == PART1_EXPECTED_SUM

# Part 2 Examples
PART2_EXAMPLES = [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
    ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 1560),
    ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 630),
    ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36)
]

# Derive the full example list from PART2_EXAMPLES (DRY principle)
PART2_FULL_EXAMPLE = [game for game, _ in PART2_EXAMPLES]

# Expected sum of all powers: 48 + 12 + 1560 + 630 + 36 = 2286
PART2_EXPECTED_SUM = 2286

class TestPart2:
    """Part 2: Calculate total power of valid games"""
    @pytest.mark.parametrize("line,expected", PART2_EXAMPLES)
    def test_individual_game_powers(self, line, expected):
        """
        **Given** a record of a game
        **When** we calculate the total power of all draws in the game
        **Then** we get the correct total power value
        """
        from day02 import solve_part2
        assert solve_part2([line]) == expected

    def test_sum_of_game_powers(self):
        """
        Given multiple game records
        When we sum the total power of all games
        Then we get the expected total power
        """
        from day02 import solve_part2
        assert solve_part2(PART2_FULL_EXAMPLE) == PART2_EXPECTED_SUM    
