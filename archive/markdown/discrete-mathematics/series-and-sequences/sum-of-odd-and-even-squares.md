---
title: "Sum of Squares"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-odd-and-even-squares.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/sum-of-odd-and-even-squares.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Sum of Squares

The sums of squares formula is as such

$$
\sum_{k=1}^n k^2 = \dfrac{n(n+1)(2n+1)}{6}
$$

# Sum of Even Squares

The sum of even squares is like this

$$
\sum_{k=1}^n (2k)^2
$$

Which when be separate it into parts, we get

$$
\begin{align}
    \sum_{k=1}^n (2k)^2 &= \sum_{k=1}^n 4k^2 \\
    &= 4 \sum_{k=1}^n k^2
\end{align}
$$

Then substitute the sum of square formula, we have

$$
\begin{align}
    4 \sum_{k=1}^n k^2 &= 4 \cdot \dfrac{n(n+1)(2n+1)}{6} \\
    &= \dfrac{2n(n+1)(2n+1)}{3}
\end{align}
$$

Thus, the `sum of even squares` up to the `n-th even number` is as such:

$$
\boxed{
    \sum_{k=1}^n (2k)^2 = \dfrac{2n(n+1)(2n+1)}{3}
}
$$

# Sum of Odd Squares

The sum of odd squares is like this

$$
\sum_{k=1}^n (2k-1)^2
$$

We could expand it out and do simplification

$$
\begin{align}
    \sum_{k=1}^n (2k-1)^2 &= \sum_{k=1}^n 4k^2 -4k + 1 \\
    &= 4 \sum_{k=1}^n k^2 -4 \sum_{k=1}^n k + \sum_{k=1}^n 1 \\
    \\
    &= 4 \cdot \dfrac{n(n+1)(2n+1)}{6} - 4 \cdot \dfrac{n(n+1)}{2} + n \\
    \\
    &= \dfrac{2n(n+1)(2n+1)}{3} - 2n(n+1) + n \\
    \\
    &= \dfrac{2n(n+1)(2n+1)-6n(n+1)+3n}{3} \\
    \\
    &= \dfrac{(2n^2 + 2n)(2n+1) -6n^2 - 6n +3n}{3} \\
    \\
    &= \dfrac{\boxed{4n^3 + 2n^2 + 4n^2 + 2n} \space \boxed{- 6n^2 - 6n} \space \boxed{+ 3n}}{3} \\
    \\
    &= \dfrac{4n^3 + \boxed{2n^2 + 4n^2 - 6n^2} + \boxed{2n - 6n + 3n}}{3} \\
    \\
    &= \dfrac{4n^3 - n}{3} \\
    \\
    &= \dfrac{n(4n^2 - 1)}{3} \\
\end{align}
$$

Thus, the `sum of odd squares` up to the `n-th odd number` is as such:

$$
\boxed{
    \sum_{k=1}^n (2k-1)^2 = \dfrac{n(4n^2 - 1)}{3}
}
$$
