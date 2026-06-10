---
title: "Pascal's Triangle"
source_notebook: "discrete-mathematics/combinatorics/pascals-triangle.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/combinatorics/pascals-triangle.ipynb"
original_human_author: B67687
polished_by: GPT-5
review_status: needs-human-review
canonical_status: draft-canonical
---

# Pascal's Triangle

This note explains Pascal's triangle from the act of choosing.

By the end, we should understand:

- why the sides are always $1$
- why each inside number is made from the two numbers above it
- why the triangle is really a table of combinations
- why the famous identity is just "current item chosen or not chosen"

## Start With Choosing

Suppose we have $n$ distinct objects.

We want to choose $r$ of them.

The number of ways to do that is:

$$
\binom{n}{r}
$$

So a row of Pascal's triangle can be read as:

```text
from n objects, how many ways are there to choose 0, 1, 2, ..., n objects?
```

For example, the row for $n = 3$ is:

```text
choose 0   choose 1   choose 2   choose 3
```

or:

$$
\binom{3}{0},\quad
\binom{3}{1},\quad
\binom{3}{2},\quad
\binom{3}{3}
$$

The values are:

$$
1,\quad 3,\quad 3,\quad 1
$$

## The Edge Values

The left side of the triangle is always:

$$
\binom{n}{0}
$$

That means:

```text
choose nothing from n objects
```

There is exactly one way to do this.

We choose no objects.

So:

$$
\binom{n}{0} = 1
$$

The right side of the triangle is always:

$$
\binom{n}{n}
$$

That means:

```text
choose everything from n objects
```

There is exactly one way to do this too.

We choose every object.

So:

$$
\binom{n}{n} = 1
$$

This is why both sides of Pascal's triangle are $1$.

They are not magic starting numbers.

They are the two easiest choosing actions:

```text
choose nothing
choose everything
```

## Building The Rows

Now list the choices row by row.

For $n = 0$, there is only one possible choice size:

$$
\binom{0}{0} = 1
$$

For $n = 1$:

$$
\binom{1}{0} = 1,
\quad
\binom{1}{1} = 1
$$

For $n = 2$:

$$
\binom{2}{0} = 1,
\quad
\binom{2}{1} = 2,
\quad
\binom{2}{2} = 1
$$

For $n = 3$:

$$
\binom{3}{0} = 1,
\quad
\binom{3}{1} = 3,
\quad
\binom{3}{2} = 3,
\quad
\binom{3}{3} = 1
$$

Put them in rows:

```text
            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
```

This is Pascal's triangle.

But the triangle shape is not the real explanation.

The real explanation is that row $n$ contains:

$$
\binom{n}{0},\binom{n}{1},\binom{n}{2},\ldots,\binom{n}{n}
$$

## The Current Object Split

Now we explain why the inside numbers come from the two numbers above.

Suppose we want to choose $r$ objects from $n$ objects.

Focus on one object.

Call it the current object:

```text
current object: A
```

There are only two cases.

Either `A` is chosen:

```text
[A]
```

or `A` is not chosen:

```text
 A
```

These two cases cannot overlap.

A choice cannot both include `A` and not include `A`.

So the total count is:

```text
ways where A is chosen
+
ways where A is not chosen
```

## If The Current Object Is Chosen

If `A` is chosen, then one of the $r$ chosen places has already been used.

So from the remaining $n - 1$ objects, we only need to choose:

$$
r - 1
$$

more objects.

That gives:

$$
\binom{n-1}{r-1}
$$

## If The Current Object Is Not Chosen

If `A` is not chosen, then none of the $r$ chosen places has been used yet.

So from the remaining $n - 1$ objects, we still need to choose:

$$
r
$$

objects.

That gives:

$$
\binom{n-1}{r}
$$

## Put The Two Cases Together

Every valid choice belongs to exactly one of these two cases:

```text
A is chosen
A is not chosen
```

So:

$$
\binom{n}{r}
=
\binom{n-1}{r-1}
+
\binom{n-1}{r}
$$

This is the whole reason Pascal's triangle adds the two numbers above.

The left-above number counts choices where the current object is chosen.

The right-above number counts choices where the current object is not chosen.

## A Concrete Example

Suppose we want:

$$
\binom{5}{2}
$$

That means:

```text
choose 2 objects from 5 objects
```

Focus on one object, say `A`.

If `A` is chosen, we need $1$ more object from the remaining $4$:

$$
\binom{4}{1}
$$

If `A` is not chosen, we still need $2$ objects from the remaining $4$:

$$
\binom{4}{2}
$$

So:

$$
\binom{5}{2}
=
\binom{4}{1}
+
\binom{4}{2}
$$

Numerically:

$$
10 = 4 + 6
$$

That is exactly the Pascal triangle rule:

```text
      4   6
        10
```

The bottom number is not made by arbitrary addition.

It is made by splitting the choices into two complete cases.

## Extreme Cases Still Work

For the left edge:

$$
\binom{n}{0}
=
\binom{n-1}{-1}
+
\binom{n-1}{0}
$$

Choosing $-1$ objects is impossible, so:

$$
\binom{n-1}{-1} = 0
$$

Choosing $0$ objects has one way, so:

$$
\binom{n-1}{0} = 1
$$

Therefore:

$$
\binom{n}{0} = 0 + 1 = 1
$$

For the right edge:

$$
\binom{n}{n}
=
\binom{n-1}{n-1}
+
\binom{n-1}{n}
$$

Choosing all $n - 1$ objects from $n - 1$ objects has one way.

Choosing $n$ objects from only $n - 1$ objects is impossible.

So:

$$
\binom{n}{n} = 1 + 0 = 1
$$

The edge values are just the same rule touching the boundary.

## Popular Name

The identity:

$$
\binom{n}{r}
=
\binom{n-1}{r-1}
+
\binom{n-1}{r}
$$

is called Pascal's identity.

The triangle that displays these values is called Pascal's triangle.

But the deeper idea is simpler than both names:

```text
For the current object, either it is chosen or it is not chosen.
```

## What This Note Achieves

We started from the meaning of $\binom{n}{r}$.

Then we saw that the side values are choosing nothing and choosing everything.

Then we focused on one current object.

That object forced two cases:

- chosen
- not chosen

Adding those two cases gave:

$$
\binom{n}{r}
=
\binom{n-1}{r-1}
+
\binom{n-1}{r}
$$

The common name for this is Pascal's identity, and Pascal's triangle is the table that keeps applying it.
