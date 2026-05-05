---
title: "Understanding Arithmetic Sums Through Symmetry of Averages"
source_notebook: "discrete-mathematics/series-and-sequences/arithmetic-sum/arithmetic-sum.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Understanding Arithmetic Sums Through Symmetry of Averages

The sum of an arithmetic series is a classic result in mathematics, often proven using the method attributed to Gauss, which pairs terms from the ends of the sequence.

> For example, to sum the numbers $1 + 2 + \cdots + 100$, Gauss paired terms from the ends ($1 + 100$, $2 + 99$, etc.) to derive the total

But lets explain it from an alternative perspective, revealing why this pairing works fundamentally

# Averages as Symmetry on a Number Line

Let’s rethink what an average means for numbers in an arithmetic sequence, where each term increases by a common difference.
- Instead of just “sum divided by the number of terms,”
- We can see the average as the central point around which the numbers are symmetrically balanced.

Consider any term:

$$
\large\boxed{a}
$$

If we move a some distance `d` away from the term, we can get to 2 points

$$
\large{\boxed{a - d} \longleftarrow a \longrightarrow \boxed{a + d}}
$$

Moving the `same amount in opposite directions` causes `a` to stay the `numerical centre`
- aka, the **average**

$$
\large{\textcolor{lightgray}{\boxed{a - d}} \textcolor{lightgray}{\longleftarrow} a \textcolor{lightgray}{\longrightarrow} \textcolor{lightgray}{\boxed{a + d}}}
$$

We can continue this pattern on and on, keeping `a` the **average**

$$
\large{\boxed{a - d} \longleftarrow a \longrightarrow \boxed{a + d}}
$$

$$
\large{ \boxed{a - 2d} \longleftarrow \boxed{a - d} \longleftarrow a \longrightarrow \boxed{a + d} \longrightarrow \boxed{a + 2d}}
$$

$$
\large{ \textcolor{gray}{\cdots \boxed{a - 3d}} \longleftarrow \boxed{a - 2d} \longleftarrow \boxed{a - d} \longleftarrow a \longrightarrow \boxed{a + d} \longrightarrow \boxed{a + 2d} \longrightarrow \textcolor{gray}{\cdots \boxed{a + 3d}}}
$$

Thus,

$$
\colorbox{lightgray}{If we keep moving the same amount in both directions, `a` will keep being the average}
$$

# Finding the Anchor Points for Calculating the Average

The **average** of any 2 points equidistant from the mid-point`a` is always `a`:

$$
\dfrac{ \textcolor{lightgray}{(} a \textcolor{lightgray}{-} \textcolor{lightgray}{0} \textcolor{lightgray}{)} + \textcolor{lightgray}{(} a \textcolor{lightgray}{+} \textcolor{lightgray}{0} \textcolor{lightgray}{)} }{2} = a
$$

$$
\dfrac{(a - d) + (a + d)}{2} = a
$$

$$
\dfrac{(a - 2d) + (a + 2d)}{2} = a
$$

$$
\vdots
$$

$$
\dfrac{\boxed{a - (n - 1)d} + \boxed{a + (n - 1)d}}{2} = a
$$

This equally means the **average** of any 2 points `equidistant from the furthest points` from `a` is also always `a`

$$
\dfrac{\boxed{a - (n - 1)d} + \boxed{a + (n - 1)d}}{2} = a
$$

$$
\vdots
$$

$$
\dfrac{(a - 2d) + (a + 2d)}{2} = a
$$

$$
\dfrac{(a - d) + (a + d)}{2} = a
$$

$$
\dfrac{ \textcolor{lightgray}{(} a \textcolor{lightgray}{-} \textcolor{lightgray}{0} \textcolor{lightgray}{)} + \textcolor{lightgray}{(} a \textcolor{lightgray}{+} \textcolor{lightgray}{0} \textcolor{lightgray}{)} }{2} = a
$$

Since the **first** and **last** points always exist,

$$
\colorbox{lightgray}{We can always find the average of the whole sum by taking the average of the first and last points}
$$

> Even for sums with `1` term, whereby the first and last points are itself

# Finalise the Formula

Therefore, since the total of this `symmetric series of common difference`, or in other words, `arithmetic sum`, is:

$$
\boxed{
    \phantom{\biggr(} \textbf{Arithmetic Sum } = \textbf{Average } \cdot \textbf{ Number of Terms} \phantom{\biggr)}
}
$$

## Find the Average

The `Average` can be found like this
$$
\begin{align}
    \text{Average of this series } &= \text{Average of the First Term and Last Term } \\
    \\
    &= \dfrac{\text{First Term} + \text{Last Term}}{2}
\end{align}
$$

Thus the `Average` is

$$
\boxed{
    \text{Average of this series} = \dfrac{\text{First Term} + \text{Last Term}}{2}
}
$$

## Find the Number of Terms

It can be found from the `First Term` and the `Last Term` like so
- The `difference over common difference` will only contain the numbers `from right after the first term, up to the last term`
- Thus, we have to `add 1`, to `account for the first term`

$$
\begin{align}
    \text{Number of Terms } &= \dfrac{\text{Difference between First Term and Last Term}}{\text{Common Difference}} + 1 \\
    \\
    &= \dfrac{\text{Last Term - First Term}}{\text{Common Difference}} + 1 \\
\end{align}
$$

Thus the `Number of Terms` is ,

$$
\boxed{
    \text{Number of Terms } = \dfrac{\text{Last Term - First Term}}{\text{Common Difference}} + 1
}
$$


##  Arithmetic Sum Formula in Terms of First Term and Last Term

Therefore, we get

$$
\boxed{
    \phantom{\Biggr(}
        \textbf{Arithmetic Sum } = \biggr( \dfrac{\textbf{First Term} + \textbf{Last Term}}{2} \biggr) \biggr( \dfrac{\textbf{Last Term - First Term}}{\textbf{Common Difference}} + 1 \biggr)
    \phantom{\Biggr)}
}
$$

# Rebuilding any Arithmetic Sequence

Consider the simple case:
$$
\boxed{a}
$$

In an arithmetic sequence, there is a common difference of `d`,

Normally the sequence is built in one direction based off the base term `a`.

In sum `S` with `n` terms:

$$
\begin{align}
    &S_1 = a \\
    &S_2 = a + \boxed{a + d} \\
    &S_3 = a + \boxed{a + d} + \boxed{a + 2d} \\
    &S_n = a + \boxed{a + d} + \boxed{a + 2d} + \dots + \boxed{a + (n - 1)d}
\end{align}
$$

## Odd-Numbered Terms

An equal way of viewing the arithmetic sequence is to `build from both sides`:

$$
\begin{array}{cc}
    S_1 = & a \\
    S_3 = & \boxed{a - d} + a + \boxed{a + d} \\
    S_5 = & \boxed{a - 2d} + \boxed{a - d} + a + \boxed{a + d} + \boxed{a + 2d} \\
    S_{2n-1} = & \boxed{a - \left( \dfrac{n - 1}{2} \right) d} + \dots + \boxed{a - 2d} + \boxed{a - d} + a + \boxed{a + d} + \boxed{a + 2d} + \dots + \boxed{a + \left( \dfrac{n - 1}{2} \right) d} \\
\end{array}
$$

## Even-Numbered Terms

This series has `odd amount of terms`, but it can also get it in `even terms` like so:
- Where the `average doesn't exist as a term` in sums with `even number of terms`

$$
\begin{array}{cc}
    S_0 = & \textcolor{lightgray}{a} \\
    S_2 = & \boxed{a - \dfrac{d}{2}} + \textcolor{lightgray}{a} + \boxed{a + \dfrac{d}{2}} \\
    S_4 = & \boxed{a - \biggr( d + \dfrac{d}{2} \biggr)} + \boxed{a - \dfrac{d}{2}} + \textcolor{lightgray}{a} + \boxed{a + \dfrac{d}{2}} + \boxed{a + \biggr( d + \dfrac{d}{2} \biggr)} \\
    S_{2n} = & \boxed{a - \Biggr( \left[ \dfrac{n}{2} - 1 \right] d + \dfrac{d}{2} \Biggr)} + \dots + \boxed{a - \biggr( d + \dfrac{d}{2} \biggr)} + \boxed{a - \dfrac{d}{2}} + \textcolor{lightgray}{a} + \boxed{a + \dfrac{d}{2}} + \boxed{a + \biggr( d + \dfrac{d}{2} \biggr)} + \dots + \boxed{ a + \Biggr( \left[ \dfrac{n}{2} - 1 \right] d + \dfrac{d}{2} \Biggr)} \\
\end{array}
$$

We can then simplify to this
- Let $b = \dfrac{d}{2}$

$$
\begin{array}{cc}
    S_2 = & \textcolor{lightgray}{a} \\
    S_2 = & \boxed{a - b} + \textcolor{lightgray}{a} + \boxed{a + b} \\
    S_4 = & \boxed{a - 3b} + \boxed{a - b} + \textcolor{lightgray}{a} + \boxed{a + b} + \boxed{a + 3b} \\
    S_{2n} = & \boxed{a - \biggr( n-1 \biggr) b} + \dots + \boxed{a - 3b} + \boxed{a - b} + \textcolor{lightgray}{a} + \boxed{a + b} + \boxed{a + 3b} + \dots + \boxed{a + \biggr( n-1 \biggr) b} \\
\end{array}
$$

# Concluding the Pattern

Therefore, for any number of terms, the average will always be `a`, and the total can be calculated as:

$$
\text{Arithmetic Sum } = \text{Average } \cdot \text{Number of Terms}
$$

Then, the `average` we know is equals to this

$$
\text{Average} = \dfrac{\text{First Term} + \text{Last Term}}{2}
$$

Thus,

$$
\boxed{
    \textbf{Arithmetic Sum } = \dfrac{\textbf{First Term} + \textbf{Last Term}}{2} \cdot \textbf{Number of Terms}
}
$$


## Arithmetic Sum Derivation

**Thus**:

Let an arithmetic sequence be defined with:
- **First term**: $a$
- **Common difference**: $d$
- **Number of terms**: $n$
- **Terms**: $a, a + d, \ldots, a + (n-1)d$
- **Arithmetic Sum**: $S_n = a + (a + d) + \cdots + (a + (n-1)d)$


The `arithmetic sum` can be `derived` as such

$$
\begin{align}
    S_n &= \dfrac{\text{First Term} + \text{Last Term}}{2} \cdot \text{Number of Terms} \\
    &= \dfrac{a + \biggr[ a + (n-1)d \biggr]}{2} \cdot n \\
    &= \dfrac{2a + (n-1)d}{2} \cdot n \\
    &= \dfrac{n}{2} \biggr[ 2a + (n-1)d \biggr]
\end{align}
$$

# Arithmetic Sum General Formula

Therefore, we get to our familiar formula for the arithmetic sum:

$$
\boxed{\textbf{Arithmetic Sum} = \dfrac{n}{2} \biggr[ 2a + (n-1)d \biggr]}
$$

# Application to the Sum of Arithmetic Sequence with Common Difference 1

Which is expressed like so

$$
\Huge{
S_1 = 1 + 2 + 3 + \dots + n
}
$$

## Arithmetic Sum Derivation

List out a few important variables
- **First term**: $1$
- **Last term**: $n$
- **Number of terms**: $n$

The `Sum of Natural Numbers` can be `derived` as such

$$
\begin{align}
    \text{Sum of Natural Numbers} &= \dfrac{\text{First Term} + \text{Last Term}}{2} \cdot \text{Number of Terms} \\
    &= \dfrac{1 + n}{2} \cdot n \\
    &= \dfrac{n(n+1)}{2}
\end{align}
$$

# Sum of Natural Numbers

Therefore, we get to our familiar formula for the arithmetic sum:

$$
\boxed{
    \textbf{Sum of Natural Numbers} = \dfrac{n(n+1)}{2}
}
$$
