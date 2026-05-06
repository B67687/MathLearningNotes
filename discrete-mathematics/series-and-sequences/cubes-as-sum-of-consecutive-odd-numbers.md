---
title: "Finding Cubes as Sums of Consecutive Odd Numbers"
source_notebook: "discrete-mathematics/series-and-sequences/cubes-as-sum-of-consecutive-odd-numbers.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/cubes-as-sum-of-consecutive-odd-numbers.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Finding Cubes as Sums of Consecutive Odd Numbers

How to find cubes?

$$
n^{3}
$$

### Sum of Cubes Formula

Since we know the formulas for `sums of cubes` as the `square` of the `sum of natural numbers` up to that point

$$
\sum_{k=1}^n k^{3} = \left( \sum_{k=1}^{n} k \right) ^ {2}
$$

We can express any $n^{3}$ as the difference of the `series up to that point`, and the `series right before that point`

$$
\begin{align}
    n^{3} &= \space \space \biggr( 1^3 + 2^3 + 3^3 + \cdots + (n-1)^3 + n^3 \biggr) \\
    & \space \space \space - \biggr( 1^3 + 2^3 + 3^3 + \cdots + (n-1)^3 \biggr) \\
\end{align}
$$

Using the `sum of cube formula`, it is equal to

$$
\begin{align}
    n^{3} &= \quad \biggr( 1 + 2 + 3 + \cdots + (n-1) + n \biggr) ^ {2} \\
    & \quad \space - \biggr( 1 + 2 + 3 + \cdots + (n-1) \biggr) ^ {2} \\
\end{align}
$$


### Sum of Odd Numbers Formula

But we also know that `squares` are equal to the `k-th` odd number up to that point, as in

$$
k^{2} = 1 + 3 + 5 + \cdots + \underline{\text{k-th odd number}}
$$

With this knowledge we now need to find `what is being squared`

$$
\begin{align}
    \textcolor{lightgray}{n^{3}} & \textcolor{lightgray}{=} \textcolor{lightgray}{\quad \biggr(} 1 + 2 + 3 + \cdots + (n-1) + n \textcolor{lightgray}{\biggr) ^ {2}} \\
    & \quad \space \textcolor{lightgray}{- \biggr(} 1 + 2 + 3 + \cdots + (n-1) \textcolor{lightgray}{\biggr) ^ {2}} \\
\end{align}
$$

Which are `arithmetic sums`, also known as `triangle numbers`

$$
\begin{align}
    n^{3} &= \quad \left( \dfrac{n(n+1)}{2} \right)^{2} \\
    & \quad \space - \left( \dfrac{n(n-1)}{2} \right)^{2} \\
\end{align}
$$


Thus we get a `difference between 2 sums of odd numbers`
- That adds up to `triangle number` amounts of odd numbers terms

$$
\begin{align}
    n^{3} &= \space \quad \left( 1 + 3 + 5 + \cdots + \dfrac{n(n-1)}{2}\text{-th odd number} + \cdots + \dfrac{n(n+1)}{2}\text{-th odd number} \right) \\
    & \quad \quad - \left( 1 + 3 + 5 + \cdots + \dfrac{n(n-1)}{2}\text{-th odd number} \right) \\
\end{align}
$$

It can be more clearly viewed, when `grouped by sizes of increasing natural numbers`
- Which is what `arithmetic sums` are

$$
\begin{align}
    n^{3} &= \space \quad \left( \underline{1} + \underline{3 + 5} + \underline{9 + 11 + 13} + \cdots + \underbrace{\cdots + \boxed{\dfrac{n(n-1)}{2} \text{-th odd number}}}_{\text{n-1 terms}} + \underbrace{\boxed{\left( \dfrac{n(n-1)}{2} + 1 \right) \text{-th odd number}} + \cdots + \boxed{\dfrac{n(n+1)}{2}\text{-th odd number}}}_{\text{n terms}} \right) \\
    & \quad \quad - \left( \underline{1} + \underline{3 + 5} + \underline{9 + 11 + 13} + \cdots + \underbrace{\cdots + \boxed{\dfrac{n(n-1)}{2}\text{-th odd number}}}_{\text{n-1 terms}} \right) \\
\end{align}
$$

Is, therefore, `n consecutive odd numbers` like this

$$
n^{3} = \underbrace{\boxed{\left( \dfrac{n(n-1)}{2} + 1 \right) \text{-th odd number}} + \cdots + \boxed{\dfrac{n(n+1)}{2}\text{-th odd number}}}_{\text{n terms}}
$$

# Conclusion

This shows that $n^3$ can be expressed as
- The sum of `n consecutive odd numbers`, that continues from where the `previous one left off`

---

When written out, the pattern looks like this

$$
\begin{align}
1^3 &= 1 \\
2^3 &= 3 + 5 \\
3^3 &= 7 + 9 + 11 \\
4^3 &= 13 + 15 + 17 + 19 \\
5^3 &= 21 + 23 + 25 + 27 + 29 \\
& \vdots
\end{align}
$$
