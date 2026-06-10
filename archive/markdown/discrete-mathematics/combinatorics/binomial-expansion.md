---
title: "Binomial Expansion"
source_notebook: "discrete-mathematics/combinatorics/binomial-expansion.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/combinatorics/binomial-expansion.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Binomial Expansion

What is the binomial expansion?

$$
(x + y)^n = \underbrace{(x+y)(x+y)(x+y)\cdots(x+y)}_{\text{n times}}
$$

How exactly can we make this into its expanded form?

Lets look into it further

---
Every term is made up of a combination of either `x` or `y` from every of these `x+y` terms

$$
(x+y)\textcolor{lightgray}{(x+y)}\textcolor{lightgray}{(x+y)}\textcolor{lightgray}{\cdots}\textcolor{lightgray}{(x+y)}
$$

$$
\textcolor{lightgray}{(x+y)}(x+y)\textcolor{lightgray}{(x+y)}\textcolor{lightgray}{\cdots}\textcolor{lightgray}{(x+y)}
$$

$$
\textcolor{lightgray}{(x+y)}\textcolor{lightgray}{(x+y)}(x+y)\textcolor{lightgray}{\cdots}\textcolor{lightgray}{(x+y)}
$$

$$
\textcolor{lightgray}{(x+y)}\textcolor{lightgray}{(x+y)}\textcolor{lightgray}{(x+y)}\cdots\textcolor{lightgray}{(x+y)}
$$

$$
\textcolor{lightgray}{(x+y)}\textcolor{lightgray}{(x+y)}\textcolor{lightgray}{(x+y)}\textcolor{lightgray}{\cdots}(x+y)
$$

From every `x+y` term, once you choose one, you will have to leave out the other
- Thus the choice is mutually exclusive

Since they are mutually exclusive, it means that it is equivalent to having `n` choices of `x` or `y`, and if we choose `k` amounts of `x` from these `n` choices, we automatically pick the corresponding `n-k` amounts of `y` to be part of that same term.
- Thus, since every term is made up of $\dbinom{n}{k}$ of `x` and corresponding $\dbinom{n}{n-k}$ amounts of `y`,
- Choosing `k` or `n-k` from `n` choices, yields the same results

Thus

$$
\boxed{
    \dbinom{n}{k} = \dbinom{n}{n-k}
}
$$

As every one of these choices from $0\le k \le n$ for `x`, `(or y)` is possible.

Lets list the distribution of these possibilities in a table, to build up the binomial expansion:

$$
(x + y) ^ {n}
$$

# Distribution of its Terms

## Kinds of Combinations

Starting from the most extreme end, we iterate up one by one for `x`, and correspondingly, down one by one for `y` until the very other end

$$
\begin{array}{c|c|c}
    \quad x \quad & \quad y \quad &\text{Variables} \\
    \hline \\
    0 & n & x^{0}y^{n} \\
    1 & n-1 & x^{1}y^{n-1} \\
    2 & n-2 & x^{2}y^{n-2} \\
    \vdots & \vdots & \vdots\\
    n-2 & 2 & x^{n-2}y^{2} \\
    n-1 & 1 & x^{n-1}y^{1} \\
    n & 0 & x^{n}y^{0} \\
\end{array}
$$

---
- Notice there are `n+1` terms as for either `x` or `y`, it has to go from `not being chosen` (contributing `1 way`)
- Then from choosing `1` to `fully chosen` (contributing `n ways`)
- Thus `n+1` kinds of combinations

$$
\underbrace{\_\_x^{0}y^{n} + \_\_x^{1}y^{n-1} + \_\_x^{2}y^{n-2} + \cdots + \_\_x^{n-2}y^{2} + \_\_x^{n-1}y^{1} + \_\_x^{n}y^{0}}_{\text{n+1 terms}}
$$

---

## Amount of Combinations

Add in the number of each term, we have
- Note that the amount of `x` and amount of `y` is equal to each other

$$
\begin{array}{c|c|c|c|c}
    \quad x \quad & \text{Amount of x} & \quad y \quad & \text{Amount of y} & \text{Raw Results}\\
    \hline \\
    0 & \dbinom{n}{0} & n & \dbinom{n}{n} & \dbinom{n}{0} x^{0}y^{n} \\
    1 & \dbinom{n}{1} & n-1 & \dbinom{n}{n-1} & \dbinom{n}{1} x^{1}y^{n-1} \\
    2 & \dbinom{n}{2} & n-2 & \dbinom{n}{n-2} & \dbinom{n}{2} x^{2}y^{n-2} \\
    \vdots & \vdots & \vdots & \vdots & \vdots\\
    n-2 & \dbinom{n}{n-2} & 2 & \dbinom{n}{2} & \dbinom{n}{n-2} x^{n-2}y^{2} \\
    n-1 & \dbinom{n}{n-1} & 1 & \dbinom{n}{1} & \dbinom{n}{n-1} x^{n-1}y^{1} \\
    n & \dbinom{n}{n} & 0 & \dbinom{n}{0} & \dbinom{n}{0} x^{n}y^{0} \\
\end{array}
$$

---

Hence, we get this expression:

$$
\dbinom{n}{0} x^{0}y^{n} +  \dbinom{n}{1} x^{1}y^{n-1} + \dbinom{n}{2} x^{2}y^{n-2} + \cdots + \dbinom{n}{n-2} x^{n-2}y^{2} + \dbinom{n}{n-1} x^{n-1}y^{1} + \dbinom{n}{n} x^{n}y^{0}
$$

---

Notice the pattern between choice and the power of `x` and `y`, and we get this simple summation

$$
\boxed{
    (x+y)^n = \sum_{k=0}^n \dbinom{n}{k} x^{k} y^{n-k}
}
$$

This is the basic summation derived already, but lets go further

## Symmetric Structure

As we know that

$$
\dbinom{n}{k} = \dbinom{n}{n-k}
$$

And we see that these combinations can be simplfied

$$
\dbinom{n}{0} = \dbinom{n}{n} = 1 \\
$$

$$
\dbinom{n}{1} = \dbinom{n}{n-1} = n \\
$$

We can simplify the results as follows

$$
\begin{array}{c|c|c|c|c|c}
    \quad x \quad & \text{Amount of x} & \quad y \quad & \text{Amount of y} & \text{Raw Results} & \text{Simplified Results}\\
    \hline \\
    0 & \dbinom{n}{0} & n & \dbinom{n}{n} & \dbinom{n}{0} x^{0}y^{n} & y^{n}\\
    1 & \dbinom{n}{1} & n-1 & \dbinom{n}{n-1} & \dbinom{n}{1} x^{1}y^{n-1} & nx^{1}y^{n-1}\\
    2 & \dbinom{n}{2} & n-2 & \dbinom{n}{n-2} & \dbinom{n}{2} x^{2}y^{n-2} & \dbinom{n}{2} x^{2}y^{n-2}\\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
    n-2 & \dbinom{n}{n-2} & 2 & \dbinom{n}{2} & \dbinom{n}{n-2} x^{n-2}y^{2} & \dbinom{n}{2} x^{n-2}y^{2} \\
    n-1 & \dbinom{n}{n-1} & 1 & \dbinom{n}{1} & \dbinom{n}{n-1} x^{n-1}y^{1} & nx^{n-1}y^{1}\\
    n & \dbinom{n}{n} & 0 & \dbinom{n}{0} & \dbinom{n}{n} x^{n}y^{0} & x^{n} \\
\end{array}
$$

---
Which is this expression:

$$
y^{n} + nx^{1}y^{n-1} + \dbinom{n}{2} x^{2}y^{n-2} + \cdots + \dbinom{n}{2} x^{n-2}y^{2} + nx^{n-1}y^{1} + x^{n}
$$

---

## Parity and Symmetry

Realise if a series is `symmetric`:

- For `odd number of terms`, it will be `symmetric` about the `term in the middle`

$$
\space T_1,\quad T_2,\quad T_3, \quad \cdots \quad \underline{T_{\text{(n+1)/2}}} \quad \cdots \quad T_{n-2}, \quad T_{n-1}, \quad T_n
$$

Presented in a table

$$
\begin{array}{c|c|c|c|c|c}
    \quad x \quad & \text{Amount of x} & \quad y \quad & \text{Amount of y} & \text{Raw Results} & \text{Simplified Results}\\
    \hline \\
    0 & \dbinom{n}{0} & n & \dbinom{n}{n} & \dbinom{n}{0} x^{0}y^{n} & y^{n}\\
    1 & \dbinom{n}{1} & n-1 & \dbinom{n}{n-1} & \dbinom{n}{1} x^{1}y^{n-1} & nx^{1}y^{n-1}\\
    2 & \dbinom{n}{2} & n-2 & \dbinom{n}{n-2} & \dbinom{n}{2} x^{2}y^{n-2} & \dbinom{n}{2} x^{2}y^{n-2}\\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
    \text{n/2} & \dbinom{n}{\space \frac{n}{2} \space} & \text{n/2} & \dbinom{n}{\space \frac{n}{2} \space} & \dbinom{n}{\space \frac{n}{2} \space} x^{\frac{n}{2}} y^{\frac{n}{2}} & \dbinom{n}{\space \frac{n}{2} \space} x^{\frac{n}{2}} y^{\frac{n}{2}} \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
    n-2 & \dbinom{n}{n-2} & 2 & \dbinom{n}{2} & \dbinom{n}{n-2} x^{n-2}y^{2} & \dbinom{n}{2} x^{n-2}y^{2} \\
    n-1 & \dbinom{n}{n-1} & 1 & \dbinom{n}{1} & \dbinom{n}{n-1} x^{n-1}y^{1} & nx^{n-1}y^{1}\\
    n & \dbinom{n}{n} & 0 & \dbinom{n}{0} & \dbinom{n}{n} x^{n}y^{0} & x^{n} \\
\end{array}
$$

---
Thus, for odd number of terms, we have:

$$
y^{n} + nx^{1}y^{n-1} + \dbinom{n}{2} x^{2}y^{n-2} + \cdots + \underline{\dbinom{n}{\space \frac{n}{2} \space} x^{\frac{n}{2}} y^{\frac{n}{2}}} + \cdots + \dbinom{n }{2} x^{n-2}y^{2} + nx^{n-1}y^{1} + x^{n}
$$

---

- For `even number of terms`, it will be `symmetric` about `2 terms in the middle`

$$
\space T_1,\quad T_2,\quad T_3, \quad \cdots \quad \underline{T_{\text{n/2}}}, \quad \underline{T_{\text{(n+2)/2}}} \quad \cdots \quad T_{n-2}, \quad T_{n-1}, \quad T_n
$$

Presented in a table

$$
\begin{array}{c|c|c|c|c|c}
    \quad x \quad & \text{Amount of x} & \quad y \quad & \text{Amount of y} & \text{Raw Results} & \text{Simplified Results}\\
    \hline \\
    0 & \dbinom{n}{0} & n & \dbinom{n}{n} & \dbinom{n}{0} x^{0}y^{n} & y^{n}\\
    1 & \dbinom{n}{1} & n-1 & \dbinom{n}{n-1} & \dbinom{n}{1} x^{1}y^{n-1} & nx^{1}y^{n-1}\\
    2 & \dbinom{n}{2} & n-2 & \dbinom{n}{n-2} & \dbinom{n}{2} x^{2}y^{n-2} & \dbinom{n}{2} x^{2}y^{n-2}\\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
    \dfrac{n-1}{2} & \dbinom{n}{\frac{n-1}{2}} & \dfrac{n+1}{2} & \dbinom{n}{\frac{n+1}{2}} & \dbinom{n}{\frac{n-1}{2}} x^{\text{(n-1)/2}} y^{\text{(n+1)/2}} & \dbinom{n}{\frac{n-1}{2}} x^{\text{(n-1)/2}} y^{\text{(n+1)/2}} \\
    \dfrac{n+1}{2} & \dbinom{n}{\frac{n+1}{2}} & \dfrac{n-1}{2} & \dbinom{n}{\frac{n-1}{2}} & \dbinom{n}{\frac{n+1}{2}} x^{\text{(n+1)/2}} y^{\text{(n-1)/2}} & \dbinom{n}{\frac{n+1}{2}} x^{\text{(n+1)/2}} y^{\text{(n-1)/2}} \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
    n-2 & \dbinom{n}{n-2} & 2 & \dbinom{n}{2} & \dbinom{n}{n-2} x^{n-2}y^{2} & \dbinom{n}{2} x^{n-2}y^{2} \\
    n-1 & \dbinom{n}{n-1} & 1 & \dbinom{n}{1} & \dbinom{n}{n-1} x^{n-1}y^{1} & nx^{n-1}y^{1}\\
    n & \dbinom{n}{n} & 0 & \dbinom{n}{0} & \dbinom{n}{n} x^{n}y^{0} & x^{n} \\
\end{array}
$$

---
- For `even terms`

$$
y^{n} + nx^{1}y^{n-1} + \dbinom{n}{2} x^{2}y^{n-2} + \cdots + \underline{\dbinom{n}{\frac{n-1}{2}} x^{\text{(n-1)/2}}} y^{\text{(n+1)/2}} + \underline{\dbinom{n}{\frac{n+1}{2}} x^{\text{(n+1)/2}} y^{\text{(n-1)/2}}} + \cdots + \dbinom{n }{2} x^{n-2}y^{2} + nx^{n-1}y^{1} + x^{n}
$$

---

# Conclusion

We have found the expanded form of the binomial expansion through choice
- Although the way we derived it above starts with $y^n$,
- We can also make it start with $x^{n}$ first by making the starting point `n` instead of `1`
- Effectively, reading the same the same expansion from the other side

$$
\boxed{
    (x + y)^n = \dbinom{n}{n}x^{n}y^{0} + \dbinom{n}{n-1}x^{n-1}y^{1} + \dbinom{n}{n-2} x^{n-2}y^{2} + \cdots + \dbinom{n}{2} x^{2}y^{n-2} + \dbinom{n}{1} x^{1}y^{n-1} + \dbinom{n}{0} x^{0}y^{n}
}
$$

We can also thus simplify them in Summation Notation such that:

$$
\boxed{
    (x+y)^n = \sum_{k=0}^n \dbinom{n}{k} x^{n-k} y^{k} = \sum_{k=0}^n \dbinom{n}{k} x^{k} y^{n-k}
}
$$

---

If we
- Simplify the combination notation,
- Remove terms with power 0,
- Remove the notation for the first power,

$$
\boxed{
    (x + y)^n = x^{n} + n x^{n-1}y + \dbinom{n}{n-2} x^{n-2}y^{2} + \cdots + \dbinom{n}{2} x^{2}y^{n-2} + n xy^{n-1} + y^{n}
}
$$

If we also `highlight the symmetry`, we will have

## Odd Number of Terms
- `n` is an `even number`
- The expansion is `symmetric` about the `middle term`

$$
\boxed{
    (x + y)^n = x^{n} + nx^{n-1}y + \dbinom{n}{2} x^{n-2}y^{2} + \cdots + \underline{\dbinom{n}{\space \frac{n}{2} \space} x^{\frac{n}{2}} y^{\frac{n}{2}}} + \cdots + \dbinom{n}{2} x^{2}y^{n-2} + nxy^{n-1} + y^{n}
}
$$


## Even Number of Terms
- `n` is an `odd number`
- The expansion is `symmetric` about the `2 middle terms`

$$
\boxed{
    (x + y)^n = x^{n} + nx^{n-1}y + \dbinom{n}{2} x^{n-2}y^{2} + \cdots + \underline{\dbinom{n}{\frac{n-1}{2}} x^{\text{(n+1)/2}} y^{\text{(n-1)/2}}} + \underline{\dbinom{n}{\frac{n+1}{2}} x^{\text{(n-1)/2}} y^{\text{(n+1)/2}}} + \cdots + \dbinom{n}{2} x^{2}y^{n-2} + nxy^{n-1} + y^{n}
}
$$

---

#### Thus exemplifying the symmetry of the binomial expansion
