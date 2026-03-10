---
title: The Page Rank Algorithm
layout: default
jax: True
---

# Motivating PageRank

The idea of the Page Rank algorithm is to determine which websites a user is
likely to visit.
First, we start by modelling the entire Internet!!! and figure out which
websites are most popular.
Note: this isn't as difficult a feat since this algorithm was introduced in the
early days of Google's search engine development, at which time the Internet was
relatively small.
The premise, at the time, is simple: if a weblink is feautured on many pages
then it must be more popular because it is more often clicked.
Now, if we let a random user surf the internet for a long time, each time
clicking on a new link from within a page (remember, 'searching it up' is not a
thing yet\~ish, we are inventing the thing to do that), where will that user
likely end up.

Suppose our Internet looks like this

<center>
<script type="text/tikz">
\begin{tikzpicture}
    % Define the vertices
    \node (A) at (0,0) [circle, draw, fill=blue!30] {A};
    \node (B) at (2,2) [circle, draw, fill=blue!30] {B};
    \node (C) at (4,0) [circle, draw, fill=blue!30] {C};
    \node (D) at (3,-2) [circle, draw, fill=blue!30] {D};
    \node (E) at (1,-2) [circle, draw, fill=blue!30] {E};
    % Draw the directed edges
    \draw[-{latex}, thick] (A) -- (B);
    \draw[-{latex}, thick] (B) -- (C);
    \draw[-{latex}, thick] (C) -- (D);
    \draw[-{latex}, thick] (D) -- (E);
    \draw[-{latex}, thick] (E) -- (A);
    \draw[-{latex}, thick] (B) -- (D);
    \draw[-{latex}, thick] (C) -- (A);
\end{tikzpicture}
</script>
</center>

Notice how we need to use a directed graph since there is a notion of 'start
point' and 'end point' and that there are no self-directing edges since you
can't link a page to itself (for now, before the big companies wanted _all_ of
our attention all the time).

If we started at website A, we can see that there is only 1 website available to
visit, so there is a 100% probability to visit B from A.
Now that we are at B, there is some probability $$p$$ that we visit C and some
other probability $$1-p$$ (recall probabilities sum to unity) that we visit D.
We can continue this process and write down the transition probabilities for
each node.

That sounds like a math and computation problem, so of course a matrix
organically crops up.
Here, we will deal with a transition matrix that is 5x5 like so

<pre style="color:white;">
      A  B    C    D  E
    ┌                   ┐
    | 0  0    0.5  0  1 | A
    | 1  0    0    0  0 | B
M = | 0  0.3  0    0  0 | C
    | 0  0.7  0.5  0  0 | D
    | 0  0    0    1  0 | E
    └                   ┘
</pre>

where the transitions probabilities that are not 0 or 1 are picked randomly for
this example.
The entry $$M[i][j]$$ is the probability of visiting website $$j$$ from website
$$i$$.
Beyond the scope of this course, we call this graph _strongly connected_ because
it is possible to reach any website from any other website in some number of
step, and we call this transition matrix irreducible (related to a strongly
connected graph), non-negative (no negative entries because they are
probabilities) and stochastic (a stochastic matrix' rows/columns sum to unity).

One last definition, we call a state vector the vector which holds the current
state of the user.
It represents where the user might be on the internet, so might start with a
state vector $$s_1$$ but as the user travels and we make guesses as to where
they are now, the state vector might look something like $$s_2$$

<pre style="color:white">
s_1 = [ 1.0  , 0.0  , 0.0  , 0.0 , 0.0  ]^T
s_2 = [ 0.02 , 0.15 , 0.21 , 0.51, 0.11 ]^T

Note, we want state-vectors to be column vectors hence the transpose.
</pre>
which says that after some time, the user is probably at website D with
probability 51%.

The last piece of linear algebra we need to introduce is the concept of power
iterations and steady-state convergence.
The Page Rank algorithm is defined as the successive application of the
transition matrix onto the initial state and the result is some vector that
approaches the dominant eigenvector (the eigen vector with the biggest
eigenvalue, which also happens to approach 1).

For the purpose of this course, we will focus on the formula

$$
\vec s \leftarrow M\cdot\vec s
$$

Let's break down the implementation:
- First define a graph
- Then create a transition matrix
- Initialise a state vector
- Apply the transition matrix k-many times onto the state vector (and store the
  result back into the state vector)
- Read the state vector back and determine where the user might end up on the
  internet
