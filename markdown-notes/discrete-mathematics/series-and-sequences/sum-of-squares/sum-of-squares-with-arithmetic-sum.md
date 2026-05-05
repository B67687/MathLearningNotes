---
title: "Combinatorial Approach to the Sum of Squares Formula"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-squares/sum-of-squares-with-arithmetic-sum.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Combinatorial Approach to the Sum of Squares Formula

Lets find the sum of squares

$$
\sum_{k=1}^{n} k^2
$$

# Algebraic Manipulation
Let's seek to make the exponential into an addition problem

$$
\sum_{k=1}^n k^2 = 1^2 + 2^2 + 3^2 + ... + n^2
$$

$$
\sum_{k=1}^n k^2 = (1 \cdot 1) + (2 \cdot 2) + (3 \cdot 3) + ... + (n \cdot n)
$$

$$
\sum_{k=1}^n k^2 = 1 + (2 + 2) + (3 + 3 + 3) + ... + (\underbrace{n + n + \dots + n}_{n \text{ times}})
$$

Arrange it vertically so that each term's contribution is clear

$$
\begin{align*}
    \sum_{k=1}^n k^2 &= 1 \\
    &\quad + (2 + 2) \\
    &\quad + (3 + 3 + 3) \\
    &\quad \vdots \\
    &\quad + (\underbrace{n + n + \dots + n}_{n \text{ times}})
\end{align*}
$$

By grouping vertically (or taking the nth term of every group) we have:

$$
\sum_{k=1}^n k^2 = \underbrace{(1 + 2 + 3 + ... + n) + (2 + 3 + 4 + ... + n) + ... + n}_{n \text{ terms}}
$$

Let's describe every individual summation with a new index `j`

$$
\sum_{k=1}^n k^2 = \underbrace{\sum_{j=1}^n j + \sum_{j=2}^n j + ... + \sum_{j=n}^n j}_{n \text{ terms}}
$$

Observe that the starting index of every individual sum, `j`, follows from its current term index, which can be described by another variable.
For which we can reuse the variable `k`, to count the progression of `j` from `1` to `n`

$$
\sum_{k=1}^n \sum_{j=k}^{n} j
$$

Therefore, we have gotten this identity described in a Double Summation:

$$
\boxed{\sum_{k=1}^n k^2 = \sum_{k=1}^n \sum_{j=k}^{n} j}
$$

# Visualising the Sum in 2 Dimensions
Sometimes, it's not convincing enough to do it algebraically

So let's visualise this transformation in a table

$$
\sum_{k=1}^n k^2 = 1^2 + 2^2 + 3^2 + ... + n^2
$$

can be visualised like this:

$$
\begin{array}{c|ccccccc}
    k=1 & 1 \\
    k=2 & 2 & 2 \\
    k=3 & 3 & 3 & 3 \\
    k=4 & 4 & 4 & 4 & 4 \\
    k=5 & 5 & 5 & 5 & 5 & 5 \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\
    k=n & n & n & n & n & n & \cdots & n \\
\end{array}
$$

Notice that the horizontal index also goes from 1 to n:

$$
\begin{array}{c|ccccc}
    & j=1 & j=2 & j=3 & \cdots & \cdots & \cdots & j=n \\
\hline
    k=1 & 1 \\
    k=2 & 2 & 2 \\
    k=3 & 3 & 3 & 3 \\
    k=4 & 4 & 4 & 4 & 4 \\
    k=5 & 5 & 5 & 5 & 5 & 5 \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\
    k=n & n & n & n & n & n & \cdots & n \\
\end{array}
$$

Notice that vertical sums gives arithmetic sums

$$
\begin{array}{c|ccccc}
    & j=1 & j=2 & j=3 & \cdots & \cdots & \cdots & j=n \\
\hline
    k=1 & 1 \\
    k=2 & 2 & 2 \\
    k=3 & 3 & 3 & 3 \\
    k=4 & 4 & 4 & 4 & 4 \\
    k=5 & 5 & 5 & 5 & 5 & 5 \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\
    k=n & n & n & n & n & n & \cdots & n \\
\hline
    & \sum_{j=1}^{n} j & \sum_{j=2}^{n} j & \sum_{j=3}^{n} j & \sum_{j=4}^{n} j & \sum_{j=5}^{n} j & \cdots & \sum_{j=n}^{n} j
\end{array}
$$

Okay great, now we can sum up all the sums of `j` to `n` for every `j` from `1` to `n`

$$
\sum_{k=1}^n k^2 = \underbrace{\sum_{j=1}^n j + \sum_{j=2}^n j + ... + \sum_{j=n}^n j}_{n \text{ terms}}
$$

We cannot use the same variable `j` for the change in starting value for each sum, because it already describes each individual arithmetic sum

So we gotta pick another variable!

Notice that `k` also progresses from `1` to `n`, equalling the progression of the starting value `j`

$$
\begin{array}{c|ccccc}
    & j=1 & j=2 & j=3 & \cdots & \cdots & \cdots & j=n \\
\hline
    k=1 & 1 \\
    k=2 & 2 & 2 \\
    k=3 & 3 & 3 & 3 \\
    k=4 & 4 & 4 & 4 & 4 \\
    k=5 & 5 & 5 & 5 & 5 & 5 \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\
    k=n & n & n & n & n & n & \cdots & n \\
\hline
    & \sum_{j=k}^{n} j & \sum_{j=k}^{n} j & \sum_{j=k}^{n} j & \sum_{j=k}^{n} j & \sum_{j=k}^{n} j & \cdots & \sum_{j=k}^{n} j
\end{array}
$$

Therefore, we can let `j` be described in terms of `k`,

as in `j = k`, for `k` from `1` to `n`

$$
\sum_{k=1}^n k^2 = \underbrace{\sum_{j=k}^{n} j + \sum_{j=k}^{n} j + ... + \sum_{j=k}^{n} j}_{\text{For k from 1 to n}}
$$

Re-write that in mathematical notation, and we have:

$$
\boxed{\sum_{k=1}^n k^2 = \sum_{k=1}^n \sum_{j=k}^{n} j}
$$

# Apply the Arithmetic Sequence Formula

Now we know with justification that
$$
\sum_{k=1}^n k^2 = \sum_{k=1}^n \sum_{j=k}^{n} j
$$

Let's focus on the inner sum

$$
\quad \sum_{j=k}^n j \quad
$$

Notice it is an arithmetic sequence with:

- First term = $k$
- Last term = $n$
- Common Difference = $d$ = $1$

- $
\begin{aligned}
    \text{Number of terms} &= \frac{n - k}{d}+1 \space \text{ (Difference of Terms + 1)}\\
    &= \frac{n - k}{1}+1 \\
    &= n - k + 1
\end{aligned}
$

The sum of this arithmetic sequence is therefore:

$$
\left(
    \dfrac{\text{first term} + \text{last term}}{2}
\right) (\text{number of terms})
$$

$$
\left(
    \dfrac{n + k}{2}
\right) (n - k + 1)
$$

$$
\dfrac{(n + k)(n - k + 1)}{2}
$$

Thus:

$$
\sum_{k=1}^n \dfrac{(n + k)(n - k + 1)}{2}
$$

Factor out $\dfrac{1}{2}$:

$$
\dfrac{1}{2} \sum_{k=1}^n (n + k)(n - k + 1)
$$

# Simplify the Inner Expression

Expand the inner expression $(n + k)(n - k + 1)$:

$$
\begin{aligned}
    (n + k)(n - k + 1) &= n^2 - nk + n + kn - k^2 + k \\
                       &= n^2 + n - k^2 + k
\end{aligned}
$$

Substitute back into the sum:

$$
\dfrac{1}{2} \sum_{k=1}^n (n^2 + n - k^2 + k)
$$

Break into individual sums:

$$
\dfrac{1}{2} \left(
    \sum_{k=1}^n n^2 + \sum_{k=1}^n n - \sum_{k=1}^n k^2 + \sum_{k=1}^n k
\right)
$$

---

Zoom in to the summations:

$$
\sum_{k=1}^n n^2 + \sum_{k=1}^n n - \sum_{k=1}^n k^2 + \sum_{k=1}^n k
$$

Notice that these 2 summations are simplifiable

$$
\sum_{k=1}^n n^2 + \sum_{k=1}^n n \textcolor{lightgray}{- \sum_{k=1}^n k^2 + \sum_{k=1}^n k}
$$

$$
n^3 + n^2 \textcolor{lightgray}{- \sum_{k=1}^n k^2 + \sum_{k=1}^n k}
$$

Notice that the expansion contains the sum we want to find itself:

$$
\textcolor{lightgray}{n^3 + n^2} - \sum_{k=1}^n k^2 + \textcolor{lightgray}{\sum_{k=1}^n k}
$$

Notice that the last term is describing an arithmetic sequence

$$
\textcolor{lightgray}{n^3 + n^2 - \sum_{k=1}^n k^2} + \sum_{k=1}^n k
$$

$$
\textcolor{lightgray}{n^3 + n^2 - \sum_{k=1}^n k^2} + \dfrac{n(n+1)}{2}
$$

---

Hence, it simplifies to:

$$
\dfrac{1}{2} \left[
    n^3 + n^2 - \sum_{k=1}^n k^2 + \dfrac{n(n+1)}{2}
\right]
$$

Since
$$
\sum_{k=1}^n k^2 = \dfrac{1}{2} \left[
    n^3 + n^2 - \sum_{k=1}^n k^2 + \dfrac{n(n+1)}{2}
\right]
$$

To make writing easier, let
$$
\mathbf{S_n} = \sum_{k=1}^n k^2
$$

Hence
$$
\mathbf{S_n} = \dfrac{1}{2} \left[
    n^3 + n^2 - \mathbf{S_n} + \dfrac{n(n+1)}{2}
\right]
$$

---

Balance the equation:

$$
2\space\mathbf{S_n} = n^3 + n^2 - \mathbf{S_n} + \dfrac{n(n+1)}{2}
$$

$$
3\space\mathbf{S_n} = n^3 + n^2 + \dfrac{n(n+1)}{2}
$$

$$
3\space\mathbf{S_n} = \dfrac{2n^3 + 2n^2 + n^2 + n}{2}
$$

$$
\begin{aligned}
    \mathbf{S_n} &= \dfrac{2n(n^2 + n) + (n^2 + n)}{6} \\
    \mathbf{S_n} &= \dfrac{(n^2 + n)(2n + 1)}{6} \\
    \mathbf{S_n} &= \dfrac{n(n + 1)(2n + 1)}{6}
\end{aligned}
$$

Therefore:

$$
\boxed{ \sum_{k=1}^n k^2 = \dfrac{n(n + 1)(2n + 1)}{6} }
$$

# General Sum of Squares

The general sum is

$$
\sum_{k=j}^n k^2 = \dfrac{n(n + 1)(2n + 1)}{6}
$$

Expand by making it a difference of two sums from `1` to `m`

$$
\begin{align*}
    \sum_{k=j}^n k^2 &= \sum_{k=1}^n k^2 - \sum_{k=1}^{j-1} k^2 \\
    &= \dfrac{n(n + 1)(2n + 1)}{6} - \dfrac{(j-1)[(j-1) + 1][2(j-1) + 1]}{6}\\
    &= \dfrac{n(n + 1)(2n + 1)}{6} - \dfrac{(j-1)j(2j-2 + 1)}{6}\\
    &= \dfrac{n(n + 1)(2n + 1)}{6} - \dfrac{(j-1)j(2j-1)}{6}\\
    &= \dfrac{n(n + 1)(2n + 1) - j(j-1)(2j-1)}{6} \\
    &= \dfrac{1}{6} \biggr[ n(n + 1)(2n + 1) - j(j-1)(2j-1) \biggr] \\
\end{align*}
$$

Thus

$$
\boxed{
    \sum_{k=j}^n k^2 =  \dfrac{1}{6} \biggr[ n(n + 1)(2n + 1) - j(j-1)(2j-1) \biggr]
}
$$

# Additional Insights

## Initial Analysis

From this we can see that also:

$$
\textcolor{lightgray}{\sum_{k=1}^n k^2 = \left( \dfrac{2n + 1}{3} \right)} \left( \dfrac{n(n + 1)}{2} \right)
$$

$$
\textcolor{lightgray}{\sum_{k=1}^n k^2 = \left( \dfrac{2n + 1}{3} \right)} \sum_{k=1}^n k
$$

$$
\sum_{k=1}^n k^2 = \left( \dfrac{2n + 1}{3} \right) \sum_{k=1}^n k
$$

Thus, the sum of squares is the common arithmetic sum by a factor of $ \boxed{\frac{2n + 1}{3}} $

$$
\boxed{
    \text{Sum of squares} \space = \left( \dfrac{2n + 1}{3} \right) \space \text{of Arithmetic sum}
}
$$

But we can go further!

## Average and Total

Notice that when the series is expanded:

$$
\begin{align*}
    \sum_{k=1}^n k^2 &= 1 \\
    &\quad + (2 + 2) \\
    &\quad + (3 + 3 + 3) \\
    &\quad \vdots \\
    &\quad + (\underbrace{n + n + \dots + n}_{n \text{ times}})
\end{align*}
$$

Each row `i.e. nth row` contributes exactly `n` terms `i.e. 1 + 2 + 3 + ... + n`

Which means the total number of terms in the addition is equal to the arithmetic sum

$$
1 + 2 + 3 + ... + n =  \sum_{k=1}^n k
$$

Thus

$$
\underline{
    \text{Total number of Addition Terms} = \text{Arithmetic Sum}
}
$$

And since

$$
\sum_{k=1}^n k = \dfrac{n(n + 1)}{2} = \text{Arithmetic Sum} = \text{Total number of Addition Terms}
$$

And

$$
\textcolor{lightgray}{\sum_{k=1}^n k^2 = \left( \dfrac{2n + 1}{3} \right)} \cdot \text{Total number of Addition Terms}
$$

It makes the other part of the formula

$$
\textcolor{lightgray}{\sum_{k=1}^n k^2 =} \left( \dfrac{2n + 1}{3} \right) \textcolor{lightgray}{\cdot \text{Total number of Addition Terms}}
$$

Equivalent to the average of those addition terms

$$
\textcolor{lightgray}{\sum_{k=1}^n k^2 =} \text{Average of Addition Terms} \textcolor{lightgray}{\cdot \text{Total number of Addition Terms}}
$$

Thus

$$
\boxed{
    \text{Average of Addition Terms} = \left( \dfrac{2n + 1}{3} \right)
}
$$

And

$$
\underline{
    \text{Sum of squares} = \text{Average of Addition Terms} \cdot \text{Total number of Addition Terms}
}
$$

But theres more!

## Relationship to the Next Odd Number

Notice this

$$
\textcolor{lightgray}{\text{Average of Addition Terms} =} \textcolor{lightgray}{\biggr(} \dfrac{2n + 1}{\textcolor{lightgray}{3}} \textcolor{lightgray}{\biggr)}
$$

It can represent all the odd numbers if we let `n` start from `0`

$$
\text{Odd Numbers} \space = \{ 1, 3, 5, 7, \cdots\} = \{2n+1 ∣ n= 0, 1, 2 \cdots \}
$$

But since `n` starts from `1`, `2n+1` represents the odd numbers from `3` onwards

$$
\text{Odd Numbers from 3} \space = \{ 3, 5, 7, \cdots\} = \{2n+1 ∣ n= 1, 2, 3 \cdots \}
$$

It is always one iteration more on the scale of all odd numbers
- Represented by `2n-1`

$$
\text{Odd Numbers} \space = \{ 1, 3, 5, 7, \cdots\} = \{2n-1 ∣ n= 1, 2, 3 \cdots \}
$$

- The next odd number `i.e. one iteration more`

$$
\text{Next Odd Number} \space = \{ \_, 3, 5, 7, \cdots\} = \{2n-1 ∣ n= \_ , 2, 3 \cdots \}
$$

Thus

$$
\boxed{
    \text{Average of Addition Terms} = \dfrac{\text{Next Odd Number}}{3}
}
$$

# Conclusion

Therefore, we get

$$
\text{Sum of squares} \space = \text{Average of Addition Terms} \cdot \space \text{Number of Addition Terms}
$$

Where

$$
\begin{align*}
    &\underline{\text{Average of Addition Terms}} = \text{A Third of the Next Odd Number} = \dfrac{2n + 1}{3}\\
    &\underline{\text{Number of Addition Terms}} = \text{Arithmetic Sum} = \dfrac{n(n+1)}{2}
\end{align*}
$$

Combined

$$
\text{Sum of squares} \space = \dfrac{2n + 1}{3} \cdot \dfrac{n(n+1)}{2}
$$

Which is the same as

$$
\text{Sum of squares} \space = \dfrac{n(n+1)(2n + 1)}{6}
$$

How Interesting!
