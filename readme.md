# What is the Game Of Life?

The Game of Life is a two-dimensional cellular automaton devised by the British mathematician John Horton Conway in 1970 that is defined by a set of simple rules. It is used in various fields, including computer science, mathematics, biology, and physics, particularly in the study of complex systems and the behavior of living organisms. The rules of the Game of Life are based on the concept of "survival of the fittest," which means that the cells that survive and reproduce the most will be the ones that are left in the end. Starting from the initial configuration, these rules are applied, and
the game board evolves, playing the game by itself!

## How to run the Game of Life?

Either run the executable file or run the python file from the terminal

## How to run the python file

1. Install the required packages listed in the requirements.txt file using `pip install -r requirements.txt`
2. Run the python file using `python game_of_life.py`

## Command line arguments to the python file

1. `-h, --help`: Show the help message and exit.
2. `--fullscreen, -f`: Run the application in fullscreen mode.
3. `--width, -w`: Set the width of the application.
4. `--height, -h`: Set the height of the application.

e.g. `python game_of_life.py -w 1280 -h 720`

## The rules of the Game of Life

#### Birth: a cell that is dead at time t will be alive at time t + 1

if exactly 3 of its eight neighbors were alive at time t.

#### Death: a cell can die by:

#### 1. Overcrowding: if a cell is alive at time t + 1 and 4 or more of

its neighbors are also alive at time t, the cell will be dead at
time t + 1.

#### 2. Exposure: If a live cell at time t has only 1 live neighbor or no

live neighbors, it will be dead at time t + 1.

#### Survival: a cell survives from time t to time t + 1 if and only if 2 or 3 of its neighbors are alive at time t.

Starting from the initial configuration, these rules are applied, and
the game board evolves, playing the game by itself!

## What are the different types of "life-forms"?

#### 1. Still Life: A stable, finite and nonempty pattern. e.g. Block, Beehive, Boat, Ship, Loaf, and various shapes of ponds.

#### 2. Periodic Life Forma / Oscilators: A pattern that repeats itself after a fixed number of generations. e.g. p (period) = 2 Blinker, Toad. p=4 Glider, Spaceship, Light Weight Space Ship (LWSS) (speed c/2), Medium Weight Space Ship (MWSS), Heavy Weight Space Ship (HWSS), Guns.
