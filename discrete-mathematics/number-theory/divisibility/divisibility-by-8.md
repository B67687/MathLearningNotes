---
title: "The Composition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-8.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/number-theory/divisibility/divisibility-by-8.ipynb"
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
    10 = 8 + 2
    \phantom{\big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
100 = 8 \cdot 10 + 2 \cdot \boxed{10}
$$

Noticing the `10` in the partition, we can split it like how we did before

$$
\begin{align}
    100 &= 8 \cdot 10 + \underline{2 \space \big( 8 + 2 \big)} \\
    &= 8 \cdot 10 + 8 \cdot 2 + 2^2 \\
\end{align}
$$

To get

$$
\boxed{
    \phantom{\big(}
    100 =  8 \cdot 10 + 8 \cdot 2 + 2^2
    \phantom{\big)}
}
$$

When we move on to the next power,

$$
1000 = 8 \cdot 10^2 + 8 \cdot 2 \cdot 10 + 2^2 \cdot \boxed{10}
$$

Split it again

$$
\begin{align}
    1000 &= 8 \cdot 10^2 + 8 \cdot 2 \cdot 10 + \underline{2^2 \space (8 + 2)} \\
    &= 8 \cdot 10^2  + 8 \cdot 2 \cdot 10 + 8 \cdot 2^2 + 2^3
\end{align}
$$

Thus,

$$
\boxed{
    \phantom{\big(}
    1000 = 8 \cdot 10^2 + 8 \cdot 2 \cdot 10 + 8 \cdot 2^2 + 2^3
    \phantom{\big)}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `3rd power onwards` up to some `n`

$$
\begin{align}
    10 &= 8 + 2 \\
    100 &= 8 \cdot 10 + 8 \cdot 2 + 2^2 \\
    1000 &= 8 \cdot 10^2 + 8 \cdot 2 \cdot 10 + 8 \cdot 2^2 + 2^3 \\
    &\vdots \\
    10^n &= 8 \cdot 2^{0} \cdot 10^{n-1} + 8 \cdot 2^{1} \cdot 10^{n-2} + \cdots + 8 \cdot 2^{n-2} \cdot 10^{1} + 8 \cdot 2^{0} \cdot 10^{0} + 2^{n} \\
\end{align}
$$

Thus the `general expression` is

$$
\boxed{
    \phantom{\Biggr(}
        10^{n} = 8 \biggr( 2^{0} \cdot 10^{n-1} + 2^{1} \cdot 10^{n-2} + \cdots + 2^{n-2} \cdot 10^{1} + 2^{n-1} \cdot 10^{0} \biggr) + 2^{n}
    \phantom{\Biggr)}
}
$$

# Special Condition That Covers Almost Every Condition

Notice that we have $2^n$

$$
\textcolor{lightgray}{
    8
    \biggr( 2^{0} \cdot 10^{n-1} + 2^{1} \cdot 10^{n-2} + \cdots + 2^{n-2} \cdot 10^{1} + 2^{0} \cdot 10^{0} \biggr)
} + 2^{n}
$$

And `8` is also $2^3$

$$
2^3
\textcolor{lightgray}{
    \biggr( 2^{0} \cdot 10^{n-1} + 2^{1} \cdot 10^{n-2} + \cdots + 2^{n-2} \cdot 10^{1} + 2^{0} \cdot 10^{0} \biggr)
} + 2^{n}
$$

Thus, we have can do this

> As long as $n \ge 3$

$$
2^3 \space \biggr( 2^{0} \cdot 10^{n-1} + 2^{1} \cdot 10^{n-2} + \cdots + 2^{n-2} \cdot 10^{1} + 2^{0} \cdot 10^{0} \biggr) + 2^{3} \cdot 2^{n-3}
$$

Then we can also group the `power of 2 expression` into the `multiple of 8`
> Allowing it to become `1 expression` of `multiple of 8`

$$
2^3 \space \biggr( 2^{0} \cdot 10^{n-1} + 2^{1} \cdot 10^{n-2} + \cdots + 2^{n-2} \cdot 10^{1} + 2^{0} \cdot 10^{0} + 2^{n-3} \biggr)
$$

Thus, the general expression for
> Where $n \ge 3$

$$
\underline{
    \phantom{\Biggr(}
    10^{n} = 8 \biggr( 2^{0} \cdot 10^{n-1} + 2^{1} \cdot 10^{n-2} + \cdots + 2^{n-2} \cdot 10^{1} + 2^{n-1} \cdot 10^{0} + 2^{n-3} \biggr)
    \phantom{\Biggr)}
}
$$

# Application of General Expressions

We can basically use this expression for almost every `power of 10`

> As long as $n \ge 3$
>
>$$
\boxed{
    \phantom{\Biggr(}
        10^{n} = 8 \biggr( 2^{0} \cdot 10^{n-1} + 2^{1} \cdot 10^{n-2} + \cdots + 2^{n-2} \cdot 10^{1} + 2^{n-1} \cdot 10^{0} + 2^{n-3} \biggr)
    \phantom{\Biggr)}
}
$$
>
>Then for $1 \le n \le 2$, we have
>
> $$
\boxed{
    \phantom{\big(}
    10^1 = 8 + 2
    \phantom{\big)}
}
$$
>
> $$
\boxed{
    \phantom{\big(}
    10^2 = 8 \cdot 12 + 2^2
    \phantom{\big)}
}
$$

# Going by the Structure

Lets look back at the number again

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space d \space c \space b \space a}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{d \cdot 10^{3}} +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

## Divisible by Place

Since we know that every `power of 10` from the `3rd power onwards` will be `divisible by 8`

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space d \space \textcolor{lightgray}{c \space b \space a}}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{d \cdot 10^{3}} \textcolor{lightgray}{+
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}}
$$

We just need to check whether the number up to the `hundreds place` is `divisible by 8`

$$
\text{Number} = \underbrace{\overline{\textcolor{lightgray}{k \space m \space \cdots \space d} \space c \space b \space a}}_{\text{n places}} =
\textcolor{lightgray}{\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{d \cdot 10^{3}}} +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

# Divisibility Rule 1

Thus, to determine if the whole number is `divisible by 8`,

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The number up to the hundreds place has to be a multiple of 8}
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
\underline{d \cdot 10^{3}} +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

We know that

> For $n \ge 3$
>
> $$
10^{n} = 8 \biggr( 2^{0} \cdot 10^{n-1} + 2^{1} \cdot 10^{n-2} + \cdots + 2^{n-2} \cdot 10^{1} + 2^{n-1} \cdot 10^{0} + 2^{n-3} \biggr)
$$
>
> For $0 \le n \le 2$
>
> $$
\begin{align}
    10^1 &= 8 + 2 \\
    10^2 &= 8 \cdot 12 + 2^2
\end{align}
$$

## Simplifying the Big Expression

Actually, since we already know that this expression is a `multiple of 8`

$$
\textcolor{lightgray}{10^n =} 8 \biggr( 2^{0} \cdot 10^{n-1} + 2^{1} \cdot 10^{n-2} + \cdots + 2^{n-2} \cdot 10^{1} + 2^{n-1} \cdot 10^{0} \biggr)
$$

We can simplify the expression inside the brackets as such

- Where $q_{n} = 2^{0} \cdot 10^{n-1} + 2^{1} \cdot 10^{n-2} + \cdots + 2^{n-2} \cdot 10^{1} + 2^{n-1} \cdot 10^{0}$
>
> For $n \ge 3$
>
> $$
\boxed{
    \phantom{\big(}
    10^n = 8q_{n}
    \phantom{\big)}
}
$$

## Algebraic Manipulation

We factor it in

$$
\text{Number} =
k \space \biggr( 8q_{n-1} \biggr) +
m \space \biggr( 8q_{n-2} \biggr) +
\cdots +
d \space \biggr( 8q_{3} \biggr) +
c \space \biggr( 8 \cdot 12 + 2^{2} \biggr) +
b \space \biggr( 8 + 2 \biggr) +
a
$$


Simplify it, and we get

$$
\text{Number} =
\boxed{ \phantom{\biggr(} 8k \cdot q_{n-1} \phantom{\biggr)}} +
\boxed{ \phantom{\biggr(} 8m \cdot q_{n-2} \phantom{\biggr)}} +
\cdots +
\boxed{\phantom{\biggr(} 8d \cdot q_{3} \phantom{\biggr)}}  +
\boxed{\phantom{\biggr(} 8 \cdot 12c + 2^{2} c \phantom{\biggr)}}  +
\boxed{\phantom{\biggr(} 8b + 2 b  \phantom{\biggr)}} +
\boxed{\phantom{\biggr(} a \phantom{\biggr)}}
$$

Regroup it like so

$$
\text{Number} =
\Biggr(
    8 \cdot kq_{n-1} +
    8 \cdot mq_{n-2} +
    \cdots +
    8 \cdot dq_{3} +
    8 \cdot 12c +
    8 b
\Biggr) +
\biggr(
    2^{2} c +
    2 b +
    a
\biggr)
$$

Regroup by `8` and we get

$$
\text{Number} =
8 \Biggr(
    kq_{n-1} +
    mq_{n-2} +
    \cdots +
    dq_{3} +
    12c +
    b
\Biggr) +
\biggr(
    2^{2} c +
    2 b +
    a
\biggr)
$$

Which when simplified is

$$
\boxed{
    \text{Number} =
    8 \Biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        dq_{3} +
        12c +
        b
    \Biggr) +
    \biggr(
        4 c +
        2 b +
        a
    \biggr)
}
$$

# Analysis of Remainder

Thus, we see that `this part` of the number is a `multiple of 8`
- Thus making it `divisible by 8`

$$
\textcolor{lightgray}{\text{Number} =}
    8 \Biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        dq_{3} +
        12c +
        b
    \Biggr)
    \textcolor{lightgray}{+
        \biggr(
            4c +
            2b +
            a
        \biggr)
    }
$$

Thus for the `whole number to be divisible by 8`,  this part also has to be a `multiple of 8`

$$
\textcolor{lightgray}{\text{Number} =
   8 \Biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        dq_{3} +
        12c +
        b
    \Biggr)
    }
    \textcolor{lightgray}{+}
    \textcolor{lightgray}{\biggr(}
    4c +
    2b +
    a
    \textcolor{lightgray}{\biggr)}
$$

Which is the **sum of** `four times the hundreds place digit`, `twice the tens place digit`, and `one of the ones place digit`

$$
\boxed{
    \phantom{\big(}
    4c + 2b + a
    \phantom{\big)}
}
$$

# Divisibility Rule 2

Thus, to determine if the `whole number is divisible by 8`,

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The sum of: } \underline{\textbf{Four times its 3rd last digit}} \textbf{, } \underline{\textbf{Twice of its 2nd last digit}} \textbf{, plus its } \underline{\textbf{last digit}} \textbf{, must be divisible by 8}
    \phantom{\biggr)}
}
$$
