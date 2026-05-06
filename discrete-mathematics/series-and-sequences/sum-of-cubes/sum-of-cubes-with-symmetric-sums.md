---
title: "Derivation of Sum of Cubes via Symmetric Sum"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-symmetric-sums.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-symmetric-sums.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Derivation of Sum of Cubes via Symmetric Sum

We start with the sum of cubes:

$$
\sum_{k=1}^n k^3 = 1^3 + 2^3 + \cdots + n^3
$$

Notice that we can make `squares` out of the cubes as such

$$
\sum_{k=1}^n k \cdot k^2 = 1 \cdot 1^2 + 2 \cdot 2^2 + \cdots + n \cdot n^2
$$

Thus we have `square amounts` of each `n`

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|cc|ccc|cccc}
    & 1 & 2 & 2 & 3 & 3 & 3 & n & \cdots \space \cdots & n \\
    & & 2 & 2 & 3 & 3 & 3 & n & \cdots \space \cdots & n \\
    & & & & 3 & 3 & 3 & n & \cdots \space \cdots & n \\
    & & & & & & & \vdots & & \vdots \\
    & & & & & & & n &\cdots \space \cdots & n \\
\end{array}
$$

We also know that `squares` are actually the same as the `sum of odd numbers` up to that point

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|ccc|ccccc|c|cccccc}
    & 1 & & 2 & & & & 3 & & & & & & & & n \\
    & & 2 & 2 & 2 & & 3 & 3 & 3 & & \cdots & & & & n & n & n \\
    & & & & & 3 & 3 & 3 & 3 & 3 & & & & n & n & n & n & n \\
    & & & & & & & & & & & & & & & \vdots & & & \\
    & & & & & & & & & & & n & \cdots & n & n & n & n & n & \cdots & n\\
\end{array}
$$

Which are also `symmetric sums` when `counted by column`

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|ccc|ccccc|c|cccccc}
    \\
    & 1 & 2 & 4 & 2 & 3 & 6 & 9 & 6 & 3 & \cdots & n & 2n & 3n & \cdots & n^{2} & \cdots & 3n & 2n & n \\
    \\
\end{array}
$$

Which are all multiples of the simple symmetric sum `1 + 2 + 3 + ... + n + ... + 3 + 2 + 1`

$$
\sum_{k=1}^n k^3 =
\begin{array}{cc|c|ccc|ccccc|c|ccccc}
    & \text{Multiple} & 1 & & 2 & & & & 3 & & & \cdots & & & & & n & & & & & \\
    & \hline
    & 1 & 1 & 2 & 1 & 1 & 2 & 3 & 2 & 1 & \cdots & 1 & 2 & 3 & \cdots & n & \cdots & 3 & 2 & 1 \\
    \\
\end{array}
$$

# Symmetry and Squares

You would also realise that since
- The sum is `symmetric`
- The symmetric sum contains `odd number of terms`
- `Sum of odd numbers` is equal to a `square` as each new `odd number` adds a bigger `right corner` to that square

$$
\colorbox{lightgray}{Thus, each new `odd-length symmetric sum` adds a right corner to the square}
$$

We can arrange it like so
- Where the `Multiple` label refers to the multiple of the `simple symmetric sum` contributing at each new `right corner`

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|c|c|c|c}
    & \cellcolor{lightblue} & \cellcolor{lightgreen} & \cellcolor{orange} & \cellcolor{pink} & \cellcolor{yellow}  \\
    \text{Multiple} & \cellcolor{lightblue} 1 & \cellcolor{lightgreen} 2 & \cellcolor{orange} 3 & \cellcolor{pink} \cdots & \cellcolor{yellow} n  \\
    \hline
    \cellcolor{lightblue} 1 & \cellcolor{lightblue} 1 & \cellcolor{lightgreen} 1 & \cellcolor{orange} 1 & \cellcolor{pink} \cdots & \cellcolor{yellow} 1 \\
    \hline
    \cellcolor{lightgreen} 2 & \cellcolor{lightgreen} 1 & \cellcolor{lightgreen} 2 & \cellcolor{orange} 2 & \cellcolor{pink} \cdots & \cellcolor{yellow} 2 \\
    \hline
    \cellcolor{orange} 3 & \cellcolor{orange} 1 & \cellcolor{orange} 2 & \cellcolor{orange} 3 & \cellcolor{pink} \cdots & \cellcolor{yellow} 3 \\
    \hline
    \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \ddots & \cellcolor{yellow} \vdots \\
    \hline
    \cellcolor{yellow} n & \cellcolor{yellow} 1 & \cellcolor{yellow} 2 & \cellcolor{yellow} 3 & \cellcolor{yellow} \cdots & \cellcolor{yellow} n \\
\end{array}
$$

Notice that the `numbers in each row`, from the `term of the multiple amount` to `n`, is the multiple itself

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|c|c|c|c}
    & \cellcolor{gray} & \cellcolor{gray} & \cellcolor{gray} & \cellcolor{gray}  & \cellcolor{gray}  \\
    \text{Multiple} & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{gray} 3 & \cellcolor{gray} \cdots & \cellcolor{gray} n  \\
    \hline
    \cellcolor{lightblue} 1 & \cellcolor{lightblue} 1 & \cellcolor{lightblue} 1 & \cellcolor{lightblue} 1 & \cellcolor{lightblue} \cdots & \cellcolor{lightblue} 1 \\
    \hline
    \cellcolor{lightgreen} 2 & \cellcolor{gray} 1 & \cellcolor{lightgreen} 2 & \cellcolor{lightgreen} 2 & \cellcolor{lightgreen} \cdots & \cellcolor{lightgreen} 2 \\
    \hline
    \cellcolor{orange} 3 & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{orange} 3 & \cellcolor{orange} \cdots & \cellcolor{orange} 3 \\
    \hline
    \cellcolor{pink} \vdots & \cellcolor{gray} \vdots & \cellcolor{gray} \vdots & \cellcolor{gray} \vdots & \cellcolor{pink} \ddots & \cellcolor{pink} \vdots \\
    \hline
    \cellcolor{yellow} n & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{gray} 3 & \cellcolor{gray} \cdots & \cellcolor{yellow} n \\
\end{array}
$$

## Observing Patterns

Now `let the rows be the constant`, and color in the multiples like so, we get


- For multiples of `1`

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|c|c|c|c}
    & & \cellcolor{lightblue} & \cellcolor{lightgreen} & \cellcolor{orange} & \cellcolor{pink} & \cellcolor{yellow}  \\
    & \text{Multiple} & \cellcolor{lightblue} 1 & \cellcolor{lightgreen} 2 & \cellcolor{orange} 3 & \cellcolor{pink} \cdots & \cellcolor{yellow} n  \\
    \hline
    & \cellcolor{lightgray} 1 & \cellcolor{lightgray} 1 & \cellcolor{lightgray} 1 & \cellcolor{lightgray} 1 & \cellcolor{lightgray} \cdots & \cellcolor{lightgray} 1 \\
    \hline
    & \cellcolor{gray} 2 & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{gray} 2 & \cellcolor{gray} \cdots & \cellcolor{gray} 2 \\
    \hline
    & \cellcolor{gray} 3 & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{gray} 3 & \cellcolor{gray} \cdots & \cellcolor{gray} 3 \\
    \hline
    & \cellcolor{gray} \vdots & \cellcolor{gray} \vdots & \cellcolor{gray} \vdots & \cellcolor{gray}\vdots & \cellcolor{gray} \ddots & \cellcolor{gray} \vdots \\
    \hline
    & \cellcolor{gray} n & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{gray} 3 & \cellcolor{gray} \cdots & \cellcolor{gray} n \\
\end{array}
$$

- For multiples of `2`

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|c|c|c|c}
    & & \cellcolor{gray} & \cellcolor{lightgreen} & \cellcolor{orange} & \cellcolor{pink} & \cellcolor{yellow}  \\
    & \text{Multiple} & \cellcolor{gray} 1 & \cellcolor{lightgreen} 2 & \cellcolor{orange} 3 & \cellcolor{pink} \cdots & \cellcolor{yellow} n  \\
    \hline
    & \cellcolor{gray} 1 & \cellcolor{gray} 1 & \cellcolor{gray} 1 & \cellcolor{gray} 1 & \cellcolor{gray} \cdots & \cellcolor{gray} 1 \\
    \hline
    & \cellcolor{lightgray} 2 & \cellcolor{lightblue} 1 & \cellcolor{lightgray} 2 & \cellcolor{lightgray} 2 & \cellcolor{lightgray} \cdots & \cellcolor{lightgray} 2 \\
    \hline
    & \cellcolor{gray} 3 & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{gray} 3 & \cellcolor{gray} \cdots & \cellcolor{gray} 3 \\
    \hline
    & \cellcolor{gray} \vdots & \cellcolor{gray} \vdots & \cellcolor{gray} \vdots & \cellcolor{gray}\vdots & \cellcolor{gray} \ddots & \cellcolor{gray} \vdots \\
    \hline
    & \cellcolor{gray} n & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{gray} 3 & \cellcolor{gray} \cdots & \cellcolor{gray} n \\
\end{array}
$$

- For multiples of `3`

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|c|c|c|c}
    & & \cellcolor{gray} & \cellcolor{gray} & \cellcolor{orange} & \cellcolor{pink} & \cellcolor{yellow}  \\
    & \text{Multiple} & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{orange} 3 & \cellcolor{pink} \cdots & \cellcolor{yellow} n  \\
    \hline
    & \cellcolor{gray} 1 & \cellcolor{gray} 1 & \cellcolor{gray} 1 & \cellcolor{gray} 1 & \cellcolor{gray} \cdots & \cellcolor{gray} 1 \\
    \hline
    & \cellcolor{gray} 2 & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{gray} 2 & \cellcolor{gray} \cdots & \cellcolor{gray} 2 \\
    \hline
    & \cellcolor{lightgray} 3 & \cellcolor{lightblue} 1 & \cellcolor{lightgreen} 2 & \cellcolor{lightgray} 3 & \cellcolor{lightgray} \cdots & \cellcolor{lightgray} 3 \\
    \hline
    & \cellcolor{gray} \vdots & \cellcolor{gray} \vdots & \cellcolor{gray} \vdots & \cellcolor{gray}\vdots & \cellcolor{gray} \ddots & \cellcolor{gray} \vdots \\
    \hline
    & \cellcolor{gray} n & \cellcolor{gray} 1 & \cellcolor{gray} 2 & \cellcolor{gray} 3 & \cellcolor{gray} \cdots & \cellcolor{gray} n \\
\end{array}
$$


Thus, we notice that
- `Every multiple` actually goes from `1` to `n`
- And `multiples` goes from `1` to `n`

Equivalent to this

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|c|c|c|c}
    & \text{Multiple} & \cellcolor{gray} & \cellcolor{gray} & \cellcolor{gray} & \cellcolor{gray} & \cellcolor{gray} \\
    \hline
    & \cellcolor{lightblue} 1 & \cellcolor{lightblue} 1 & \cellcolor{lightblue} 2 & \cellcolor{lightblue} 3 & \cellcolor{lightblue} \cdots & \cellcolor{lightblue} n \\
    \hline
    & \cellcolor{lightgreen} 2 & \cellcolor{lightgreen} 1 & \cellcolor{lightgreen} 2 & \cellcolor{lightgreen} 3 & \cellcolor{lightgreen} \cdots & \cellcolor{lightgreen} n \\
    \hline
    & \cellcolor{orange} 3 & \cellcolor{orange} 1 & \cellcolor{orange} 2 & \cellcolor{orange} 3 & \cellcolor{orange} \cdots & \cellcolor{orange} n \\
    \hline
    & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \ddots & \cellcolor{pink} \vdots \\
    \hline
    & \cellcolor{yellow} n & \cellcolor{yellow} 1 & \cellcolor{yellow} 2 & \cellcolor{yellow} 3 & \cellcolor{yellow} \cdots & \cellcolor{yellow} n \\
\end{array}
$$

# An Equivalent Transformation

The series of observations above also has a simple transformation

Which is to take the form we got earlier using symmetric sums

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|c|c|c|c}
    & & \cellcolor{lightblue} & \cellcolor{lightgreen} & \cellcolor{orange} & \cellcolor{pink} & \cellcolor{yellow}  \\
    & \text{Multiple} & \cellcolor{lightblue} 1 & \cellcolor{lightgreen} 2 & \cellcolor{orange} 3 & \cellcolor{pink} \cdots & \cellcolor{yellow} n  \\
    \hline
    & \cellcolor{lightblue} 1 & \cellcolor{lightblue} 1 & \cellcolor{lightgreen} 1 & \cellcolor{orange} 1 & \cellcolor{pink} \cdots & \cellcolor{yellow} 1 \\
    \hline
    & \cellcolor{lightgreen} 2 & \cellcolor{lightgreen} 1 & \cellcolor{lightgreen} 2 & \cellcolor{orange} 2 & \cellcolor{pink} \cdots & \cellcolor{yellow} 2 \\
    \hline
    & \cellcolor{orange} 3 & \cellcolor{orange} 1 & \cellcolor{orange} 2 & \cellcolor{orange} 3 & \cellcolor{pink} \cdots & \cellcolor{yellow} 3 \\
    \hline
    & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \ddots & \cellcolor{yellow} \vdots \\
    \hline
    & \cellcolor{yellow} n & \cellcolor{yellow} 1 & \cellcolor{yellow} 2 & \cellcolor{yellow} 3 & \cellcolor{yellow} \cdots & \cellcolor{yellow} n \\
\end{array}
$$

Put the multiples back in

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|c|c|c|c}
    \quad \quad & \cellcolor{lightblue} & \cellcolor{lightgreen} & \cellcolor{orange} & \cellcolor{pink} & \cellcolor{yellow} \\
    \hline
    \cellcolor{lightblue} & \cellcolor{lightblue} 1 & \cellcolor{lightgreen} 2 & \cellcolor{orange} 3 & \cellcolor{pink} \cdots & \cellcolor{yellow} n \\
    \hline
    \cellcolor{lightgreen} & \cellcolor{lightgreen} 2 & \cellcolor{lightgreen} 4 & \cellcolor{orange} 6 & \cellcolor{pink} \cdots & \cellcolor{yellow} 2n \\
    \hline
    \cellcolor{orange} & \cellcolor{orange} 3 & \cellcolor{orange} 6 & \cellcolor{orange} 9 & \cellcolor{pink} \cdots & \cellcolor{yellow} 3n \\
    \hline
    \cellcolor{pink} & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \ddots & \cellcolor{yellow} \vdots \\
    \hline
    \cellcolor{yellow} & \cellcolor{yellow} n & \cellcolor{yellow} 2n & \cellcolor{yellow} 3n & \cellcolor{yellow} \cdots & \cellcolor{yellow} n^{2} \\
\end{array}
$$

Then factor out the common multiples of each row

$$
\sum_{k=1}^n k^3 =
\begin{array}{c|c|c|c|c|c}
    & \text{Multiple} & \cellcolor{gray} & \cellcolor{gray} & \cellcolor{gray} & \cellcolor{gray} & \cellcolor{gray} \\
    \hline
    & \cellcolor{lightblue} 1 & \cellcolor{lightblue} 1 & \cellcolor{lightblue} 2 & \cellcolor{lightblue} 3 & \cellcolor{lightblue} \cdots & \cellcolor{lightblue} n \\
    \hline
    & \cellcolor{lightgreen} 2 & \cellcolor{lightgreen} 1 & \cellcolor{lightgreen} 2 & \cellcolor{lightgreen} 3 & \cellcolor{lightgreen} \cdots & \cellcolor{lightgreen} n \\
    \hline
    & \cellcolor{orange} 3 & \cellcolor{orange} 1 & \cellcolor{orange} 2 & \cellcolor{orange} 3 & \cellcolor{orange} \cdots & \cellcolor{orange} n \\
    \hline
    & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \vdots & \cellcolor{pink} \ddots & \cellcolor{pink} \vdots \\
    \hline
    & \cellcolor{yellow} n & \cellcolor{yellow} 1 & \cellcolor{yellow} 2 & \cellcolor{yellow} 3 & \cellcolor{yellow} \cdots & \cellcolor{yellow} n \\
\end{array}
$$

To get the same result

> But the previous way explains why this works, instead of just using this transformation

# Conclusion

We realise that we have $1 + 2 + 3 + \cdots + n$ rows of $1 + 2 + 3 + ... + n$

$$
\sum_{k=1}^n k^3 = (1 + 2 + 3 + \cdots + n) \quad \text{of} \quad (1 + 2 + 3 + \cdots + n)
$$

Which is the same as

$$
\sum_{k=1}^n k^3 = (1 + 2 + 3 + \cdots + n) \quad \times \quad (1 + 2 + 3 + \cdots + n)
$$

Which is the same as

$$
\sum_{k=1}^n k^3 = (1 + 2 + 3 + \cdots + n)^{2}
$$

Substitute in the formula for this sum, we have

$$
\boxed{
    \sum_{k=1}^n k^3 = \biggl[ \dfrac{n(n+1)}{2} \biggr]^{2}
}
$$
