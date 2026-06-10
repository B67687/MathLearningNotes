---
title: "Combinatorial Approach to the Sum of Cubes Formula"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-sum-of-squares.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-sum-of-squares.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Combinatorial Approach to the Sum of Cubes Formula

We derive the formula for the sum of squares using a combinatorial approach by expressing the sum as a double summation, applying the arithmetic sequence formula, and then using algebraic manipulation.

---
Before Anything lets play with the sum a little

## Algebraic Manipulation
Let's seek to make the exponential into an addition problem
$$
\sum_{k=1}^n k^3 = 1^3 + 2^3 + 3^3 + ... + n^3
$$

Re-write it in terms of multiplication
$$
\sum_{k=1}^n k^3 = (1 \cdot 1 \cdot 1) + (2 \cdot 2 \cdot 2) + (3 \cdot 3 \cdot 3) + ... + (n \cdot n \cdot n)
$$

Re-write it in terms of addition
$$
\begin{align*}
    \sum_{k=1}^n k^3 &= 1 \quad \\
    &\quad + (2 + 2) + (2 + 2) \quad \\
    &\quad + (3 + 3 + 3) + (3 + 3 + 3) + (3 + 3 + 3) \quad \\
    &\quad \vdots \\
    &\quad + \underbrace{(n + \dots + n) + \dots + (n + \dots + n)}_{n \text{ terms}}
\end{align*}
$$

Notice that we have the sum of squares

$$\sum_{k=1}^n k^3 =
\begin{array}{c|c|cc|ccc|cccc}
    & 1 & 2 & 2 & 3 & 3 & 3 & n & \cdots & n \\
    & & 2 & 2 & 3 & 3 & 3 & n & \cdots & n \\
    & & & & 3 & 3 & 3 & n & \cdots & n \\
    & & & & & & & \vdots & & \vdots \\
    & & & & & & & n &\cdots & n \\
\end{array}
$$

Therefore this is the sum of squares with an increasing starting point

$$
\sum_{k=1}^n k^3 = \left( \sum_{j=1}^n j^2 + \sum_{j=2}^n j^2 + \sum_{j=3}^n j^2 + \dots + \sum_{j=n}^n j^2 \right)
$$

Thus
$$
\sum_{k=1}^n k^3 = \underbrace{\left( \sum_{j=k}^n j^2 + \sum_{j=k}^n j^2 + \sum_{j=k}^n j^2 + \dots + \sum_{j=k}^n j^2 \right)}_{\text{k from 1 to n}}
$$

This generalizes to:
$$
\sum_{k=1}^n k^3 = \sum_{k=1}^n \left( \sum_{j=k}^n j^2 \right)
$$

Thus, we have a double summation
$$
\boxed{
    \sum_{k=1}^n k^3 = \sum_{k=1}^n \sum_{j=k}^n j^2
}
$$

# Applying the sum of squares formula

Lets isolate this:

$$
\textcolor{darkgray}{\sum_{k=1}^n k^3 = \sum_{k=1}^n} \sum_{j=k}^n j^2
$$

We know:

$$
\sum_{j=1}^n j^2 = \dfrac{n(n+1)(2n+1)}{6}
$$

The partial sum from $j=k$ to $j=n$ can be described like so:

$$
\sum_{j=k}^n j^2 = \sum_{j=1}^n j^2 - \sum_{j=1}^{k-1} j^2
$$

Substituting the right variables we get:

$$
\begin{align*}
    \sum_{j=k}^n j^2 &= \dfrac{n(n+1)(2n+1)}{6} - \dfrac{(k-1)k(2k-1)}{6} \\
    &= \dfrac{n(n+1)(2n+1)}{6} - \dfrac{k(k-1)(2k-1)}{6}
\end{align*}
$$

Thus, we have:

$$
\sum_{k=1}^n k^3  = \sum_{k=1}^n \left( \dfrac{n(n+1)(2n+1)}{6} - \dfrac{k(k-1)(2k-1)}{6} \right)
$$

# Expand and Simplify
Let

$$
\mathbf{S_n} = \sum_{k=1}^n k^3
$$

Simplify the expression:

$$
\mathbf{S_n} = \sum_{k=1}^n \left( \dfrac{n(n+1)(2n+1)}{6} - \dfrac{k(k-1)(2k-1)}{6} \right)
$$

Factor out the constant

$$
\mathbf{S_n} = \dfrac{1}{6} \sum_{k=1}^n \underline{n(n+1)(2n+1) - k(k-1)(2k-1)}
$$

Shift it to the left

$$
6\mathbf{S_n} = \sum_{k=1}^n \underline{n(n+1)(2n+1) - k(k-1)(2k-1)}
$$

Distribute the summation notation

$$
6\mathbf{S_n} = \sum_{k=1}^n n(n+1)(2n+1) - \sum_{k=1}^n k(k-1)(2k-1)
$$

Simplify the expression with only `n`, as it is a `relative constant` here

$$
6\mathbf{S_n} = n^{2}(n+1)(2n+1) - \sum_{k=1}^n k(k-1)(2k-1)
$$

### Expand the inner expression

Let's simplify this

$$
\textcolor{lightgray}{6\mathbf{S_n} = n^{2}(n+1)(2n+1) - \sum_{k=1}^n} k(k-1)(2k-1)
$$

Expand and Simplify
$$
\begin{align*}
    k(k-1)(2k-1) &= (k^2 - k)(2k - 1) \\
    &= 2k^3 - k^2 - 2k^2 + k \\
    &= 2k^3 - 3k^2 + k
\end{align*}
$$

Substitute back
$$
6\mathbf{S_n} = n^2(n+1)(2n+1) - \sum_{k=1}^n (2k^3 - 3k^2 + k)
$$

# Solve Each Part Separately

Focusing on this term
$$
\textcolor{lightgray}{6\mathbf{S_n} = n^2(n+1)(2n+1)} \textcolor{lightgray}{-} \sum_{k=1}^n (2k^3 - 3k^2 + k)
$$

Distribute the summation

$$
\sum_{k=1}^n (2k^3 - 3k^2 + k) = 2 \left( \sum_{k=1}^n k^3 \right) - 3 \left( \sum_{k=1}^n k^2 \right) + \sum_{k=1}^n k
$$

---

This part is the sum we want to find

$$
2 \left( \sum_{k=1}^n k^3 \right) \textcolor{lightgray}{- 3 \left( \sum_{k=1}^n k^2 \right) + \sum_{k=1}^n k}
$$

$$
2\mathbf{S_n} \textcolor{lightgray}{- 3 \left( \sum_{k=1}^n k^2 \right) + \sum_{k=1}^n k}
$$

This is the sum of squares
$$
\textcolor{lightgray}{2\mathbf{S_n}} - 3 \left( \sum_{k=1}^n k^2 \right)  \textcolor{lightgray}{+} \textcolor{lightgray}{\sum_{k=1}^n k}
$$

$$
\textcolor{lightgray}{2\mathbf{S_n}} - 3 \cdot \dfrac{n(n+1)(2n+1)}{6}  \textcolor{lightgray}{+} \textcolor{lightgray}{\sum_{k=1}^n k}
$$

$$
\textcolor{lightgray}{2\mathbf{S_n}} - \dfrac{n(n+1)(2n+1)}{2}  \textcolor{lightgray}{+} \textcolor{lightgray}{\sum_{k=1}^n k}
$$

This is the arithmetic sum

$$
\textcolor{lightgray}{2\mathbf{S_n} - \dfrac{n(n+1)(2n+1)}{2}} + \sum_{k=1}^n k
$$

$$
\textcolor{lightgray}{2\mathbf{S_n} - \dfrac{n(n+1)(2n+1)}{2}} + \dfrac{n(n+1)}{2}
$$

Hence

$$
\textcolor{lightgray}{\sum_{k=1}^n (2k^3 - 3k^2 + k) =} 2\mathbf{S_n} - \dfrac{n(n+1)(2n+1)}{2} + \dfrac{n(n+1)}{2}
$$

---

# Algebraic Manipulation

Substitute back:
$$
\textcolor{lightgray}{6\mathbf{S_n} = n^2(n+1)(2n+1)} \textcolor{lightgray}{-} \sum_{k=1}^n (2k^3 - 3k^2 + k)
$$

To get

$$
6\mathbf{S_n} = n^2(n+1)(2n+1) - \biggr[ 2\mathbf{S_n} - n^2(n+1) \biggr]
$$

Distribute the signs:

$$
6\mathbf{S_n} = n^2(n+1)(2n+1) - 2\mathbf{S_n} + n^2(n+1)
$$

Shift $S_n$ over

$$
8\mathbf{S_n} = n^2(n+1)(2n+1) + n^2(n+1)
$$

Combine like terms

$$
8\mathbf{S_n} = n^2(n+1)\left( \boxed{2n+1}+1 \right)
$$

$$
8\mathbf{S_n} = n^2(n+1)(2n+2)
$$

Simplify

$$
8\mathbf{S_n} = 2n^2(n+1)(n+1)
$$

$$
4\mathbf{S_n} = n^2(n+1)^2
$$

Finally, we get

$$
\mathbf{S_n} = \dfrac{n^2(n+1)^2}{4}
$$

$$
\mathbf{S_n} = \dfrac{n^2(n+1)^2}{2^2}
$$

$$
\mathbf{S_n} = \left[ \dfrac{n(n+1)}{2} \right]^2
$$

---

# Conclusion
Thus, we find the formula for the sum of cubes as

$$
\boxed{\sum_{k=1}^n k^3 = \biggr[ \dfrac{n(n+1)}{2} \biggr]^2}
$$

---

# Insights

Notice that the arithmetic sum is contained in the formula
$$
\textcolor{lightgray}{
    \sum_{k=1}^n k^3 =  }\left[ \dfrac{n(n+1)}{2} \right] \textcolor{lightgray}{^{2}}
$$

Thus the the sum of cubes is also the arithmetic sum squared

$$
\boxed{
    \sum_{k=1}^n k^3 = \left( \sum_{k=1}^n k \right) ^{2}
}
$$

$$
\boxed{
    \text{Sum of cubes } = \text{Square of Arithmetic Sum }
}
$$

---

# Explore Other Methods (Comprehensive Understanding)

To deepen understanding, explore alternative methods:
- **Mathematical Induction**: Prove the formula by assuming it holds for $n$ and showing it holds for $n+1$.
    - This is a verification approach
- **Telescoping Series**: Use $(k+1)^4 - k^4 = 4k^3 + 6k^2 + 4k + 1$ to derive the sum.
    - This is a top-down derivation approach

This comprehensive approach ensures a holistic grasp of the concept.
