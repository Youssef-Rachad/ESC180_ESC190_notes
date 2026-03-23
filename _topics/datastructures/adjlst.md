---
title: Graphs - Adjacency Lists
layout: default
jax: True
---
# Adjacency List Data Structure
We can implement graphs using linked lists by storing all graph vertices in a linked list and each of those are the head of a linked list which holds nodes for all of the connected vertices. 
Since we focus on representing how the vertices are connected, we can think of adjacency lists as an edge-first approach to implementing graphs and indeed the size of the adjacency list depends on the number of edges in the graph.

# Python Implementation
```python
class Graph:
  ''' 
  We will implement a graph using an adjacency list by storing
  a list for each node in the graph and each entry in the list
  contains a linked list to store the neighbours of that node.

  Note that the linked list of neighbours has an order in its
  representation but that order doesn't matter when it comes 
  to representing the graph's data so any order is okay.
  '''
  def __init__(self, num_nodes):
    self.adj_list = [None] * num_nodes  # An empty list, big enough to hold every vertex's LL

  def is_edge(self, i, j):
    ''' Given vertex indices i and j, check if there is an edge between these vertices'''
    pass

  def put_edge(self, i, j):
    ''' Given vertex indices i and j, place an edge from i to j'''
    pass

  def remove_edge(self, i, j):
    ''' Given vertex indices i and j, remove the edge from i to j'''
    pass
```

## A Vertex is a Node
Let's implement a `Node` class to represent the vertices of the graph.
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
```
## Recall Linked Lists
Let's also recall `Linked List`s and implement them quickly in `LL.py` (along with `Node`):
```python
# LL.py
class LL:
  def __init__(self):
    self.head = None

  def insert(self, idx, data):
    new_node = Node(data)

    if self.head == None:  # Empty LL case
      self.head = new_node
    else:
      if idx == 0:         # Prepending case
        head_save = self.head
        self.head = new_node
        self.head.next = head_save
      else:
        cur = self.head
        for jdx in range(idx - 1): # traverse LL, stop before idx
          cur = cur.next

        tmp = cur.next
        cur.next = new_node
        new_node.next = tmp
        #  Or we could use Python's swap
        #cur.next, new_node.next = new_node, cur.next
  
  def is_in(self, data):
    cur = self.head
    while cur: # equiv. while cur != None
      if cur.data == data:
        return True
      cur = cur.next
    return False # after traversing, return False if not found

  def remove(self, data):
    if head.data == data:
      self.head = self.head.next # Let the gc take care of freeing the old head
      return
    cur = self.head

    # Now traverse as long as the next node exists and
    #   its data is not the value we are looking for
    while cur.next and cur.next.data != data:
      cur = cur.next

    # Either we reached the end ...
    if cur.next == None: # equiv. if not cur.next:
      print(f"[ERROR] failed to remove {data}")
      return

    # ... Or we succeeded 
    cur.next = cur.next.next

  def __str__(self): # this allows us to print("My linked list is", LL)
    cur = self.head
    string = "(head) "
    while cur: # equiv. while cur != None
      string += str(cur.data) + " -> "
      cur = cur.next
    return string + "None"
```
## Adjacency Lists
We can now import the code we wrote as follows
```python
import LL # assuming Node and LL are defined in LL.py

class Graph:
  ''' 
  We will implement a graph using an adjacency list by storing
  a list for each node in the graph and each entry in the list
  contains a linked list to store the neighbours of that node.

  Note that the linked list of neighbours has an order in its
  representation but that order doesn't matter when it comes 
  to representing the graph's data so any order is okay.
  '''
  def __init__(self, num_nodes):
    self.adj_list = [None] * num_nodes  # An empty list, big enough to hold every vertex's LL
    self.num_nodes = num_nodes
    for idx in range(self.num_nodes):
      self.adj_list.append(LL.LL())

  def is_edge(self, i, j):
    ''' Given vertex indices i and j, check if there is an edge between these vertices
        Access LL i in the List adj_list, and search for Node with data j
    '''
    return self.adj_list[i].is_in(j)

  def put_edge(self, i, j):
    ''' Given vertex indices i and j, place an edge from i to j
        Always insert at the head of the ith LL to save time (instead of traversing)
        Here we haven't implemented an deduplication mechanism, 
        though one should be considered in practise
    '''
    self.adj_list[i].insert(0, j) # At the ith LL, insert j in the head

  def remove_edge(self, i, j):
    ''' Given vertex indices i and j, remove the edge from i to j'''
    self.adj_list[i].remove(j)
```

Now let's use our graph:
```python
if __name__ == "__main__":
  g = Graph(4)     # equiv. Graph.__init__(4)
  g.put_edge(1, 2) # equiv. Graph.put_edge(g, 1, 2)
  print(g.is_edge(1, 2)) # True
```

## Labelled Nodes
It will often be useful to represent object in a graph and use named labels instead of keeping a mapping between names and the indices used in the graph. This requires us to alter our implementation of the graph slightly:
```python
import LL # assuming Node and LL are defined in LL.py

class Graph:
  ''' 
  We will implement a graph using an adjacency list by storing
  a list for each node in the graph and each entry in the list
  contains a linked list to store the neighbours of that node.

  Note that the linked list of neighbours has an order in its
  representation but that order doesn't matter when it comes 
  to representing the graph's data so any order is okay.
  '''
  def __init__(self, num_nodes = 0):
    # num_nodes is 0 by default, so if we want to use an unamed graph we simply pass num_nodes
    # and avoid calling the ..._name() methods
    # if we instead want a named graph, we omit num_nodes and add the nodes manually
    self.adj_list = [None] * num_nodes  # An empty list, big enough to hold every vertex's LL
    self.num_nodes = num_nodes
    self.node_names, self.node_names_rev = {}, {}
    for idx in range(self.num_nodes):
      self.adj_list.append(LL.LL())

  def add_node(self, name):
    self.node_names[name] = len(self.adj_list)
    self.node_names_rev[len(self.adj_list)] = name
    self.adj_list.append(LL.LL())
    self.num_nodes += 1

  def is_edge(self, i, j):
    ''' Given vertex indices i and j, check if there is an edge between these vertices
        Access LL i in the List adj_list, and search for Node with data j
    '''
    return self.adj_list[i].is_in(j)

  def is_edge_name(self, name_i, name_j):
  ''' Look up an edge from vertex i to vertex j by looking up the names first '''
    return self.is_edge(self.node_names[name_i], self.node_names[name_j])

  def put_edge(self, i, j):
    ''' Given vertex indices i and j, place an edge from i to j
        Always insert at the head of the ith LL to save time (instead of traversing)
        Here we haven't implemented an deduplication mechanism, 
        though one should be considered in practise
    '''
    self.adj_list[i].insert(0, j) # At the ith LL, insert j in the head

  def is_edge_name(self, name_i, name_j):
  ''' Put an edge from vertex i to vertex j by looking up the names first '''
    return self.put_edge(self.node_names[name_i], self.node_names[name_j])

  def remove_edge(self, i, j):
    ''' Given vertex indices i and j, remove the edge from i to j'''
    self.adj_list[i].remove(j)
```

## Airport Networks

We can now use our graph datastructure to implement an airport network

```python
if __name__ == "__main__":
  # Create a named graph
  airports = Graph()
  # Populate vertices
  airports.add_node("YYZ")
  airports.add_node("YVR")
  airports.add_node("JFK")
  # Connect with edges
  airports.put_edge_name("YVR", "YYZ")
  airports.put_edge_name("YYZ", "YVZ")
  airports.put_edge_name("YYZ", "JFK")
```
<center>
<script type="text/tikz">
\begin{tikzpicture}[
  node distance=1.5cm and 1cm,
  every node/.style={rectangle split, rectangle split parts=2, draw, rectangle split horizontal, minimum width=2.5cm, minimum height=0.75cm, align=center},
  nodearrow/.style={*->, >=latex, shorten <=-8pt, shorten >=0pt, },
]

% Heads
\node (YYZ) at (0, 0) {YYZ};
\node (YVR) [below=0.15cm of YYZ] {YVR};
\node (JFK) [below=0.15cm of YVR] {JFK};
\node (YUL) [below=0.15cm of JFK] {YUL};
\node (LAX) [below=0.15cm of YUL] {LAX};
\node (SFO) [below=0.15cm of LAX] {SFO};
\node (YXZ) [below=0.15cm of SFO] {YXZ};

% YYZ
\node (YYZ1) [right=of YYZ] {YUL};
\node (YYZ2) [right=of YYZ1] {JFK};
\node (YYZ3) [right=of YYZ2] {YVR};
\node (YYZ4) [right=of YYZ3] {NUL \nodepart{second}X};
\draw[nodearrow] (YYZ) -- (YYZ1);
\draw[nodearrow] (YYZ1) -- (YYZ2);
\draw[nodearrow] (YYZ2) -- (YYZ3);
\draw[nodearrow] (YYZ3) -- (YYZ4);

% YVR
\node (YVR1) [right=of YVR] {YYZ};
\node (YVR2) [right=of YVR1] {NUL \nodepart{second}X};
\draw[nodearrow] (YVR) -- (YVR1);
\draw[nodearrow] (YVR1) -- (YVR2);

% JFK
\node (JFK1) [right=of JFK] {LAX};
\node (JFK2) [right=of JFK1] {NUL \nodepart{second}X};
\draw[nodearrow] (JFK) -- (JFK1);
\draw[nodearrow] (JFK1) -- (JFK2);

% YUL
\node (YUL1) [right=of YUL] {YXZ};
\node (YUL2) [right=of YUL1] {NUL \nodepart{second}X};
\draw[nodearrow] (YUL) -- (YUL1);
\draw[nodearrow] (YUL1) -- (YUL2);

% LAX
\node (LAX1) [right=of LAX] {SFO};
\node (LAX2) [right=of LAX1] {NUL \nodepart{second}X};
\draw[nodearrow] (LAX) -- (LAX1);
\draw[nodearrow] (LAX1) -- (LAX2);

% SFO
\node (SFO1) [right=of SFO] {NUL \nodepart{second}X};
\draw[nodearrow] (SFO) -- (SFO1);

% YXZ
\node (YXZ1) [right=of YXZ] {NUL \nodepart{second}X};
\draw[nodearrow] (YXZ) -- (YXZ1);
\end{tikzpicture}
</script>
</center>

# C Implementation

## A Vertex is a Node
## Recall Linked Lists
## Nesting Linked Lists
