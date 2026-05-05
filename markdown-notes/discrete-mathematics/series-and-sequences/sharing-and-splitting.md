---
title: "Motivation"
source_notebook: "discrete-mathematics/series-and-sequences/sharing-and-splitting.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Motivation

This jupyter notebook is motivated to understand why this pattern is true:

$$
\begin{align}
    1 + 2 &= 3 \\
    4 + 5 + 6 &= 7 + 8 \\
    9 + 10 + 11 + 12 &= 13 + 14 + 15 \\
    & \vdots
\end{align}
$$

# Partitioning and Sharing
An Integer

$$
12
$$

Can be split into different parts

$$
\begin{align}
    12 &= 2 + 2 + 8 \\
    &= 1 + 5 + 6 \\
    &= 1 + 1 + 1 + 1 + 1 + 7 \\
    &= \cdots
\end{align}
$$

This is called `partitioning`, in fact, there are `77 ways` to partition `12`!
> That will take forever to list out here!

We also may have more than `1` integer together

$$
5 + 13 + 9
$$

We can split any of the terms, but lets say the first term, into integer parts, and share it to the other terms like so

- Split `5` into `n-1 parts`, where `n` is the total number of terms

$$
\underline{(2 + 3)} + \underline{13} + \underline{9}
$$

- Then distribute it in however way you want

$$
\underline{\textcolor{lightgray}{0}} + \underline{13 + \boxed{2}} + \underline{9 + \boxed{3}}
$$

- To get this

$$
\underline{\textcolor{lightgray}{0}} + \underline{15} + \underline{12}
$$

# Identity - Partition Regrouping of a Sum

Notice we have actually proven an identity of

$$
\boxed{
    \phantom{\biggr(}
    5 + 13 + 9 = 15 + 12
    \phantom{\biggr)}
}
$$

Or further, that in a `series of integers` like this, with `n` terms

$$
\underbrace{a + b + c + d + \cdots + g}_{\text{n terms}}
$$

If any of its integers can be broken into `n-1` integer parts
> Lets say the `first integer`

$$
a = \underbrace{a_1 + a_2 + a_3 + \cdots + a_{n-1}}_{\text{n-1 terms}}
$$

Then the original series of integers can `share those parts` and turn into a series with `1 fewer term`

$$
\underline{\textcolor{lightgray}{0}} + \underbrace{\boxed{b + a_1} + \boxed{c + a_2} + \boxed{d + a_3} + \cdots + \boxed{g + a_{n-1}}}_{\text{n-1 terms}}
$$

Thus, establishing this identity

$$
\boxed{
    \phantom{\Biggr(}
    \underbrace{a + b + c + d + \cdots + g}_{\text{n terms}} = \underline{\textcolor{lightgray}{0}} + \underbrace{\boxed{b + a_1} + \boxed{c + a_2} + \boxed{d + a_3} + \cdots + \boxed{g + a_{n-1}}}_{\text{n-1 terms}}
    \phantom{\Biggr)}
}
$$

# Maximum Partitions

Furthering this concept, we notice that

> The `maximum length` of an `integers' partition` will determine the `maximum amount of terms` it can `share its parts` with.

This maximum length is just the integer itself, since it can be split into parts of `1`
- Take `13` for example

$$
\text{Maximum Terms to Distribute for} \space 13 = \underbrace{1 + 1 + 1 + \cdots + 1 + 1}_{\text{13 times}} = 13 \space \text{Terms}
$$

# Uniform Partitions
What if we want to split it evenly between the other terms?

- For example

$$
\underline{9} + \underline{4} + \underline{5} + \underline{7}
$$

- Where `9` is split evenly into `3 parts`

$$
\underline{\textcolor{lightgray}{0}} + \underline{(4 + \boxed{3})} + \underline{(5 + \boxed{3})} + \underline{(6 + \boxed{3})}
$$

- To get this

$$
\underline{\textcolor{lightgray}{0}} + \underline{7} + \underline{8} + \underline{9}
$$


Thus establishing this

$$
\boxed{
    \phantom{\biggr(}
    9 + 4 + 5 + 6 = 7 + 8 + 9
    \phantom{\biggr)}
}
$$

# Arithmetic Series Observation

Notice this

$$
\underline{\textcolor{lightgray}{9} + 4 + 5 + 6} = \underline{7 + 8 + 9}
$$

## Multiples of Common Difference

The series with `common difference 1`

$$
\underline{\textcolor{lightgray}{9} + 4 + 5 + 6} = \underline{\textcolor{lightgray}{7 + 8 + 9}}
$$

Was shifted by the `same amount`, `3`, thus `keeping their difference common`

$$
\underline{\textcolor{lightgray}{9 + 4 + 5 + 6}} = \underline{7 + 8 + 9}
$$

And because the `shift amount: 3` is a `whole multiple` of the `common difference`,
> This results in a shift to a `later portion` of that series, in this case, it's the `natural number series`

$$
1, \space 2 \space, \space 3 \space, \underline{\space 4 \space, \space 5 \space, \space 6 \space}, \underline{\space 7 \space, \space 8 \space, \space 9 \space}, \space 10 \space, \space 11 \space, \space 12 \space, \space 13 \space \cdots
$$

## Non-Multiples of Common Difference

Lets go over the scenario where `shift amount` is `not a whole multiple of the common difference`

- For example starting with `3`, common difference `2`, with `3` more terms

$$
3 + 5 + 7 + 9
$$

- Split and Share

$$
\textcolor{lightgray}{0} + \underline{5 + \boxed{1}} + \underline{7 + \boxed{1}} + \underline{9 + \boxed{1}}
$$


- To get this

$$
\textcolor{lightgray}{0} + 6 + 8 + 10
$$


Thus, resulting in a shift to a `different series of the same common difference` of that series, by `shift amount within that new series`

$$
\boxed{
    \phantom{\biggr(}
    3 + 5 + 7 + 9 = 6 + 8 + 10
    \phantom{\biggr)}
}
$$

# Identity - Uniform Partition Regrouping of an Arithmetic Sum

In an arithmetic series

$$
\underbrace{
    \boxed{
        \phantom{\big(}
        a
        \phantom{\big)}
        } +
    \boxed{
        \phantom{\big(}
        a+d
        \phantom{\big)}
        } +
    \boxed{
        \phantom{\big(}
        a+2d
        \phantom{\big)}
        } +
    \boxed{
        \phantom{\big(}
        a+3d
        \phantom{\big)}
        } +
    \cdots +
    \boxed{
        \phantom{\big(}
        a+(n-1)d
        \phantom{\big)}
        }
    }_{\text{n terms}}
$$

We can re-express the series in terms of its terms
> Where $T_n = a + (n-1)d$

$$
\underbrace{T_1 + T_2 + T_3 + T_4 + ... + T_n}_{\text{n terms}}
$$

If the number of terms after `a`, is equal to a `factor of a`
- We can distribute the `factors of a` into an `arithmetic sum` like so

> Where $q = \dfrac{a}{n-1}$

$$
\underbrace{
    \boxed{
        \phantom{\big(}
        a
        \phantom{\big)}
        } +
    \boxed{
        \phantom{\big(}
        a+d
        \phantom{\big)}
        } +
    \boxed{
        \phantom{\big(}
        a+2d
        \phantom{\big)}
        } +
    \boxed{
        \phantom{\big(}
        a+3d
        \phantom{\big)}
        } +
    \cdots +
    \boxed{
        \phantom{\big(}
        a+(n-1)d
        \phantom{\big)}
        }
}_{\text{n terms}} =
\underline{\textcolor{lightgray}{0}} +
\underbrace{
    \boxed{
        \phantom{\big(}
        a+d + \mathbf{q}
        \phantom{\big)}
        } +
    \boxed{
        \phantom{\big(}
        a+2d + \mathbf{q}
        \phantom{\big)}
        } +
    \boxed{
        \phantom{\big(}
        a+3d + \mathbf{q}
        \phantom{\big)}
        } +
    \cdots +
    \boxed{
        \phantom{\big(}
        a+(n-1)d + \mathbf{q}
        \phantom{\big)}
        }
    }_{\text{n-1 terms}}
$$

Thus when we simplify it, we find

$$
\boxed{
    \phantom{\Biggr(}
    \underbrace{T_1 + T_2 + T_3 + T_4 + \cdots + T_n}_{\text{n terms}} =
        \underline{\textcolor{lightgray}{0}} +
        \underbrace{
            \boxed{
                \phantom{\big(}
                T_2 + \mathbf{q}
                \phantom{\big)}
                } +
            \boxed{
                \phantom{\big(}
                T_3 + \mathbf{q}
                \phantom{\big)}
                } +
            \boxed{
                \phantom{\big(}
                T_4 + \mathbf{q}
                \phantom{\big)}
                } +
            \cdots +
            \boxed{
                \phantom{\big(}
                T_n + \mathbf{q}
                \phantom{\big)}
                }
                }_{\text{n-1 terms}
            }
    \phantom{\Biggr)}
}
$$

# Dissecting the Identity

We come back to this identity

$$
\begin{align}
    1 + 2 &= 3 \\
    4 + 5 + 6 &= 7 + 8 \\
    9 + 10 + 11 + 12 &= 13 + 14 + 15 \\
    & \vdots
\end{align}
$$

## Establishing the Simple Pattern

Lets start from `0`,
- Although `0` has `uncountably infinite factors`, it `cannot be split into things to share`, because it is `nothing`

$$
0 = 0
$$

So we have to start from its successor: `1`
- Now `1` only has itself, thus it can only be partitioned into one other thing

Lets also start from an `arithmetic series` with `common difference 1` as well, to match the identity we are trying to understand

$$
1 + 2
$$


So we share

$$
\textcolor{lightgray}{0} + (2+1)
$$

And get

$$
\textcolor{lightgray}{0} + 3
$$

Thus, we have the fundamental

$$
\boxed{
    \phantom{\big(}
    1 + 2 = 3
    \phantom{\big)}
}
$$

# Finding Patterns

Notice that in the identity,

- The `number of terms on each side` actually `increases by 1 per iteration`, and
- The `total number of terms` in the `input sum` is exactly `one more than the row number`

$$
\begin{align}
    1 + 2 &= 3 \\
    4 + 5 + 6 &= 7 + 8 \\
    9 + 10 + 11 + 12 &= 13 + 14 + 15 \\
    & \vdots
\end{align}
$$

Meaning that the `number of terms to share, and equally the number of partitions, is exactly the row number itself`
- Increasing steadily by `1` from `1`

Since every row is as such

$$
\text{Row r:} \underbrace{\cdots}_{\text{r+1 terms}} = \underbrace{\cdots}_{\text{r terms}}
$$

Thus, we can mark the contributions per row

$$
\begin{align}
    \text{Every row contributes} \space
    &= \underline{r + 1} + \underline{r} \\
    &= 2r + 1
\end{align}
$$

> Thus every row contributes `2r + 1` terms into the `natural number series`, which means every row contributes an odd number

# Continuation

In order to find out how this will continue, we first need to `find what number starts in the next row`
> Where `m` is the current row

$$
\text{Number that Starts in the} \space (m+1)^{th} \space \text{row}
$$

We can find the number through its position in the natural numbers
- Which is **the same as the number itself!**

$$
\text{Number that Starts in the} \space (m+1)^{th} \space \text{row} = \text{Position in the natural numbers}
$$

Which the position can be found like this

$$
\text{Number that Starts in the} \space (m+1)^{th} \space \text{row} \space = \text{How many terms has been gone through} + 1
$$

Since every row contributes `2r + 1` terms, we just need to sum `2r + 1` up to the current row
- `r` ranges from `1` to the current row `m`

$$
\begin{align}
    \text{Number that Starts in the} \space (m+1)^{th} \space \text{row} \space &= \boxed{\sum_{r=1}^m \underline{2r+1}} + 1 \\
    &= \boxed{2 \sum_{r=1}^m r + \sum_{r=1}^m 1} + 1\\
    &= \boxed{\cancel{2} \cdot \dfrac{m(m+1)}{\cancel{2}} + m} + 1 \\
    &= \boxed{m(m+1) + m} + 1 \\
    &= \boxed{m^2 + m + m} + 1 \\
    &= \boxed{m^2 + 2m} + 1 \rightarrow \text{Let's make this nicer by completing the square} \\
    &= \boxed{(m+1)^2 - 1} + 1 \\
    &= (m+1)^2 \\
\end{align}
$$

Thus we find that `number starting in the row` is exactly the `row squared`

$$
\text{Number that Starts in the} \space (m+1)^{th} \space \text{row} = (m+1)^2
$$

Which can be simplified like this

$$
\text{Number that Starts in the} \space m^{th} \space \text{row} = m^2
$$

# General Pattern for Common Difference 1

Since `each row` opens with the `number` that is exactly the `row squared`,

Which means each `row m`, can be modelled like this:

> Where $m_1 = m^2$

$$
\boxed{
    \phantom{\Biggr(}
    \phantom{\Biggr(}
    \overbrace{
        \underline{m_1} +
        \underbrace{
            \underline{m_1 + \boxed{1}} +
            \underline{m_1 + \boxed{2}} +
            \cdots +
            \underline{m_1 + \boxed{m}}
            }_{\text{m terms}}
    }^{m+1 \space \text{terms}} =
    \underbrace{
        \underline{m_1 + \boxed{m + 1}} +
        \underline{m_1 + \boxed{m + 2}} +
        \cdots +
        \underline{
            m_1 +
            \overbrace{
                \boxed{m + m}
            }^{\text{2m}}
        }
    }_{\text{m terms}}
    \phantom{\Biggr)}
    \phantom{\Biggr(}
}
$$


With this pattern derived, this series will continue on in this fashion forever:

$$
\begin{align}
    1 + 2 &= 3 \\
    4 + 5 + 6 &= 7 + 8 \\
    9 + 10 + 11 + 12 &= 13 + 14 + 15 \\
    16 + 17 + 18 + 19 + 20 &= 21 + 22 + 23 + 24 \\
    & \vdots \\
    \overbrace{
        \underline{m_1} +
        \underbrace{
            \underline{m_1 + \boxed{1}} +
            \underline{m_1 + \boxed{2}} +
            \cdots +
            \underline{m_1 + \boxed{m}}
            }_{\text{m terms}}
    }^{m+1 \space \text{terms}} &=
    \underbrace{
        \underline{m_1 + \boxed{m + 1}} +
        \underline{m_1 + \boxed{m + 2}} +
        \cdots +
        \underline{
            m_1 +
            \overbrace{
                \boxed{m + m}
            }^{\text{2m}}
        }
    }_{\text{m terms}}
\end{align}
$$
