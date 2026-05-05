---
title: "The Composition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-2.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# The Composition of a Number

This is the structure of a number

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

Notice that `10` can be `partitioned` into just one part that contains `2`

$$
\boxed{
    \phantom{\big(}
    10 = 2 \cdot 5
    \phantom{\big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
\boxed{
    \phantom{\big(}
    100 = 2 \cdot 50
    \phantom{\big)}
}
$$

Similarly, when we move on to the next power, we have

$$
\boxed{
    \phantom{\big(}
    1000 = 2 \cdot 500
    \phantom{\big)}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `1st power onwards` up to some `n`

$$
\begin{align}
    10 &= 2 \cdot 5 \\
    100 &= 2 \cdot 50 \\
    1000 &= 2 \cdot 500 \\
    &\vdots \\
    10^{n} &= 2 \biggr( 5 \cdot 10^{n-1} \biggr)
\end{align}
$$

Thus, the general expression is

$$
\boxed{
    \phantom{\Big(}
    10^{n} = 2 \biggr( 5 \cdot 10^{n-1} \biggr)
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

Since we know that every `power of 10` from the `1st power onwards` will be `divisible by 2`

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space c \space b \space \textcolor{lightgray}{a}}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} \textcolor{lightgray}{+
\underline{a \cdot 10^{0}}}
$$

We just need to check whether the `ones place` is `divisible by 2`

$$
\text{Number} = \underbrace{\overline{\textcolor{lightgray}{k \space m \space \cdots \space c \space b} \space a}}_{\text{n places}} =
\textcolor{lightgray}{\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}}} +
\underline{a \cdot 10^{0}}
$$

# Multiples of 2

There are only `5 digits` that is a `multiple of 2`:

$$
\begin{align}
    0 &: \space \text{As it is a 0-th multiple of all numbers} \\
    2 &: \space \text{The 1st multiple of 2} \\
    4 &: \space \text{The 2nd multiple of 2} \\
    6 &: \space \text{The 3rd multiple of 2} \\
    8 &: \space \text{The 4th multiple of 2} \\
\end{align}
$$

All the other `multiples of 2` are `too big` to be a `positive single digit`

# Divisibility Rule

Thus, to determine if a number is `divisible by 2`

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The digit in the ones place has to be either of: 0, \ 2, \ 4, \ 6, \ 8}
    \phantom{\biggr)}
}
$$

Or in other words

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The digit in the ones place is an even number}
    \phantom{\biggr)}
}
$$
