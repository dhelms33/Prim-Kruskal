# Minimum Spanning Trees

## Introduction

This Python script implements two algorithms, Prim's algorithm and Kruskal's algorithm, to find the Minimum Spanning Tree (MST) of a connected, undirected graph. The script demonstrates the functionality of both algorithms and compares their performance.

## Algorithms

### Prim's Algorithm

Prim's algorithm starts with an arbitrary vertex and repeatedly grows a tree from the chosen vertex by adding the shortest edge that connects the tree to a vertex not yet in the tree until all vertices are included. It maintains a set of visited vertices and repeatedly selects the minimum-weight edge that connects a visited vertex to an unvisited vertex.

### Kruskal's Algorithm

Kruskal's algorithm constructs the MST by adding edges to the tree in ascending order of their weights. It initially treats each vertex as a separate component and then iteratively adds the shortest edge that connects two different components until all vertices are connected.

## Implementation

### Input

The script reads an adjacency matrix from a text file. The adjacency matrix represents the graph, where each row and column represent a vertex, and the values represent the weights of the edges between vertices. Infinite weight (INF) indicates the absence of an edge.

### Output

The script outputs the runtime of both algorithms and the total weight of the MST obtained by each algorithm. It also verifies that both algorithms produce the same MST by comparing the total weights.

## Usage

To use the script:

1. Prepare a text file containing the adjacency matrix of the graph.
2. Update the filename in the script to point to your graph file.
3. Run the script. It will output the runtime of each algorithm and the total weight of the MST obtained.

## Example

```python
if __name__ == '__main__':
    # Create adjacency matrix from a file
    g = createAdjMatrix("graph_verts10.txt")
    
    # Run Prim's algorithm
    start_time = time.time()
    res_prim = prim(g)
    elapsed_time_prim = time.time() - start_time
    print(f"Prim's runtime: {elapsed_time_prim:.2f}")
    
    # Run Kruskal's algorithm
    start_time = time.time()
    res_kruskal = kruskal(g)
    elapsed_time_kruskal = time.time() - start_time
    print(f"Kruskal's runtime: {elapsed_time_kruskal:.2f}")
    
    # Compare MST costs
    cost_prim = sum([e[2] for e in res_prim])
    print("MST cost w/ Prim: ", cost_prim)
    
    cost_kruskal = sum([e[2] for e in res_kruskal])
    print("MST cost w/ Kruskal: ", cost_kruskal)
    
    assert cost_prim == cost_kruskal
