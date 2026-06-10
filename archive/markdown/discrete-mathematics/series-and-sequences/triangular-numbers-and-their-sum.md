---
title: "Triangular Numbers"
source_notebook: "discrete-mathematics/series-and-sequences/triangular-numbers-and-their-sum.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/triangular-numbers-and-their-sum.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Triangular Numbers

We know that the arithmetic sum is

$$
\sum_{k=1}^{n} k = 1 + 2 + 3 + \cdots + n = \dfrac{n(n+1)}{2}
$$

Let's do something of recursion!

Let's create a series of arithmetic sums up to that point!

$$
\sum_{k=1}^{1} k \quad , \space \sum_{k=1}^{2} k \quad , \space \sum_{k=1}^{3} k \quad , \space \cdots , \sum_{k=1}^{n} k
$$

Use the formula

$$
\dfrac{\boxed{1}(\boxed{1}+1)}{2}, \dfrac{\boxed{2}(\boxed{2}+1)}{2}, \dfrac{\boxed{3}(\boxed{3}+1)}{2}, \cdots, \dfrac{n(n+1)}{2}
$$

Evaluate

$$
1, 3, 6, 10, \cdots, \dfrac{n(n+1)}{2}
$$

These are actually the triangular numbers!

They represent the number of dots required to arrange into an **equilateral triangle**.

For example:
- The 1st triangular number is `1` → one dot

$$
\bullet
$$

- The 2nd is `3` → a two-row triangle `(1 + 2)`

$$
\begin{array}{c}
    \bullet \\
    \bullet \quad \bullet \\
\end{array}
$$

- The 3rd is `6` → a three-row triangle `(1 + 2 + 3)`

$$
\begin{array}{c}
    \bullet \\
    \bullet \quad \bullet \\
    \bullet \quad \bullet \quad \bullet \\
\end{array}
$$

- The 4th is `10` → a four-row triangle `(1 + 2 + 3 + 4)`

$$
\begin{array}{c}
    \bullet \\
    \bullet \quad \bullet \\
    \bullet \quad \bullet \quad \bullet \\
    \bullet \quad \bullet \quad \bullet \quad \bullet \\
\end{array}
$$

And so on.

Therefore, the `n`-th triangular number is simply the sum of the first `n` natural numbers:

$$
T_n = \sum_{k=1}^n k = \dfrac{n(n+1)}{2}
$$
Numbers that creates a growing equilateral triangle, when expressed in dots!

# Sum of Triangular Numbers

Now that we know that triangular numbers are, we can go and find its sum, which is expressed like this

$$
\dfrac{\boxed{1} \left( \boxed{1} + 1 \right)}{2} + \dfrac{\boxed{2} \left( \boxed{2} + 1 \right)}{2} + \dfrac{\boxed{3} \left( \boxed{3} + 1 \right)}{2} + \cdots + \dfrac{\boxed{n} \biggr( \boxed{n} + 1 \biggr)}{2}
$$

Compressed is like this

$$
\sum_{k=1}^n \dfrac{k(k+1)}{2}
$$

Which when we factor out the constant, we have

$$
\dfrac{1}{2} \sum_{k=1}^n k(k+1)
$$

Notice the `sum of 2 consecutive multiples`

$$
\textcolor{lightgray}{\dfrac{1}{2}} \sum_{k=1}^n k(k+1)
$$

We have derived in another notebook as this

$$
\sum_{k=1}^n k(k+1) = \dfrac{n(n+1)(n+2)}{3}
$$

Thus, when we substitute it back in

$$
\dfrac{1}{2} \sum_{k=1}^n k(k+1) = \dfrac{1}{2} \cdot \boxed{\dfrac{n(n+1)(n+2)}{3}}
$$

---

Then combine the constant back, we have the general formula

$$
\boxed{
    \sum_{k=1}^n \dfrac{k(k+1)}{2} = \dfrac{n(n+1)(n+2)}{6}
}
$$
