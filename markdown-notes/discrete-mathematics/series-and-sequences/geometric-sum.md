---
title: "What is the Geometric Sum"
source_notebook: "discrete-mathematics/series-and-sequences/geometric-sum.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# What is the Geometric Sum

For a geometric sum, it takes the form

$$
S_n = a + ar + ar^{2} + ar^{3} + \cdots + ar^{n-1}, \text{ for n terms}
$$

Where `a` is the first term and `r` is the constant multiple of the previous terms

Which means it can also be presented in this form:

$$
S_n = a \space (1 + r + r^{2} + r^{3} + \cdots + r^{n-1})
$$

#### How do we derive the general form of the geometric sum?
- Well, notice that each term ratio to the next term is exactly `r`?
- And we want to simplify this formula
- That means each term can move into the next term by exactly the same ratio `r`
- Which means in a series, most terms stay the same when the whole series is moved up by factor of `r`
- We can use this fact to set up a circumstance whereby we can cancel out almost all of the terms in between and just leave the first and last term

# Work it Out

Let us focus on this part instead

$$
\textcolor{lightgray}{S_n = a \space (} 1 + r + r^{2} + r^{3} + \cdots + r^{n-1}\textcolor{lightgray}{)}
$$

Let this be

$$
Z = 1 + r + r^{2} + r^{3} + \cdots + r^{n-1}
$$

Now lets set up a difference between itself and `r` of itself

$$
\begin{align}
    Z \space (1-r) &= (1 + r + r^{2} + r^{3} + \cdots + r^{n-1}) \space (1-r)\\
    \\
    &= \space (1 + r + r^{2} + r^{3} + \cdots + r^{n-1}) \\
    & \quad - (r + r^{2} + r^{3} + r^{4} + \cdots + r^{n}) \\
    \\
    &= (1 + r + r^{2} + r^{3} + r^{4} + \cdots + r^{n-1}) \\
    &\qquad \space - (r + r^{2} + r^{3} + r^{4} + \cdots + r^{n-1} + r^{n})
\end{align}
$$

Here, we can cancel out the rest in between
- And introducing a new largest term

$$
\begin{align}
    Z \space (1-r) &= (1 + \cancel{r} + \cancel{r^{2}} + \cancel{r^{3}} + \cancel{r^{4}} + \cdots + \cancel{r^{n-1}}) \\
    &\qquad \space - (\cancel{r} + \cancel{r^{2}} + \cancel{r^{3}} + \cancel{r^{4}} + \cdots + \cancel{r^{n-1}} + r^{n}) \\
    &= 1 - r^{n}\\
\end{align}
$$

Therefore, finding the simplified formula for $Z$

$$
\boxed{
    Z = \dfrac{1 - r^{n}}{1-r}
}
$$

---

Difference works both ways, we can thus take the other difference

$$
\begin{align}
    Z \space (r-1) &= \qquad \quad (\cancel{r} + \cancel{r^{2}} + \cancel{r^{3}} + \cancel{r^{4}} + \cdots + \cancel{r^{n-1}} + r^{n}) \\
    &\qquad - (1 + \cancel{r} + \cancel{r^{2}} + \cancel{r^{3}} + \cancel{r^{4}} + \cdots + \cancel{r^{n-1}}) \\
    \\
    &= r^{n} - 1\\
\end{align}
$$

Thus, we get the other part of the formula, formed by taking the difference

$$
\boxed{
    Z = \dfrac{r^{n} - 1}{r-1}
}
$$

---

We can actually just stop here, since this describes the most basic geometric series

$$
\boxed{
    Z = \dfrac{1 - r^{n}}{1-r} \qquad \text{or} \qquad  Z = \dfrac{r^{n} - 1}{r-1}
}
$$

But since the constant is part of the formula lets continue

# General Form

Substitute it back
$$
\textcolor{lightgray}{S_n = a \space (}1 + r + r^{2} + r^{3} + \cdots + r^{n-1} \textcolor{lightgray}{)}
$$

We have

$$
S_n = a \left( \dfrac{1 - r^{n}}{1-r} \right) \qquad \text{or} \qquad S_n = a \left( \dfrac{r^{n} - 1}{r-1} \right)
$$

Or more normally seen as

$$
\boxed{
    S_n = \dfrac{a(1 - r^{n})}{1-r} \qquad \text{or} \qquad S_n = \dfrac{a(r^{n} - 1)}{r-1}
}
$$

# Exponentials

For exponentials if $|r| > 1$ then $r^{n}$ grows exponentially, it grows without bound
- But if $|r| < 1$, then $r^{n}$ shrinks exponentially, thus it is bounded

Thus, where $|r| > 1$


$$
\lim_{n \to \infty}{r^n} = \infty
$$

Thus for the geometric series as well

$$
\lim_{n \to \infty}{\dfrac{a(1-r^n)}{1-r}} = \infty
$$

Thus for $|r| < 1$ there is no convergent answer

But how about for $|r| < 1$ ?

$$
\lim_{n \to \infty}{r^n} = 0
$$

The geometric series will be

$$
\lim_{n \to \infty}{\dfrac{a(1-r^n)}{1-r}}
$$

Which everything else is regarded as a constant except where the limit applies

$$
\dfrac{a \biggr( 1- (\lim_{n \to \infty}{r^n}) \biggr)}{1-r}
$$

Evaluate

$$
\dfrac{a(1 - 0)}{1-r}
$$

And simplify

$$
\dfrac{a}{1-r}
$$

Thus

$$
\lim_{n \to \infty}{\dfrac{a(1-r^n)}{1-r}} = \dfrac{a}{1-r}
$$

# Convergent Form

Thus, we conclude that the limit to infinity of geometric series with $|r| < 1$ has a convergent answer!

$$
\boxed{
    \text{Infinite Geometric Sum where |r| < 1} = \dfrac{a}{1-r}
}
$$
