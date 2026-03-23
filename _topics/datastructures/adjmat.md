---
title: Graphs - Adjacency Matrix
layout: default
jax: True
---
# Adjacency Matrix Data Structure
We can implement graphs using a matrix, or more specifically a 2D array, by creating an array of the same length as the number of vertices in the graph.
Then create an array, again of the same length as the number of vertices in the graph, for each entry of the initial array and represent the existence of an edge by storing a 1 in the array or the absence of an edge by storing a 0. 
The usual convention is to use 0 and 1 when the graph is unweighted but this can be modified.
Additionally, in a weighted graph we can store the weight of an edge in the matrix (instead of just 0 or 1) and a digraph is simply an adjacency matrix which is not necessarily symmetric.
For example: suppose if $$V_1$$ points to $$V_2$$ with an edge of weight 2 but not the other way around, then $$M[1][2] = 2$$ and $$M[2][1]= 0$$.
Since we focus on representing all of the vertices and how they can be connected, we can think of adjacency matrices as a vertex-first approach to implementing graphs and indeed the size of the adjacency matrix depends on the number of vertices in the graph.

# Python Implementation
```python
import numpy as np  # numpy has really nice functionality for their arrays
                    # Note np.Array is not the same a Python lists
class Graph:
  ''' 
  We will implement a graph using an adjacency matrix by storing
  a matrix (so an array of arrays) in the graph object and using the 
  entries in the matrix to describe the edges of the graph.
  '''
  def __init__(self, num_nodes):
    # np.zeros takes a 'shape' tuple and returns a array with those dimensions
    self.adj_mat = np.zeros((num_nodes, num_nodes))

  def is_edge(self, i, j):
    ''' Given vertex indices i and j, check if there is an edge between these vertices'''
    return self.adj_mat[i][j]

  def put_edge(self, i, j):
    ''' Given vertex indices i and j, place an edge from i to j'''
    self.adj_mat[i][j] = 1 # Assuming weighted graph
    # self.adj_mat[j][i] = 1 # If assuming undirected graph

  def remove_edge(self, i, j):
    ''' Given vertex indices i and j, remove the edge from i to j'''
    self.adj_mat[i][j] = 0
    # self.adj_mat[j][i] = 0 # If assuming undirected graph
```

Now let's use our graph:
```python
if __name__ == "__main__":
  g = Graph(4)     # equiv. Graph.__init__(4)
  g.put_edge(1, 2) # equiv. Graph.put_edge(g, 1, 2)
  print(g.is_edge(1, 2)) # True
```
## Recall List of Lists
## Implementing Vertices as Nodes

# C Implementation

## Recall Array of Arrays
## Implementing Vertices as Nodes
