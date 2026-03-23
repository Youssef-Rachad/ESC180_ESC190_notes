---
title: Exploration & Path Finding
layout: default
jax: True
---

Two of the most fundamental classes of algorithms on graphs are 
1. **Graph Exploration** and traversal which is the backbone of many other
   algorithms. 
   These are used to hop from node to node given the available edges in the
   graph.
   Often, if you squint enough, the graph algorithms covered later look very
   much like graph explorations that are modified to achieved some objective.
2. **Path Finding**, here we will focus on finding the shortest path between 2
   nodes.
   This class of algorithm has many algorithms with varying efficiency and
   complexity (the main tradeoff made).

# Graph Exploration Algorithm

Graph exploration algorithms allows us to visit each node in a graph exactly
once. 
Given a graph, that is a set of nodes and a set of edges, we can generally
describe an exploration as follows

```
Initialise a list of visited nodes VN

while (not all nodes are visited)
    Initialise data structure DS
    Add a non visited node, v_i, to DS
    Mark v_i as visited in VN
    while (DS is not empty)
        Remove a node, v_j, from DS
        Mark v_j as visited
        # Print node v_j
        Add non visited nodes that are adjacent to v_j to DS
```
