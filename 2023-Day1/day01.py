def get_calibration_value_part1(line: str) -> int:
    """
    Given a line with mixed text and digits
    When we extract the first and last digit
    Then we get the correct two-digit calibration value
    """
    digits = [char for char in line if char.isdigit()]
    return int(digits[0] + digits[-1]) if digits else 0

def solve_part1(lines: list[str]) -> int:
    """
    Given multiple calibration lines
    When we sum all calibration values
    Then we get the expected total
    """
    return sum(get_calibration_value_part1(line) for line in lines)

def get_calibration_value_part2(line: str) -> int:
    """
    Given a line with mixed text and digits (including spelled-out)
    When we extract the first and last digit
    Then we get the correct two-digit calibration value
    """
    WORD_TO_DIGIT = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    digits = []
    for i, char in enumerate(line):
        if char.isdigit():
            digits.append(char)
        else:
            # Check if any spelled-out digit starts at this position
            for word, digit in WORD_TO_DIGIT.items():
                if line[i:].startswith(word):
                    digits.append(digit)
                    break  # Only match one digit per position
    
    return int(digits[0] + digits[-1]) if digits else 0

def solve_part2(lines: list[str]) -> int:
    """
    Given multiple calibration lines with spelled-out digits
    When we sum all calibration values
    Then we get the expected total
    """
    return sum(get_calibration_value_part2(line) for line in lines)

def main():
    """
    Reads the input file, calculates the total calibration value for both parts, 
    and prints the results.
    """
    with open('/workspaces/SpecByExample-AOC/2023-Day1/input.txt', 'r') as f:
        lines = [line.strip() for line in f]
    
    print(f"The sum of all calibration values for Part 1 is: {solve_part1(lines)}")
    print(f"The sum of all calibration values for Part 2 is: {solve_part2(lines)}")

if __name__ == "__main__":
    main()
