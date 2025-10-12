# Day 1: Trebuchet?!

## Part 1: Extract calibration values

**Given** a line of text with digits mixed in
**When** we extract the first and last digit
**Then** we combine them to form a two-digit number

### Examples:
- `1abc2` → 12
- `pqr3stu8vwx` → 38
- `a1b2c3d4e5f` → 15
- `treb7uchet` → 77

**Sum of all calibration values**: 142

## Part 2: Handle spelled-out digits

**Given** digits can be spelled out (one, two, three, etc.)
**When** we extract first and last digit (numeric or spelled)
**Then** we combine them to form a two-digit number

### Examples:
- `two1nine` → 29
- `eightwothree` → 83
- `abcone2threexyz` → 13
- `xtwone3four` → 24
- `4nineeightseven2` → 42
- `zoneight234` → 14
- `7pqrstsixteen` → 76