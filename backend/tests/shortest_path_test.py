## Author(s): Daniel Yan
## Date: 2018-11-11
## Email: daniel.yan@vanderbilt.edu
## Filename: shortest_path_test.py
## Description: Tests for src/shortest_path.py which implements Dijkstra's
# shortest path to find shortest paths from each location to other locations.

## Libraries to import
from src import data_loader as dl
from src import locations as loc
from src import shortest_path as sp
import pytest


# Test that shortest path from hallway5_1 to hallway5_2 is correct for
# Stevenson math (should just be these two hallways)
def test_shortest_path_1():
    # Get the graph from the data loader for Stevenson
    graph = dl.graph
    # Get the start location as hallway5_1
    start = dl.hallway5_1
    # Get the map for shortest paths for hallway5_1 using shortest path
    paths = sp.shortest_path(graph=graph, start=start)
    # Check that the path to hallway5_1 is correct
    assert paths[dl.hallway5_2] == [dl.hallway5_1, dl.hallway5_2]


# Test that shortest path from hallway2_2 to hallway5_1 is correct for
# Stevenson math.
def test_shortest_path_2():
    # Get the graph from the data loader for Stevenson
    graph = dl.graph
    # Get the start location as hallway2_2
    start = dl.hallway2_2
    # Get the map for shortest paths for hallway2_2 using shortest path
    paths = sp.shortest_path(graph=graph, start=start)
    # Check that the path to hallway5_1 is correct
    assert paths[dl.hallway5_1] == [dl.hallway2_2, dl.hallway2_1,
                                    dl.staircase2_1, dl.staircase3_1,
                                    dl.staircase4_1, dl.staircase5_1,
                                    dl.hallway5_1]


# Check that a start and end location that is the same just has that one
# location in the list representing the path.
def test_shortest_path_3():
    # Get the graph from the data loader for Stevenson
    graph = dl.graph
    # Get the start location as hallway3_1
    start = dl.hallway3_1
    # Get the map for shortest paths for hallway3_1 using shortest path
    paths = sp.shortest_path(graph=graph, start=start)
    # Check that the path to hallway3_1 is just the hallway itself.
    assert paths[dl.hallway3_1] == [dl.hallway3_1]


# Check that a a start location that is not in the graph will return false.
def test_shortest_path_4():
    # Get the graph from the data loader for Stevenson
    graph = dl.graph
    # Get the start location as another location
    start = loc.Hallway()
    # Assert that there are no shortest path for the start location since it
    # is not in the graph
    assert sp.shortest_path(graph=graph, start=start) == False


# Test finding the shortest path between two rooms.
# Test that invalid room returns false
def test_get_path_from_rooms_1():
    path = sp.get_path_from_rooms("1514", "ATKL")
    assert path == False


# Test that same room returns just the adjacent hallway.
def test_get_path_from_rooms_2():
    path = sp.get_path_from_rooms("1206", "1206")
    assert path == [dl.hallway2_2]


# Test that two rooms adjacent to the same hallway returns just that hallway.
def test_get_path_from_rooms_3():
    path = sp.get_path_from_rooms("1401", "1420")
    assert path == [dl.hallway4_2]


# Tests for path that traverses several locations
def test_get_path_from_rooms_4():
    path = sp.get_path_from_rooms("1531", "1113")
    assert path == [dl.hallway5_1, dl.staircase5_1, dl.staircase4_1,
                    dl.staircase3_1, dl.staircase2_1, dl.staircase1_1,
                    dl.hallway1_1]

def test_get_path_from_rooms_5():
    path = sp.get_path_from_rooms("1110C", "1232")
    assert path == [dl.hallway1_2, dl.staircase1_2, dl.staircase2_2,
                    dl.hallway2_2, dl.hallway2_1]