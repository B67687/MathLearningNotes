---
title: "The Composition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-13.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/number-theory/divisibility/divisibility-by-13.ipynb"
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

Notice that `13` can be expressed in `10` and `3`

$$
\boxed{
    \phantom{\big(}
        10 = 13 - 3
    \phantom{\big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
\boxed{
    \phantom{\big(}
    100 = 13 \cdot 10 - 3 \cdot 10
    \phantom{\big)}
}
$$

And the same for the `next power of 10`

$$
\boxed{
    \phantom{\big(}
    1000 = 13 \cdot 10^2 - 3 \cdot 10^2
    \phantom{\big)}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `1st power onwards` up to some `n`

$$
\begin{align}
    10 &= 13 - 3 \\
    100 &= 13 \cdot 10 - 3 \cdot 10 \\
    1000 &= 13 \cdot 10^2 - 3 \cdot 10^2 \\
    &\vdots \\
    10^n &= 13 \cdot 10^{n-1} - 3 \cdot 10^{n-1} \\
\end{align}
$$

Thus the general expression is

$$
\boxed{
    \phantom{\big(}
        10^n = 13 \cdot 10^{n-1} - 3 \cdot 10^{n-1}
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
10^n = 13 \cdot 10^{n-1} - 3 \cdot 10^{n-1}
$$

We factor it in

$$
\text{Number} =
\space k \space \biggr( 13 \cdot 10^{n-2} - 3 \cdot 10^{n-2} \biggr) +
m \space \biggr( 13 \cdot 10^{n-3} - 3 \cdot 10^{n-3} \biggr) +
\cdots +
c \space \biggr( 13 \cdot 10 - 3 \cdot 10 \biggr) +
b \space \biggr( 13 - 3 \biggr) +
a
$$

Simplify it, and we get

$$
\text{Number} =
\boxed{ \phantom{\biggr(} 13 \cdot 10^{n-2}k - 3 \cdot 10^{n-2}k \phantom{\biggr)}} +
\boxed{ \phantom{\biggr(} 13 \cdot 10^{n-3}m - 3 \cdot 10^{n-3}m \phantom{\biggr)}} +
\cdots +
\boxed{\phantom{\biggr(} 13 \cdot 10c - 3 \cdot 10c \phantom{\biggr)}}  +
\boxed{\phantom{\biggr(} 13b - 3b  \phantom{\biggr)}} +
\boxed{\phantom{\biggr(} a \phantom{\biggr)}}
$$

Regroup it like so

$$
\text{Number} =
\Biggr(
    13 \cdot 10^{n-2}k +
    13 \cdot 10^{n-3}m +
    \cdots +
    13 \cdot 10c +
    13b
\Biggr) -
\biggr(
    3 \cdot 10^{n-2}k +
    3 \cdot 10^{n-3}m +
    \cdots +
    3 \cdot 10c +
    3b
\biggr) +
    a
$$

Regroup those groups by `13`and `3` we get

$$
\text{Number} =
13 \Biggr(
    10^{n-2}k +
    10^{n-3}m +
    \cdots +
    10c +
    b
\Biggr) -
3 \biggr(
    10^{n-2}k +
    10^{n-3}m +
    \cdots +
    10c +
    b
\biggr) +
a
$$

Which realise is also a `portion` of that number in `base-10`

$$
\text{Number} =
13 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} \space -
3 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} +
a
$$

# Analysis of Remainder

Thus, we see that `this part` of the number is a `multiple of 13`
- Thus making it `divisible by 13`

$$
\textcolor{lightgray}{\text{Number} = }
    13 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}}
\space
\textcolor{lightgray}{-}
\space
\textcolor{lightgray}{
    3 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} + a
}
$$

Thus for the `whole number to be divisible by 13`,  this part also has to be a `multiple of 13`

$$
\textcolor{lightgray}{\text{Number} =
    13 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}}} \space -
    3 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} + a
$$

But it is still `2 expressions`, let us simplify it into `1 expression` instead

$$
\textcolor{lightgray}{\text{Number} =
    13 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}}} \space -
    \biggr( 3 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} - a \biggr)
$$

So that we can just look at the `absolute expression` instead

$$
\textcolor{lightgray}{\text{Number} =
    13 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} \space -}
    \biggr( 3 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} - a \biggr)
$$


Which is this

$$
\boxed{
    3 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} - a
}
$$

# Divisibility Rule 1


Thus, to determine if the `whole number is divisible by 13`,

$$
\boxed{
    \phantom{\biggr(}
        \underline{
            \textbf{3 times the number without the ones place}
        }
        \space
        \textbf{minus}
        \space
        \underline{\textbf{the number in the ones place}}
        \space
        \textbf{, must be divisible by 13}
    \phantom{\biggr)}
}
$$

# Finding a Better Rule

What if we let `a` be integrated into the `multiple of 13` such that we only have to look at what is `inside the brackets`?

$$
\textcolor{lightgray}{\text{Number} =
13 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} -
3 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} \space +} \space
a
$$

To not leave any parts behind,

We need `a` to be expressible in 2 parts where
- One part must `integrate into` the expression with `multiple 13`
- While the other `integrates into` the expression with `multiple 3`

Like so

$$
\textcolor{lightgray}{\text{Number} =
13 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} -
3 \cdot \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} \space +} \space
(13a - 3 \cdot 4a)
$$

Integrate into the expressions

$$
\textcolor{lightgray}{\text{Number} =
13 \Biggr(
    \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}}} + a
\textcolor{lightgray}{\Biggr)}
\textcolor{lightgray}{-
3 \biggr(
    \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}}} + 4a
\textcolor{lightgray}{\biggr)}
$$

And now we only need to look at `expression inside the brackets` here to determine `divisibility by 13`

$$
\textcolor{lightgray}{\text{Number} =
13 \Biggr(
   \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} + a
\Biggr) -
3 \biggr(}
    \underbrace{\overline{k \space m \space \cdots \space c \space b}}_{\text{n-1 places}} + 4a
\textcolor{lightgray}{\biggr)}
$$


Realise that it contains `all the digits of the number itself in order` up to the `n-1`-th place plus `4a`

$$
\boxed{
    \underbrace{\overline{k \space m \space \cdots \space c \space b \space}}_{\text{n-1 places}} + 4a
}
$$

# Divisibility Rule 2

Thus, to determine if the `whole number is divisible by 13`,


$$
\boxed{
    \phantom{\biggr(}
        \underline{
            \textbf{The number that doesn't include the ones place}
        }
        \space
        \textbf{plus}
        \space
        \underline{\textbf{4 times the number in the ones place}}
        \space
        \textbf{, must be divisible by 13}
    \phantom{\biggr)}
}
$$

---

### **Lets try partitioning more intensely instead and see if there is another way to tell**

---

# Intense Partitioning

Notice that `10` can be expressed in `13` and `3`

$$
\boxed{
    \phantom{\big(}
    10 = 13 - 3
    \phantom{\big)}
}
$$

If we move on to the `next power of 10`, we multiply by `10` to get this

$$
100 = 13 \cdot 10 - 3 \cdot \boxed{10}
$$

Notice that the single expression `10` is the only expression not in terms of `13`
- We can `split it` like how we did before

$$
\begin{align}
    100 &= \textcolor{lightgray}{13 \cdot 10} - 3 \cdot (13 - 3) \\
    &= 13 \cdot 10 - 13 \cdot 3 + 3 \cdot 3 \\
    &= 13 \cdot 10 - 13 \cdot 3 + 3^2 \\
\end{align}
$$

To get this

$$
\boxed{
    \phantom{\big(}
        100 = 13 \cdot 10 - 13 \cdot 3 + 3^2
    \phantom{\big)}
}
$$

Moving to the `next power of 10`, we have

$$
1000 = 13 \cdot 10^2 - 13 \cdot 3 \cdot 10 + 3^2 \cdot \boxed{10}
$$

Again, the expression `10` is the only expression not in terms of `11`
- We `split it`

$$
\begin{align}
    1000 &= 13 \cdot 10^2 - 13 \cdot 3 \cdot 10 + 3^2 \cdot (13 - 3) \\
    &= 13 \cdot 10^2 - 13 \cdot 3 \cdot 10 + 13 \cdot 3^2 - 3^2 \cdot 3 \\
    &= 13 \cdot 10^2 - 13 \cdot 3 \cdot 10 + 13 \cdot 3^2 - 3^3 \\
\end{align}
$$

And we get this

$$
\boxed{
    \phantom{\big(}
    1000 = 13 \cdot 10^2 - 13 \cdot 3 \cdot 10 + 13 \cdot 3^2 - 3^3
    \phantom{\big)}
}
$$

## Generalisation of Such Partitioning

Thus, we get this pattern that replicates itself from the `1st power onwards` up to some `n`

$$
\begin{align}
    10 &= 13 - 3 \\
    100 &= 13 \cdot 10 - 13 \cdot 3 + 3^2 \\
    1000 &= 13 \cdot 10^2 - 13 \cdot 3 \cdot 10 + 13 \cdot 3^2 - 3^3 \\
    &\vdots \\
        10^n &= 13 \cdot 3^0 \cdot 10^{n-1} - 13 \cdot 3^1 \cdot 10^{n-2} + \cdots \pm 13 \cdot 3^{n-1} \cdot 10^0 \mp 3^n \\
\end{align}
$$

We can further simplify the general expression as this

- **Overall**

$$
\boxed{
    10^n = 13 \biggr( 3^0 \cdot 10^{n-1} - 3^1 \cdot 10^{n-2} + \cdots \pm 3^{n-1} \cdot 10^{0} \biggr) \mp 3^{n}
}
$$

---

> Where if n is `odd`
>
> $$
\textcolor{lightgray}{
    10^n = 13 \biggr( 3^0 \cdot 10^{n-1} - 3^1 \cdot 10^{n-2} + \cdots
    }
    + 3^{n-1} \cdot 10^{0}
    \textcolor{lightgray}{\biggr)}
    - 3^{n}
$$
>
> Where if n is `even`
>
> $$
\textcolor{lightgray}{
    10^n = 13 \biggr( 3^0 \cdot 10^{n-1} - 3^1 \cdot 10^{n-2} + \cdots
    }
    - 3^{n-1} \cdot 10^{0}
    \textcolor{lightgray}{\biggr)}
    + 3^{n}
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
10^n = 13 \biggr( 3^0 \cdot 10^{n-1} - 3^1 \cdot 10^{n-2} + \cdots \pm 3^{n-1} \cdot 10^{0} \biggr) \mp 3^{n}
$$

## Simplifying the Expression

Actually, since we already know that this part is a `multiple of 11`

$$
\textcolor{lightgray}{10^n =} 13 \biggr( 3^0 \cdot 10^{n-1} - 3^1 \cdot 10^{n-2} + \cdots \pm 3^{n-1} \cdot 10^{0} \biggr) \textcolor{lightgray}{\mp} \textcolor{lightgray}{3^{n}}
$$

We can simplify the expression inside the brackets as such

> Where $q_{n} = 3^0 \cdot 10^{n-1} - 3^1 \cdot 10^{n-2} + \cdots \pm 3^{n-1} \cdot 10^{0}$


$$
\boxed{
    10^n = 13q_{n} \mp 3^n
}
$$

---

> Where if n is `odd`
>
> $$
\textcolor{lightgray}{
    10^n = 13q_{n}
} - 3^n
$$
>
> Where if n is `even`
>
> $$
\textcolor{lightgray}{
    10^n = 13q_{n}
} + 3^n
$$

---

## Algebraic Manipulation

We factor it in

$$
\text{Number} =
\space k \space \biggr( 13q_{n-1} \mp 3^{n-1} \biggr) +
m \space \biggr( 13q_{n-2} \pm 3^{n-2} \biggr) +
\cdots +
c \space \biggr( 13q_{2} + 3^{2} \biggr) +
b \space \biggr( 13q_{1} - 3^{1} \biggr) +
a
$$

Simplify it, and we get

$$
\text{Number} =
\boxed{ \phantom{\biggr(} 13k \cdot q_{n-1} \mp 3^{n-1} k \phantom{\biggr)}} +
\boxed{ \phantom{\biggr(} 13m \cdot q_{n-2} \pm 3^{n-2} m \phantom{\biggr)}} +
\cdots +
\boxed{\phantom{\biggr(} 13c \cdot q_{2} + 3^{2} c \phantom{\biggr)}}  +
\boxed{\phantom{\biggr(} 13b \cdot q_{1} - 3 b  \phantom{\biggr)}} +
\boxed{\phantom{\biggr(} a \phantom{\biggr)}}
$$

Regroup it like so

$$
\text{Number} =
\Biggr(
    13 \cdot kq_{n-1} +
    13 \cdot mq_{n-2} +
    \cdots +
    13 \cdot cq_{2} +
    13 \cdot bq_{1}
\Biggr) +
\biggr(
    \mp 3^{n-1} k
    \pm 3^{n-2} m
    \mp
    \cdots
    +
    3^{2} c
    -
    3 b
\biggr) +
a
$$

Regroup those groups by `13`, and we get

$$
\text{Number} =
    13 \Biggr(
        kq_{n-1} +
        mq_{n-2} +
        \cdots +
        cq_{2} +
        bq_{1}
    \Biggr) +
    \biggr(
        \mp 3^{n-1} k
        \pm 3^{n-2} m
        \mp
        \cdots
        +
        3^{2} c
        -
        3 b
    \biggr) +
    a
$$


---

> Where if `n is even`
>
> $$
\textcolor{lightgray}{
    \text{Number} =
        13 \Biggr(
            kq_{n-1} +
            mq_{n-2} +
            \cdots +
            cq_{2} +
            bq_{1}
        \Biggr) +
}
    \biggr(
        - 3^{n-1} k
        + 3^{n-2} m
        -
        \cdots
        +
        3^{2} c
        -
        3 b
    \biggr)
    \textcolor{lightgray}{+ a}
$$
>
> Where if `n is odd`
>
> $$
\textcolor{lightgray}{
    \text{Number} =
        13 \Biggr(
            kq_{n-1} +
            mq_{n-2} +
            \cdots +
            cq_{2} +
            bq_{1}
        \Biggr) +
}
    \biggr(
        3^{n-1} k
        - 3^{n-2} m
        +
        \cdots
        +
        3^{2} c
        -
        3 b
    \biggr)
    \textcolor{lightgray}{+a}
$$

---

# Re-Express the Place Values

Let the `place value` be expressed in terms of $f_h$ instead, where

$$
\text{Number}
= \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}}
= \underbrace{\overline{f_{n} \space f_{n-1} \space \cdots \space f_{3} \space f_{2} \space f_{1}}}_{\text{n places}}
$$

It is `easier to see the pattern` and `compress it` this way

$$
\text{Number} =
    13 \Biggr(
        f_n q_{n-1} +
        f_{n-1} q_{n-2} +
        \cdots +
        f_{3} q_{2} +
        f_{2} q_{1}
    \Biggr) +
    \biggr(
        \mp 3^{n-1} f_n
        \pm 3^{n-2} f_{n-1}
        \mp
        \cdots
        + 3^{2} f_{3}
        - 3^{1} f_{2}
    \biggr) +
    f_{1}
$$

---

> Where if `n is even`
>
> $$
\textcolor{lightgray}{
    \text{Number} =
        13 \Biggr(
                f_n q_{n-1} +
                f_{n-1} q_{n-2} +
                \cdots +
                f_3 q_{2} +
                f_2 q_{1}
            \Biggr) +
}
    \biggr(
        - 3^{n-1} f_{n}
        + 3^{n-2} f_{n-1}
        - \cdots
        + 3^{2} f_3
        - 3^{1} f_2
    \biggr)
    \textcolor{lightgray}{
        + f_1
    }
$$
>
> Where if `n is odd`
>
> $$
\textcolor{lightgray}{
    \text{Number} =
        13 \Biggr(
            f_n q_{n-1} +
            f_{n-1} q_{n-2} +
            \cdots +
            f_3 q_{2} +
            f_2 q_{1}
        \Biggr) +
}
    \biggr(
        3^{n-1} f_{n}
        - 3^{n-2} f_{n-1}
        + \cdots
        + 3^{2} f_3
        - 3^{1} f_2
    \biggr)
    \textcolor{lightgray}{
        + f_1
    }
$$

---

# Group the Coefficients by Power of 3

And we get the overall expression of

> Where $\text{odd} = 2d + 1$, $d \in \mathbf{Z}$

$$
\boxed{
    \text{Number} =
        13 \Biggr(
            f_n q_{n-1} +
            f_{n-1} q_{n-2} +
            \cdots +
            f_{3} q_{2} +
            f_{2} q_{1}
        \Biggr) +
            \biggr(
                \sum_{h=2}^{n}
                    \underline{
                        (-1)^{h + \text{odd}} \space 3^{h-1} f_h
                    }
                    + f_1
            \biggr)
}
$$

# Analysis of Remainder

Thus, we see that `this part` of the number is a `multiple of 13`

$$
\textcolor{lightgray}{\text{Number} = }
    13 \Biggr(
        f_n q_{n-1} +
        f_{n-1} q_{n-2} +
        \cdots +
        f_{3} q_{2} +
        f_{2} q_{1}
    \Biggr)
\textcolor{lightgray}{+}
\textcolor{lightgray}{
    \biggr(
        \sum_{h=2}^{n}
            \underline{
                (-1)^{h + \text{odd}} \space 3^{h-1} f_h
            }
            + f_1
    \biggr)
}
$$

Thus for the `whole number to be divisible by 13`,  this part also has to be a `multiple of 13`

$$
\textcolor{lightgray}{\text{Number} =
    13 \Biggr(
        f_n q_{n-1} +
        f_{n-1} q_{n-2} +
        \cdots +
        f_{3} q_{2} +
        f_{2} q_{1}
    \Biggr)
}
\textcolor{lightgray}{+}
    \textcolor{lightgray}{\biggr(}
        \sum_{h=2}^{n}
            \underline{
                (-1)^{h + \text{odd}} \space 3^{h-1} f_h
            }
            + f_1
    \textcolor{lightgray}{\biggr)}
$$

Which is the `alternating sum` of `(place - 1)-th power of 3` multiplied by its `place value` from the `2nd place onwards`, then plus the `place value` in the `ones place`

$$
\boxed{
    \phantom{\big(}
        \sum_{h=2}^{n}
            \underline{
                (-1)^{h + \text{odd}} \space 3^{h-1} f_h
            }
            + f_1
    \phantom{\big)}
}
$$

# Divisibility Rule 3

Thus, to determine if the `whole number is divisible by 13`,


$$
\boxed{
    \phantom{\biggr(}
        \textbf{Alternating Sum of:}
        \space
        \underline{
            \textbf{Power of 3 at one less than its place}
        }
        \space
        \textbf{multiplied by}
        \space
        \underline{\textbf{its place value}}
        \space
        \textbf{, plus}
        \space
        \underline{\textbf{ones place}}
        \space
        \textbf{, must be divisible by 13}
    \phantom{\biggr)}
}
$$
