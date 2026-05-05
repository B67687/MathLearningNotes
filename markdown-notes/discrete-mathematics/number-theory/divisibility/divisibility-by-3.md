---
title: "The Composition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-3.ipynb"
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

Notice that `10` can be `partitioned` into a part that contains `3`, and another that is `1`

$$
\boxed{
    \phantom{\big(}
    10 = 3^2 + 1}
    \phantom{\big)}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
100 = 3^2 \cdot 10 + \boxed{10}
$$

Noticing the `10` in the partition, we can split it like how we did before

$$
\boxed{
    \phantom{\big(}
    100 = 3^2 \cdot 10 + 3^2 + 1
    \phantom{\big)}
}
$$

Similarly, when we move on to the next power,

$$
1000 = 3^2 \cdot 100 + 3^2 \cdot 10 + 10
$$

We can do this

$$
\boxed{
    \phantom{\big(}
    1000 = 3^2 \cdot 100 + 3^2 \cdot 10 + 3^2 + 1
    \phantom{\big)}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `1st power onwards` up to some `n`

$$
\begin{align}
    10 &= 3^2 + 1 \\
    100 &= 3^2 \cdot 10 + 3^2 + 1 \\
    1000 &= 3^2 \cdot 100 + 3^2 \cdot 10 + 3^2 + 1 \\
    &\vdots \\
    10^{n} &= 3^2 \cdot 10^{n-1} + 3^2 \cdot 10^{n-2} + \cdots + 3^2 \cdot 10^{1} + 3^2 \cdot 10^{0} + 1
\end{align}
$$

We can group the `general expression` in terms of $3^2$

$$
10^{n} = 3^2 \space \Big( 10^{n-1} + 10^{n-2} + \cdots + 10^{1} + 10^{0} \Big) + 1
$$

Notice that this is actually `1 of each place` up to the `n-th place`

$$
\textcolor{lightgray}{
    10^{n} = 3^2 \space}
    \Big( 10^{n-1} + 10^{n-2} + \cdots + 10^{1} + 10^{0} \Big)
    \textcolor{lightgray}{+}
    \textcolor{lightgray}{1}
$$

Thus, when we express it `number form`, we get

$$
\boxed{
    10^{n} = 9 \cdot \underbrace{\overline{11\cdots11}}_{\text{n digits}} + 1
}
$$

Re-group by `Multiple of 3` and we get

$$
\boxed{
    10^{n} = 3 \cdot \underbrace{\overline{33\cdots33}}_{\text{n digits}} + 1
}
$$

# Factoring the Number

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

Since we know this

$$
10^{n} = 3 \cdot \underbrace{ \overline{33\cdots33}}_{\text{n digits}} + 1
$$

We factor it in

$$
\text{Number} =
k \biggr( 3 \cdot \underbrace{ \overline{33\cdots33}}_{\text{n-1 digits}} + 1 \biggr) +
m \biggr( 3 \cdot \underbrace{ \overline{33\cdots33}}_{\text{n-2 digits}} + 1 \biggr) +
\cdots +
c \Biggr( 3 \cdot 33 + 1 \Biggr) +
b \Biggr( 3 \cdot 3 + 1 \Biggr) +
a \Biggr(1 \Biggr)
$$

Let the numbers with repeating digits be expressed like so

$$
q_{n} = \underbrace{\overline{33\cdots33}}_{\text{n digits}}
$$

Then we have,

$$
\text{Number} =
k \biggr( 3q_{n-1} + 1 \biggr) +
m \biggr( 3q_{n-2} + 1 \biggr) +
\cdots +
c \Biggr( 3q_{2} + 1 \Biggr) +
b \Biggr( 3q_{1} + 1 \Biggr) +
a \Biggr(1 \Biggr)
$$

Simplify it, and we get

$$
\text{Number} =
\boxed{ \phantom{\biggr(} 3k \cdot q_{n-1} + k \phantom{\biggr)}} +
\boxed{ \phantom{\biggr(} 3m \cdot q_{n-2} + m \phantom{\biggr)}} +
\cdots +
\boxed{\phantom{\biggr(} 3c \cdot q_{2} + c \phantom{\biggr)}}  +
\boxed{\phantom{\biggr(} 3b \cdot q_{1} + b \phantom{\biggr)}} +
\boxed{\phantom{\biggr(} a \phantom{\biggr)}}
$$

Regroup it like so

$$
\text{Number} =
\biggr(
    3k \cdot q_{n-1} +
    3m \cdot q_{n-2} +
    \cdots +
    3c \cdot q_{2} +
    3b \cdot q_{1}
\biggr) +
\big(
    k + m + \cdots + c + b + a
\big)
$$

And factor out the constant `3` and we get

$$
\boxed{
    \text{Number} =
    3 \biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        cq_{2} +
        bq_{1}
    \biggr) +
    \big(
        k + m + \cdots + c + b + a
    \big)
}
$$

# Analysis of Remainder

Thus, we see that `this part` of the number is a `multiple of 3`
- Thus making it `divisible by 3`

$$
\textcolor{lightgray}{\text{Number} = }
3 \biggr(
    kq_{n-1} +
    mq_{n-2} +
    \cdots +
    cq_{2} +
    bq_{1}
\biggr)
\textcolor{lightgray}{+
\big( k + m + \cdots + c + b + a \big)}
$$

Thus for the `whole number to be divisible by 3`,  this part also has to be a `multiple of 3`

$$
\textcolor{lightgray}{\text{Number} =
3 \biggr(
    kq_{n-1} +
    mq_{n-2} +
    \cdots +
    cq_{2} +
    bq_{1}
\biggr)} +
\big( k + m + \cdots + c + b + a \big)
$$

Realise that it contains `all the digits of the number itself in order`

$$
\text{Number} \space = \space \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}}
$$

# Divisibility by 3

Thus, to determine if the `whole number is divisible by 3`,

$$
\boxed{
    \phantom{\biggr(}
        \textbf{Sum of all its the digits is a multiple of 3}
    \phantom{\biggr)}
}
$$

# Recursive Iteration

Thus, since the sum of the `digits of a number` is always `equal or smaller than the number` itself

---

We can add the digits of the original number, and see if we know it is `divisible by 3`
- If it is not clear, we can `add the digits of that sum` and determine whether the `sum of the digits of that sum` is `divisible by 3`


> We can repeat this operation `until it is obvious` that `one of the iteration of the sum of digits` is `divisible by 3`!
