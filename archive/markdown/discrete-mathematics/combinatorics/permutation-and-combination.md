---
title: "Permutation And Combination"
source_notebook: "discrete-mathematics/combinatorics/permutation-and-combination.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/combinatorics/permutation-and-combination.ipynb"
original_human_author: B67687
polished_by: GPT-5
review_status: needs-human-review
canonical_status: draft-canonical
---

# Permutation And Combination

This note explains permutation and combination from the act of choosing.

By the end, we should understand:

- what it means for one object to be chosen
- why order creates extra copies of the same group
- why permutation counts ordered choices
- why combination counts unordered choices
- why the edge cases are not random exceptions

## Start With One Thing

Suppose there is one object:

```text
A
```

There are only two possibilities.

We choose it:

```text
[A]
```

Or we do not choose it:

```text
 A
```

So choosing begins with a yes-or-no action on an object.

When there are many objects, choosing means deciding which objects enter the selected group.

For example, from:

```text
A  B  C  D
```

we might choose:

```text
[A] [C]
```

The selected group is:

```text
A, C
```

At this point, there is no order yet.

It is just the fact that `A` and `C` were chosen.

## A Group Is Not The Same As A Row

This is the first important split.

A group only cares about membership:

```text
{A, C}
```

A row cares about position:

```text
A C
```

and:

```text
C A
```

are different rows.

But they are the same group.

Both rows use the same chosen objects:

```text
{A, C}
```

So before we count anything, we must ask:

```text
Do positions matter?
```

If positions matter, we count arrangements.

If positions do not matter, we count groups.

## Filling Ordered Slots

Suppose we have $n$ distinct objects.

We want to fill $r$ ordered slots.

For example, if $r = 3$, the shape is:

```text
slot 1   slot 2   slot 3
  ___      ___      ___
```

For the first slot, any of the $n$ objects can be used:

```text
n choices
```

After we use one object, it cannot be used again.

So for the second slot, there are only $n - 1$ choices:

```text
n choices, then n - 1 choices
```

For the third slot, there are $n - 2$ choices:

```text
n choices, then n - 1 choices, then n - 2 choices
```

The pattern continues until $r$ slots are filled.

So the ordered count is:

$$
n(n - 1)(n - 2)\cdots(n - r + 1)
$$

The last term is $n - r + 1$ because the first term is $n - 0$, the second is $n - 1$, and after $r$ terms we have subtracted $r - 1$.

## Why Factorials Appear

The factorial $n!$ means:

$$
n! = n(n - 1)(n - 2)\cdots 3 \cdot 2 \cdot 1
$$

It is the number of ways to arrange all $n$ distinct objects in a row.

But if we only want $r$ slots, we only want the first $r$ falling factors:

$$
n(n - 1)(n - 2)\cdots(n - r + 1)
$$

We can get this from $n!$ by removing the unused tail:

$$
\frac{n!}{(n-r)!}
$$

Why division?

Because factorials are multiplied chains.

To remove a multiplied tail, we divide by that tail.

So:

$$
n(n - 1)(n - 2)\cdots(n - r + 1)
=
\frac{n!}{(n-r)!}
$$

## Permutation

This ordered count is called a permutation.

Permutation counts ways to choose and arrange $r$ distinct objects from $n$ distinct objects.

The usual notation is:

$$
{}^nP_r
$$

So:

$$
{}^nP_r
=
n(n - 1)(n - 2)\cdots(n - r + 1)
=
\frac{n!}{(n-r)!}
$$

Permutation is the right count when the slots have meaning.

For example:

```text
1st place, 2nd place, 3rd place
```

Here:

```text
A B C
```

and:

```text
C B A
```

are different outcomes.

The same people appear, but they occupy different positions.

## When Order Does Not Matter

Now suppose we only care about the chosen group.

From:

```text
A  B  C  D
```

choosing `A` and `C` gives the group:

```text
{A, C}
```

But permutation would count both:

```text
A C
C A
```

Those are two ordered rows.

They are not two different groups.

So permutation overcounts the group.

## How Much Does Permutation Overcount?

If a group has $r$ objects, then the same group can be arranged in:

$$
r!
$$

orders.

For example, the group:

```text
{A, B, C}
```

can appear as:

```text
A B C
A C B
B A C
B C A
C A B
C B A
```

That is $3! = 6$ rows.

But it is still one group:

```text
{A, B, C}
```

So if permutation counts every group $r!$ times, then the group count is:

$$
\frac{\text{ordered count}}{r!}
$$

That gives:

$$
\frac{{}^nP_r}{r!}
$$

Substitute the permutation formula:

$$
\frac{1}{r!}\cdot\frac{n!}{(n-r)!}
$$

So:

$$
\frac{n!}{r!(n-r)!}
$$

## Combination

This unordered count is called a combination.

Combination counts ways to choose $r$ distinct objects from $n$ distinct objects, where order does not matter.

The usual notation is:

$$
{}^nC_r
$$

or:

$$
\binom{n}{r}
$$

So:

$$
{}^nC_r
=
\binom{n}{r}
=
\frac{{}^nP_r}{r!}
=
\frac{n!}{r!(n-r)!}
$$

Combination is the right count when the selected group is all that matters.

For example:

```text
Choose 3 people for a team.
```

There is no $1^{\text{st}}$ teammate, $2^{\text{nd}}$ teammate, or $3^{\text{rd}}$ teammate.

There is only the team.

## Edge Cases

Edge cases are not strange.

They come directly from what choosing means.

### Choosing Nothing

There is exactly one way to choose nothing:

```text
choose no objects
```

So:

$$
\binom{n}{0} = 1
$$

This is not saying nothing is an object.

It is saying there is one empty choice.

### Choosing Everything

There is exactly one way to choose all $n$ objects:

```text
choose every object
```

So:

$$
\binom{n}{n} = 1
$$

### Choosing More Than Exists

If there are $n$ objects, we cannot choose $n + 1$ objects without reusing something.

So:

$$
\binom{n}{r} = 0
\quad\text{when}\quad
r > n
$$

### Choosing A Negative Number Of Things

Choosing begins from zero selected objects.

To choose fewer than zero objects would mean removing objects from a selection that does not exist yet.

That is not a valid choosing action.

So:

$$
\binom{n}{r} = 0
\quad\text{when}\quad
r < 0
$$

### The Valid Range

For ordinary combinations, the meaningful range is:

$$
0 \le r \le n
$$

Inside this range, choosing is valid.

Outside this range, there is no valid group to count.

## Repetition Changes The Question

Everything above assumes distinct objects and no repeated use.

That means after an object is chosen, it is gone from the available objects.

If repeated use is allowed, the problem changes.

For ordered slots:

```text
slot 1   slot 2   slot 3
  ___      ___      ___
```

each slot still has $n$ choices.

So the count becomes:

$$
n^r
$$

For unordered groups with repetition allowed, the problem becomes a distribution problem:

```text
How many of each object type did we choose?
```

That is the shape counted by stars and bars.

## Quick Decision Guide

Ask these questions in order.

First:

```text
Are the objects distinct?
```

Then:

```text
Can an object be used more than once?
```

Then:

```text
Does order matter?
```

For the basic distinct, no-repeat cases:

| Question | Count |
|---|---|
| Order matters | ${}^nP_r = \dfrac{n!}{(n-r)!}$ |
| Order does not matter | $\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ |

## What This Note Achieves

We started from one object being chosen or not chosen.

Then we separated two ideas:

- a selected group
- an ordered row

Filling ordered slots gave the falling product:

$$
n(n - 1)(n - 2)\cdots(n - r + 1)
$$

That is permutation.

Then we noticed that each unordered group appears $r!$ times among the ordered rows.

Dividing by those repeated internal arrangements gave:

$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

That is combination.
