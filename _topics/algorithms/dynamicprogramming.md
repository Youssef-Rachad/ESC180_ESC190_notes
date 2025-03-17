---
title: Algorithms
layout: default
jax: True
---
# What is Dynamic Programming?
Dynamic programming refers to a class of problem solving techniques (another you have heard of is 'divide and conquer') which tries to break up a problem into subproblems and as these subproblems are solved, their values are used to construct the final solution as well as re-used to avoid unecessary computation. This is often a new way to solve problem to students so examples are very handy to understand DP. In later courses, you may revisit dynamic programming and specifically study what is called "the optimality" of a solution. 

For now, let's look at a first and familiar example:

# Memoising Fibonacci Numbers
We want to compute the n-th Fibonacci number, as defined by the recurence relation:

$$F_i = \begin{cases}0 & i=0\\1&i=1\\F_{i-1} + F_{i-2}&i>1\end{cases}$$

{% include quiz.html question="Write a function that recursively computes the n-th Fibonacci (Python or C is fine)."
   answer="
   ```python
def fib(n):
 if n == 0:
     return 0
 if n == 1:
     return 1
 return fib(n-1) + fib(n-2)
```
   "
%}
While this works, it is extremely inefficient because it calculates the same values over and over again. This is because the function calls itself twice with the same argument in the recursive case. As a result, the time complexity of this implementation is exponential, which means it grows very quickly with increasing values of n.

Doing this computation by hand,or by using print statements, we can see that this implementation grows a call tree and its complexity can be found to be $$\mathcal O(1.61^n)$$ - and it's not a coincidence that the golden ratio shows up! So the naive recursive approach that would be suitable in ESC180 clearly grows exponentially. 

This expensive computation motivates us to look for patterns and indeed:

$$F_3 = F_2 + F_1 = (F_1 + F_0) + F_1 = \dots = 2$$

so it's clear that we are repeating computations and this prompts us to store previous results and retrieve them later. 
This is called **memoisation** (which is not a typo, but you can think of "memorisation" as an analogy) and it's accepted without further proof that we can store results in some hashtable such that lookup is done in constant time (i.e. without extra cost).

With memoisation, we can implement a more efficient algorithm:
```python
def fib(n, mem = {}):
    if n in mem:
        return mem[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    mem[n] = fib(n-1, mem) + fib(n-2, mem)
    return mem[n]
```

Therefore, if we have already computed something, we don't have to go through an entire series of recursive calls! The time complexity of this implementation is now linear, because we only have to do $$3n$$ recursive calls. Analysing the algorithm, we can see that each entry in `mem` is computed once exactly so `fib(i-1)` and `fib(i-2)` do not produce recursive calls. Since we compute up to $$n$$ entries in `mem`, the time complexity is said to be linear, $$\mathcal O(n)$$ (drop the constant 3). Note that this analysis assumes retrieval is constant and addition is constant in time, which is true for doubles, but may not be true for other data types (since fibonacci integers can increase exponentially)

<center>
{% include quiz.html question="
Since recursion and iteration are equally expressive, we can rewrite the above algorithm to use a `for-loop` instead of a recursion. 
Even though the two are equivalent, in practise there some differences and in this case, the iterative implementation should truly make n computations.
Implement this iterative version of the algorithm"
answer="
```python
def fib_iter(int n):
    fib_list = [0] * n
    fib_list[0:2] = [0, 1]
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[n]
```
**Open Ended Follow Up:**

The size of this array is linear in n. Can you do this task in constant space (i.e. the size of the array does not depend on m?)
"
%}
</center>

## Dynamic Programming Method
In general, for dynamic programming:

1. Divide a complex problem into a number of simpler overlapping problem.
2. Defined a relationship between solutions to more complex problems and solutions to simpler problems. 
This is known as a Bellman Equation.
This is an important step. 
For the Fibonacci example, we had
$$F_i = \begin{cases}0 & i=0\\1&i=1\\F_{i-1} + F_{i-2}&i>1\end{cases}$$
3. Store solutions to each subproblem, solving each subproblem once (i.e. using `fib_list` to store solutions)
4. Use stored solutions to solve the original problem.

# Painting the Whole Neighbourhood
> There are a row of $$n$$ houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
>
> The cost of painting each house with a certain color is represented by a `n x 3` cost matrix. For example, `costs[0][0]` is the cost of painting house 0 with color red; `costs[1][2]` is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note that the above wording was taken from a LeetCode medium problem, but encodes the same information as the problem in the lecture. (Generally, coding interviews will contain questions at this level, so it is good practice to do medium-level Leetcode problems fast if you are trying to get software engineering PEY positions at top companies.)

Let's apply the Dynamic Programming Method:
1. Divide the problem into computing the minimum cost for each colour at each house.
2. Define a relationship between the subproblems and the original problem:
$$\begin{cases}R(i) & = \text{cost}(i, \text{red}) + \text{min}(G(i-1),B(i-1)) \\G(i) & = \text{cost}(i, \text{green}) + \text{min}(R(i-1),B(i-1)) \\B(i) & = \text{cost}(i, \text{blue}) + \text{min}(R(i-1),G(i-1))\\ \text{Cost}(i) &= \text{min}(R(i), G(i), B(i)) \end{cases}$$
   Here, $$R(i), G(i), B(i)$$ are the optimal cost if the $$i^{\text{th}}$$ house was painted red, green, or blue respectively. Note that these equations also reflect that no two adjacent houses can be painted the same colour.

3. Store the minimum cost for each house in the `n x 3` cost matrix.
4. Pick the minimum cost for each house (min of each column in the cost matrix) and take the sum for a total cost.


Let's see an implementation of the solution:
```python
# Suppose we have 6 houses
N = 6

# Cost matrix 
houses = [[7, 6, 7, 8, 9, 20],
          [3, 8, 9, 22, 12, 8],
          [16, 10, 4, 2, 5, 7]]


cost = [[0] * N,
        [0] * N,
        [0] * N]



cost[0][0] = houses[0][0]
cost[1][0] = houses[1][0]
cost[2][0] = houses[2][0]

for i in range(1, N):
    # the min cost to paint the first i houses, with the i-th being painted red
    cost[0][i] = houses[0][i] + min(cost[1][i-1], cost[2][i-1])

    # the min cost to paint the first i houses, with the i-th being painted green
    cost[1][i] = houses[1][i] + min(cost[0][i-1], cost[2][i-1])

    # the min cost to paint the first i houses, with the i-th being painted blue
    cost[2][i] = houses[2][i] + min(cost[0][i-1], cost[1][i-1])

min(cost[0][5], cost[1][5], cost[2][5])

cols = [0] * N
i = N-1
if cost[0][N-1] <= min(cost[1][N-1], cost[2][N-1]):
    cols[N-1] = 0
elif cost[1][N-1] <= min(cost[0][N-1], cost[2][N-1]):
    cols[N-1] = 1
else:
    cols[N-1] = 2

for i in range(N-2, -1, -1):
    cur_min = 10000
    cur_min_col = -1
    for col in [0, 1, 2]:
        if col == cols[i+1]:
            continue
        if cost[col][i] < cur_min:
            cur_min = cost[col][i]
            cur_min_col = col
    cols[i] = cur_min_col


def paint_house_cost(houses, col, i):
    '''Return the cost of painting houses
    0, 1, 2, ,,, i, with the i-th houses painted col
    and the total cost minimized'''
    if i == 0:
        return houses[col][i]

    cur_min = sum(sum(costs) for costs in houses)
    cur_min_col = -1
    for color in [0, 1, 2]:
        if color == col:
            continue
        cost_color_i = paint_house_cost(houses, color, i-1)
        if cost_color_i < cur_min:
            cur_min = cost_color_i
            cur_min_col = color
    return houses[col][i] + cur_min
```

# Change Change Optimally

> Given a list of n denominations of coins $$\{d_1, d_2, \dots, d_n\}$$ and a target sum $$V$$, find the minimum number of coins needed to make change for the target sum.

Using Canadian coins, this problem turns out to be quite straightforwards since the denominations ($$\{5, 10, 25, 100, 200\}$$) are set up such that a greedy approach where picking the highest value coin possible every time works out to produce the smallest number of coins picked (e.g. 75&#x00A2; is always minimally made with 3 25&#x00A2; coins). 

**What about the penny??** You may have keenly noticed that the 1&#x00A2; denomination is missing from the Canadian coins list. As a fun aside, show that the solution is off by at most 4 coins when missing the penny then, show that rounding the original target value to the nearest 5&#x00A2; increment bounds the error to at most 2 coins.

A better example would be a list of 3 denominations $$\{1, 4, 5\}$$ with a target sum of 8$. We can easily see that the answer is 2 coins of 4$ - note that the greedy approach does not work in this case because the list of denominations contains coprime pairs.

Let's define $$\text{OPT}(v) := \text{minimum of coins to make } v$$ as the solution to a problem with target sum $$v$$ with base case of $$\text{OPT}(0) = 0$$. Note that we cannot make a negative sum so for posterity we impose $$\text{OPT}(v < 0) = \infty$$. Now, let's apply the Dynamic Programming Method:

1. Divide the problem into computing the minimum number of coins needed to make the target sum *minus* each of the denominations (considered separately).
2. This allows us to define our Bellman equation which relates the subproblem to the original problem $$\text{OPT}(v) = \underset{d\in\text{denominations}}{\text{min}}\{1 + \text{OPT}(v - d)\}$$.
3. Store the solution to each subproblem, solving each subproblem once and storing the result in an list we can call $$\verb#OPT#$$
4. Use the stored solutions to solve the original problem

## Iterative Solution
## Retrieving the Coins
## Recursive Solution
## Memoisation
# I Have a Pen, I Have an Apple ...
This problem is taken from lab 8 (also from the 2024 Exam)
> Given a non-empty string $$s$$ and a dictionary $$\text{wordDict}$$ containing a list of non-empty words, determin if $$s$$ can be segmented into a space-separated sequence of one or more dictionary words.
>
> *clarifying: $$\text{wordDict}$$ is a Python `list`.*
>
> For example: Given $$s=$$ "applepenapple" and $$\text{wordDict}=$$ ["apple", "pen"]
>
> Return `True` because we can segment the string into "apple pen apple"

Observe that this problem is very similar to the coin change problem in that we can fit each word in the dictionary as a prefix to the string and solve a smaller problem so the analogy is that the wordDict is a list of denominations that potentially make up the string.

Let's work out the above example: If we are specifically interested in knowing if the string *can be* seegmented (later we will try to retrieve the segmentation) then we can try:
```
s = "applepenapple"

wordDict = ["apple", "pen", "app"] # I'm adding "app" to make the example non-trivial

canSegment(s, wordDict) = canSegment("penapple", wordDict) OR
                          canSegment("lepenapple", wordDict)

# Solve first subproblem
canSegment("lepenapple", wordDict) = False # There are no words that fit as a prefix

# Solve second subproblem
canSegment("penapple", wordDict) = canSegment("apple", wordDict)

# Solve third subproblem
canSegment("apple", wordDict) = True # "apple" is a dictionary word!

# Bubble up the solutions
canSegment(s, wordDict) = ( (True) ) OR (False)
                        = True
```

