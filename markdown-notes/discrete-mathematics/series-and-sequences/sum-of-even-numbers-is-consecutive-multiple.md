---
title: "Sum of Even Numbers"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-even-numbers-is-consecutive-multiple.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Sum of Even Numbers

This is a pattern that emerged from the sum of even numbers
$$
\begin{align}
    0 &= 0 \rightarrow 1 \times 0 \\
    2 &= 2 \rightarrow 2 \times 1 \\
    2 + 4 &= 6 \rightarrow 3 \times 2 \\
    2 + 4 + 6 &= 12 \rightarrow 4 \times 3 \\
    2 + 4 + 6 + 8 &= 20 \rightarrow 5 \times 4 \\
    2 + 4 + 6 + 8 + 10 &= 30 \rightarrow 6 \times 5 \\
    2 + 4 + 6 + 8 + 10 + 12 &= 42 \rightarrow 7 \times 6 \\
    2 + 4 + 6 + 8 + 10 + 12 + 14 &= 56 \rightarrow 8 \times 7 \\
    2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 &= 72 \rightarrow 9 \times 8 \\
\end{align}
$$

It seems that the sum of even numbers is the `current iteration` times its `previous iteration number`.

But let's prove it!


# Deriving this Pattern

We start from this:

$$
\sum_{k=0}^n 2k
$$

Expand and Simplify

> We are going to use `0` to `n-1` here because
> - `0` is the first even number,
> - To reach the `n`-th iteration, it will move another `n-1` steps, which lands us at `0 + n-1 = n-1`
> - Which is why the last value for `k` is `n-1` instead of what we might mistake as `n`

$$
\begin{align*}
    \sum_{k=0}^{n-1} 2k &= 2\sum_{k=0}^{n-1} k \\
    &= 2 \space \left( 0 + \sum_{k=1}^{n-1} k \right) \\
    &= 2 \sum_{k=1}^{n-1} k \\
    &= \cancel{2} \cdot \dfrac{(1 + (n-1))(n-1)}{\cancel{2}} \\
    &= n(n-1) \\
\end{align*}
$$

Thus we have proven this cool identity!

$$
\boxed{
    \sum_{k=0}^{n-1} 2k = n(n-1)
}
$$

Notice although even numbers start from `0`, zero does not contribute to the sum, thus it is equivalent to starting from `1`
- That fact is also present in our derivation step

$$
\begin{align*}
    \textcolor{lightgray}{\sum_{k=0}^{n-1} 2k} & \textcolor{lightgray}{=} \textcolor{lightgray}{2\sum_{k=0}^{n-1} k} \\
    & \textcolor{lightgray}{=} \textcolor{lightgray}{2} \space \left( 0 + \sum_{k=1}^{n-1} k \right) \\
    & \textcolor{lightgray}{\vdots}
\end{align*}
$$


Thus

$$
\underline{\sum_{k=1}^{n-1} 2k = n(n-1)}
$$

# Ascending Multiple

The flipped multiplication, where the smaller number multiplies the bigger number is also true

$$
\begin{align}
    0 &= \space \space 0 \rightarrow 0 \times 1 \\
    2 &= \space \space 2 \rightarrow 1 \times 2 \\
    2 + 4 &= \space \space 6 \rightarrow 2 \times 3 \\
    2 + 4 + 6 &= 12 \rightarrow 3 \times 4 \\
    2 + 4 + 6 + 8 &= 20 \rightarrow 4 \times 5 \\
    2 + 4 + 6 + 8 + 10 &= 30 \rightarrow 5 \times 6 \\
    2 + 4 + 6 + 8 + 10 + 12 &= 42 \rightarrow 6 \times 7 \\
    2 + 4 + 6 + 8 + 10 + 12 + 14 &= 56 \rightarrow 7 \times 8 \\
    2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 &= 72 \rightarrow 8 \times 9 \\
\end{align}
$$

So if we let it end at `k=n` instead of `k=n-1`

$$
\begin{align*}
    \sum_{k=0}^{n} 2k &= 2\sum_{k=0}^{n} k \\
    &= 2 \space \left( 0 + \sum_{k=1}^{n} k \right) \\
    &= 2 \sum_{k=1}^{n} k \\
    &= \cancel{2} \cdot \dfrac{n(n+1)}{\cancel{2}} \\
    &= n(n+1) \\
\end{align*}
$$

Thus we have proven this cool identity in another perspective!

$$
\boxed{\sum_{k=0}^{n} 2k = n(n+1)}
$$

With the same fact that zero does not contribute to the sum, we have this!

$$
\underline{\sum_{k=1}^{n} 2k = n(n+1)}
$$

# Conclusion

Therefore!
$$
\boxed{\sum_{k=0}^{n-1} 2k = n(n-1)} \quad \text{and} \quad \boxed{\sum_{k=0}^{n} 2k = n(n+1)}
$$

And thus!

$$
\underline{\sum_{k=1}^{n-1} 2k = n(n-1)} \quad \text{and} \quad \underline{\sum_{k=1}^{n} 2k = n(n+1)}
$$
