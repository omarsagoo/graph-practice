# Homework 1: Graph ADT & Traversals

Follow the instructions [here](https://make-school-courses.github.io/CS-2.2-Graphs-Recursion/#/Assignments/01-Graph-ADT) to complete this assignment.

## Discussion Questions

1. How is Breadth-first Search different in graphs than in trees? Describe the differences in your own words.

In a tree, Breadth-first Search, BFS, will go through each level of the tree individually. Meaning it will search all of the nodes at a specific depth before moving deeper into the tree. In a graph, BFS searches all neighbor vertices one edge distance away at a time. Meaning it will search all vertices at a certain edge distance from the starting vertex before it moves farther through the graph.

2. What is one application of Breadth-first Search (besides social networks)? Describe how BFS is used for that application. If you need some ideas, check out [this article](https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/?ref=rp).

BFS in a graph allows the program to find the shortest path between two vertecies by checking all of the neighbors and their children simultaneously, instead of down each path individually. This can be used to find relational data in statistics. For Example, how many actors link two actors together, or to follow along the path of a series of events.