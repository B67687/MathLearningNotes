---
title: "Sum Of Reciprocal Triangle Numbers"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-reciprocal-triangle-numbers.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/sum-of-reciprocal-triangle-numbers.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

Lets find the `sum` of `reciprocal triangle numbers`

$$
\dfrac{1}{1} + \dfrac{1}{1+2} + \dfrac{1}{1+2+3} + \cdots + \dfrac{1}{1+2+3+\cdots+n}
$$

It can be expressed like so using the formula for triangle numbers

$$
\sum_{k=1}^n \dfrac{1}{\left( \dfrac{k(k+1)}{2} \right) }
$$

Which when we `simplify the fraction` turns into this

$$
\sum_{k=1}^n \dfrac{2}{k(k+1)}
$$

And with the `constant factored out`

$$
2 \sum_{k=1}^n \dfrac{1}{k(k+1)}
$$

Focusing on this sum

$$
\textcolor{lightgray}{2} \sum_{k=1}^n \dfrac{1}{k(k+1)}
$$

We derived in another notebook:
> The `sum of reciprocal 2 consecutive multiples` is this

$$
\sum_{k=1}^n \dfrac{1}{k(k+1)} = \dfrac{n}{n+1}
$$

Thus, `twice of that` is equal to this

$$
2 \sum_{k=1}^n \dfrac{1}{k(k+1)} = 2 \cdot \dfrac{n}{n+1}
$$

Which is

$$
2 \sum_{k=1}^n \dfrac{1}{k(k+1)} = \dfrac{2n}{n+1}
$$

Thus, the `sum of reciprocal triangle numbers` is
- Where `n` is the `n-th` triangle number

$$
\boxed{
    \text{Sum of Reciprocal Triangle Numbers}  = \dfrac{2n}{n+1}
}
$$
