---
title: "The Composition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-powers-of-2.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/number-theory/divisibility/divisibility-by-powers-of-2.ipynb"
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

Notice that `10` can be `partitioned` into `2` and `5`

$$
\boxed{
    \phantom{\big(}
    10 = 2 \cdot 5
    \phantom{\big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
100 = \biggr( 2 \cdot 5 \biggr) \cdot \boxed{10}
$$

Noticing the `10` in the partition, we can split it like how we did before

$$
100 = \biggr( 2 \cdot 5 \biggr) \cdot \biggr( 2 \cdot 5 \biggr)
$$

And then we get

$$
\boxed{
    \phantom{\big(}
    100 = 2^2 \cdot 5^2
    \phantom{\big)}
}
$$

This works when we move on to the next power,

$$
1000 = \biggr( 2^2 \cdot 5^2 \biggr) \cdot \boxed{10}
$$

Split it
$$
1000 = \biggr( 2^2 \cdot 5^2 \biggr) \cdot \biggr( 2 \cdot 5 \biggr)
$$


And then we get
$$
\boxed{
    \phantom{\big(}
    1000 = 2^3 \cdot 5^3
    \phantom{\big(}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `2nd power onwards` up to some `n`

$$
\begin{align}
    10 &= 2 \cdot 5 \\
    100 &= 2^2 \cdot 5^2 \\
    1000 &= 2^3 \cdot 5^3 \\
    &\vdots \\
    10^n &= 2^n \cdot 5^n \\
\end{align}
$$

Thus, the overall expression is

$$
\boxed{
    \phantom{\Big(}
    10^n = 2^n \cdot 5^n
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

Since we know that every `power of 10` from the `t-th power onwards` will be `divisible by` $2^t$

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space h \space \textcolor{lightgray}{\cdots \space c \space b \space a}}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{h \cdot 10^{t}} \textcolor{lightgray}{+
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}}
$$

We just need to check whether the number up to the `(t-1)-th place` is `divisible by` $2^t$

$$
\text{Number} = \underbrace{\overline{\textcolor{lightgray}{k \space m \space \cdots \space h} \space \cdots \space c \space b \space a}}_{\text{n places}} =
\textcolor{lightgray}{\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{h \cdot 10^{t}}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

# Rule of Divisibility by Powers of 2

$$
\boxed{
    \phantom{\biggr(}
    \textbf{The number up to the (t-1)-th place is divisible by} \ 2^t
    \phantom{\biggr)}
}
$$

> **Visualised**

$$
\text{Number} = \underbrace{\overline{\textcolor{lightgray}{k \space m \space \cdots \space h \space} \cdots \space c \space b \space a}}_{\text{n places}} =
\textcolor{lightgray}{\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{h \cdot 10^{t}}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$
