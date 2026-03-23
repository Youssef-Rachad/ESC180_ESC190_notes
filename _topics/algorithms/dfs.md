---
title: Deep First Search
layout: default
jax: True
---
# Depth First Search
Depth First Search focuses on exploring each available path fully before moving onto the next one at a given node.

> ***
> **Algorithm:** Depth First Search
>
> -----
>
>   **Input:** Graph G(V, E)
1. while (there are non-visited nodes)
2. $$\qquad$$ Initialise stack S
3. $$\qquad$$ Push a non-visited vertex $$v_i$$ to S
4. $$\qquad$$ Mark $$v_i$$ as visited
5. $$\qquad$$ while (S is not empty)
6. $$\qquad$$ $$\qquad$$ Pop $$v_j$$ from S
7. $$\qquad$$ $$\qquad$$ Mark $$v_j$$ as visited
8. $$\qquad$$ $$\qquad$$ Push non-visited vertices adjacent to $$v_j$$ to S
>
> ***


<center>
<script type="text/tikz">
\begin{tikzpicture}
    % Define the vertices
    \node (F) at (0,0) [circle, draw, fill=blue!30] {F};
    \node (B) at (2,1) [circle, draw, fill=blue!30] {B};
    \node (C) at (4,0) [circle, draw, fill=blue!30] {C};
    \node (D) at (3,-2) [circle, draw, fill=blue!30] {D};
    \node (E) at (1,2) [circle, draw, fill=blue!30] {E};
    \node (A) at (3,3) [circle, draw, fill=red!30] {A};
    % Draw the directed edges
    \draw[-, thick] (F) -- (B);
    \draw[-, thick] (B) -- (C);
    \draw[-, thick] (C) -- (F);
    \draw[-, thick] (F) -- (D);
    \draw[-, thick] (F) -- (E);
    \draw[-, thick] (C) -- (A);
    \draw[-, thick] (C) -- (D);
    \draw[-, thick] (E) -- (A);
\end{tikzpicture}
</script>
</center>

| Iteration | Stack Contents | Traversal Path |
| --------- | -------------- | -------------- |
| 0         | A              |                |
| 1         | _C E_          | A              |
| 2         | _B F D_ E      | A C            |
| 3         | F D E          | A C B          |
| 4         | D E            | A C B F        |
| 5         | E              | A C B F D      |
| 6         |                | A C B F D E    |

To implement DFS, we will use the <a href="{{ site.baseurl }}{% link _topics/datastructures/stacks.md %}#python-list-implementation-of-stacks">stacks</a> defined previously.

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

```python
def depth_first_traversal(g, start_name):
  start_idx = g.node_names[start_name]
  visited = [False] * g.num_nodes
  S = Stack()
  S.push(start_i)
  # Remove the next node from the DS, add all its neighbours and mark the node visited
  while not S.is_empty():
    current_node = S.pop()
    if not visited[current_node]:
      print(g.nodes_names_rev[current_node])
      visited[current_node] = True
      # Adding all neighbours
      current_node = g.nodes[current_node].head.next
      while current_node:
        if not visited[current_node.data]:
          S.push(current_node.data)
        current_node = current_node.next
```

Now we can test our graph traversal using the <a href="{{ site.baseurl }}{% link _topics/datastructures/adjlst.md %}#airport-networks">airports example</a>:

```python
if __name__ == "__main__":
  # Create a named graph
  airports = Graph()
  # Populate vertices
  airports.add_node("YYZ")
  airports.add_node("YYR")
  airports.add_node("JFK")
  airports.add_node("UOT")
  airports.add_node("LAX")
  airports.add_node("MMG")
  # Connect with edges
  airports.put_edge_name("YYR", "YYZ")
  airports.put_edge_name("YYZ", "YYR")
  airports.put_edge_name("YYZ", "JFK")
  airports.put_edge_name("YYZ", "UOT")
  airports.put_edge_name("JFK", "LAX")
  airports.put_edge_name("LAX", "MMG")

  # Traverse the graph
  depth_first_traversal(airports, "YYR")
```

