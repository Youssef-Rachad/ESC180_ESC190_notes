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
