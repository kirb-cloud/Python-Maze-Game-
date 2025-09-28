# Maze Game (Python)

A text-based maze navigation game built in Python. The player begins at the **start (`s`)** and must navigate through open paths to reach the **finish (`f`)**, while avoiding walls (`*`). Your current position is displayed as **`X`** within the maze.

## Features

- Reads maze layout from `maze.txt`
- Live maze rendering with player position
- Movement options: **North, South, West, East**
- Prevents movement into walls (`*`)
- Detects win condition when reaching `f`
- Input validation using `check_input.py`

## How to Play

1. Place `maze_game.py`, `check_input.py`, and `maze.txt` in the same directory.
2. Run the program:

```bash
python maze_game.py

 - Maze Game - 
*************
*X     *    f
* *** ***** *
*     *     *
***** * *****
*           *
*************

Choose a direction:
1. North
2. South
3. West
4. East




