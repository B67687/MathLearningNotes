---
title: "The Composition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-7.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/number-theory/divisibility/divisibility-by-7.ipynb"
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

Notice that `10` can be `partitioned` into `7`, and `3`

$$
\boxed{
    \phantom{\big(}
        10 = 7 + 3
    \phantom{\big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
100 = 7 \cdot 10 + 3 \cdot \boxed{10}
$$

Noticing the `10` in the partition where it isn't grouped by the multiple `7`, we can split it like how we did before

$$
\begin{align}
    100 &= 7 \cdot 10 + \underline{3 \cdot (7 + 3)} \\
    &= 7 \cdot 10 + 7 \cdot 3 + 3 \cdot 3 \\
    &= 7 \cdot 10 + 7 \cdot 3 + 3^{2}
\end{align}
$$

Thus,

$$
\boxed{
    \phantom{\big(}
        100 = 7 \cdot 10 + 7 \cdot 3 + 3^{2}
    \phantom{\big)}
}
$$

This works when we move on to the next power,

$$
1000 = 7 \cdot 10^2 + 7 \cdot 3 \cdot 10 + 3^{2} \cdot \boxed{10}
$$

We can split the `10` again

$$
\begin{align}
    1000 &= 7 \cdot 10^2 + 7 \cdot 3 \cdot 10 + 3^{2} \cdot (7 + 3) \\
    &= 7 \cdot 10^2 + 7 \cdot 3 \cdot 10 + 7 \cdot 3^{2} + 3^3 \\
\end{align}
$$

To get

$$
\boxed{
    \phantom{\big(}
        1000 = 7 \cdot 10^2 + 7 \cdot 3 \cdot 10 + 7 \cdot 3^{2} + 3^3
    \phantom{\big)}
}
$$

When we move on to the next power,

$$
10000 = 7 \cdot 10^3 + 7 \cdot 3 \cdot 10^2 + 7 \cdot 3^{2} \cdot 10 + 3^3 \cdot \boxed{10}
$$

Doing the same grouping

$$
\begin{align}
    10000 &= 7 \cdot 10^3 + 7 \cdot 3 \cdot 10^2 + 7 \cdot 3^{2} \cdot 10 + 3^3 \cdot (7 + 3) \\
    &= 7 \cdot 10^3 + 7 \cdot 3 \cdot 10^2 + 7 \cdot 3^{2} \cdot 10 + 7 \cdot 3^3 + 3^4 \\
\end{align}
$$

Then we get

$$
\boxed{
    \phantom{\big(}
        10000 = 7 \cdot 10^3 + 7 \cdot 3 \cdot 10^2 + 7 \cdot 3^{2} \cdot 10 + 7 \cdot 3^3 + 3^4
    \phantom{\big)}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `1st power onwards` up to some `n`

$$
\begin{align}
    10 &= 7 \cdot 3 \\
    100 &= 7 \cdot 10 + 7 \cdot 3 + 3^{2} \\
    1000 &= 7 \cdot 10^2 + 7 \cdot 3 \cdot 10 + 7 \cdot 3^{2} + 3^3 \\
    10000 &= 7 \cdot 10^3 + 7 \cdot 3 \cdot 10^2 + 7 \cdot 3^{2} \cdot 10 + 7 \cdot 3^3 + 3^4 \\
    &\vdots \\
    10^n &= 7 \cdot 3^{0} \cdot 10^{n-1} + 7 \cdot 3^1 \cdot 10^{n-2} + \cdots + 7 \cdot 3^{n-1} \cdot 10^0 + 3^{n} \\
\end{align}
$$

Thus the overall expression is

$$
\boxed{
    \phantom{\Biggr(}
        10^n = 7 \biggr( 3^{0} \cdot 10^{n-1} + 3^1 \cdot 10^{n-2} + \cdots + 3^{n-1} \cdot 10^0 \biggr) + 3^{n} \\
    \phantom{\Biggr)}
}
$$

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

Since we know this

$$
10^n = 7 \biggr( 3^{0} \cdot 10^{n-1} + 3^1 \cdot 10^{n-2} + \cdots + 3^{n-1} \cdot 10^0 \biggr) + 3^{n}
$$

## Simplifying the Expression

Actually, since we already know that this part is a `multiple of 7`

$$
\textcolor{lightgray}{10^n =}  7 \biggr( 3^{0} \cdot 10^{n-1} + 3^1 \cdot 10^{n-2} + \cdots + 3^{n-1} \cdot 10^0 \biggr) \textcolor{lightgray}{+} \textcolor{lightgray}{3^{n}}
$$

We can simplify the expression inside the brackets as such

> Where $q_{n} = 3^{0} \cdot 10^{n-1} + 3^1 \cdot 10^{n-2} + \cdots + 3^{n-1} \cdot 10^0$


$$
\boxed{
    10^n = 7q_{n} + 3^n
}
$$

## Algebraic Manipulation


We factor it in

$$
\text{Number} =
\space k \space \biggr( 7q_{n-1} + 3^{n-1} \biggr) +
m \space \biggr( 7q_{n-2} + 3^{n-2} \biggr) +
\cdots +
c \space \biggr( 7q_{2} + 3^{2} \biggr) +
b \space \biggr( 7q_{1} + 3^{1} \biggr) +
a
$$

Simplify it, and we get

$$
\text{Number} =
\boxed{ \phantom{\biggr(} 7k \cdot q_{n-1} + 3^{n-1}k \phantom{\biggr)}} +
\boxed{ \phantom{\biggr(} 7m \cdot q_{n-2} + 3^{n-2}m \phantom{\biggr)}} +
\cdots +
\boxed{\phantom{\biggr(} 7c \cdot q_{2} + 3^{2}c \phantom{\biggr)}}  +
\boxed{\phantom{\biggr(} 7b \cdot q_{1} + 3b \phantom{\biggr)}} +
\boxed{\phantom{\biggr(} a \phantom{\biggr)}}
$$

Regroup it like so

$$
\text{Number} =
\Biggr(
    7k \cdot q_{n-1} +
    7m \cdot q_{n-2} +
    \cdots +
    7c \cdot q_{2} +
    7b \cdot q_{1}
\Biggr) +
\biggr(
    3^{n-1}k + 3^{n-2}m + \cdots + 3^{2}c + 3b + a
\biggr)
$$

Regroup those groups by `7`

$$
\text{Number} =
7 \Biggr(
    kq_{n-1} +
    mq_{n-2} +
    \cdots +
    cq_{2} +
    bq_{1}
\Biggr) +
\biggr(
    3^{n-1}k + 3^{n-2}m + \cdots + 3^{2}c + 3b + a
\biggr)
$$

# Re-Express Place Values

Let the `place value` be expressed in terms of $f_h$ instead
> It is easier to see the pattern and compress it this way

$$
\text{Number} =
7 \Biggr(
    f_n q_{n-1} +
    f_{n-1} q_{n-2} +
    \cdots +
    f_{3} q_{2} +
    f_{2} q_{1}
\Biggr) +
\biggr(
    3^{n-1} f_n + 3^{n-2} f_{n-1} + \cdots + 3^{2} f_{3} + 3^{1} f_{2} + 3^{0} f_{1}
\biggr)
$$

Group the `coefficients by power of 3`

$$
\text{Number} =
7 \Biggr(
    f_n q_{n-1} +
    f_{n-1} q_{n-2} +
    \cdots +
    f_{3} q_{2} +
    f_{2} q_{1}
\Biggr) +
    \sum_{h=1}^{n-1} 3^{h-1} f_h
$$

# Analysis of Remainder

Thus, we see that `this part` of the number is a `multiple of 7`

$$
\textcolor{lightgray}{\text{Number} = }
    7 \Biggr(
        f_n q_{n-1} +
        f_{n-1} q_{n-2} +
        \cdots +
        f_{3} q_{2} +
        f_{2} q_{1}
    \Biggr)
\textcolor{lightgray}{+}
\textcolor{lightgray}{
     \sum_{h=1}^{n-1} 3^{h-1} f_h
}
$$

Thus for the `whole number to be divisible by 7`,  this part also has to be a `multiple of 7`

$$
\textcolor{lightgray}{\text{Number} =
    7 \Biggr(
        f_n q_{n-1} +
        f_{n-1} q_{n-2} +
        \cdots +
        f_{3} q_{2} +
        f_{2} q_{1}
    \Biggr)
} +
     \sum_{h=1}^{n-1} 3^{h-1} f_h
$$

Which is the sum of `(place - 1)-th power of 3` multiplied by its `place value`

$$
\boxed{
    \phantom{\big(}
        \sum_{h=1}^{n-1} 3^{h-1} f_h
    \phantom{\big)}
}
$$

# Divisibility Rule 1

Thus, to determine if the whole number is `divisible by 7`,

$$
\boxed{
    \phantom{\biggr(}
        \textbf{Sum of:}
        \space
        \underline{
            \textbf{Power of 3 at one less than the place number}
        }
        \space
        \textbf{multiplied by the}
        \space
        \underline{\textbf{place value}}
        \space
        \textbf{, must be divisible by 7}
    \phantom{\biggr)}
}
$$

# Partitioning Less Strictly

Notice that `10` can be `partitioned` into `7`, and `3`

$$
\boxed{
    \phantom{\big(}
        10 = 7 + 3
    \phantom{\big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
\boxed{
    \phantom{\big(}
        100 = 7 \cdot 10 + 3 \cdot 10
    \phantom{\big(}
}
$$

This works when we move on to the next power,

$$
\boxed{
    \phantom{\big(}
        1000 = 7 \cdot 10^2 + 3 \cdot 10^2
    \phantom{\big(}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `1st power onwards` up to some `n`

$$
\begin{align}
    10 &= 7 + 3 \\
    100 &= 7 \cdot 10 + 3 \cdot 10 \\
    1000 &= 7 \cdot 10^2 + 3 \cdot 10^2 \\
    &\vdots \\
    10^n &= 7 \cdot 10^{n-1} + 3 \cdot 10^{n-1} \\
\end{align}
$$

Thus, the overall expression is

$$
\boxed{
    \phantom{\big(}
        10^n = 7 \cdot 10^{n-1} + 3 \cdot 10^{n-1}
    \phantom{\big)}
}
$$

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

Since we know this
- Where `n` increases from `1`

$$
10^n = 7 \cdot 10^{n-1} + 3 \cdot 10^{n-1}
$$

We factor it in

$$
\text{Number} =
\space k \space \biggr( 7 \cdot 10^{n-2} + 3 \cdot 10^{n-2} \biggr) +
m \space \biggr( 7 \cdot 10^{n-3} + 3 \cdot 10^{n-3} \biggr) +
\cdots +
c \space \biggr( 7 \cdot 10 + 3 \cdot 10 \biggr) +
b \space \biggr( 7 + 3 \biggr) +
a
$$

Simplify it, and we get

$$
\text{Number} =
\boxed{ \phantom{\biggr(} 7 \cdot 10^{n-2}k + 3 \cdot 10^{n-2}k \phantom{\biggr)}} +
\boxed{ \phantom{\biggr(} 7 \cdot 10^{n-3}m + 3 \cdot 10^{n-3}m \phantom{\biggr)}} +
\cdots +
\boxed{\phantom{\biggr(} 7 \cdot 10c + 3 \cdot 10c \phantom{\biggr)}}  +
\boxed{\phantom{\biggr(} 7b + 3b  \phantom{\biggr)}} +
\boxed{\phantom{\biggr(} a \phantom{\biggr)}}
$$

Regroup it like so

$$
\text{Number} =
\Biggr(
    7 \cdot 10^{n-2}k +
    7 \cdot 10^{n-3}m +
    \cdots +
    7 \cdot 10c +
    7b
\Biggr) +
\biggr(
    3 \cdot 10^{n-2}k + 3 \cdot 10^{n-3}m + \cdots + 3 \cdot 10c + 3b
\biggr) +
    a
$$

Regroup those groups by `7` and `3` respectively and we get

$$
\boxed{
    \text{Number} =
    7 \Biggr(
        10^{n-2}k +
        10^{n-3}m +
        \cdots +
        10c +
        b
    \Biggr) +
    3 \biggr(
        10^{n-2}k + 10^{n-3}m + \cdots + 10c + b
    \biggr) +
    a
}
$$

# Analysis of Remainder

Thus, we see that `this part` of the number is a `multiple of 7`
- Thus making it `divisible by 7`

$$
\textcolor{lightgray}{\text{Number} = }
    7 \Biggr(
        10^{n-2}k +
        10^{n-3}m +
        \cdots +
        10c +
        b
    \Biggr)
\textcolor{lightgray}{+}
\textcolor{lightgray}{
    3 \biggr(
        10^{n-2}k + 10^{n-3}m + \cdots + 10c + b
    \biggr) +
    a
}
$$

Thus for the `whole number to be divisible by 7`,  this part also has to be a `multiple of 7`

$$
\textcolor{lightgray}{\text{Number} =
    7 \Biggr(
        10^{n-2}k +
        10^{n-3}m +
        \cdots +
        10c +
        b
    \Biggr)
} +
   3 \biggr(
        10^{n-2}k + 10^{n-3}m + \cdots + 10c + b
    \biggr) +
    a
$$

Realise that it contains `3` times `all the digits of the number itself in order` up to the `n-1`-th place plus `a`

$$
\boxed{
    \phantom{\big(}
        3 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b \space}}_{\text{n-1 places}} + a
    \phantom{\big)}
}
$$

# Divisibility Rule 2

Thus, to determine if the `whole number is divisible by 7`,

$$
\boxed{
    \phantom{\biggr(}
        \underline{
            \textbf{3 times the number without the ones place}
        }
        \space
        \textbf{plus}
        \space
        \underline{\textbf{the number in the ones place}}
        \space
        \textbf{, must be divisible by 7}
    \phantom{\biggr)}
}
$$

# Finding a Better Rule

What if we let `a` be integrated into the `multiple of 3` such that we only have to look at what is `inside the brackets`?

$$
\textcolor{lightgray}{\text{Number} =
7 \Biggr(
    10^{n-2}k +
    10^{n-3}m +
    \cdots +
    10c +
    b
\Biggr) +
3 \biggr(
    10^{n-2}k + 10^{n-3}m + \cdots + 10c + b
\biggr) +} \space
a
$$

To not leave any parts behind,

We need `a` to be expressible in 2 parts where
- One part must `integrate into` the expression with `multiple 7`
- While the other `integrates into` the expression with `multiple 3`

Like so

$$
\textcolor{lightgray}{\text{Number} =
7 \Biggr(
    10^{n-2}k +
    10^{n-3}m +
    \cdots +
    10c +
    b
\Biggr) +
3 \biggr(
    10^{n-2}k + 10^{n-3}m + \cdots + 10c + b
\biggr) +} \space
(7a - 6a)
$$

Integrate into the expressions

$$
\textcolor{lightgray}{\text{Number} =
7 \Biggr(
    10^{n-2}k +
    10^{n-3}m +
    \cdots +
    10c +
    b} +
    a
\textcolor{lightgray}{\Biggr) +
3 \biggr(
    10^{n-2}k + 10^{n-3}m + \cdots + 10c + b} - 2a
\textcolor{lightgray}{\biggr)}
$$

And now we only need to look at `expression inside the brackets` here to determine `divisibility by 7`

$$
\textcolor{lightgray}{\text{Number} =
7 \Biggr(
    10^{n-2}k +
    10^{n-3}m +
    \cdots +
    10c +
    b +
    a
\Biggr) +
3 \biggr(}
    \underline{10^{n-2}k +
    10^{n-3}m +
    \cdots +
    10c +
    b} -
    2a
\textcolor{lightgray}{\biggr)}
$$


Realise that it contains `all the digits of the number itself in order` up to the `n-1`-th place minus `2a`

$$
\boxed{
    \phantom{\big(}
        \underbrace{\overline{k \space m \space \cdots \space c \space b \space}}_{\text{n-1 places}} - 2a
    \phantom{\big)}
}
$$

# Divisibility Rule 3

Thus, to determine if the `whole number is divisible by 7`,

$$
\boxed{
    \phantom{\biggr(}
        \underline{
            \textbf{The number without the ones place}
        }
        \space
        \textbf{minus}
        \space
        \underline{\textbf{twice the number in the ones place}}
        \space
        \textbf{, must be divisible by 7}
    \phantom{\biggr)}
}
$$
