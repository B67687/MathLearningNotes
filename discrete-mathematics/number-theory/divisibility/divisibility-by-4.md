---
title: "The Composition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-4.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/number-theory/divisibility/divisibility-by-4.ipynb"
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

Notice that `10` can be `partitioned` into a `quotient that contains 4`, and the `remainder that is 2`

$$
\boxed{
    \phantom{\big(}
        10 = 4 \cdot 2 + 2
    \phantom{\big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
100 = 4 \cdot 2 \cdot 10 + 2 \cdot \boxed{10}
$$

Noticing the `10` in the partition, we can split it like how we did before

$$
\begin{align}
    100 &= 4 \cdot 2 \cdot 10 + \underline{2 \space \big( 4 \cdot 2 + 2 \big)} \\
    &= 4 \cdot 2 \cdot 10 + 4 \cdot 2^2 + 2^2 \\
\end{align}
$$

Thus,

$$
\boxed{
    \phantom{\big(}
        100 = 4 \cdot 2 \cdot 10 + 4 \cdot 2^2 + 2^2
    \phantom{\big)}
}
$$

This works when we move on to the next power,

$$
1000 = 4 \cdot 2 \cdot 10^2 + 4 \cdot 2^2 \cdot 10 + 2^2 \cdot \boxed{10}
$$

We can simplify like how we did before

$$
\begin{align}
    1000 &= 4 \cdot 2 \cdot 10^2 + 4 \cdot 2^2 \cdot 10 + 2^2 \cdot \big( 4 \cdot 2 + 2 \big) \\
    &= 4 \cdot 2 \cdot 10^2 + 4 \cdot 2^2 \cdot 10 + 4 \cdot 2^3 + 2^3
\end{align}
$$

$$
\boxed{
    \phantom{\big(}
        1000 = 4 \cdot 2 \cdot 10^2 + 4 \cdot 2^2 \cdot 10 + 4 \cdot 2^3 + 2^3
    \phantom{\big)}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `2nd power onwards` up to some `n`

$$
\begin{align}
    10 &= 4 \cdot 2 + 2 \\
    100 &= 4 \cdot 2 \cdot 10 + 4 \cdot 2^2 + 2^2 \\
    1000 &= 4 \cdot 2 \cdot 10^2 + 4 \cdot 2^2 \cdot 10 + 4 \cdot 2^3 + 2^3 \\
    &\vdots \\
    10^n &= 4 \cdot 2^1 \cdot 10^{n-1} + 4 \cdot 2^2 \cdot 10^{n-2} + \cdots + 4 \cdot 2^{n} \cdot 10^{0} + 2^n \\
\end{align}
$$

Thus, the overall expression is

$$
\boxed{
    \phantom{\Big(}
        10^n = 4 \biggr( 2^1 \cdot 10^{n-1} + 2^2 \cdot 10^{n-2} + \cdots + 2^{n} \cdot 10^{0} \biggr) + 2^n
    \phantom{\Big)}
}
$$

# Special Condition That Covers Almost Every Condition

Notice that we have $2^n$

$$
\textcolor{lightgray}{
    4
    \biggr( 2^1 \cdot 10^{n-1} + 2^2 \cdot 10^{n-2} + \cdots + 2^{n} \cdot 10^{0} \biggr)
} + 2^{n}
$$

And `4` is also $2^2$

$$
2^2
\textcolor{lightgray}{
    \biggr( 2^1 \cdot 10^{n-1} + 2^2 \cdot 10^{n-2} + \cdots + 2^{n} \cdot 10^{0} \biggr)
} + 2^{n}
$$

Thus, we have can do this

> As long as $n \ge 2$

$$
2^2 \space \biggr( 2^1 \cdot 10^{n-1} + 2^2 \cdot 10^{n-2} + \cdots + 2^{n} \cdot 10^{0} \biggr) + 2^{2} \cdot 2^{n-2}
$$

Then we can also group the `power of 2 expression` into the `multiple of 4`
> Allowing it to become `1 expression` of `multiple of 4`

$$
2^2 \space \biggr( 2^1 \cdot 10^{n-1} + 2^2 \cdot 10^{n-2} + \cdots + 2^{n} \cdot 10^{0} + 2^{n-2} \biggr)
$$

Thus, the general expression for
> Where $n \ge 2$

$$
\underline{
    \phantom{\Biggr(}
        10^{n} = 4 \biggr( 2^1 \cdot 10^{n-1} + 2^2 \cdot 10^{n-2} + \cdots + 2^{n} \cdot 10^{0} + 2^{n-2} \biggr)
    \phantom{\Biggr)}
}
$$

# Application of General Expressions

We can basically use this expression for almost every `power of 10`

> As long as $n \ge 2$
>
> $$
\boxed{
    \phantom{\Biggr(}
        10^{n} = 4 \biggr( 2^1 \cdot 10^{n-1} + 2^2 \cdot 10^{n-2} + \cdots + 2^{n} \cdot 10^{0} + 2^{n-2} \biggr)
    \phantom{\Biggr)}
}
$$
>
> Then for $n = 1$, we have
>
> $$
\boxed{
    \phantom{\big(}
    10^1 = 4 \cdot 2 + 2
    \phantom{\big)}
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

Since we know that every `power of 10` from the `2nd power onwards` will be `divisible by 4`

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space c \space \textcolor{lightgray}{b \space a}}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} \textcolor{lightgray}{+
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}}
$$

We just need to check whether the number up to the `tens place` is `divisible by 4`

$$
\text{Number} = \underbrace{\overline{\textcolor{lightgray}{k \space m \space \cdots \space c} \space b \space a}}_{\text{n places}} =
\textcolor{lightgray}{\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

# Divisibility Rule 1

Thus, to determine if the whole number is `divisible by 4`,

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The number up to the tens place has to be a multiple of 4}
    \phantom{\biggr)}
}
$$

---

### **Lets try factoring instead and see if there is another way to tell**

---

# Factoring the Number

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

We know that

> For $n \ge 2$
>
> $$
10^{n} = 4 \biggr( 2^1 \cdot 10^{n-1} + 2^2 \cdot 10^{n-2} + \cdots + 2^{n} \cdot 10^{0} + 2^{n-2} \biggr)
$$
>
> For $n = 1$
>
> $$
10^1 = 4 \cdot 2 + 2
$$


## Simplifying the Big Expression

Actually, since we already know that this expression is a `multiple of 8`

$$
\textcolor{lightgray}{10^n =} 4 \biggr( 2^1 \cdot 10^{n-1} + 2^2 \cdot 10^{n-2} + \cdots + 2^{n} \cdot 10^{0} + 2^{n-2} \biggr)
$$

We can simplify the expression inside the brackets as such

> For $n \ge 2$
>
> > Where $q_{n} = 2^1 \cdot 10^{n-1} + 2^2 \cdot 10^{n-2} + \cdots + 2^{n} \cdot 10^{0} + 2^{n-2}$
>
> $$
\boxed{
    \phantom{\big(}
        10^n = 4q_{n}
    \phantom{\big)}
}
$$
>

## Algebraic Manipulation

We factor it in

$$
\text{Number} =
k \space \biggr( 4q_{n-1} \biggr) +
m \space \biggr( 4q_{n-2} \biggr) +
\cdots +
c \space \biggr( 4q_{2} \biggr) +
b \space \biggr( 4 \cdot 2 + 2 \biggr) +
a
$$


Simplify it, and we get

$$
\text{Number} =
\boxed{ \phantom{\biggr(} 4k \cdot q_{n-1} \phantom{\biggr)}} +
\boxed{ \phantom{\biggr(} 4m \cdot q_{n-2} \phantom{\biggr)}} +
\cdots +
\boxed{\phantom{\biggr(} 4c \cdot q_{2} \phantom{\biggr)}}  +
\boxed{\phantom{\biggr(} 4 \cdot 2b + 2b  \phantom{\biggr)}} +
\boxed{\phantom{\biggr(} a \phantom{\biggr)}}
$$

Regroup it like so

$$
\text{Number} =
\Biggr(
    4 \cdot kq_{n-1} +
    4 \cdot mq_{n-2} +
    \cdots +
    4 \cdot cq_{2} +
    4 \cdot 2b
\Biggr) +
\biggr(
    2b +
    a
\biggr)
$$

Regroup by `4` and we get

$$
\boxed{
    \text{Number} =
    4 \Biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        cq_{2} +
        2b
    \Biggr) +
    \biggr(
        2b +
        a
    \biggr)
}
$$

# Analysis of Remainder

Thus, we see that `the quotient` of the number is a `multiple of 4`
- Thus making it `divisible by 4`

$$
\textcolor{lightgray}{\text{Number} =}
    4 \biggr(
    kq_{n-3} +
    mq_{n-4} +
    \cdots +
    cq_{0} +
    2b
    \biggr)
    \textcolor{lightgray}{+
    \biggr(
    2b +
    a
    \biggr)
    }
$$

Thus for the `whole number to be divisible by 4`,  the `remainder` also has to be a `multiple of 4`

$$
\textcolor{lightgray}{\text{Number} =
    4 \biggr(
    kq_{n-3} +
    mq_{n-4} +
    \cdots +
    cq_{0} +
    2b
    \biggr)} +
    \biggr(
    2b +
    a
    \biggr)
$$

# Divisibility Rule 2

Thus, to determine if the `whole number is divisible by 4`,

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The sum of: } \underline{\textbf{Twice of its 2nd last digit}} \textbf{ plus its } \underline{\textbf{last digit}} \textbf{, must be divisible by 4}
    \phantom{\biggr)}
}
$$
