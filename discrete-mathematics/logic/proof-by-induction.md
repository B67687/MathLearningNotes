---
generated_by: GPT-5
review_status: needs-human-review
---

# Proof By Induction

Proof by induction is a way of proving infinitely many statements by making them fall like dominoes.

The idea is not just:

$$
P(1) \Rightarrow P(2) \Rightarrow P(3) \Rightarrow \cdots
$$

The real idea is:

1. The first statement is true.
2. Any true statement can push the next one to be true.

If both are true, then the whole chain has no place to break.

## Start With A Row Of Statements

Suppose we have one statement for each positive integer:

$$
P(1), P(2), P(3), P(4), \ldots
$$

For example:

$$
1 + 2 + 3 + \cdots + n = \frac{n(n + 1)}{2}
$$

This is not one statement.

It is a whole family of statements, one for every `$n$`.

When `$n = 1$`:

$$
1 = \frac{1(1 + 1)}{2}
$$

When `$n = 2$`:

$$
1 + 2 = \frac{2(2 + 1)}{2}
$$

When `$n = 3$`:

$$
1 + 2 + 3 = \frac{3(3 + 1)}{2}
$$

Induction is used when we want to prove the whole chain at once.

## The First Domino

First, we check the starting case.

For:

$$
1 + 2 + 3 + \cdots + n = \frac{n(n + 1)}{2}
$$

the first case is `$n = 1$`.

Left side:

$$
1
$$

Right side:

$$
\frac{1(1 + 1)}{2} = 1
$$

So `$P(1)$` is true.

The first domino is standing in the right place.

## The Push From One Case To The Next

Now we do not try to prove `$P(2)$`, `$P(3)$`, `$P(4)$`, and so on one by one.

Instead, we prove this:

If `$P(k)$` is true, then `$P(k + 1)$` must be true.

So we temporarily assume:

$$
1 + 2 + 3 + \cdots + k = \frac{k(k + 1)}{2}
$$

This is called the induction hypothesis.

It is not pretending the whole result is true.

It is asking:

If the `$k$`-case has already been reached, can it force the next case?

## Building The Next Case

The next case is:

$$
1 + 2 + 3 + \cdots + k + (k + 1)
$$

But the first part is already the `$k$`-case:

$$
1 + 2 + 3 + \cdots + k
$$

By the induction hypothesis, we can replace that part:

$$
1 + 2 + 3 + \cdots + k + (k + 1)
=
\frac{k(k + 1)}{2} + (k + 1)
$$

Now factor out the common `$(k + 1)$`:

$$
\frac{k(k + 1)}{2} + (k + 1)
=
(k + 1)\left(\frac{k}{2} + 1\right)
$$

$$
=
(k + 1)\left(\frac{k + 2}{2}\right)
$$

$$
=
\frac{(k + 1)(k + 2)}{2}
$$

This is exactly the formula for the next case:

$$
\frac{(k + 1)((k + 1) + 1)}{2}
$$

So `$P(k)$` forces `$P(k + 1)$`.

## Why This Proves Everything

We proved:

- `$P(1)$` is true.
- If `$P(k)$` is true, then `$P(k + 1)$` is true.

So `$P(1)$` pushes `$P(2)$`.

Then `$P(2)$` pushes `$P(3)$`.

Then `$P(3)$` pushes `$P(4)$`.

And this never stops.

So all positive integer cases are true.

## What Induction Is Really Checking

Induction checks that there is:

- a starting point
- a reliable next-step machine

If the starting point is missing, nothing begins.

If the next-step machine is broken, the chain can stop.

But if both exist, then every later statement is reached.

## What This Note Achieves

We started from a family of statements.

We proved the first statement.

We proved that any reached statement forces the next one.

That is why induction can prove infinitely many integer-indexed statements with only two checks.
