---
title: "Sum of Consecutive Multiples"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-consecutive-multiples.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/sum-of-consecutive-multiples.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Sum of Consecutive Multiples

We have

$$
\sum_{k=1}^n k(k+1)
$$

Let's start

$$
\begin{align*}
    \sum_{k=1}^n k(k+1) &= \sum_{k=1}^n \underline{k^2 + k} \\
    &= \sum_{k=1}^n k^2 + \sum_{k=1}^n k \\
    &= \dfrac{n(n+1)(2n+1)}{6} + \dfrac{n(n+1)}{2} \\
    &= \dfrac{n(n+1)(2n+1)}{6} + \dfrac{3n(n+1)}{6} \\
    &= \dfrac{n(n+1)[(2n+1) + 3]}{6} \\
    &= \dfrac{n(n+1)(2n+4)}{6} \\
    &= \dfrac{2n(n+1)(n+2)}{6} \\
    &= \dfrac{n(n+1)(n+2)}{3} \\
\end{align*}
$$

Therefore

$$
\boxed{
     \sum_{k=1}^n k(k+1) = \dfrac{n(n+1)(n+2)}{3}
}
$$

# Additional Insights

Also know that the `k(k+1)` is itself the sum of even numbers

$$
k(k+1) = \sum_{j=1}^k 2j
$$

And same thing for `n(n+1)`, just expressed differently

$$
n(n+1) = \sum_{k=1}^n 2k
$$

Thus these parts are the sum of even numbers

$$
\textcolor{lightgray}{\sum_{k=1}^n} k(k+1) \textcolor{lightgray}{=} \dfrac{n(n+1)\textcolor{lightgray}{(n+2)}}{\textcolor{lightgray}{3}}
$$

It can broken like this

$$
\textcolor{lightgray}{\sum_{k=1}^n} k(k+1) \textcolor{lightgray}{=} \textcolor{lightgray}{\dfrac{(n+2)}{3}} \cdot n(n+1)
$$

Substitute in the relevant representations

$$
\textcolor{lightgray}{\sum_{k=1}^n} \sum_{j=1}^k 2j \textcolor{lightgray}{=} \textcolor{lightgray}{\dfrac{(n+2)}{3}} \cdot \sum_{k=1}^n 2k
$$

And we have this

$$
\sum_{k=1}^n \sum_{j=1}^k 2j = \dfrac{(n+2)}{3} \cdot \sum_{k=1}^n 2k
$$

Thus we know that

$$
\underline{\text{The sum of the sum of even numbers}} \space = \dfrac{(n+2)}{3} \times \underline{\text{The sum of even numbers}}
$$

Refine the language
$$
\boxed{
    \underline{\text{The 2-nd order sum of even numbers}} \space = \dfrac{(n+2)}{3} \times \underline{\text{The 1st-order sum of even numbers}}
}
$$
