---
title: "Symmetric Sum"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-squares/sum-of-squares-with-stack-of-symmetric-sums.ipynb"
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
    & & & & & & \quad 1 \quad & & & & & &\\
    & & & & & 1 & \quad 2 \quad & 1 & & & & &\\
    & & & & 1 & 2 & \quad 3 \quad & 2 & 1 & & & & \\
    & & & 1 & 2 & 3 & \quad 4 \quad & 3 & 2 & 1 & & &\\
    & & & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & & & \\
    & \quad 1 \quad & \ \cdots \ & \underline{n-3} & \underline{n-2} & \underline{n-1} & \underline{\quad n \quad} & \underline{n-1} & \underline{n-2} & \underline{n-3} & \ \cdots \ & \quad 1 \quad & \\
\end{array}
$$

Split it vertically, and we see arithmetic sums

$$
\sum_{k=1}^n k^2 =
\begin{array}{c|c|c|c|c|c}
    & & & & & & \quad 1 \quad & & & & & &\\
    & & & & & 1 & \quad 2 \quad & 1 & & & & &\\
    & & & & 1 & 2 & \quad 3 \quad & 2 & 1 & & & & \\
    & & & 1 & 2 & 3 & \quad 4 \quad & 3 & 2 & 1 & & &\\
    & & & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & & & \\
    & \quad 1 \quad & \ \ \cdots \ \ & \underline{n-3} & \underline{n-2} & \underline{n-1} & \underline{\quad n \quad} & \underline{n-1} & \underline{n-2} & \underline{n-3} & \ \ \cdots \ \ & \quad 1 \quad & \\
\end{array}
$$

# Arithmetic Sum

Thus, we can express the `sum of squares` in terms of `arithmetic sums` like this

$$
\begin{align}
    \sum_{k=1}^n k^2 &= \quad \ \ \biggr(  1 + 2 + \cdots + \underline{n-2} + \underline{n-1} + n \biggr) \\
    & \ \ \ + \space 2 \space \biggr( 1 + 2 + \cdots + \underline{n-2} + \underline{n-1} \biggr) \\
    & \ \ \ + \space 2 \space \biggr( 1 + 2 + \cdots + \underline{n-2} \biggr) \\
    & \ \ \ + \space \vdots \\
    & \ \ \ + \space 2 \space \biggr( 1 \biggr)
\end{align}
$$

Simplify the expression into `summation notation` which expresses the `sum of arithmetic sums` up to some `j`

$$
\begin{align}
    \sum_{k=1}^n k^2 &= \quad \biggr(  1 + 2 + \cdots + \underline{n-2} + \underline{n-1} + n \biggr) \\
    & \ \ \ + \space 2 \sum_{j=1}^{n-1} \Biggr( \sum_{k=1}^{j} k \Biggr)
\end{align}
$$

Substitute the `formula for arithmetic sums`

$$
\sum_{k=1}^n k^2 = \dfrac{n \space (n+1)}{2} + \space 2 \sum_{j=1}^{n-1} \dfrac{j \space (j+1)}{2}
$$

Take out the `constant`

$$
\sum_{k=1}^n k^2 = \dfrac{n \space (n+1)}{2} + \space \cancel{2} \cdot \dfrac{1}{\cancel{2}} \sum_{j=1}^{n-1} j \space (j+1)
$$

Substitute the formula for `sum of consecutive multiples`

$$
\sum_{k=1}^n k^2 = \dfrac{n \space (n+1)}{2} + \space \dfrac{\boxed{n - 1} \biggr( \boxed{n - 1} + 1 \biggr) \biggr( \boxed{n - 1} + 2 \biggr)}{3}
$$

Simplify the factors

$$
\sum_{k=1}^n k^2 = \dfrac{n \space (n+1)}{2} + \space \dfrac{(n-1)\space n \space (n+1)}{3}
$$

Factor out `n(n+1)`

$$
\sum_{k=1}^n k^2 = n(n+1) \biggr( \dfrac{1}{2} + \dfrac{n-1}{3} \biggr)
$$

Combine into `one fraction`

$$
\sum_{k=1}^n k^2 = n(n+1) \biggr( \dfrac{3 + 2(n-1)}{6} \biggr)
$$

Expand

$$
\sum_{k=1}^n k^2 = n(n+1) \biggr( \dfrac{3 + 2n - 2}{6} \biggr)
$$

Simplify

$$
\sum_{k=1}^n k^2 = n(n+1) \biggr( \dfrac{2n + 1}{6} \biggr)
$$

# Formula for Sum of Squares

$$
\boxed{
    \sum_{k=1}^n k^2 = \dfrac{n(n+1)(2n+1)}{6}
}
$$
