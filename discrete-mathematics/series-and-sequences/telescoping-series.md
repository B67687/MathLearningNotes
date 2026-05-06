---
title: "Introduction to Telescoping"
source_notebook: "discrete-mathematics/series-and-sequences/telescoping-series.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/telescoping-series.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Introduction to Telescoping

Let us start from the duality of arithmetics

Where we have

$$
+a \quad -a
$$

Every addition $+a$ has its counterpart $-a$ that does the opposite effect
- When both are used together, they eliminate each other

We can continuously do either of them

$$
+a \space +a \space +a \space +a \space +a \space +a \cdots
$$

Or

$$
-a \space -a \space -a \space -a \space -a \space -a \cdots
$$

And there is a notation that simplifies this process

$$
\sum_{k=1}^{n} +a = \underbrace{+a \space +a \space +a \space +a \space +a \space +a \cdots + a}_{\text{n terms}}
$$

Or

$$
\sum_{a=1}^{n} -a = \underbrace{-a \space -a \space -a \space -a \space -a \space -a \cdots - a}_{\text{n terms}}
$$

What if we combine them together during the summation?

$$
\sum_{k=1}^{n} +a -a = \overbrace{\underbrace{(+a -a)}_{0} \space \underbrace{(+a -a)}_{0} \cdots \underbrace{(+a -a)}_{0}}^{\text{n terms}} = 0
$$

We will just end up with each a bunch of zeros, that amount to nothing.

What if we want it to amount to something instead of nothing?

# Structure of a Summation

Lets examine the structure of a summation

When we do summation, we have the terms we want to sum

- This is if we want to sum the same terms
$$
\textcolor{lightgray}{\sum_{k=1}^{n}} +a
$$

And we have the starting point `k=1`, and ending point `k=n` of that term

$$
\sum_{k=1}^{n} \textcolor{lightgray}{+a}
$$

And we also have the `step` of the summation, which is how the start point progresses to the end, by increments of how much?

- The step used in summation is the unit step `1`

$$
1 \rightarrow 2 \rightarrow 3 \rightarrow \cdots  \rightarrow n
$$

# To Amount to Something

In order for a summation to amount to something instead of nothing, it must `contain terms that are eliminated`

But we have established that in its simplest form, this summation amounts to nothing

$$
\sum_{k=1}^n +a -a = 0
$$


#### Since all terms are generated from the same mold,

The only way to eliminate terms without dissolving the entire expression into `0`, is to have
- `Terms that are not eliminated`, and thus
- Terms that are `eliminated by their later counterparts`.

$$
\colorbox{lightgray}{The summation must already contain both `the term to be eliminated` and the `term that will eliminate previous terms`}
$$

Thus, $+a$ and $-a$ must be `related` in some way

$$
\textcolor{lightgray}{\sum_{k=1}^n} \boxed{+a} \longleftrightarrow \boxed{-a}
$$

---

How are they related?

- It might be hard to imagine what kinds of terms are not eliminated.
- But we can think about the `terms that are eliminated by their later counterparts`,

What does this mean?

It means the current term must be able to match its later counterpart within some steps.

## Relationship with Increments

- `Matching within some steps` means that it the `terms has to increment`

$$
\colorbox{lightgray}{Thus the `terms are related to the increments`}
$$

$$
\sum_{k=1}^n +k -k
$$

- `Matching its later counterpart` means its later counterpart must `already be represented in the summation`
- And thus related to the `current term` by some relation

What is the relation?

## Relationship between Terms

$$
\colorbox{lightgray}{The later counterpart must be `able to overcome with steps`}
$$

Which means it must be some multiple of the `steps`

Since
- `step` is `incremental` and in `integers`,
- The difference must be some `positive integer multiple` of the `step`

Thus
- Let step be `s`, and
- `m` be the  multiple of the step, such that $m \in \mathbf{Z^{+}}$
- Where the difference, `d`, is a `positive integer multiple of s`,
    - Such that `d = ms`

$$
\sum_{k=1}^n \underline{+k} \space -\underline{(k+ms)}, \quad \text{for} \space m \in \mathbf{Z^{+}}
$$

---

And for Summation purposes, the step is `1`
- Thus this simplifies

$$
\sum_{k=1}^n \underline{+k} \space - \underline{(k+m \cdot 1)}
$$

- To this

$$
\sum_{k=1}^n \underline{+k} \space - \underline{(k+m)}
$$

Which means, it is the same as, having the `difference between terms equal to the multiple of the step`,
- `d = m`

$$
\boxed{
    \sum_{k=1}^n \underline{+k} \space - \underline{(k+d)}, \quad \text{for} \space d \in \mathbf{Z^{+}}
}
$$

> Notice that because of a `common difference` that `d` is, the terms in this summation, are also part of an arithmetic series

# Analyse the Pattern

Lets expand it as such as spot for patterns

$$
\sum_{k=1}^n \underline{+k} \space - \underline{(k+d)}
$$

For `d = 3`,

$$
\begin{align}
    \sum_{k=1}^n \underline{+k} \space - \underline{(k+3)} &= 1 - \cancel{4} \\
    &= 2 - \cancel{5} \\
    &= 3 - \cancel{6} \\
    &= \cancel{4} - \cdots \\
    &= \cancel{5} - \cdots \\
    &= \cancel{6} - \cdots \\
    &  \vdots \\
    &= \cdots - \cancel{n-2} \\
    &= \cdots - \cancel{n-1} \\
    &= \cdots - \cancel{n} \\
    &= \cancel{n-2} - (n+1) \\
    &= \cancel{n-1} - (n+2) \\
    &= \cancel{n} - (n+3) \\
\end{align}
$$

Notice how the terms in the middle `start to cancel out` once the `increment catches up with the difference` between the terms?

The number of terms left is exactly
-  `d` amount of the first `smaller terms`
    > As they would not have enough increments to start cancelling out the bigger term

- And `d` amount of the last `bigger terms`
    > As they would have `just enough to not be cancelled out` by the `smaller terms catching up`

Thus

$$
\sum_{k=1}^n \underline{+k} \space - \underline{(k+d)} = \text{d amount of the first smaller terms} - \text{d amount of the last bigger terms}
$$

Which is

$$
\boxed{
    \sum_{k=1}^n \underline{+k} \space - \underline{(k+d)} = \sum_{k=1}^{d} k - \sum_{k=(n-d+1)}^n (k+d),  \quad \text{for} \space d \in \mathbf{Z^{+}}
}
$$

---

Notice that the part containing the last larger terms, can be simplified according to its relationship with the smaller terms

$$
\textcolor{lightgray}{\sum_{k=1}^n \underline{+k} \space - \underline{(k+d)} = \sum_{k=1}^{d} k \space - } \sum_{k=(n-d+1)}^n (k+d)
$$

- As they are always `d` bigger, they also equal to the summation of the smaller terms extended over `d` range

Which in summation presents as the addition of `d` shifting from the terms to the indices

$$
\textcolor{lightgray}{\sum_{k=1}^n \underline{+k} \space - \underline{(k+d)} = \sum_{k=1}^{d} k \space - } \sum_{k=(n-d+1)+d}^{n+d} k
$$

And thus

$$
\textcolor{lightgray}{\sum_{k=1}^n \underline{+k} \space - \underline{(k+d)} = \sum_{k=1}^{d} k \space - } \sum_{k=n+1}^{n+d} k
$$

Thus, we have the simplified formula of

$$
\boxed{
    \sum_{k=1}^n \underline{+k} \space - \underline{(k+d)} = \sum_{k=1}^{d} k \space - \sum_{k=n+1}^{n+d} k,  \quad \text{for} \space d \in \mathbf{Z^{+}}
}
$$

# The Simple Case

Notice that in the previous case, we set `d` to `3` to show how it cancels out

$$
\begin{align}
    \sum_{k=1}^n \underline{+k} \space - \underline{(k+3)} &= 1 - \cancel{4} \\
    &= 2 - \cancel{5} \\
    &= 3 - \cancel{6} \\
    &= \cancel{4} - \cdots \\
    &= \cancel{5} - \cdots \\
    &= \cancel{6} - \cdots \\
    &  \vdots \\
    &= \cdots - \cancel{n-2} \\
    &= \cdots - \cancel{n-1} \\
    &= \cdots - \cancel{n} \\
    &= \cancel{n-2} - (n+1) \\
    &= \cancel{n-1} - (n+2) \\
    &= \cancel{n} - (n+3) \\
\end{align}
$$

Notice that if we shrink `d` to `1`, this happens

$$
\begin{align}
    \sum_{k=1}^n \underline{+k} \space - \underline{(k+1)} &= 1 - \cancel{2} \\
    &= \cancel{2} - \cancel{3} \\
    &= \cancel{3} - \cancel{4} \\
    &= \cancel{4} - \cdots \\
    &  \vdots \\
    &= \cdots - \cancel{n-1} \\
    &= \cancel{n-1} - \cancel{n} \\
    &= \cancel{n} - (n+1) \\
\end{align}
$$

We are left with just the `first smaller term`, and the `last bigger term`
- This is because with a difference, `d`, of only `1`, the next iteration already caught up with the difference
- Which causes direct elimination on iteration right after the first

Thus, we can simplify this case where `d=1`, from the formula as well

- From the formula

$$
\sum_{k=1}^n \underline{+k} \space - \underline{(k+d)} = \sum_{k=1}^{d} k \space - \sum_{k=n+1}^{n+d} k
$$

- Let `d=1`

$$
\begin{align}
    \sum_{k=1}^n \underline{+k} \space - \underline{(k+\boxed{1})} &= \sum_{k=1}^{\boxed{1}} k \space - \sum_{k=n+1}^{n+\boxed{1}} k \\
    &= \underline{\text{1st term}} - \underline{\text{(n+1)-th term}} \\
    &= k_{1} - k_{n+1}
\end{align}
$$

And Thus, we can also see that we arrived at the same conclusion

$$
\boxed{
    \sum_{k=1}^n \underline{+k} \space - \underline{(k+1)} = k_{1} - k_{n+1}
}
$$

Of course the direct answer here is `-n`, but we are looking for patterns, not just direct answers

# For all Transformations

Thus, from the above, we concluded that as long as the `2 terms` are `related in difference` that is a `positive multiple of the step`, `(which is an incrementing positive integer)`, the step will be able to `catch up with the difference`

---

- Where `d = ms`

$$
\sum_{k=1}^n \underline{+k} \space - \underline{(k+d)}, \quad \text{for} \space d \in \mathbf{Z^{+}}
$$

- Causing `later terms cancel out previous terms`, which `simplifies the sum`

$$
\sum_{k=1}^n \underline{+k} \space - \underline{(k+d)} = \sum_{k=1}^{d} k \space - \sum_{k=n+1}^{n+d} k, \quad \text{for} \space d \in \mathbf{Z^{+}}
$$

- And with the special case

$$
\sum_{k=1}^n \underline{+k} \space - \underline{(k+1)} = k_{1} - k_{n+1}
$$

---

Since telescoping properties only depend on
- The `2 terms`, for which they have `operations inverse of each other`, that match the `repeated operator`
    - i.e. `For Summation: add/subtract, For Product: multiply/divide`
- The difference between those 2 terms is a `positive multiple` of the step

#### Any unique transformation of those 2 terms, as long as it is the same transformation, will be able to carry over these properties.

And what things transform uniquely?
> Functions!

Thus, with functions, we carry over the same properties of the `step catching up with the difference`

$$
\boxed{
    \text{Telescoping Sum} \space = \space \sum_{k=1}^n \underline{f(k)} - \underline{f(k+d)}, \quad \text{for} \space d \in \mathbf{Z^{+}}
}
$$

Which means, undergoing the same derivations, this works

$$
\boxed{
    \sum_{k=1}^n \underline{f(k)} - \underline{f(k+d)} = \sum_{k=1}^{d} f(k) \space - \sum_{k=n+1}^{n+d} f(k), \quad \text{for} \space d \in \mathbf{Z^{+}}
}
$$

- Note that the above works, whether or not `step = 1`

And the special case where `d=1`, works too

$$
\boxed{
    \sum_{k=1}^n \underline{f(k)} - \underline{f(k+1)} = f(1) - f(n+1)
}
$$

> Those are thus the General Form of Telescoping Sums

# Telescoping Products from Telescoping Sums

With this knowledge we can also expand it to Telescoping Products.


> Since telescoping properties only depend on
> - The `2 terms`, for which they have `operations inverse of each other`, that match the `repeated operator`
    - i.e. `For Summation: add/subtract, For Product: multiply/divide`
> - The difference between those 2 terms is a `positive multiple` of the step

Then we have
- Where `d = ms`


$$
\prod_{k=1}^n \dfrac{k}{k+d}, \quad \text{for} \space d \in \mathbf{Z^{+}}
$$

Thus, with the same logic, for lets say `d = 2`

$$
\prod_{k=1}^n \dfrac{k}{k+d} = \dfrac{1}{\cancel{3}} \cdot \dfrac{2}{\cancel{4}} \cdot \dfrac{\cancel{3}}{\cdots} \cdot \dfrac{\cancel{4}}{\cdots} \cdots \dfrac{\cdots}{\cancel{n-1}} \dfrac{\cdots}{\cancel{n}} \cdot \dfrac{\cancel{n-1}}{n+1} \cdot \dfrac{\cancel{n}}{n+2}
$$

We can arrive at the general formula

$$
\prod_{k=1}^n \dfrac{k}{k+d} = \dfrac{\prod_{k=1}^{d} k}{\prod_{k=n+1}^{n+d} k}, \quad \text{for} \space d \in \mathbf{Z^{+}}
$$

And its special case

$$
\prod_{k=1}^n \dfrac{k}{k+1} = \dfrac{1}{n+1}
$$

For which, any unique transformation of that property, will retain the properties of telescoping.


$$
\boxed{
    \text{Telescoping Product} \space = \space \prod_{k=1}^n \dfrac{f(k)}{f(k+d)}, \quad \text{for} \space d \in \mathbf{Z^{+}}
}
$$

Such that

$$
\boxed{
    \prod_{k=1}^n \dfrac{f(k)}{f(k+d)} = \dfrac{\prod_{k=1}^{d} f(k)}{\prod_{k=n+1}^{n+d} f(k)}, \quad \text{for} \space d \in \mathbf{Z^{+}}
}
$$

And its special case

$$
\boxed{
    \prod_{k=1}^n \dfrac{f(k)}{f(k+1)} = \dfrac{f(1)}{f(n+1)}
}
$$

# Conclusion

Thus! Since, any expression in repeated operator such that
- The input of the `2 terms` are related by a `positive multiple` of the step of the repeated operator i.e. `Summation/Product`
- And their `inverse operations` are exactly `the same as` that of the repeated operator

You can get a definite simplified answer by expressing some expressions in these forms

---

- Where `d = ms`

### Telescoping Sum
$$
\boxed{
    \sum_{k=1}^n \underline{f(k)} - \underline{f(k+d)} = \sum_{k=1}^{d} f(k) \space - \sum_{k=n+1}^{n+d} f(k), \quad \text{for} \space d \in \mathbf{Z^{+}}
}
$$

### Telescoping Product
$$
\boxed{
    \prod_{k=1}^n \dfrac{f(k)}{f(k+d)} = \dfrac{\prod_{k=1}^{d} f(k)}{\prod_{k=n+1}^{n+d} f(k)}, \quad \text{for} \space d \in \mathbf{Z^{+}}
}
$$

# Table of Reference

---

# Sums

$$
\begin{array}{c|c|c}
\hline
\quad \textbf{Step Difference } (d) & \textbf{Surviving Terms} & \textbf{Simplified Result} \\
\hline
1 & f(1), f(n+1) & f(1) - f(n+1) \\
2 & f(1), f(2), f(n+1), f(n+2) & f(1) + f(2) - f(n+1) - f(n+2) \\
3 & f(1), f(2), f(3), f(n+1), f(n+2), f(n+3) & f(1) + f(2) + f(3) - f(n+1) - f(n+2) - f(n+3) \\
\vdots & \vdots & \vdots \\
d & \sum_{k=1}^{d} f(k), \sum_{k=n+1}^{n+d} f(k) & \sum_{k=1}^{d} f(k) - \sum_{k=n+1}^{n+d} f(k) \\
\hline
\end{array}
$$


# Products

$$
\begin{array}{c|c|c}
\hline
\quad \textbf{Step Difference } (d) & \textbf{Surviving Terms} & \textbf{Simplified Result} \\
\hline
1 & f(1), f(n+1) & \displaystyle \frac{f(1)}{f(n+1)} \\
2 & f(1), f(2), f(n+1), f(n+2) & \displaystyle \frac{f(1) \cdot f(2)}{f(n+1) \cdot f(n+2)} \\
3 & f(1), f(2), f(3), f(n+1), f(n+2), f(n+3) & \displaystyle \frac{f(1) \cdot f(2) \cdot f(3)}{f(n+1) \cdot f(n+2) \cdot f(n+3)} \\
\vdots & \vdots & \vdots \\
d & \prod_{k=1}^{d} f(k), \prod_{k=n+1}^{n+d} f(k) & \displaystyle \frac{\prod_{k=1}^{d} f(k)}{\prod_{k=n+1}^{n+d} f(k)} \\
\hline
\end{array}
$$
