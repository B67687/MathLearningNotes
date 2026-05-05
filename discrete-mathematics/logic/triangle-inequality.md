---
generated_by: GPT-5
review_status: needs-human-review
---

# Triangle Inequality

The triangle inequality is not first a formula.

It is first a fact about paths.

Between two dots, the straight path is the shortest path.

Everything else is a reroute.

## Start With Two Dots

Imagine two points:

```text
Start ---------------- End
```

The straight path from `Start` to `End` is the direct distance.

There is no unnecessary turning.

There is no detour.

This is the shortest possible way to travel from the first dot to the second dot.

## Add A Third Dot

Now add a third point somewhere else:

```text
          Third
         /     \
        /       \
Start ----------- End
```

If we force the route to pass through `Third`, then the path becomes:

```text
Start -> Third -> End
```

This is no longer the direct path.

It is a reroute.

So it cannot be shorter than the straight path:

$$
\text{Start to End}
\leq
\text{Start to Third}
+
\text{Third to End}
$$

## The Triangle Appears

The three dots form a triangle.

The direct path from `Start` to `End` is one side of the triangle.

The reroute is made from the other two sides:

$$
\text{one side}
\leq
\text{other side}
+
\text{other side}
$$

That is the triangle inequality.

## Why The Equal Sign Exists

For a meaningful triangle, the third dot is not on the same straight path between the first two dots.

Then the reroute is strictly longer.

$$
\text{Start to End}
<
\text{Start to Third}
+
\text{Third to End}
$$

The equal sign exists for edge cases.

For example, if the third dot is exactly on the straight path, then going through it does not create a real detour.

```text
Start ---- Third ---- End
```

Then:

$$
\text{Start to End}
=
\text{Start to Third}
+
\text{Third to End}
$$

Another edge case is when the third dot is the same as `Start` or the same as `End`.

Then one part of the reroute has length `$0$`, so equality is also possible.

## Turning This Into Symbols

Let the direct path have length `$C$`.

Let the reroute pieces have lengths `$A$` and `$B$`.

Since the direct path is shortest:

$$
C \leq A + B
$$

or equivalently:

$$
A + B \geq C
$$

The formula is just saying:

```text
reroute length >= direct path length
```

## Why Absolute Values Appear

In algebra, absolute value is distance.

So when we write:

$$
|a + b| \leq |a| + |b|
$$

we are saying the same thing.

`$|a + b|$` is the direct displacement after combining the movement.

`$|a| + |b|$` is the route where we travel the two movements separately.

The final direct displacement cannot be longer than the whole route.

## What This Note Achieves

We started from the simplest geometric intuition: the straight path between two dots is shortest.

We added a third dot and forced the path to reroute through it.

That reroute formed the two-side path of a triangle.

So the sum of two sides must be at least the remaining side.

For meaningful triangles, it is strictly longer. The equal sign belongs to the edge cases.
