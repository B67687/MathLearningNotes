---
generated_by: GPT-5
review_status: needs-human-review
---

# Modular Arithmetic

Modular arithmetic is what happens when counting wraps around.

The simplest example is a clock.

After `12`, we do not say `13`.

We go back to `1`.

```text
... 10, 11, 12, 1, 2, 3, ...
```

So modular arithmetic starts from addition.

It asks:

```text
If we keep adding, where do we land in the cycle?
```

## Start With Repeated Addition

Imagine a cycle with five positions:

```text
0 -> 1 -> 2 -> 3 -> 4 -> 0 -> 1 -> 2 -> ...
```

Start at `0`.

Add `1` each time.

```text
0
1
2
3
4
0
1
2
```

The numbers keep growing in ordinary counting:

```text
0, 1, 2, 3, 4, 5, 6, 7
```

But their positions in the five-cycle are:

```text
0, 1, 2, 3, 4, 0, 1, 2
```

So `$7$` lands in the same cycle position as `$2$`.

That is the meaning of:

$$
7 \equiv 2 \pmod{5}
$$

It means:

```text
7 and 2 land on the same position in a cycle of length 5
```

## Same Position In The Cycle

Modulo `$5$` has five positions:

$$
0, 1, 2, 3, 4
$$

Every time we add `$5$`, we go one full cycle and return to the same position.

So:

$$
2 \equiv 7 \equiv 12 \equiv 17 \pmod{5}
$$

These numbers are not the same size.

They are the same position in the cycle.

That is the first meaning of modular arithmetic.

## Complete Cycles And Leftover Steps

Now we can connect this to division.

Take `$17$` in a five-cycle.

Starting from `0`, count `$17$` steps.

Every `$5$` steps makes one complete cycle.

```text
5 steps  -> back to 0
10 steps -> back to 0
15 steps -> back to 0
17 steps -> 2 steps past 15
```

So `$17$` is three complete cycles of `$5$`, plus `$2$` extra steps:

$$
17 = 3 \cdot 5 + 2
$$

The `$2$` is the leftover position.

This is why remainder appears.

Division is not the starting idea here.

The starting idea is repeated addition around a cycle.

Division is just the compressed way to say:

```text
how many full cycles, and how many leftover steps?
```

## Why Addition Works

If two numbers land in the same position, adding the same number to both should keep them together.

For example:

$$
2 \equiv 7 \pmod{5}
$$

Now add `$3$` to both:

$$
2 + 3 = 5
$$

and:

$$
7 + 3 = 10
$$

Both `$5$` and `$10$` land at position `$0$` in a five-cycle.

So:

$$
2 + 3 \equiv 7 + 3 \pmod{5}
$$

Adding the same number moves both positions by the same number of steps.

So if they started together, they stay together.

## Why Subtraction Works

Subtraction is moving backward around the same cycle.

If two numbers are in the same position, moving both backward by the same number of steps keeps them in the same position.

So if:

$$
a \equiv b \pmod{m}
$$

then:

$$
a - c \equiv b - c \pmod{m}
$$

## Why Multiplication Works

Multiplication is repeated addition.

For example:

$$
3 \cdot 4
$$

means:

$$
4 + 4 + 4
$$

So if two numbers land in the same cycle position, adding copies of them the same number of times also lands in the same position.

If:

$$
a \equiv b \pmod{m}
$$

then:

$$
a + a + a \equiv b + b + b \pmod{m}
$$

So:

$$
3a \equiv 3b \pmod{m}
$$

More generally:

$$
ca \equiv cb \pmod{m}
$$

Multiplication works because it is built from addition.

## Why Powers Work

Powers are repeated multiplication.

Multiplication is repeated addition.

So powers still preserve cycle position.

If:

$$
a \equiv b \pmod{m}
$$

then:

$$
a^2 \equiv b^2 \pmod{m}
$$

and:

$$
a^3 \equiv b^3 \pmod{m}
$$

The higher operation works because it is built from the lower operation.

## Why Division Is Dangerous

Division asks us to reverse multiplication.

But reversing multiplication is dangerous because multiplication can merge different positions into the same position.

For example, in modulo `$6$`:

$$
1 \not\equiv 4 \pmod{6}
$$

They are different positions.

Now multiply both by `$2$`:

$$
2 \cdot 1 = 2
$$

and:

$$
2 \cdot 4 = 8
$$

But `$8$` lands in the same position as `$2$` modulo `$6$`.

So:

$$
2 \cdot 1 \equiv 2 \cdot 4 \pmod{6}
$$

Two different starting positions collapsed into one position.

So if we cancel the `$2$`, we would wrongly conclude:

$$
1 \equiv 4 \pmod{6}
$$

which is false.

## When Cancellation Is Safe

Cancellation is safe when multiplying by that number does not collapse different positions together.

This happens when the number we cancel shares no factor with the cycle length.

For example, multiplication by `$5$` modulo `$6$` is safe because `$5$` and `$6$` share no factor except `$1$`.

But multiplication by `$2$` modulo `$6$` is not safe because `$2$` is part of `$6$`.

The shared factor makes the cycle fold onto itself.

In formal words, cancellation by `$c$` is safe modulo `$m$` when:

$$
\gcd(c, m) = 1
$$

## Why This Explains Divisibility Rules

A base-10 number is built by adding place-value pieces.

For example:

$$
4725
=
4 \cdot 10^3
+
7 \cdot 10^2
+
2 \cdot 10
+
5
$$

If we are working modulo `$3$`, then:

$$
10 \equiv 1 \pmod{3}
$$

So every power of `$10$` also lands where `$1$` lands:

$$
10^2 \equiv 1^2 \pmod{3}
$$

$$
10^3 \equiv 1^3 \pmod{3}
$$

That means every place value acts like `$1$`.

So the number acts like the sum of its digits.

That is why divisibility by `$3$` and `$9$` can be checked through digit sums.

## What This Note Achieves

We started from repeated addition around a cycle.

We saw that congruence means landing in the same cycle position.

Then division appeared as a compressed way to count complete cycles and leftover steps.

We saw why addition, subtraction, multiplication, and powers preserve cycle position.

We also saw why division and cancellation need extra care.

This gives the language needed to reprove divisibility rules instead of memorizing them.
