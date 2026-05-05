---
generated_by: GPT-5
review_status: needs-human-review
---

# Stars And Bars

Stars and bars is a way to count distributions.

The question is usually:

```text
How many ways can we split identical things into different groups?
```

The things are identical.

The groups are distinct.

That is the shape of the problem.

## Start With A Small Example

Suppose we have `$5$` identical stars.

We want to distribute them into `$3$` boxes.

One possible distribution is:

```text
Box 1: **
Box 2: *
Box 3: **
```

Instead of drawing boxes, we can place dividers between the stars:

```text
**|*|**
```

The stars represent the objects.

The bars represent the separations between boxes.

So:

```text
**|*|**
```

means:

$$
(2, 1, 2)
$$

## Empty Boxes Are Allowed

If a box gets nothing, two bars can touch.

For example:

```text
***||**
```

means:

$$
(3, 0, 2)
$$

The empty space between the bars is the empty second box.

So stars and bars naturally counts distributions where zero is allowed.

## Counting The Symbols

For `$5$` stars and `$3$` boxes, we need:

- `$5$` stars
- `$2$` bars

Why only `$2$` bars?

Because `$3$` boxes need `$2$` separations.

So we arrange `$7$` total symbols:

$$
*****||
$$

Every valid distribution is just a choice of where the bars go.

So the number of distributions is:

$$
\binom{7}{2}
$$

Equivalently, choose where the stars go:

$$
\binom{7}{5}
$$

Both are the same because choosing bars automatically determines stars.

## General Form

If we distribute `$n$` identical objects into `$k$` distinct boxes, allowing boxes to be empty, then we need:

- `$n$` stars
- `$k - 1$` bars

Total symbols:

$$
n + k - 1
$$

Choose the positions of the bars:

$$
\binom{n + k - 1}{k - 1}
$$

So:

$$
\text{number of distributions}
=
\binom{n + k - 1}{k - 1}
$$

## If Every Box Must Get At Least One

If every box must get at least one object, give one object to each box first.

That uses `$k$` objects.

Then there are:

$$
n - k
$$

objects left to distribute freely.

So the count becomes:

$$
\binom{(n - k) + k - 1}{k - 1}
$$

which simplifies to:

$$
\binom{n - 1}{k - 1}
$$

## Why The Pattern Continues

The "at least one in every box" version is easier to understand if we start from the minimum.

Suppose we have `$3$` boxes.

If every box must have at least one object, then the smallest possible distribution is:

```text
Box 1: *
Box 2: *
Box 3: *
```

or:

```text
*|*|*
```

This is the base state.

There is no choice yet. Every box only has what it must have.

Now suppose we have extra objects.

Each extra object can be added to any box.

So after the minimum has been paid, the problem becomes:

```text
How do we distribute the remaining objects freely?
```

For example, if there are `$5$` objects and `$3$` boxes, first give one to each box:

```text
*|*|*
```

That uses `$3$` objects.

There are `$2$` extra objects left.

Those extras can continue the pattern by being added anywhere:

```text
***|*|*
```

or:

```text
*|**|**
```

or:

```text
**|*|**
```

The important idea is that the minimum objects make every box valid first.

After that, every extra object is just part of an ordinary stars-and-bars distribution.

So "at least one each" is not a completely different rule.

It is:

```text
give every box the minimum first, then distribute the remaining extras
```

## What This Note Achieves

We started from distributing identical things into distinct boxes.

We replaced the boxes with bars.

We saw that each distribution is really one arrangement of stars and bars.

That turned the problem into choosing positions for the bars.

So the formula is:

$$
\binom{n + k - 1}{k - 1}
$$

when empty boxes are allowed.

When every box needs at least one object, we first put the minimum object in every box, then distribute the remaining objects using the same pattern.
