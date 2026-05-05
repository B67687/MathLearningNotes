---
title: "Symmetric Sum"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-squares/sum-of-squares-with-symmetric-sum.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Symmetric Sum

Lets find the sum of squares

$$
\sum_{k=1}^{n} k^2
$$

When expanded out, it looks like this

$$
\sum_{k=1}^n k^2 = 1^2 + 2^2 + 3^2 + ... + n^2
$$

# Squares

Remember that squares are also the sum of odd numbers up to that point,
- $n^2$ is the sum up to the `n-th odd number`, in the form of `2n-1`, from `1` to `n`

$$
\sum_{k=1}^n k^2 = \boxed{1} + \boxed{1 + 3} + \boxed{1 + 3 + 5} + ... + \boxed{1 + 3 + 5 + \cdots + 2n-1}
$$

# Symmetric Sum
Remember also that the sum of odd numbers is equal to an odd-length symmetric sum
- `1` up to `n`, and back down to `1`

$$
\sum_{k=1}^n k^2 = \boxed{1} + \boxed{1 + 2 + 1} + \boxed{1 + 2 + 3 + 2 + 1} + ... + \boxed{1 + 2 + 3 + \cdots + n + \cdots + 3 + 2 + 1}
$$

Arrange it vertically, we have

$$
\sum_{k=1}^n k^2 =
\begin{array}{c}
    & 1 \\
    & 1 & 2 & 1\\
    & 1 & 2 & 3 & 2 & 1 \\
    & 1 & 2 & 3 & 4 & 3 & 2 & 1 \\
    & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\
    & 1 & 2 & 3 & 4 & 5 & 6 & 7 & \cdots & n & \cdots & 5 & 4 & 3 & 2 & 1 \\
\end{array}
$$

# Sum of Triangle Numbers

Notice on the `ascending portion` of each symmetric sum, we have the `arithmetic sums` up to `n`

$$
\sum_{k=1}^n k^2 =
\begin{array}{c}
    & 1 \\
    & 1 & 2 & \textcolor{lightgray}{1}\\
    & 1 & 2 & 3 &  \textcolor{lightgray}{2} &  \textcolor{lightgray}{1} \\
    & 1 & 2 & 3 & 4 &  \textcolor{lightgray}{3} &  \textcolor{lightgray}{2} &  \textcolor{lightgray}{1} \\
    & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots &  \textcolor{lightgray}{\ddots} \\
    & 1 & 2 & 3 & 4 & 5 & 6 & 7 & \cdots & n &  \textcolor{lightgray}{\cdots} &  \textcolor{lightgray}{5} &  \textcolor{lightgray}{4} &  \textcolor{lightgray}{3} &  \textcolor{lightgray}{2} &  \textcolor{lightgray}{1} \\
\end{array}
$$

On the `descending portion` of each symmetric sum, we have the `arithmetic sums` up to `n-1`

$$
\sum_{k=1}^n k^2 =
\begin{array}{}
    & \textcolor{lightgray}{1} \\
    & \textcolor{lightgray}{1} & \textcolor{lightgray}{2} & 1\\
    & \textcolor{lightgray}{1} & \textcolor{lightgray}{2} & \textcolor{lightgray}{3} & 2 & 1 \\
    & \textcolor{lightgray}{1} & \textcolor{lightgray}{2} & \textcolor{lightgray}{3} & \textcolor{lightgray}{4} & 3 & 2 & 1 \\
    & \textcolor{lightgray}{\vdots} & \textcolor{lightgray}{\vdots} & \textcolor{lightgray}{\vdots} & \textcolor{lightgray}{\vdots} & \textcolor{lightgray}{\vdots} & \textcolor{lightgray}{\vdots} & \textcolor{lightgray}{\vdots} & \ddots \\
    & \textcolor{lightgray}{1} & \textcolor{lightgray}{2} & \textcolor{lightgray}{3} & \textcolor{lightgray}{4} & \textcolor{lightgray}{5} & \textcolor{lightgray}{6} & \textcolor{lightgray}{7} & \textcolor{lightgray}{\cdots} & \textcolor{lightgray}{n} & \underline{n-1} & \cdots & 5 & 4 & 3 & 2 & 1 \\
\end{array}
$$

The `sum of squares` is thus the same as the `sum of the arithmetic sums` up to `n` plus the `sum of the arithmetic sum` up to `n-1`

$$
\sum_{k=1}^n k^2 =
\begin{array}{c}
    & 1 \\
    & 1 & 2 \\
    & 1 & 2 & 3 \\
    & 1 & 2 & 3 & 4 \\
    & \vdots & \vdots & \vdots & \vdots & \ddots \\
    & 1 & 2 & 3 & 4 & 5 & 6 & 7 & \cdots & \underline{n-1} & \underline{n} \\
\end{array}
+
\begin{array}{c}
    & \\
    & 1 \\
    & 1 & 2 \\
    & 1 & 2 & 3 \\
    & \vdots & \vdots & \vdots & \vdots & \ddots \\
    & 1 & 2 & 3 & 4 & 5 & 6 & 7 & \cdots & \underline{n-1} \\
\end{array}
$$

Arithmetic sums are also called triangular numbers, due to how they procedurally form bigger and bigger triangles
- Thus, the `sum of squares` is made up of the `2 sums of triangle numbers`,
- One from `1` to `n`
- The other from `1` to `n-1`

We know the sums of triangle numbers as

$$
\sum_{k=1}^n \text{Triangle Numbers} = \dfrac{n(n+1)(n+2)}{6}
$$

# Algebraic Manipulation

Thus, the `sum of squares` is as such

$$
\sum_{k=1}^n k^2 = \dfrac{n(n+1)(n+2)}{6} + \dfrac{\boxed{n-1}(\boxed{n-1}+1)(\boxed{n-1}+2)}{6}
$$

Further simplify it

$$
\begin{align}
    \sum_{k=1}^n k^2 &= \dfrac{n(n+1)(n+2)}{6} + \dfrac{(n-1)n(n+1)}{6} \\
    &= \textcolor{lightgray}{\dfrac{n(n+1)(n+2)}{6}} + \dfrac{n(n+1)(n-1)}{6} \\
    &= \dfrac{n(n+1)(\boxed{n+2} + \boxed{n-1})}{6} \\
    &= \dfrac{n(n+1)(2n+1)}{6}
\end{align}
$$

# Conclusion
And there we have it! The `sum of squares` formula!

$$
\sum_{k=1}^n k^2 = \dfrac{n(n+1)(2n+1)}{6}
$$
