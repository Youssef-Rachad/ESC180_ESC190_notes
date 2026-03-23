---
title: Bread First Search
layout: default
jax: True
---
# Breadth First Search
Breadth First Search focuses on exploring all of the possible paths available from a given node one step at a time.
Referring back to the [graph traversal]({{ site.baseurl }}{% link _topics/algorithms/traversal.md %}) template, we can define DS to be a queue.
Recall that a queue is a FIFO system such that by adding the nearest neighbours at each step of the BFS algorithm, we are starting a some starting vertex and exploring outwards almost like starting in the centre of an onion and exploring the layers away from the centre.

We may fill in the graph traversal algorithm as such 

> ***
> **Algorithm:** Breadth First Search
>
> -----
>
>   **Input:** Graph G(V, E)
1. while (there are non-visited nodes)
2. $$\qquad$$ Initialise queue Q
3. $$\qquad$$ Enqueue a non-visited vertex $$v_i$$ to Q
4. $$\qquad$$ Mark $$v_i$$ as visited
5. $$\qquad$$ while (Q is not empty)
6. $$\qquad$$ $$\qquad$$ Dequeue $$v_j$$ from Q
7. $$\qquad$$ $$\qquad$$ Mark $$v_j$$ as visited
8. $$\qquad$$ $$\qquad$$ Enqueue non-visited vertices adjacent to $$v_j$$ to Q
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

| Iteration | Queue Contents | Traversal Path |
| --------- | -------------- | -------------- |
| 0         | A              |                |
| 1         | _C E_          | A              |
| 2         | E _B F D_      | A C            |
| 3         | B F D          | A C E          |
| 4         | F D            | A C E B        |
| 5         | D              | A C E B F      |
| 6         |                | A C E B F D    |

To implement BFS, we will use the <a href="{{ site.baseurl }}{% link _topics/datastructures/queues.md %}#python-list-implementation-of-queues">queues</a> defined previously.

```python
def breadth_first_traversal(g, start_name):
  start_idx = g.node_names[start_name]
  visited = [False] * g.num_nodes
  Q = Queue()
  Q.enqueue(start_i)
  # Remove the next node from the DS, add all its neighbours and mark the node visited
  while not Q.is_empty():
    current_node = Q.dequeue()
    if not visited[current_node]:
      print(g.nodes_names_rev[current_node])
      visited[current_node] = True
      # Adding all neighbours
      current_node = g.nodes[current_node].head.next
      while current_node:
        if not visited[current_node.data]:
          Q.enqueue(current_node.data)
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
  breadth_first_traversal(airports, "YYR")
```
