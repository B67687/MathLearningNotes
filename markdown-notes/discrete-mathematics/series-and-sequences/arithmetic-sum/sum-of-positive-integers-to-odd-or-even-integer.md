---
title: "What is the Sum of Natural Numbers Up To That Odd or Even Number?"
source_notebook: "discrete-mathematics/series-and-sequences/arithmetic-sum/sum-of-positive-integers-to-odd-or-even-integer.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# What is the Sum of Natural Numbers Up To That Odd or Even Number?

We all know of then formula for the sum of the natural numbers

$$
1 + 2 + \cdots + (n-1) + n
$$

Is this

$$
\dfrac{n(n+1)}{2}
$$

---

But what is the sum of the natural numbers up to an `odd number` or `even number`?

---

We know that, where `n` is the `n-th term` in the series of odd/even numbers,

- Odd numbers can be expressed in an `odd-length symmetric sum` such that

$$
1 + 2 + \cdots + n + \cdots + 2 + 1
$$

- Even numbers can be expressed in an `even-length symmetric sum` such that

$$
1 + 2 + \cdots + n + n + \cdots + 2 + 1
$$

The only difference between these 2 `symmetric sums` is just that even sums will have one more term `n`, because of `even-length` symmetry

# Adding Up to the N-th Odd Number

Contructing the sum of natural numbers up to the the `n-th` odd numbers, we see this

$$
1 + 2 + 3 + 4 + 5 + \cdots + \underline{\text{n-th odd number}}
$$

It can be deconstructed into a `series of even numbers` and another `series of odd numbers`

$$
\begin{array}
    & +1 & & +3 & & +5 & \cdots & + \underline{\text{(n-1)-th odd number}} && + \underline{\text{n-th odd number}} \\
    & +2 & & +4 & & +6 & \cdots & + \underline{\text{(n-1)-th even number}} \\
\end{array}
$$

Which when viewed in symmetric sums is this

$$
\begin{array}
    & \quad \space \space 1 + 2 + \cdots + (n-1) + n + (n-1) + \cdots + 2 + 1 \\
    \space + 1 + 2 + \cdots + (n-1) \qquad +
    (n-1) + \cdots + 2 + 1 \\
\end{array}
$$

Now we simply add it together

$$
\begin{align}
    & \text{Arithmetic Sum up to the n-th odd number} \\
    &= 2 \biggr( 1 + 2 + \cdots + (n-1) \biggr) + n + 2 \biggr( (n-1) + \cdots 2 + 1 \biggr) \\
\end{align}
$$

Expand and Simplify

$$
4 \biggr( 1 + 2 + \cdots + (n-1) \biggr) + n
$$

Combine the 2 `equal sums`

$$
4 \biggr( \dfrac{n(n-1)}{2} \biggr) + n
$$

Simpify

$$
\begin{align}
    & 2n(n-1) + n \\
    \\
    &= 2n^{2} -2n + n \\
    \\
    &= 2n^{2} - n \\
    \\
    &= n (2n - 1)
\end{align}
$$

Thus,

$$
\boxed{
    \begin{align}
        & \text{Arithmetic Sum up to the n-th odd number} \\
        &= n (2n - 1)
    \end{align}
}
$$

# Adding Up to the N-th Even Number

Contructing the sum of natural numbers up to the the `n-th` even numbers

$$
1 + 2 + 3 + 4 + 5 + \cdots + \underline{\text{n-th even number}}
$$

It can be deconstructed into a `series of even numbers` and another `series of odd numbers`

$$
\begin{array}
    & +1 & & +3 & & +5 & \cdots & \underline{\text{(n-1)-th odd number}} &  & + \underline{\text{n-th odd number}} \\
    & +2 & & +4 & & +6 & \cdots & + \underline{\text{(n-1)-th even number}} && + \underline{\text{n-th even number}} \\
\end{array}
$$

Which when viewed in symmetric sums is this

$$
\begin{array}
    & \quad \space \space 1 + 2 + \cdots + (n-1) + n + n + (n-1) + \cdots + 2 + 1 \\
    + \space\space 1 + 2 + \cdots + (n-1) \quad  + n \quad
    + (n-1) + \cdots + 2 + 1 \\
\end{array}
$$

Now we simply add it together

$$
\begin{align}
    & \text{Arithmetic Sum up to the n-th odd number} \\
    &= 2 \biggr( 1 + 2 + \cdots + (n-1) \biggr) + 3n + 2 \biggr( (n-1) + \cdots 2 + 1 \biggr) \\
\end{align}
$$

Expand and Simplify

$$
4 \biggr( 1 + 2 + \cdots + (n-1) \biggr) + 3n
$$

Combine the 2 `equal sums`

$$
4 \biggr( \dfrac{n(n-1)}{2} \biggr) + 3n
$$

Simpify

$$
\begin{align}
    & 2n(n-1) + 3n \\
    \\
    &= 2n^{2} -2n + 3n \\
    \\
    &= 2n^{2} + n \\
    \\
    &= n (2n + 1)
\end{align}
$$

Thus,

$$
\boxed{
    \begin{align}
        & \text{Arithmetic Sum up to the n-th even number} \\
        &= n (2n + 1)
    \end{align}
}
$$

# Conclusion

---

Thus, for Sums of Natural Numbers:

##### Up to the `n-th odd number`

$$
\boxed{
    \begin{align}
        & \text{Arithmetic Sum up to the n-th odd number} \\
        &= n (2n - 1)
    \end{align}
}
$$

##### Up to `n-th even number`

$$
\boxed{
    \begin{align}
        & \text{Arithmetic Sum up to the n-th even number} \\
        &= n (2n + 1)
    \end{align}
}
$$
