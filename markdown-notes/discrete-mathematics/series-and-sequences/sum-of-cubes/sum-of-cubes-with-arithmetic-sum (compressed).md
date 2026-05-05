---
title: "Combinatorial Derivation of Sum of Cubes via Vertical Grouping"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-arithmetic-sum (compressed).ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Combinatorial Derivation of Sum of Cubes via Vertical Grouping

## Initial Setup
We start with the sum of cubes:
$$
\sum_{k=1}^n k^3 = 1^3 + 2^3 + \cdots + n^3
$$

## Step 1: Expand Cubes as Repeated Addition
Each cube term can be expanded vertically:
$$
\begin{align*}
1^3 &= 1 \\
2^3 &= (2 + 2) + (2 + 2) \\
3^3 &= (3 + 3 + 3) + (3 + 3 + 3) + (3 + 3 + 3) \\
&\vdots \\
n^3 &= \underbrace{\underbrace{(n + \cdots + n)}_{n \text{ times}} + \cdots + {(n + \cdots + n)}}_{n \text{ times}}
\end{align*}
$$

Notice for the first row, we have $1$ of $1$
- for the 2nd row, we have $2^2$ of $2$
- for the 3rd row, we have $3^2$ of $3$
- ...
- This will continue for $n$ rows
- for the nth row, we have $n^2$ of $n$

This makes sense because

$$
\begin{align}
    n^3 &= n^2 \cdot n \\
    &= n \cdot n^2 \\
    &= n \text{ of } n^2 \\
\end{align}
$$

Hence

$$
\text{Number of } n^2 \text{ is } \boxed{n}
$$

## Step 2: Observe Grouping Pattern

List out the individual terms that add up to each term in the series

$$
\begin{array}{c|ccccccccccc}
    1^3 & 1 \\
    2^3 & 2 & 2 & 2 & 2 \\
    3^3 & 3 & 3 & 3 & 3 & 3 & 3 & 3 & 3 & 3 \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots\\
    n^3 & n & n & n & n & n & n & n & n & n & \cdots & n\\
\end{array}
$$

By grouping vertically we have

$$
\begin{array}{c|c:c:c:c:c:c:c:c:c:cc}
    1^3 & 1 \\
    2^3 & 2 & 2 & 2 & 2 \\
    3^3 & 3 & 3 & 3 & 3 & 3 & 3 & 3 & 3 & 3 \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots\\
    n^3 & n & n & n & n & n & n & n & n & n & \cdots & n\\
\end{array}
$$

Separate the groups by starting term

$$
\begin{array}{c|c:ccc:ccccc:cc}
    1^3 & 1 \\
    2^3 & 2 & 2 & 2 & 2 \\
    3^3 & 3 & 3 & 3 & 3 & 3 & 3 & 3 & 3 & 3 \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots\\
    n^3 & n & n & n & n & n & n & n & n & n & \cdots & n\\
\end{array}
$$

And we have:

$$
\begin{align*}
    \sum_{k=1}^n k^3 &= 1 \cdot (1 + 2 + \cdots + n) \\
    &+ 3 \cdot (2 + \cdots + n) \\
    &+ 5 \cdot (3 + \cdots + n) \\
    &\vdots \\
    &+ \,(2k-1) \cdot (n) \,?\\
\end{align*}
$$

It seems that this sum has odd weighted multipliers `e.g. 1, 3, 5`

But let's verify it

## Step 3: Verify the pattern
We know that the number of each sequence starting from some number `k` is

$$
\begin{align*}
    &\boxed{\text{Number of raw current sequence: that starts from }k \text{ of the k-th term}} - \boxed{\text{That of the previous sequence: } k-1} \\
    &= \boxed{k^2 \textcolor{gray}{\text{ of } k}} - \boxed{(k-1)^2 \textcolor{gray}{\text{ of } (k-1)}} \\
    &= k^2 - (k-1)^2
\end{align*}
$$

Let's expand and simplify that

$$
\begin{align*}
    &  k^2 - (k-1)^2 \\
    &= k^2 - (k^2 - 2k + 1) \\
    &= \cancel{k^2} - \cancel{k^2} + 2k - 1 \\
    &= 2k - 1
\end{align*}
$$

Wow! So the difference of squares is also the odd number at that point!

$$
\boxed{
    \begin{align*}
    &\text{Difference of squares} \\
    &= \text{Odd number}
\end{align*}
}
$$

Thus we can affirm that

$$
\begin{align*}
    \sum_{k=1}^n k^3 &= 1 \cdot (1 + 2 + 3 + \cdots + n) \\
    &+ 3 \cdot (2 + 3 +\cdots + n)\\
    &+ 5 \cdot (3 + \cdots + n) \\
    &\vdots \\
    &+ (2k - 1)(n) \\
\end{align*}
$$

Thus in summation terms:

$$
\begin{align*}
    \sum_{k=1}^n k^3 &= 1 \cdot \sum_{j=1}^n j + 3 \cdot \sum_{j=2}^n j + 5 \cdot \sum_{j=3}^n j + \cdots + (2k - 1) \sum_{j=k}^n j \\
    &= \underbrace{(2k - 1) \sum_{j=k}^n j + (2k - 1) \sum_{j=k}^n j + (2k - 1) \sum_{j=k}^n j + \cdots + (2k - 1) \sum_{j=k}^n j}_{\text{k from 1 to n}} \\
    &= \sum_{k=1}^n \left[ (2k - 1) \sum_{j=k}^n j \right]
\end{align*}
$$

## Conclusion
$$
\boxed{
    \sum_{k=1}^n k^3 = \sum_{k=1}^n \left[ (2k - 1) \sum_{j=k}^n j \right]
}
$$

# Derivation of Sum of Cubes from Double-Sum Identity

## Given Identity
$$
\sum_{k=1}^n k^3 = \sum_{k=1}^n \left[ (2k - 1) \sum_{j=k}^n j \right]
$$

## Step 1: Simplify Inner Sum
Look at the inner sum

$$
\textcolor{lightgray}{\sum_{k=1}^n k^3 = \sum_{k=1}^n} \left[ \textcolor{lightgray}{(2k - 1)} \sum_{j=k}^n j \right]
$$

We can derive the general form of the sum of squares by removing a part from the whole

$$
\begin{align}
    \sum_{j=k}^n j &= \sum_{j=1}^n j - \sum_{j=1}^{k-1} j \\
    &= \dfrac{n(n+1)}{2} - \dfrac{\left[ \left( \boxed{k-1} - 1 \right) + 1 \right] \left( \boxed{k-1}+1 \right)}{2} \\
    &= \dfrac{n(n+1)}{2} - \dfrac{(k-1)k}{2} \\
    &= \dfrac{n^2 + n - (k^2 - k)}{2} \\
    &= \dfrac{n^2 + n - k^2 + k}{2} \\
\end{align}
$$

Hence

$$
\boxed{\sum_{j=k}^n j = \dfrac{n^2 + n - k^2 + k}{2}}
$$

## Step 2: Substitute into Double Sum

So we have this

$$
\sum_{k=1}^n k^3 = \sum_{k=1}^n (2k - 1) \left( \frac{n^2 + n - k^2 + k}{2} \right)
$$

Move the constant out

$$
\sum_{k=1}^n k^3 = \frac{1}{2}\sum_{k=1}^n (2k - 1) (n^2 + n - k^2 + k)
$$

Shift constant to the left

$$
2\sum_{k=1}^n k^3 = \sum_{k=1}^n (2k - 1) (n^2 + n - k^2 + k)
$$

## Step 3: Distribute Terms

Lets focus on this

$$
\textcolor{lightgray}{2\sum_{k=1}^n k^3 =} \sum_{k=1}^n (2k - 1)(n^2 + n - k^2 + k)
$$


Take a step further to focus on this

$$
\textcolor{lightgray}{\sum_{k=1}^n} (2k - 1)(n^2 + n - k^2 + k)
$$

We will expand it out
- Focus on grouping `k` because the summation is in terms of `k`

$$
\begin{align*}
    (2k - 1)(n^{2}+n - k^{2}+k) &=2k(n^{2}+n - k^{2}+k)-(n^{2}+n - k^{2}+k)\\
    &=(2kn^{2}+2kn-2k^{3}+2k^{2})-(n^{2}+n - k^{2}+k)\\
    &=2kn^{2}+2kn-2k^{3}+2k^{2}-n^{2}-n + k^{2}-k\\
    &=-2k^{3}+(2k^{2}+k^{2})+2kn+(2kn - k)+( - n^{2}-n)\\
    &=-2k^{3}+3k^{2}+(2n^{2} + 2n - 1)k - n^{2}-n
\end{align*}
$$

Thus

$$
\textcolor{lightgray}{2\sum_{k=1}^n k^3 =} \sum_{k=1}^n \biggr[ -2k^{3} + 3k^{2} + (2n^{2} + 2n - 1)k - n^{2} - n \biggr]
$$

Expand
$$
\begin{align*}
    2\sum_{k = 1}^{n}k^{3}&=-2\sum_{k = 1}^{n}k^{3}+3\sum_{k = 1}^{n}k^{2}+(2n^{2} + 2n - 1)\sum_{k = 1}^{n}k-\sum_{k = 1}^{n}n^{2}-\sum_{k = 1}^{n}n
\end{align*}
$$

Simplify

$$
\begin{align*}
    2\sum_{k = 1}^{n}k^{3}&=-2\sum_{k = 1}^{n}k^{3}+3 \cdot \frac{n(n + 1)(2n + 1)}{6}+(2n^{2} + 2n - 1) \cdot \frac{n(n + 1)}{2}-n^{3}-n^{2}\\
    2\sum_{k = 1}^{n}k^{3}+2\sum_{k = 1}^{n}k^{3}&=\frac{n(n + 1)(2n + 1)}{2}+\frac{(2n^{2} + 2n - 1)n(n + 1)}{2}-n^{3}-n^{2}\\
\end{align*}
$$

Further simplify

$$
\begin{align*}
    4\sum_{k = 1}^{n}k^{3}&=\frac{n(n + 1)(2n + 1)+n(n + 1)(2n^{2} + 2n - 1)}{2}-n^{3}-n^{2}\\
    &=\frac{n(n + 1) \biggr[(2n + 1)+(2n^{2} + 2n - 1) \biggr]}{2}-n^{3}-n^{2}\\
    &=\frac{n(n + 1)(2n^{2}+4n)}{2}-n^{3}-n^{2}\\
    &=n(n + 1)(n^{2}+2n)-n^{3}-n^{2}\\
    &=n(n + 1)(n^{2}+2n)-n(n+1)(n)\\
    &=n(n + 1)(n^{2}+n)\\
    &=n(n + 1)[n(n+1)]\\
    &=n^2 (n+1)^2
\end{align*}
$$

And finally we get

$$
\begin{align*}
    \sum_{k = 1}^{n}k^{3} &=\frac{n^2 (n+1)^2}{4} \\
    &=\frac{n^2 (n+1)^2}{2^{2}} \\
    &=\left[ \frac{n(n + 1)}{2} \right] ^{2}
\end{align*}
$$

---

## Conclusion

Thus, we have arrived at

$$
\boxed{
    \sum_{k = 1}^{n}k^{3} = \left[ \frac{n(n + 1)}{2} \right] ^{2}
}
$$
