Traffic Network Optimization with Dijkstra's Algorithm

Features

Represents a traffic network as a weighted graph.

Applies Dijkstra's algorithm to compute the shortest travel time from any source node.

Presents optimized travel times from each node to all other nodes in the network.

Intended for examining and optimizing traffic flow among road intersections.

Technology Used

Language: Python 3

Libraries: heapq (for priority queue operation)


How It Works

1. The traffic network is represented as a graph in an adjacency list.


2. Dijkstra's algorithm is used to determine the shortest path from any given node to the others.

3. The algorithm is executed for every node within the network to compute travel times from all intersections.

4. The result shows the travel time optimized between all pairs of nodes.

Data Collection

Source: Hardcoded in Python code.

The graph is an example traffic network.

Each edge is a road segment with a given travel time (weight).

Objective

To mimic and maximize city traffic flow based on Dijkstra's algorithm, which aids in determining the shortest and most optimal travel routes among intersections within a road network.

Controls

No GUI or user inputs.

Run the script simply by python filename.py.

Output is shown in the terminal/console.

ML Techniques Used

No machine learning utilized; the project relies on traditional graph algorithms.

Model Training

Not applicable (no ML model or training step).

Output Explanation (Optional)

The output shows:

The minimum travel time between each node (intersection) and all other nodes.

Aids to visualize shortest paths and detect possible bottlenecks or traffic congestion in the network.