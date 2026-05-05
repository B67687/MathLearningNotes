---
generated_by: GPT-5
review_status: needs-human-review
---

# Circular Arrangements

Circular arrangements are arrangements where turning the whole thing does not create something new.

The key difference is this:

```text
Line:   positions are named by left, middle, right
Circle: positions are only named by who is next to who
```

In a line, the first position is real.

In a circle, the first position is chosen by the reader.

## Start With A Line

Suppose we arrange four people in a line:

```text
A B C D
```

This is different from:

```text
B C D A
```

because the leftmost position changed.

So in a line, every position has a fixed meaning:

```text
1st  2nd  3rd  4th
 A    B    C    D
```

That is why four distinct people in a line have:

$$
4!
$$

arrangements.

## Put The Same Order Around A Circle

Now put the same people around a circle:

```text
      A
   /     \
 D       B
   \     /
      C
```

If we start reading at `A`, we get:

```text
A B C D
```

If we start reading at `B`, we get:

```text
B C D A
```

If we start reading at `C`, we get:

```text
C D A B
```

If we start reading at `D`, we get:

```text
D A B C
```

These are not four different circles.

They are the same circle read from four different starting points.

## Rotation Is Not A New Arrangement

Rotation means turning the whole circle.

For example:

```text
      A                 B
   /     \           /     \
 D       B    ->   A       C
   \     /           \     /
      C                 D
```

Nobody changed neighbors.

`A` is still next to `B` and `D`.

`B` is still next to `A` and `C`.

The whole circle only turned.

So rotations are the same circular arrangement.

## Why We Divide By n

For `$n$` distinct objects, every circular arrangement can be read from `$n$` starting points.

So the line count `$n!$` counts each circle `$n$` times.

Therefore:

$$
\text{circular arrangements}
=
\frac{n!}{n}
$$

which simplifies to:

$$
(n - 1)!
$$

## Fixing One Object

Another way to remove the repeated rotations is to fix one object.

For example, keep `A` at the top:

```text
      A
   /     \
 ?       ?
   \     /
      ?
```

Now only `B`, `C`, and `D` move around `A`.

There are:

$$
3!
$$

ways to arrange them.

For `$n$` people, fixing one person leaves:

$$
(n - 1)!
$$

arrangements.

The fixed person is not special in the real problem.

They are only used as a reference point so we stop counting the same circle again and again.

## Reflection Is A Different Question

Rotation means turning the circle.

Reflection means flipping it over like a mirror.

Start with:

```text
      A
   /     \
 D       B
   \     /
      C
```

Read clockwise from `A`:

```text
A B C D
```

Now reflect the circle:

```text
      A
   /     \
 B       D
   \     /
      C
```

Read clockwise from `A`:

```text
A D C B
```

This is the reverse order.

So reflection changes clockwise order into anticlockwise order.

## When Reflection Counts As Different

For people sitting around a table, reflection is usually different.

Why?

Because we can rotate the table in our imagination, but we cannot flip everyone through the table.

The order:

```text
A B C D
```

around the table is different from:

```text
A D C B
```

because `B` and `D` swapped sides around `A`.

So for a normal circular table, we usually only remove rotations.

The count is:

$$
(n - 1)!
$$

## When Reflection Counts As The Same

For a necklace or bracelet, reflection may be the same.

Why?

Because if you pick up the necklace and flip it over, the clockwise order becomes the anticlockwise order.

The object itself can be physically reversed.

So:

```text
A B C D
```

and:

```text
A D C B
```

may represent the same necklace.

For `$n \geq 3$` distinct beads, if rotations and reflections are both considered the same, then each circular order is counted twice after removing rotations:

- once clockwise
- once anticlockwise

So the count becomes:

$$
\frac{(n - 1)!}{2}
$$

## The Question To Ask

For every circular arrangement problem, ask two questions:

```text
If I rotate it, is it the same?
If I flip it over, is it the same?
```

For circular tables:

```text
rotation same, reflection different
```

For necklaces:

```text
rotation same, reflection same
```

That is the whole difference.

## What This Note Achieves

We started from line arrangements.

We saw that a circle has no natural first position.

So every circular order is counted once for every possible starting point.

That is why arranging `$n$` distinct objects in a circle gives:

$$
(n - 1)!
$$

Then we separated rotation from reflection.

Rotation only changes where we start reading.

Reflection reverses the order.

Whether reflection counts as the same depends on whether the object can be flipped over in the problem.
