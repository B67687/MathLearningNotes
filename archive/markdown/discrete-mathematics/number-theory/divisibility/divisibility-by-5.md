---
title: "The Composition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-5.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/number-theory/divisibility/divisibility-by-5.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# The Composition of a Number

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

Lets look into the `powers of 10`

# Factoring Powers of 10

Lets start from $10^0$
- Which equals `1`

$$
10^{0} = 1
$$

We cannot `partition` nor `factor` this that so lets move on to $10^1$

## Intentional Partitioning

Notice that `10` can be `partitioned` into `2 fives`

$$
\boxed{
    \phantom{\Big(}
    10 = 5 \cdot 2
    \phantom{\Big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
\boxed{
    \phantom{\Big(}
    100 = 5 \cdot 20
    \phantom{\Big)}
}
$$

Noticing the `10` in the partition, we can split it like how we did before

$$
\boxed{
    \phantom{\Big(}
    1000 = 5 \cdot 200
    \phantom{\Big)}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `1st power onwards` up to some `n`

$$
\begin{align}
    10 &= 5 \cdot 2 \\
    100 &= 5 \cdot 20 \\
    1000 &= 5 \cdot 200 \\
    &\vdots \\
    10^{n} &= 5 \biggr( 2 \cdot 10^{n-1} \biggr)
\end{align}
$$

Thus, the general expression is

$$
\boxed{
    \phantom{\Big(}
    10^{n} = 5 \biggr( 2 \cdot 10^{n-1} \biggr)
    \phantom{\Big)}
}
$$

# Going by the Structure

Lets look back at the number again

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

## Divisible by Place

Since we know that every `power of 10` from the `1st power onwards` will be `divisible by 5`

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space c \space b \space \textcolor{lightgray}{a}}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} \textcolor{lightgray}{+
\underline{a \cdot 10^{0}}}
$$

We just need to check whether the `ones place` is `divisible by 5`

$$
\text{Number} = \underbrace{\overline{\textcolor{lightgray}{k \space m \space \cdots \space c \space b} \space a}}_{\text{n places}} =
\textcolor{lightgray}{\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}}} +
\underline{a \cdot 10^{0}}
$$

# Multiples of 5

There are only `2 digits` that is a `multiple of 5`:

$$
\begin{align}
    0 &: \space \text{As it is a 0-th multiple of all numbers} \\
    5 &: \space \text{The 1st multiple of 5}
\end{align}
$$

All the other `multiples of 5` are `too big` to be a `positive single digit`

# Divisibility Rule

Thus, to determine if a number is `divisible by 5`

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The digit in the ones place has to be 0 or 5}
    \phantom{\biggr)}
}
$$
