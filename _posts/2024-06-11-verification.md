---
title: Praxis is Upon Thee!
layout: default
jax: true
---
# Note Taking Verification

This website should fullfill stakeholder requirements that are neatly expressed through the following DfX:
- Design for simplicity
- Design for readability
- Design for cohesion

# Code Blocks
Let's write a function in python
```python
import sys

def foo(bar):
    return bar

if __name__ == "__main__":
    print(foo)
```

and define an object in C
```c
#ifndef STUDENT
#define STUDENT

typedef struct Student {
    int  CompilationErrors;
    char *AcademicHoroscope;
} Student;

#endif
```

# LaTeX 
You could be reading an inconspicuous sentence describing the funs and wonders of triangle and suddenly BAM Pythagoras' theorem \\(a^2+b^2=c^2\\) and that's not all: oh noo this one generalises too $a^2+b^2-2ab\cos(\theta)=c^2$. Try to use inlines sensibly...

Block equations however, now those are the wild west of Latex. Anything can happen: $$\underbrace{F = ma.}_{\text{an interesting equation}}$$

Wanna use additional packages, sure! though I'm not sure what's included and not:

$$
\begin{align}
\mathbf M &= \begin{pmatrix} 
0&1\\
1&0
\end{pmatrix}\\
M &= U^\dagger U
\end{align}
$$

Editor's note: gotta use double dollars for anything worthwhile...

## TiKz
We want to make plots, draw shapes and make graphs of all sorts. Here are a few examples which should be met:
<script type="text/tikz">
  \begin{tikzpicture}
    \draw (0,0) circle (1in);
  \end{tikzpicture}
</script>
<script type="text/tikz">
\begin{tikzpicture}
    % Draw a shaded circle
    \fill[blue!30] (2,2) circle (1.5);
    % Draw a curvy blob
    \fill[red!50] plot [smooth cycle, tension=0.8] coordinates {(5,1) (6,2.5) (7,1.8) (6.5,0.5) (5.5,0.2)};
    % Add labels
    \node at (2,2) {Circle};
    \node at (6,1.5) {Blob};
\end{tikzpicture}
</script>
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

## pgf Plots?
Nope, but we will bootleg plots using tikz:

<script type="text/tikz">
\begin{tikzpicture}[scale=1.5]
    % Draw axes
    \draw[-{latex}] (-0.5,0) -- (5,0) node[right] {$x$};
    \draw[-{latex}] (0,-1.5) -- (0,1.5) node[above] {$f(x)$};
    % Draw function plot
    \draw[domain=0:4.5, smooth, variable=\x, blue, thick] plot (\x, {sin(\x r)});
    % Label for the function
    \node[blue, below right] at (4.5,1) {$f(x) = \sin(x)$};
    % Mark some points
    \filldraw[red] (1,{sin(1 r)}) circle (1.5pt) node[above right, black] {$(1, \sin(1))$};
    \filldraw[red] (2,{sin(2 r)}) circle (1.5pt) node[below right, black] {$(2, \sin(2))$};
    \filldraw[red] (3,{sin(3 r)}) circle (1.5pt) node[above left, black] {$(3, \sin(3))$};
\end{tikzpicture}
</script>
Well, looks like commas are not properly rendered. Let's debug that another day

# Colour Boxes

So far we are lean and green... more colours (CSS lol) coming soon but we have demonstrated the _most unbelievable aspect_ of our prototype!
{% include box.html content="Definition" %}
A real number is a number that is not unreal
{% include end.html %}

# Pseudocode
This one may be used less often, and surprisingly the text workaround is better than brute forcing some \\(\LaTeX\\) solution from what I gather.

###### Insertion Sort Algorithm
> Input: array A
>
> Insertion Sort(A)
 1. for $j=2$ to $A.length$
 2.   key = A[j]
 3.   // Insert A[j] into the sorted sequence A[1..j-1]
 4.   i = j - 1
 5.   while $i > 0$ and $A[i] > key$
 6.     A[i+1] = A[i]
 7.     i --
 8.   A[i+1] = key
 for $j=2$ to $A.length$
   key = A[j]
   // Insert A[j] into the sorted sequence A[1..j-1]
   i = j - 1
   while $i > 0$ and $A[i] > key$
     A[i+1] = A[i]
     i --
   A[i+1] = key
