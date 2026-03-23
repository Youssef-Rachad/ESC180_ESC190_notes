---
title: Artificial Intelligence
layout: default
jax: True
---
# Artificial Intelligence
In this section we will introduce the basics of artificial intelligence to give both a motiviation and a footing for future courses that involve topics like machine learing, deep learning, natural language processing, reinforcement learning and more. 
In fact these topics, properly defined, nest within each other based on specific definitions so it's important to first learn that really all we are doing is taking some input vector, transforming it using matrices and non-linear function and obtaining an output vector that we hope approaches the correct solution.

# Feed Forward Neural Networks

Stacking [perceptrons](https://en.wikipedia.org/wiki/perceptron) together gets us a feed forward layer and stacking those layers one after the other allows us to build a feed forward neural network. 
The layers are also referred to as dense layers or densly connected layers while the network itself is also referred to as **Artificial Neural Network** when used standalone. 
Semantics aside, the key idea here is that we have a model that takes numerical inputs (aka examples) and produces an output (aka labels) and we are trying to learn what function our model should compute to predict the output (as best as possible) given some valid input. 
ANNs are very useful on large scale data sets with many dimensions - recall hyperplanes from linear algebra and how solving systems of many variables requires higher dimensionality.

The idea of using neural networks in general comes from the theory that a sufficiently large amount of "neurons" organised in particular ways and all activating each other based on inputs is how computation can be done. 
Additionally, we will use neural networks as a statistical model and see how it is able to do computation in a completely different way than we are used to.
The early days of AI involved rule based models; many many if-statements are nested in growing complexity until any one input can definitively be placed in a category.
While this was not very effective for large problems, adding a bit of stochasticity ultimately lead to the random forest model.
Random forests are not covered in this course, though the use of a stochastic approach instead of a deterministic one is a theme that will pop up time and time again in AI.


