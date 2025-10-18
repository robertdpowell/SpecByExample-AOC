import re
from typing import Dict, List

# Default maximum cubes available (12 red, 13 green, 14 blue)
# This matches the problem specification
DEFAULT_MAX_CUBES = {'red': 12, 'green': 13, 'blue': 14}


def parse_game(line: str) -> tuple[int, List[Dict[str, int]]]:
    """
    Parse a game line into game ID and list of cube draws.
    
    Example: "Game 1: 3 blue, 4 red; 1 red, 2 green"
    Returns: (1, [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2}])
    """
    game_part, draws_part = line.split(': ')
    game_id = int(game_part.split()[1])
    
    # Parse each draw (separated by semicolons)
    draws = []
    for draw in draws_part.split('; '):
        # Parse each color count in the draw
        cube_counts = {}
        for match in re.finditer(r'(\d+) (\w+)', draw):
            count, color = int(match.group(1)), match.group(2)
            cube_counts[color] = count
        draws.append(cube_counts)
    
    return game_id, draws


def is_game_valid(draws: List[Dict[str, int]], max_cubes: Dict[str, int] = None) -> bool:
    """
    Check if all draws in a game are valid (don't exceed max_cubes).
    
    Args:
        draws: List of draw dictionaries with color counts
        max_cubes: Maximum cubes available per color (defaults to DEFAULT_MAX_CUBES)
    """
    if max_cubes is None:
        max_cubes = DEFAULT_MAX_CUBES
    
    return all(
        count <= max_cubes.get(color, 0)
        for draw in draws
        for color, count in draw.items()
    )


def get_valid_game_part1(line: str, max_cubes: Dict[str, int] = None) -> bool:
    """
    Given a game record, determine if the game is valid.
    A game is valid if no draw exceeds the maximum cubes available.
    
    Args:
        line: Game record string
        max_cubes: Maximum cubes available per color (defaults to DEFAULT_MAX_CUBES)
    """
    _, draws = parse_game(line)
    return is_game_valid(draws, max_cubes)


def solve_part1(lines: List[str], max_cubes: Dict[str, int] = None) -> int:
    """
    Given multiple game records, sum the IDs of all valid games.
    
    Args:
        lines: List of game record strings
        max_cubes: Maximum cubes available per color (defaults to DEFAULT_MAX_CUBES)
    """
    if max_cubes is None:
        max_cubes = DEFAULT_MAX_CUBES
    
    return sum(
        game_id
        for line in lines
        for game_id, draws in [parse_game(line)]
        if is_game_valid(draws, max_cubes)
    )


def get_minimum_cubes(draws: List[Dict[str, int]]) -> Dict[str, int]:
    """
    Find the minimum number of cubes of each color required for a game.
    This is the maximum count seen for each color across all draws.
    
    Args:
        draws: List of draw dictionaries with color counts
    
    Returns:
        Dictionary with minimum required cubes per color
    """
    min_cubes = {}
    for draw in draws:
        for color, count in draw.items():
            min_cubes[color] = max(min_cubes.get(color, 0), count)
    return min_cubes


def calculate_power(cubes: Dict[str, int]) -> int:
    """
    Calculate the power of a set of cubes.
    Power is the product of all cube counts (red × green × blue).
    
    Args:
        cubes: Dictionary with cube counts per color
    
    Returns:
        Power value (product of all counts)
    """
    power = 1
    for count in cubes.values():
        power *= count
    return power


def solve_part2(lines: List[str]) -> int:
    """
    Given multiple game records, calculate the sum of powers of minimum required cubes.
    
    For each game:
    1. Find the minimum cubes required (max of each color across all draws)
    2. Calculate power (product of all cube counts)
    3. Sum all powers
    
    Args:
        lines: List of game record strings
    
    Returns:
        Sum of all game powers
    """
    return sum(
        calculate_power(get_minimum_cubes(draws))
        for line in lines
        for _, draws in [parse_game(line)]
    )


def main():
    """
    Reads the input file, calculates solutions for both parts, 
    and prints the results.
    """
    with open('/workspaces/SpecByExample-AOC/2023-Day2/input.txt', 'r') as f:
        lines = [line.strip() for line in f]
    
    print(f"The sum of all valid game IDs for Part 1 is: {solve_part1(lines)}")
    print(f"The sum of all game powers for Part 2 is: {solve_part2(lines)}")


if __name__ == "__main__":
    main()
