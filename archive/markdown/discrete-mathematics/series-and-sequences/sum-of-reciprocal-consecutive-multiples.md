---
title: "Denominator Consecutive Multiples"
source_notebook: "discrete-mathematics/series-and-sequences/sum-of-reciprocal-consecutive-multiples.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/sum-of-reciprocal-consecutive-multiples.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Denominator Consecutive Multiples

Consider this series

$$
\dfrac{1}{2} + \dfrac{1}{6} + \dfrac{1}{12} + \dfrac{1}{20} + \dfrac{1}{30} + \cdots
$$

Notice that the denominators consist of consecutive multiples

$$
\dfrac{1}{1\cdot2} + \dfrac{1}{2\cdot3} + \dfrac{1}{3\cdot4} + \dfrac{1}{4\cdot5} + \dfrac{1}{5\cdot6} + \cdots
$$

Which simplfies to

$$
\sum_{k=1}^n \dfrac{1}{n(n+1)}
$$

How do we solve this?
- We can attempt to simplify this fraction even more by breaking it into smaller fractions each with its prime polynomial denominator

# Solving with Partial Fractions

Focusing on this

$$
\textcolor{lightgray}{\sum_{k=1}^n} \dfrac{1}{n(n+1)}
$$


Set up partial fractions

$$
\dfrac{1}{n(n+1)} = \dfrac{A}{n} + \dfrac{B}{n+1}
$$

Start solving

Let `A` and `B` be comparable by making the denominators the same on both sides

$$
\dfrac{1}{n(n+1)} = \dfrac{A(n+1)}{n(n+1)} + \dfrac{Bn}{(n+1)n}
$$

Combine

$$
\dfrac{1}{n(n+1)} = \dfrac{A(n+1) + Bn}{n(n+1)}
$$

Since the denominators are the same now, we can just compare the numerators instead

$$
1 = A(n+1) + Bn
$$

Lets expand and group by `n`

$$
1 = An + A + Bn
$$

Where

$$
1 = (A+B)n + A
$$

Now when we compare the coefficients of the constants on both sides we get:

$$
\boxed{A = 1}
$$

When we compare the coefficients of `n` on both sides we get:

$$
A + B = 0
$$

Which is

$$
1 + B = 0
$$

$$
\boxed{B = -1}
$$

Thus now we have both `A` and `B`, we can complete the partial fraction decomposition as such

$$
\dfrac{1}{n(n+1)} = \dfrac{\boxed{1}}{n} + \dfrac{\boxed{-1}}{n+1}
$$

Which when redistributed is thus!

$$
\boxed{
    \dfrac{1}{n(n+1)} = \dfrac{1}{n} - \dfrac{1}{n+1}
}
$$

# Telescoping Sum

Now when we go back to the sum

$$
\sum_{k=1}^n \dfrac{1}{n(n+1)}
$$

We have instead

$$
\sum_{k=1}^n \left( \dfrac{1}{n} - \dfrac{1}{n+1} \right)
$$

If you notice, this is a telescoping sum!
- Which means there is a convergent answer to a problem of any length!

Let us set it up

$$
\begin{align*}
    \sum_{k=1}^n \left( \dfrac{1}{n} - \dfrac{1}{n+1} \right) &= \dfrac{1}{1} - \dfrac{1}{2} \\
    & + \left( \dfrac{1}{2} - \dfrac{1}{3} \right) \\
    & + \left( \dfrac{1}{3} - \dfrac{1}{4} \right) \\
    & \vdots \\
    & + \left( \dfrac{1}{n} - \dfrac{1}{n+1} \right) \\
\end{align*}
$$

We can then cancel out the terms that came negative the previous iteration and positive the next

$$
\begin{align*}
    \sum_{k=1}^n \left( \dfrac{1}{n} - \dfrac{1}{n+1} \right) &= \dfrac{1}{1} - \cancel{\dfrac{1}{2}} \\
    & + \left( \cancel{\dfrac{1}{2}} - \cancel{\dfrac{1}{3}} \right) \\
    & + \left( \cancel{\dfrac{1}{3}} - \cancel{\dfrac{1}{4}} \right) \\
    & + \left( \cancel{\dfrac{1}{4}} - \cdots \right) \\
    & \vdots \\
    & + \left( \cdots - \cancel{\dfrac{1}{n}} \right) \\
    & + \left( \cancel{\dfrac{1}{n}} - \dfrac{1}{n+1} \right) \\
    & = 1 - \dfrac{1}{n+1}
\end{align*}
$$

Thus we have

$$
\sum_{k=1}^n \left( \dfrac{1}{n} - \dfrac{1}{n+1} \right) = 1 - \dfrac{1}{n+1}
$$

Focus on simplifying this part

$$
\textcolor{lightgray}{\sum_{k=1}^n \left( \dfrac{1}{n} - \dfrac{1}{n+1} \right) =} 1 - \dfrac{1}{n+1}
$$

---

We have

$$
1 - \dfrac{1}{n+1}
$$

Then

$$
\dfrac{n+1}{n+1} - \dfrac{1}{n+1}
$$

Then

$$
\dfrac{(n + 1) - 1}{n+1}
$$

Thus

$$
\dfrac{n}{n+1}
$$

And thus

$$
\sum_{k=1}^n \left( \dfrac{1}{n} - \dfrac{1}{n+1} \right) = \dfrac{n}{n+1}
$$

# Conclusion

And therefore, the sum of reciprocal consecutive multiples is as such!

$$
\boxed{
    \sum_{k=1}^n \dfrac{1}{n(n+1)} = \dfrac{n}{n+1}
}
$$
