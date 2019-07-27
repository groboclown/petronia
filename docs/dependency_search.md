# Finding Dependencies

Like a lot of things in software, Petronia needs to find the "best match" for version package dependencies.

This is a kind of [Constraint Satisfaction Problem](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)

I've written this up as a way to record my findings on the different algorithms out there.  Primarily, it's because I can't find good references that fully describe the range of the problem.  There are some that discuss why it's an NP hard problem (it is), but none that really go into stating the problem and its complexities and solutions.

## The Problem

For this discussion, I'll call extensions by a capital letter, with a version number beside it.  Version ranges in Petronia only allow for an absolute minimum and an optional open maximum, but for this discussion I'll refer to exact values in the form `A(0,1,2)` to mean either A0, A1, or A2 as acceptable choices.

The usual case is a simple directed acyclic graph, where extension A depends on extension B and so on.  The difficulty comes with supporting a range of versions, and different versions have conflicting requirements.

Here's an example of the complexity.

* A1 depends on B(1,2) and C(1,2)
* B1 depends on D(1,2)
* B2 depends on D2 and E1
* C1 depends on D1
* C2 depends on D2 and E2

![Version Conflict Graph](../../master/docs/imgs/dependency-grapin-1.svg?raw=true)

A1 cannot depend on both B2 and C2 at the same time, because they conflict on E1 and E2.  So the algorithm can choose either B1+C1+D1 or B1+C2+D2+E2.  The algorithm will prefer higher versions over lower versions.  However, there are situations where no choice is overall "higher" than others.

## Simple solution

One simple, slow solution involves have a depth first search with backtracking of the node graph, with added constraints.  We will have a "preference function" for the highest version (`f`).  The algorithm will use a "current search space" concept, which contains a "current selection" list (`C`), the current version node being inspected (`N`), and a list of possible values to try (`P`).  `C` will be added incrementally until either the complete graph is generated, or there is a conflict in which case we go back to a previous search space.  With this definition, we must clarify that a specific `N`<sub>`P`</sub> has a set of its own 0 or more children `N`, each of which must be recursively added.

Of importance is the choice of `N` and `P`.  `N` is the current extension, and `P` is the list of acceptable versions of `N` to try that haven't been tried yet for the current search space.  The first value of `P` to try is selected by the preference function.

1. Set `H` to an empty stack. Set `C` to an empty map which will map an extension name to a version.  Set `A` to the children groups of the root node (each group is the collection of versions to choose for a single extension).  Set `C'` to a null value.
2. Push a copy of `C` and `A` onto the stack `H`.
3. If `H` is empty, then we're done searching - if `C` contains all the direct child extension names of the root node, then there is a match; otherwise no compatible search could be made.
4. Pop the top item from `H` and assign the popped values to `C` (map), and `A` (remaining children groups).
5. If `C'` is not null, then assign `C` to `C'` (not a copy!), then set `C'` to null.
6. If `A` is empty, then this node was successfully searched.  Set `C'` to `C` (not a copy!) and go back to 3.
7. Remove a group from `A` and assign it to `N`.
8. Set `P` to the list of versions in `N`.
9. If `P` is empty, then no version could be selected, and this is an invalid path.  Go back to 3.
10. Use `f` to remove an item from `P` and assign it to `Q`.
11. If there is a `N` in `C` with the same version as `Q`, then it's already been added to the list, so go back to 6.
12. If there is an `N` in `C` with a different version than `Q`, then it's a conflict.  Go back to 9.
13. We now have a choice for `N`.  Set `N` in `C` with version `Q`.  Go back to 2.

Worst-case scenario, this looks like *O(n<sup>n</sup>)* if it's a fully connected graph.  It has some big memory hogs, too (lots of copies of a dictionary and a deep stack up to *n * (n - 1)* in size).  However, because this has an early search for best choice, it doesn't need to find all the solutions, just the first one.  That means this returns a local maxima rather than one with a higher count of "better" versions; that is, this chooses the highest early, when taking a lower version might cause more later versions to be higher.  This situation in a real world is less likely.

This algorithm does not create a topological sorted return value.  There's a good chance that it could be added.

## Other Ideas

### Matrix

An N x N matrix of compatible dependencies can be created by performing a depth or breadth first search of each possible extension in the graph.  Each entry of the matrix can be assigned to 0.5 (a dependency on that extension is not specified), 0 (that extension is specified, but this version is not in the list), and 1 (the version is a dependency).  We can also say that an extension version is compatible with itself (1) so the diagonal is all 1s.  Additionally, a version of an extension is not compatible with any other version of that extension, so those are all 0s.

If all the extensions can be discovered outside of runtime, then the universe of all extensions in the system can be cached, and the complete matrix can be referenced by any algorithm.  And if you have a total of 100 extension versions, a 100 x 100 matrix isn't very big in a computer world.

But what does this tell us?

#### Example from above

We'll assign each dependency in the universe a column/row index.  We'll also add in an extra dependency to the universe of extensions, so we can see how it behaves.

```python
i_a1 = 0
i_b1 = 1
i_b2 = 2
i_c1 = 3
i_c2 = 4
i_d1 = 5
i_d2 = 6
i_e1 = 7
i_e2 = 8
i_f0 = 9

import numpy
compat = numpy.array([
    #  a1,  b1,  b2,  c1,  c2,  d1,  d2,  e1,  e2,  f0
    [   1,   1,   1,   1,   1, 0.5, 0.5, 0.5, 0.5, 0.5 ], # a1
    [ 0.5,   1,   0, 0.5, 0.5,   1,   1, 0.5, 0.5, 0.5 ], # b1
    [ 0.5,   0,   1, 0.5, 0.5,   0,   1,   1,   0, 0.5 ], # b2
    [ 0.5, 0.5, 0.5,   1,   0,   1,   0, 0.5, 0.5, 0.5 ], # c1
    [ 0.5, 0.5, 0.5,   0,   1,   0,   1,   0,   1, 0.5 ], # c2
    [ 0.5, 0.5, 0.5, 0.5, 0.5,   1,   0, 0.5, 0.5, 0.5 ], # d1
    [ 0.5, 0.5, 0.5, 0.5, 0.5,   0,   1, 0.5, 0.5, 0.5 ], # d2
    [ 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,   1,   0, 0.5 ], # e1
    [ 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,   0,   1, 0.5 ], # e2
    [ 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,   1 ], # f0
])
```

In this example, for my personal sanity, I ordered the columns according to a known dependency graph.  In practice, there is no expectation that the matrix forms an upper or lower triangle.  If the extension versions are grouped together, then an identity matrix is created for that sub-matrix.

A transposed element-wise multiplication turns the matrix into mirrored triangles.  Because that's what the operation does.

```python
>>> (compat * compat.T)
array([[ 1.  ,  0.5 ,  0.5 ,  0.5 ,  0.5 ,  0.25,  0.25,  0.25,  0.25,  0.25],
       [ 0.5 ,  1.  ,  0.  ,  0.25,  0.25,  0.5 ,  0.5 ,  0.25,  0.25,  0.25],
       [ 0.5 ,  0.  ,  1.  ,  0.25,  0.25,  0.  ,  0.5 ,  0.5 ,  0.  ,  0.25],
       [ 0.5 ,  0.25,  0.25,  1.  ,  0.  ,  0.5 ,  0.  ,  0.25,  0.25,  0.25],
       [ 0.5 ,  0.25,  0.25,  0.  ,  1.  ,  0.  ,  0.5 ,  0.  ,  0.5 ,  0.25],
       [ 0.25,  0.5 ,  0.  ,  0.5 ,  0.  ,  1.  ,  0.  ,  0.25,  0.25,  0.25],
       [ 0.25,  0.5 ,  0.5 ,  0.  ,  0.5 ,  0.  ,  1.  ,  0.25,  0.25,  0.25],
       [ 0.25,  0.25,  0.5 ,  0.25,  0.  ,  0.25,  0.25,  1.  ,  0.  ,  0.25],
       [ 0.25,  0.25,  0.  ,  0.25,  0.5 ,  0.25,  0.25,  0.  ,  1.  ,  0.25],
       [ 0.25,  0.25,  0.25,  0.25,  0.25,  0.25,  0.25,  0.25,  0.25,  1.  ]])
```
