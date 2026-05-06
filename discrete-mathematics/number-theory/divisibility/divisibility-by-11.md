---
title: "The Composition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-11.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/number-theory/divisibility/divisibility-by-11.ipynb"
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

Notice that `10` can be expressed in `11` and `1`

$$
\boxed{
    \phantom{\big(}
    10 = 11 - 1
    \phantom{\big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
\boxed{
    \phantom{\big(}
    100 = 11 \cdot 10 - 10
    \phantom{\big)}
}
$$

And the same for the `next power of 10`

$$
\boxed{
    \phantom{\big(}
    1000 = 11 \cdot 10^2 - 10^2
    \phantom{\big)}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `1st power onwards` up to some `n`

$$
\begin{align}
    10 &= 11 - 1 \\
    100 &= 11 \cdot 10 - 10 \\
    1000 &= 11 \cdot 10^2 - 10^2 \\
    &\vdots \\
    10^n &= 11 \cdot 10^{n-1} - 10^{n-1} \\
\end{align}
$$

Thus, the general expression is

$$
\boxed{
    \phantom{\big(}
    10^n = 11 \cdot 10^{n-1} - 10^{n-1}
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
10^n = 11 \cdot 10^{n-1} - 10^{n-1}
$$

We factor it in

$$
\text{Number} =
\space k \space \biggr( 11 \cdot 10^{n-2} - 10^{n-2} \biggr) +
m \space \biggr( 11 \cdot 10^{n-3} - 10^{n-3} \biggr) +
\cdots +
c \space \biggr( 11 \cdot 10 - 10 \biggr) +
b \space \biggr( 11 - 1 \biggr) +
a
$$

Simplify it, and we get

$$
\text{Number} =
\boxed{ \phantom{\biggr(} 11 \cdot 10^{n-2}k - 10^{n-2}k \phantom{\biggr)}} +
\boxed{ \phantom{\biggr(} 11 \cdot 10^{n-3}m - 10^{n-3}m \phantom{\biggr)}} +
\cdots +
\boxed{\phantom{\biggr(} 11 \cdot 10c - 10c \phantom{\biggr)}}  +
\boxed{\phantom{\biggr(} 11b - b  \phantom{\biggr)}} +
\boxed{\phantom{\biggr(} a \phantom{\biggr)}}
$$

Regroup it like so

$$
\text{Number} =
\Biggr(
    11 \cdot 10^{n-2}k +
    11 \cdot 10^{n-3}m +
    \cdots +
    11 \cdot 10c +
    11b
\Biggr) -
\biggr(
    10^{n-2}k + 10^{n-3}m + \cdots + 10c + b
\biggr) +
    a
$$

Regroup those groups by `11`and we get

$$
\text{Number} =
11 \Biggr(
    10^{n-2}k +
    10^{n-3}m +
    \cdots +
    10c +
    b
\Biggr) -
\biggr(
    10^{n-2}k + 10^{n-3}m + \cdots + 10c + b
\biggr) +
a
$$

Which realise is also a `portion` of that number in `base-10`

$$
\text{Number} =
11 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} \space -
\underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} +
a
$$

# Analysis of Remainder

Thus, we see that `this part` of the number is a `multiple of 11`
- Thus making it `divisible by 11`

$$
\textcolor{lightgray}{\text{Number} = }
    11 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}}
\space
\textcolor{lightgray}{-}
\space
\textcolor{lightgray}{
    \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} + a
}
$$

Thus for the `whole number to be divisible by 11`,  this part also has to be a `multiple of 11`

$$
\textcolor{lightgray}{\text{Number} =
    11 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}}} \space -
    \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} + a
$$

But it is still `2 expressions`, let us simplify it into `1 expression` instead

$$
\textcolor{lightgray}{\text{Number} =
    11 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}}} \space -
    \biggr( \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} - a \biggr)
$$

So that we can just look at the `absolute expression` instead

$$
\textcolor{lightgray}{\text{Number} =
    11 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} \space -}
    \biggr( \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} - a \biggr)
$$


Which is this

$$
\boxed{
    \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} - a
}
$$

# Divisibility Rule 1


Thus, to determine if the `whole number is divisible by 11`,

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The number that doesn't include the ones place minus the number in the ones place, must be divisible by 11}
    \phantom{\biggr)}
}
$$

---

### **Lets try partitioning more intensely instead and see if there is another way to tell**

---

## Intense Partitioning

Notice that `10` can be expressed in `11` and `1`

$$
\boxed{
    \phantom{\big(}
        10 = 11 - 1
    \phantom{\big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
100 = 11 \cdot 10 - \boxed{10}
$$

Notice that the single expression `10` is the only expression not in terms of `11`
- We can `split it` like how we did before

$$
\begin{align}
    100 &= 11 \cdot 10 - (11 - 1) \\
    &= 11 \cdot 10 - 11 + 1
\end{align}
$$

To get this

$$
\boxed{
    \phantom{\big(}
        100 = 11 \cdot 10 - 11 + 1
    \phantom{\big)}
}
$$

Moving to the `next power of 10`, we have

$$
1000 = 11 \cdot 10^2 - 11 \cdot 10 + 1 \cdot \boxed{10}
$$

Again, the expression `10` is the only expression not in terms of `11`
- We `split it`

$$
\begin{align}
    1000 &= 11 \cdot 10^2 - 11 \cdot 10 + (11 - 1) \\
    &= 11 \cdot 10^2 - 11 \cdot 10 + 11 - 1
\end{align}
$$

And we get this

$$
\boxed{
    \phantom{\big(}
        1000 = 11 \cdot 10^2 - 11 \cdot 10 + 11 - 1
    \phantom{\big)}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `1st power onwards` up to some `n`

$$
\begin{align}
    10 &= 11 - 1 \\
    100 &= 11 \cdot 10 - 11 + 1 \\
    1000 &= 11 \cdot 10^2 - 11 \cdot 10 + 11 - 1 \\
    &\vdots \\
        10^n &= 11 \cdot 10^{n-1} - 11 \cdot 10^{n-2} + \cdots \pm 11 \cdot 10^{0} \space \mp 1 \\
\end{align}
$$

We can further simplify the general expression as this

- **Overall**

$$
\boxed{
    10^n = 11 \biggr( 10^{n-1} - 10^{n-2} + \cdots \pm 1 \biggr) \mp 1
}
$$

---

> Where if n is `odd`
>
> $$
\textcolor{lightgray}{
    10^n = 11 \biggr( 10^{n-1} - 10^{n-2} + \cdots
    }
    - 1
    \textcolor{lightgray}{\biggr)}
    + 1
$$
>
> Where if n is `even`
>
> $$
\textcolor{lightgray}{
    10^n = 11 \biggr( 10^{n-1} - 10^{n-2} + \cdots
    }
    + 1
    \textcolor{lightgray}{\biggr)}
    - 1
$$

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

Since we know this
- Where `n` increases from `1`

$$
10^n = 11 \biggr( 10^{n-1} - 10^{n-2} + \cdots \pm 1 \biggr) \mp 1
$$

## Simplifying the Expression

Actually, since we already know that this part is a `multiple of 11`

$$
\textcolor{lightgray}{10^n =} 11 \biggr( 10^{n-1} - 10^{n-2} + \cdots \pm 1 \biggr) \textcolor{lightgray}{\mp} \textcolor{lightgray}{1}
$$

We can simplify the expression inside the brackets as such

> Where $q_{n} = 10^{n-1} - 10^{n-2} + \cdots \pm 1$


$$
\boxed{
    10^n = 11q_{n} \mp 1
}
$$

## Algebraic Manipulation

We factor it in

$$
\text{Number} =
\space k \space \biggr( 11q_{n-1} \mp 1 \biggr) +
m \space \biggr( 11q_{n-2} \pm 1 \biggr) +
\cdots +
c \space \biggr( 11q_{2} \mp 1 \biggr) +
b \space \biggr( 11q_{1} \pm 1 \biggr) +
a
$$

Simplify it, and we get

$$
\text{Number} =
\boxed{ \phantom{\biggr(} 11k \cdot q_{n-1} \mp k \phantom{\biggr)}} +
\boxed{ \phantom{\biggr(} 11m \cdot q_{n-2} \pm m \phantom{\biggr)}} +
\cdots +
\boxed{\phantom{\biggr(} 11c \cdot q_{2} \mp c \phantom{\biggr)}}  +
\boxed{\phantom{\biggr(} 11b \cdot q_{1} \pm b  \phantom{\biggr)}} +
\boxed{\phantom{\biggr(} a \phantom{\biggr)}}
$$

Regroup it like so

$$
\text{Number} =
\Biggr(
    11 \cdot kq_{n-1} +
    11 \cdot mq_{n-2} +
    \cdots +
    11 \cdot cq_{2} +
    11 \cdot bq_{1}
\Biggr) +
\biggr(
    \mp k \pm m \mp \cdots \pm c \mp b
\biggr) +
a
$$

Regroup those groups by `11` and we get

$$
\text{Number} =
    11 \Biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        cq_{2} +
        bq_{1}
    \Biggr) +
    \biggr(
        \mp k \pm m \mp \cdots \pm c \mp b
    \biggr)
    + a
$$

---

> Where if `n is even`, it is
>
> $$
\textcolor{lightgray}{
    \text{Number} =
    11 \Biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        cq_{2} +
        bq_{1}
    \Biggr) +}
    \biggr(
        - k + m - \cdots - c + b
    \biggr)
    \textcolor{lightgray}{+a}
$$
>
> Where if `n is odd`, it is
>
> $$
\textcolor{lightgray}{
    \text{Number} =
    11 \Biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        cq_{2} +
        bq_{1}
    \Biggr) +}
    \biggr(
        k - m + \cdots + c - b
    \biggr)
    \textcolor{lightgray}{+a}
$$

---

# Analysis of Remainder

Thus, we see that `this part` of the number is a `multiple of 11`
- Thus making it `divisible by 11`

$$
\textcolor{lightgray}{\text{Number} = }
11 \Biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        cq_{2} +
        bq_{1}
    \Biggr)
\textcolor{lightgray}{+
\big( \mp k \pm m \mp \cdots \pm c \mp b \big) + a}
$$

Thus for the `whole number to be divisible by 11`,  this part also has to be a `multiple of 11`

$$
\textcolor{lightgray}{\text{Number} =
11 \Biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        cq_{2} +
        bq_{1}
    \Biggr)} +
\big( \mp k \pm m \mp \cdots \pm c \mp b \big) + a
$$

Realise that it contains `all the digits of the number itself in order`, but with `alternating operations`, except for `a`

$$
\text{Number} \space = \space \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}}
$$

## Even and Odd Scenarios

Realise the 2 different scenarios of `that part with all the digits divisible by 11`

> Where if n is `even`
>
> $$
\underline{- k + m - \cdots + c - b} + a
$$
>
> Where if n is `odd`
>
> $$
\underline{k - m + \cdots + c - b} + a
$$

## Equivalent Features of Polarity

Notice that it is also true that its `negative counterparts` must also be `divisible by 11`

> Where if n is `even`
>
> $$
\underline{k - m + \cdots - c + b} - a
$$
>
> Where if n is `odd`
>
> $$
\underline{- k + m - \cdots - c + b} - a
$$

## Pick out Positive Starters

We can thus pick those that `start off with a positive number` instead and end up with this

> Where if n is `even`
>
> $$
\underline{k - m + \cdots - c + b} - a
$$
>
> Where if n is `odd`
>
> $$
\underline{k - m + \cdots + c - b} + a
$$

# Combine into General Expression

This means we start from positive k, then **alternate between negative and positive operators**

$$
\boxed{
    \phantom{\Big(}
    k - m + \cdots \pm c \mp b \pm a
    \phantom{\Big)}
}
$$

Because the sum is `alternating`,
- The digits in the `odd positions are all positive`, and
- The digits in the `even positions are all negative`

Thus, Where a `number` is expressed like so

$$
\text{Number} = \underbrace{\overline{a_{n} \space a_{n-1} \space \cdots \space a_{3} \space a_{2} \space a_{1}}}_{\text{n places}} =
\space \underline{a_{n} \cdot 10^{n-1}} +
\underline{a_{n-1} \cdot 10^{n-2}} +
\cdots +
\underline{a_{3} \cdot 10^{2}} +
\underline{a_{2} \cdot 10^{1}} +
\underline{a_{1} \cdot 10^{0}}
$$

We can arrange all the **digits in the odd positions** together and the **digits in the even positions** together

$$
\phantom{\Big(}
    \underline{
        a_1 + a_3 + \cdots + a_{n-3} + a_{n-1}
    }
    \quad
    \underline{
        - a_2 - a_4 - \cdots - a_{n-2} - a_{n}
    }
\phantom{\Big)}
$$

We can then `simplify the calculation` by taking the **sum of the digits in the odd positions** minus the **sum of the digits in the even positions**


$$
\boxed{
    \phantom{\Big(}
        \biggr( a_1 + a_3 + \cdots + a_{n-3} + a_{n-1} \biggr)
        - \biggr( a_2 + a_4 + \cdots + a_{n-2} + a_{n} \biggr)
    \phantom{\Big)}
}
$$

# Divisibility Rule 2

Thus, to determine if the `whole number is divisible by 11`,

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The alternating sum of the digits, starting from positive digit in the largest place, must be divisible by 11}
    \phantom{\biggr)}
}
$$

$$
\textbf{or}
$$

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The sum of the digits in the odd positions, minus the sum of the digits in the even positions, must be divisible by 11}
    \phantom{\biggr)}
}
$$
