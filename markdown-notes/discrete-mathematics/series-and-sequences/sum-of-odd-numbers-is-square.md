---
title: "Sum Of Odd Numbers Is Square"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-odd-numbers-is-square.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

## (Sum of Odd Numbers -> Square) Identity
We have this interesting observation

$$
\begin{align}
    1 &= \space \space 1 \rightarrow 1^{2} \\
    1 + 3 &= \space \space 4 \rightarrow 2^{2} \\
    1 + 3 + 5 &= \space \space 9 \rightarrow 3^{2} \\
    1 + 3 + 5 + 7 &= 16 \rightarrow 4^{2} \\
    1 + 3 + 5 + 7 + 9 &= 25 \rightarrow 5^{2} \\
    1 + 3 + 5 + 7 + 9 + 11 &= 36 \rightarrow 6^{2} \\
    1 + 3 + 5 + 7 + 9 + 11 + 13 &= 49 \rightarrow 7^{2} \\
    1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 &= 64 \rightarrow 8^{2} \\
\end{align}
$$

It seems that the sum of odd numbers is equal to the square of that iteration at that point, so let's prove if its true!

---

We start from this:

$$
\sum_{k=1}^n (2k - 1)
$$

Expand and Simplify

$$
\begin{align*}
    \sum_{k=1}^n (2k - 1) &= 2\sum_{k=1}^n k - \sum_{k=1}^n 1 \\
    &= \cancel{2} \cdot \dfrac{n(n+1)}{\cancel{2}} - n \\
    &= (n^2 + \cancel{n}) - \cancel{n} \\
    &= n^2
\end{align*}
$$

Thus we have proven this cool identity!

$$
\boxed{\sum_{k=1}^n (2k - 1) = n^2}
$$

#### <center>The sum of odd numbers up to n is the square at that point $n^2$

Thus, this also describes the square numbers

$$
1, 4, 9, 16, \cdots, n^2
$$
