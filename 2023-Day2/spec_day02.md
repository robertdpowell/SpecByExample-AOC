# Day 1: Cube conondrum

## Part 1: Determine valid games

**Given** a record of a game and a max number of cubes available for the game
**When** we determine if the game is viable by comparing the game record with the max number of cubes
**Then** we mark the game as valid/invalid

### Examples:

Max number of cubes
'12 red cubes, 13 green cubes, and 14 blue cubes'

- 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green' -> valid
- 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue' -> valid
- 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red' -> invalid
- 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'-> invalid
- 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green' -> valid

**Sum of all valid game IDs **: 8

## Part 2: Determine minimum required values 

**Given** a record of a game 
**When** we identify the highest number of each ball colour played in that game
**Then** we determine the power of those highest numbers

- 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green' -> 4 red, 2 green, and 6 blue cubes --> power = 48
- 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue' -> 1 red, 3 green, and 4 blue cubes --> power = 12
- 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red' -> 20 red, 13 green, and 6 blue cubes --> power = 1560
- 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'-> 14 red, 3 green, and 15 blue cubes --> 630
- 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green' --> 6 red, 3 green, and 2 blue cubes --> power = 36

**Sum of powers of all game IDs **: 2286
