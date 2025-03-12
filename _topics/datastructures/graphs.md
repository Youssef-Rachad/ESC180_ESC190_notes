---
title: Graphs
layout: default
jax: True
---
# What is a graph?

A graph is a general way to describe a collection of nodes and the arrows that point to them. In fact, three special cases of graphs are linked lists, trees and heaps! Let's define this general concept:

{% include colorbox.html title="Definition: Graph"
   content="A graph is an ADT consisting of a set of nodes called **vertices, _V_** together with a set of **edges, _E_** which describe the relationship between the vertices. We denote a graph _G_ by 

   $$\text{G = (V, E)}$$
   "
%}

For example, the following is a graph:

<center>
<script type="text/tikz">
    \begin{tikzpicture}[scale=3]
    \tikzstyle{vertex}=[circle,fill=black!25,minimum size=40pt,inner sep=2pt]

    \node[vertex] (A) at (0,1.8)  {A};
    \node[vertex] (B) at (0.8,0.6)  {B};
    \node[vertex] (C) at (0.3,-0.7)  {C};
    \node[vertex] (D) at (-0.7,-0.4)  {D};
    \node[vertex] (E) at (-0.8,0.8)  {E};

    \draw (A) -- node[midway, above right] {edge 1} (B);
    \draw (B) -- node[midway, right] {edge 2} (D);
    \draw (B) -- node[midway, right] {edge 3} (C);
    \draw (C) -- node[midway, below left] {edge 4} (E);
    \end{tikzpicture}
</script>
</center>

where

$$
\begin{align*}
G &= (V,E) \\
V &= \{v_1, v_2, v_3, v_4, v_5\} \\
E &= \{e_1, e_2, e_3, e_4, e_5\} \\
\text{and}&\\
e_1 &= (v_1, v_2) \\
e_2 &= (v_2, v_3) \\
e_3 &= (v_2, v_4) \\
e_4 &= (v_3, v_5)
\end{align*}
$$

Here, the edges can either be undirected or directed. If no arrows are drawn, we assume the edges are
undirected (so we can travel from $$v_1$$ to $$v_2$$ and from $$v_2$$ to $$v_1$$) and we treat $$(v_1,v_2)$$
as an unordered pair. The edges are also unweighted in this example, this means all of the edges have the same weight (or that weighing the edges doesn't apply to our current graph at all). 

Let's look at directed and weighted graphs in more detail:

# Digraphs
Directed graphs are also called "digraphs" and their edges have an associated direction.

<center>
<script type="text/tikz">
\begin{tikzpicture}[scale=2]
\tikzstyle{vertex}=[circle,fill=black!25,minimum size=40pt,inner sep=2pt]

% Define the nodes
\node[vertex] (1) at (2,2)  {Node 1};
\node[vertex] (2) at (3,1)  {Node 2};
\node[vertex] (3) at (0,1)  {Node 3};
\node[vertex] (4) at (2,0)  {Node 4};

% Draw the edges
\draw[->] (2) -- node[midway, above] {Edge 1} (1);
\draw[->] (1) -- node[midway, above] {Edge 2} (3);
\draw[->] ([xshift=.5cm]3) -- node[midway, right] {Edge 3} (4);
\draw[->] ([xshift=-.5cm]4) -- node[midway, left] {Edge 4} (3);
\draw[->] (4) -- node[midway, below] {Edge 5} (1);

\end{tikzpicture}
</script>
</center>

Here, we write $$e_1 = (v_2,v_1)$$ where the order matters now. The first element is the predecessor (or source) and the second element is the successor (or target).

# Weighted Graphs
In a weighted graph, the edges have an associated weight that often represents a cost or a strength. Weighted graphs can either be undirected or directed and when they are also directed, the weight going one way ($$\text{weight}(v_1, v_2)$$) is not necessarily the same as the weight of the opposite edge ($$\text{weight}(v_2, v_1)$$).

<center>
<script type="text/tikz">
\begin{tikzpicture}[scale=2]
\tikzstyle{vertex}=[circle,fill=black!25,minimum size=40pt,inner sep=2pt]

% Define the nodes with labels
\node[vertex] (1) at (3, 1)  {Node 1};
\node[vertex] (2) at (2, 2)  {Node 2};
\node[vertex] (3) at (2, 0)  {Node 3};
\node[vertex] (4) at (4, 1)  {Node 4};

% Draw the edges and label them
\draw (1) -- node[midway, above] {30} (2);
\draw (1) -- node[midway, below] {45} (3);
\draw (1) -- node[midway, above] {60} (4);
\draw (2) -- node[midway, right] {25} (3);
\draw (2) -- node[midway, above] {10} (4);
\draw (3) -- node[midway, below] {20} (4);

\end{tikzpicture}
</script>
</center>
# Why might we use graphs?

We use graph because graph theory is plentiful and offers many standard algorithms that solve specific problems. 
Interestingly, many common problems can be reformulated as (or mapped to) graph problems. Here are a few examples:
- **Context:**Want to find the best route between cities
  - _Graph_:Vertices are cities, edges are direct flights between cities 
  - _Reformulate_:Find the shortest distance between two nodes on a graph
- **Context:**Want to find scheduling times/locations for classes
  - _Graph_:Vertices are school classes, edges connect classes whose schedules overlap
  - _Reformulate_:Find a set of nodes that are completely disconnected from each other (i.e. no two nodes share an edge)
- **Context:**Want to know when an object can be freed
  - _Graph_:Vertices are objects in memory, edges connect objects that refer to each other
  - _Reformulate_:Find the set of nodes that connect to a certain node

Learning about graphs is important for problem solving because we can focus on framing a problem as a graph problem and obtain a solution almost automatically using graph theory results!

# Some More Terminology
- Vertex $$v_1$$ is **adjacent** to vertex $$v_2$$ if an edge connects them.
- A **path** is a sequence of vertices that are connected by edges. The length of the path is the number of _edges_ in it
- A **cycle** is a path that starts and ends at the same vertex
- A graph with no cycles is called a **acyclic graph**
- A directed acyclic graph is abbreviated as **DAG**
- A **simple path** is a path that does not contain any repeated vertices
- A **simple cycle** is a cycle that does not contain any repeated vertices (except for the first and last vertex) 
- Two vertices are **connected** if there is a path between them 
- A subset of vertices is a **connected component** if every pair of vertices in the subset is connected 
- The **degree** of vertex $$v$$ is the number of edges that connect to it

With all that, how do we actually implement a graph? We will use adjacency lists and adjacency matrices to implement a graph, though the term "graph" will be used interchangeably to denote the ADT or either of these datastructures. The comparison between adjacency lists and adjacency matrices is very similar to that between linked lists and arrays.

Note that we often refer to the number of vertices in a graph as $n\coloneq |V|$.

# Adjacency List
An adjacency list is a list of $n$ linked lists where the $i^{\text{th}}$ linked list represents the list of vertices adjacent to $v_i$. 
The nodes in the linked lists holds the name of the vertex and can also store the weight of the edge if applicable.
Since we are only storing vertices that are connected, we say that an adjacency list is a edge first approach to implementing a graph.

<center>
<script type="tikz/text">
\begin{figure}[!ht]
\centering
\resizebox{1\textwidth}{!}{
\begin{circuitikz}
\tikzstyle{every node}=[font=\LARGE]
\draw  (4.25,12.5) rectangle (5,11.75);
\draw  (4.25,11) rectangle (5,10.25);
\draw  (4.25,9.5) rectangle (5,8.75);
\draw  (4.25,10.25) rectangle (5,9.5);
\draw  (4.25,6.5) rectangle (5,5.75);
\draw  (4.25,7.25) rectangle (5,6.5);
\draw  (4.25,8.75) rectangle (5,8);
\draw  (4.25,8) rectangle (5,7.25);
\draw  (5.75,12.5) rectangle (6.5,11.75);
\draw  (6.5,12.5) rectangle (7.25,11.75);
\draw [->, >=Stealth] (4.75,12) .. controls (5.25,12) and (5.25,12) .. (5.75,12) ;
\draw  (6.5,11) rectangle (7.25,10.25);
\draw [->, >=Stealth] (4.75,10.5) .. controls (5.25,10.5) and (5.25,10.5) .. (5.75,10.5) ;
\draw  (5.75,11) rectangle (6.5,10.25);
\draw  (6.5,10.25) rectangle (7.25,9.5);
\draw [->, >=Stealth] (4.75,9.75) .. controls (5.25,9.75) and (5.25,9.75) .. (5.75,9.75) ;
\draw  (5.75,10.25) rectangle (6.5,9.5);
\draw  (6.5,7.25) rectangle (7.25,6.5);
\draw [->, >=Stealth] (4.75,6.75) .. controls (5.25,6.75) and (5.25,6.75) .. (5.75,6.75) ;
\draw  (5.75,7.25) rectangle (6.5,6.5);
\draw [->, >=Stealth] (4.75,8.25) .. controls (5.25,8.25) and (5.25,8.25) .. (5.75,8.25) ;
\draw  (5.75,8.75) rectangle (6.5,8);
\draw  (6.5,8.75) rectangle (7.25,8);
\draw  (6.5,9.5) rectangle (7.25,8.75);
\draw  (5.75,9.5) rectangle (6.5,8.75);
\draw [->, >=Stealth] (4.75,9) .. controls (5.25,9) and (5.25,9) .. (5.75,9) ;
\draw [->, >=Stealth] (7,6.75) .. controls (7.5,6.75) and (7.5,6.75) .. (8,6.75) ;
\draw  (8,7.25) rectangle (8.75,6.5);
\draw  (8.75,7.25) rectangle (9.5,6.5);
\draw [->, >=Stealth] (7,8.25) .. controls (7.5,8.25) and (7.5,8.25) .. (8,8.25) ;
\draw  (8,8.75) rectangle (8.75,8);
\draw  (8.75,8.75) rectangle (9.5,8);
\draw [->, >=Stealth] (7,12) .. controls (7.5,12) and (7.5,12) .. (8,12) ;
\draw  (8,12.5) rectangle (8.75,11.75);
\draw  (8.75,12.5) rectangle (9.5,11.75);
\node [font=\LARGE] at (4,11.25) {1};
\node [font=\LARGE] at (4,10.5) {2};
\node [font=\LARGE] at (4,9.75) {3};
\node [font=\LARGE] at (4,9) {4};
\node [font=\LARGE] at (4,8.25) {5};
\node [font=\LARGE] at (4,7.5) {6};
\node [font=\LARGE] at (4,6.75) {7};
\node [font=\LARGE] at (4,6) {8};
\draw  (4.25,11.75) rectangle (5,11);
\draw  (6.5,11.75) rectangle (7.25,11);
\draw [->, >=Stealth] (4.75,11.25) .. controls (5.25,11.25) and (5.25,11.25) .. (5.75,11.25) ;
\draw  (5.75,11.75) rectangle (6.5,11);
\node [font=\LARGE] at (4,12) {0};
\node [font=\LARGE] at (6,12) {2};
\node [font=\LARGE] at (6,11.25) {6};
\node [font=\LARGE] at (6,10.5) {6};
\node [font=\LARGE] at (6,9.75) {4};
\node [font=\LARGE] at (6,9) {5};
\node [font=\LARGE] at (6,8.25) {3};
\node [font=\LARGE] at (6,6.75) {2};
\node [font=\LARGE] at (8.25,12) {5};
\node [font=\LARGE] at (8.25,8.25) {7};
\node [font=\LARGE] at (8.25,6.75) {8};
\end{circuitikz}
}
\end{figure}
</script>
</center>

In an adjacency list:
- Looking up if an edge between $v_i$ and $v_j$ exists takes $\mathcal O(d)$ where $d$ is the maximum vertex degree in the graph because we are traversing the $i^\text{th}$ linked list until we find $v_j$. 
- Finding all of the vertices adjacent to $v_i$ takes $\mathcal O(d)$ again and for the same reason. 
- The space requirement to store the whole graph is $\mathcal O(|V| + |E|)$ where $|V|, |E|$ denote the number of vertices and of edges in the graph respectively.

# Adjacency Matrix
An adjacency matrix is an $n\times n$ matrix, typically an $n$ long array of arrays of $n$ nodes and the entries of that array represents the presence of an edge if using using 0 for no edge and 1 for an edge.
In the case of a weighted graph, the entry is the weight of the edge instead of just 1.

In an adjacency matrix:
- Looking up if an edge between $v_i$ and $v_j$ exists takes $\mathcal O(1)$ because we are accessing the $M[i][j]$ entry of the matrix and [array]({{ site.baseurl }}{% link _topics/datastructures/ADT.md %}#Arrays) lookup is done in constant time. 
- Finding all of the vertices adjacent to $v_i$ takes $\mathcal O(|V|)$ which equates to iterating through the $i^\text{th}$ array. 
- The space requirement to store the whole graph is $\mathcal O(|V|^2)$ where $|V|$ denotes the number of vertices in the graph.


# Comparison Recap

| Operation | Adjacency List | Adjacency Matrix |
| --------- | -------------- | ---------------- |
| Edge Lookup | $\mathcal O(d)$ | $\mathcal O(1)$ |
| List Neighbours | $\mathcal O(d)$ | $\mathcal O(|V|)$ |
| Space Required | $\mathcal O(|V| + |E|)$ | $\mathcal O(|V|^2)$ |

Generally, an adjacency list will use less memory than an adjacency matrix. As the graph gets more and more dense, meaning more and more edges are formed, the spatial requirement approaches that of the adjacency matrix where the there is already enough space allocated for every vertex to connect to every other vertex.