"""
Dereck Helms
CS 4050
Assignment 4: Minimum Spanning Trees
"""

# for timing checks
import time

# Placeholder for infinity
INF = float('inf')


def createAdjMatrix(filename):
    """Create an adj/weight matrix from a file with verts, neighbors, and weights."""
    f = open(filename, "r")
    n_verts = int(f.readline())
    print(f" n_verts = {n_verts}")
    adjmat = [[INF] * n_verts for i in range(n_verts)]
    for i in range(n_verts):
        adjmat[i][i] = 0
    for line in f:
        int_list = [int(i) for i in line.split()]
        vert = int_list.pop(0)
        assert len(int_list) % 2 == 0
        n_neighbors = len(int_list) // 2
        neighbors = [int_list[n] for n in range(0, len(int_list), 2)]
        distances = [int_list[d] for d in range(1, len(int_list), 2)]
        for i in range(n_neighbors):
            adjmat[vert][neighbors[i]] = distances[i]
    f.close()
    return adjmat


def kruskal(W):
    """Finds a minimum spanning tree (MST) for a connected, undirected graph using sets for disjoint subsets."""
    n = len(W)
    edges = []
    # Collect all edges from the adjacency matrix
    for i in range(n):
        for j in range(i + 1, n):
            if W[i][j] != INF:  # Assuming INF represents absence of an edge
                edges.append((i, j, W[i][j]))
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    # Initialize sets for each vertex
    sets = [set([i]) for i in range(n)]  # Each vertex initially in its own set
    min_edges = []
    for edge in edges:
        u, v, weight = edge
        u_set = None
        v_set = None
# Find the sets containing u and v
        for i, s in enumerate(sets):
            if u in s:
                u_set = i
            if v in s:
                v_set = i
# If u and v are in different sets, merge the sets and add the edge to the MST
        if u_set != v_set:
            min_edges.append(edge)
            sets[u_set] = sets[u_set].union(sets[v_set])
            sets.pop(v_set)
    return min_edges


def prim(W):
    """Implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph."""
    n = len(W)
    visited = [False] * n
    min_edges = []
    visited[0] = True
    for _ in range(n - 1):
        min_weight = float('inf')
        min_edge = None
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and W[i][j] < min_weight:
                        min_weight = W[i][j]
                        min_edge = (i, j, min_weight)
        min_edges.append(min_edge)
        visited[min_edge[1]] = True
    return min_edges


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    """Demonstrate the functions, starting with creating the graph."""
    g = createAdjMatrix("graph_verts10.txt")
    # Run Prim's algorithm
    start_time = time.time()
    res_prim = prim(g)
    elapsed_time_prim = time.time() - start_time
    print(f"Prim's runtime: {elapsed_time_prim:.2f}")
    # Run Kruskal's for a single starting vertex, 2
    start_time = time.time()
    res_kruskal = kruskal(g)
    elapsed_time_kruskal = time.time() - start_time
    print(f"Kruskal's runtime: {elapsed_time_kruskal:.2f}")
    # Check that the sum of edges weights is the same for this graph
    cost_prim = sum([e[2] for e in res_prim])
    print("MST cost w/ Prim: ", cost_prim)
    cost_kruskal = sum([e[2] for e in res_kruskal])
    print("MST cost w/ Kruskal: ", cost_kruskal)
    assert cost_prim == cost_kruskal
