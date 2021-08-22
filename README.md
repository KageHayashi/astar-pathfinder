# Pathfinder
A visualizer for various pathfinding algorithms.

## A*
### Introduction
The A* Search algorithm is one of the most popular algorithms used in path-finding and graph traversals.

### Example
We start at the top left corner of the maze and want to get to the bottom right.

#### Cell colors
Black cell - wall
<br>
Red cell - close (traversed already and not optimal)
<br>
Green cell - open (considered for traversing later on)
<br>
Blue cell - path (the route taken so-far)

#### Mouse and key interactions
spacebar - starts the search
<br>
r - resets the grid
<br>
left mouse - place wall
<br>
right mouse - remove wall

![astar](/images/astar.gif)

## Dijkstra

# TO-DO
- [ ] Refactor code into separate functions and modules
- [ ] Add ability to place walls (mouse and 'a' 's' keys), replay same grid (spacebar), reset to new grid ('r' key) 
- [ ] Implement different heuristics
- [ ] Extend to other pathfinding algorithms
- [ ] Add 'heatmap'
