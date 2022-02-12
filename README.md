
This program provides a solution to all solvable 8-tile puzzles.

- Implements A\*search algorithm by keeping an open and closed priority queue and only exploring promising new states with a better heuristic and lower move count. Allows redirection of paths if a better way to arrive at the same point is found. Uses backtracking to generate final path after arriving at goal state
- The board is represented by a 1d array ```[r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3]```
- The heuristic used is l1-norm Manhattan distance of each tile to its goal position
- propogates successor states

### Usage
Launch the program with ```python3 -i 8tileSolver.py``` Then use the following command to obtain the steps to the solution represented as a list of states:
```solve(<puzzle>)``` where puzzle must be in the format mentioned above.
