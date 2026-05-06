---
title: "Arithmetic Sum Generalisation"
source_notebook: "discrete-mathematics/series-and-sequences/arithmetic-sum/arithmetic-sum-generalisation.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/arithmetic-sum/arithmetic-sum-generalisation.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Arithmetic Sum Generalisation

Lets look at this

$$
3 + 6 + 9 + \cdots + 3n
$$

Which can be written like this

$$
3 + 6 + 9 + \cdots + 3n = \sum_{k=1}^n 3k \\
$$

Simplify

$$
\begin{align*}
    \sum_{k=1}^n 3k &= 3 \sum_{k=1}^n k \\
    &= 3 \cdot \dfrac{n(n+1)}{2} \\
    &= \dfrac{3}{2} n(n+1) \\
\end{align*}
$$

So we get this

$$
\sum_{k=1}^n 3k = \dfrac{3}{2} n(n+1)
$$

Which can be separated into

$$
\boxed{\dfrac{3}{2}} \quad \text{and} \quad \boxed{n(n+1)}
$$

Which is

$$
\boxed{\text{Constant}} \quad \text{and} \quad \boxed{n(n+1)}
$$

> I wonder if this can be generalised for any multiple? Well, lets see!

# Generalising series of any multiples

So we should start here

$$
\sum_{k=1}^n ck, \space \text{where c is a constant,} \space c \in\mathbf{R}
$$

Break it down

$$
\begin{align*}
    \sum_{k=1}^n ck &= c \sum_{k=1}^n k \\
    &= c \cdot \dfrac{n(n+1)}{2} \\
    &= \dfrac{c}{2} n(n+1) \\
\end{align*}
$$

Thus

$$
\boxed{
    \sum_{k=1}^n ck = \dfrac{c}{2} n(n+1)
}
$$

> Notice that the denominator `2` means there may be simpler forms for even numbers, lets check out what simpler forms exist for the `integer` multiples!

# Generalising for integer multiples

Let $m \in \mathbf Z$

$$
\text{Let the odd numbers be} \space \underline{c_{odd}} = 2m - 1
$$

$$
\text{Let the even numbers be} \space \underline{c_{even}} = 2m
$$

Separate the general form into odd and even multiples

For odd multiples, it actually stays the same

$$
\boxed{
    \sum_{k=1}^n c_{odd} \cdot k = \dfrac{c_{odd}}{2} \space n(n+1)
}
$$

But if you really wanted to, you could of course do this

$$
\begin{align*}
    \sum_{k=1}^n c_{odd} \cdot k &= \dfrac{c_{odd}}{2} \cdot n(n+1) \\
    &= \dfrac{2m - 1}{2} \cdot n(n+1) \\
    &= \biggr( \dfrac{\cancel{2}m}{\cancel{2}} - \dfrac{1}{2} \biggr) \cdot n(n+1) \\
    &= \biggr( m - \dfrac{1}{2} \biggr) \cdot n(n+1) \\
\end{align*}
$$

For even multiples, a little bit of change

$$
\begin{align*}
    \sum_{k=1}^n c_{even} \cdot k &= \dfrac{c_{even}}{2} \cdot n(n+1) \\
    &= \dfrac{\cancel{2}m}{\cancel{2}} \cdot n(n+1) \\
    &= m \cdot n(n+1) \\
\end{align*}
$$

Since $m \in \mathbf Z$, let us use a new multiple to represent this constant

$$
c = m, \space c \space \text{represents any constant}
$$

Thus for even multiples is

$$
\boxed{
    \sum_{k=1}^n c_{even} \cdot k =  c \cdot n(n+1), \space \text{where c is either even or odd}
}
$$

---

## Conclusion

$$
\sum_{k=1}^n c_{odd} \cdot k = \boxed{\dfrac{c_{odd}}{2} \space n(n+1)}
\quad \text{or} \quad
\sum_{k=1}^n c_{even} \cdot k =  \boxed{c \cdot n(n+1), \space \text{where c is either even or odd}}
$$

---

But how about sums like this

$$
5 + 8 + 11 + \cdots + (3n + 2)
$$

Where every number is has a common difference, but they are not multiples of each other because they are displaced by some constant
- In the above case, the displacement is `2` units

$$
(3+2) + (6+2) + (9+2) + \cdots + (3n + 2)
$$

Does this mean that any series with `common` difference can be generalised from the series of `constant` multiples?

Lets find out.

---

# General Arithmetic Series

The sum of the displaced multiples series can be seen like this

$$
\sum_{k=1}^n \underline{ck + b}, \space \text{where b is the displacement}, b \in \mathbf{R}
$$

Expand and Simplify

$$
\begin{align*}
    \sum_{k=1}^n \underline{ck + b} &= c\sum_{k=1}^n k + \sum_{k=1}^n b \\
    &= c \cdot \dfrac{n(n+1)}{2} + nb \\
    &= n \biggr[ \dfrac{c}{2} \space (n+1) + b \biggr]
\end{align*}
$$

Thus

$$
\boxed{
    \sum_{k=1}^n \underline{ck + b} = n \biggr[ \dfrac{c}{2} \space (n+1) + b \biggr]
}
$$

This looks oddly familiar ... where have I seen it before ... ?
- It looks like the arithmetic sum

$$
\text{Arithmetic Sum,} \space \sum_{j=1}^n j = \space \dfrac{n}{2} [2a + (n-1)d]
$$

We see that in the original equation the half factor is on the inside of the bracket,

$$
\textcolor{lightgray}{\sum_{k=1}^n \underline{ck + b} = n} \biggr[ \dfrac{c}{2} \space (n+1) + \textcolor{lightgray}{b} \biggr]
$$

and in the arithemtic sum it is on the outside

$$
\textcolor{lightgray}{\sum_{k=1}^n k = } \dfrac{n}{2} \textcolor{lightgray}{[2a + (n-1)d]}
$$

Thus lets move it in

$$
\dfrac{n}{2} \space [2a + (n-1)d] \\
$$

$$
n \biggr[ a + \dfrac{(n-1)d}{2} \biggr]
$$

Rearranging the terms

$$
n \biggr[ \dfrac{(n-1)d}{2} + a \biggr]
$$

Shift the numerators

$$
n \biggr[\dfrac{d}{2}(n-1) + a \biggr]
$$

We get

$$
\text{Arithmetic Sum} = n \biggr[\dfrac{d}{2}(n-1) + a \biggr]
$$

AHA!

The structure of the arithmetic sum matches our sum of multiples with displacement!

$$
\sum_{k=1}^n \underline{ck + b} = n \biggr[ \dfrac{c}{2} \space (n+1) + b \biggr] \Longleftrightarrow n \biggr[\dfrac{d}{2}(n-1) + a \biggr] = \sum_{k=1}^n k
$$

Thus

$$
\sum_{k=1}^n \underline{ck + b} = \sum_{j=1}^n j
$$

Or rather, that any arithmetic sequence can be also expanded in this way

$$
\boxed{
    \sum_{j=1}^n j = \sum_{k=1}^n \underline{ck + b}
}
$$

---

It is awesome discovery!

We used the formula for the arithmetic series from `1` to `n` to get our own formula
- That means this generalisation preserves the structure of the arithmetic series, because every term still has a common difference
- Therefore, this is the general representation of the arithmetic formula in summation terms

$$
\boxed{
\text{General Sum of Arithmetic Sequence =} \sum_{k=1}^n \underline{ck + b}
}
$$

$$
\space \text{where c is the constant multiple, b is the displacement}, c \in \mathbf{R}, b \in \mathbf{R}
$$

---

# Conclusion

### Series of `Any` Multiple
$$
\boxed{
    \sum_{k=1}^n ck = \dfrac{c}{2} n(n+1)
}
$$

### Series of `Integer` Multiple

$$
\sum_{k=1}^n c_{odd} \cdot k = \boxed{\dfrac{c_{odd}}{2} \space n(n+1)}
\quad \text{or} \quad
\sum_{k=1}^n c_{even} \cdot k =  \boxed{c \cdot n(n+1), \space \text{where c is either even or odd}}
$$

### Series of `Integer` Multiple with `Displacement`
#### I.e. Arithmetic Sum

$$
\boxed{
\text{General Sum of Arithmetic Sequence =} \sum_{k=1}^n \underline{ck + b}
}
$$

$$
\space \text{where c is the constant multiple, b is the displacement}, c \in \mathbf{R}, b \in \mathbf{R}
$$
