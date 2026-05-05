---
title: "Chain of Dots and Even Numbers"
source_notebook: "discrete-mathematics/series-and-sequences/symmetric-sums/sum-of-even-numbers-in-symmetric-sum.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Chain of Dots and Even Numbers

Consider a starting point of nothing

$$
\_
$$

If we extend it from both sides

$$
\textcolor{lightgray}{\bullet} \quad \_ \quad \textcolor{lightgray}{\bullet}
$$

We get

$$
\bullet \quad \_ \quad \bullet
$$

We can keep extending both sides at once to get bigger and bigger sets

$$
\textcolor{lightgray}{\cdots} \quad \textcolor{lightgray}{\bullet} \quad \textcolor{lightgray}{\bullet} \quad \textcolor{lightgray}{\bullet} \quad \bullet \quad \_ \quad \bullet \quad \textcolor{lightgray}{\bullet} \quad \textcolor{lightgray}{\bullet} \quad \textcolor{lightgray}{\bullet} \quad \textcolor{lightgray}{\cdots}
$$

Since this set of dots started from nothing

$$
\_
$$

It starts off as an `even` number

$$
0
$$

And extends by `2` everytime

$$
\textcolor{lightgray}{1} \textcolor{lightgray}{+} 0 \textcolor{lightgray}{+} \textcolor{lightgray}{1}
$$

`1` from both sides

$$
\textcolor{lightgray}{1} \textcolor{lightgray}{+} 1 + 0 + 1 \textcolor{lightgray}{+} \textcolor{lightgray}{1}
$$

It continues to be even all the way down the chain

$$
\textcolor{lightgray}{\cdots} \quad \textcolor{lightgray}{1} \textcolor{lightgray}{+} 1 + 1 + 0 + 1 + 1 \textcolor{lightgray}{+} \textcolor{lightgray}{1} \quad  \textcolor{lightgray}{\cdots}
$$

# Stack of Dots and Sum of Even Numbers

Thus since we know now that this chain contains even numbers,

To find the sum of even numbers, we can stack it like so

- Zero-th Stack

$$
\_
$$

- First Stack

$$
\begin{array}{c}
    \bullet & \_ & \bullet \\
\end{array}
$$

- Second Stack

$$
\begin{array}{c}
    & \bullet & \_ & \bullet & \\
    \bullet & \bullet & \_ & \bullet & \bullet \\
\end{array}
$$

- Third Stack

$$
\begin{array}{c}
    & & \bullet & \_ & \bullet & & \\
    & \bullet & \bullet & \_ & \bullet & \bullet & \\
    \bullet & \bullet & \bullet & \_ & \bullet & \bullet & \bullet \\
\end{array}
$$

- So on and so forth

$$
\begin{array}{c}
    & & & \bullet & \_ & \bullet & & & \\
    & & \bullet & \bullet & \_ & \bullet & \bullet & & \\
    & \bullet & \bullet & \bullet & \_ & \bullet & \bullet & \bullet & \\
    \textcolor{lightgray}{\bullet} & \textcolor{lightgray}{\bullet} & \textcolor{lightgray}{\bullet} & \textcolor{lightgray}{\bullet} & \textcolor{lightgray}{\_} & \textcolor{lightgray}{\bullet} & \textcolor{lightgray}{\bullet} & \textcolor{lightgray}{\bullet} & \textcolor{lightgray}{\bullet} \\
    & & & & \textcolor{lightgray}{\vdots} & & & &
\end{array}
$$

## Observe the Columns

Notice how the columns of these stacks change

- Zero-th Stack

$$
\begin{array}{c}
    \_ \\
\end{array}
$$

- First Stack

$$
\begin{array}{c|c|c}
    \bullet & \_ & \bullet \\
\end{array}
$$

- Second Stack

$$
\begin{array}{c|c|c|c}
    & \bullet & \_ & \bullet & \\
    \bullet & \bullet & \_ & \bullet & \bullet \\
\end{array}
$$

- Third Stack

$$
\begin{array}{c|c|c|c|c|c}
    & & \bullet & \_ & \bullet & & \\
    & \bullet & \bullet & \_ & \bullet & \bullet & \\
    \bullet & \bullet & \bullet & \_ & \bullet & \bullet & \bullet \\
\end{array}
$$

Every new stack
- `Introduces 1 more dot into every pre-existing column that already has dots`, and
- `Introduces a column on its left and right for its new dots on its left and right`

## Convert to Numbers

It is equivalent to these sums

- Zero-th Stack

$$
\textcolor{lightgray}
{
    \begin{array}{c}
        \_ \\
    \end{array}
}
$$

- First Stack

$$
\textcolor{lightgray}
{
    \begin{array}{c|c|c}
        \bullet & \_ & \bullet \\
    \end{array}
}
$$

$$
1 + 0 + 1
$$

- Second Stack

$$
\textcolor{lightgray}
{
    \begin{array}{c|c|c|c|c}
        & \bullet & \_ & \bullet & \\
        \bullet & \bullet & \_ & \bullet & \bullet \\
    \end{array}
}
$$

$$
1 + 2 + 0 + 2 + 1
$$

- Third Stack

$$
\textcolor{lightgray}
{
    \begin{array}{c|c|c|c|c|c}
        & & \bullet & \_ & \bullet & & \\
        & \bullet & \bullet & \_ & \bullet & \bullet & \\
        \bullet & \bullet & \bullet & \_ & \bullet & \bullet & \bullet \\
    \end{array}
}
$$

$$
1 + 2 + 3 + 0 + 3 + 2 + 1
$$

Following this pattern

$$
\begin{array}{c}
    & & & 1 & 0 & 1 & & & \\
    & & \downarrow +1 & \downarrow +1 & \downarrow & \downarrow +1 & \downarrow +1 & & \\
    & & 1 & 2 & 0 & 2 & 1 & & \\
    & \downarrow +1 & \downarrow +1 & \downarrow +1 & \downarrow & \downarrow +1 & \downarrow +1 & \downarrow +1 & \\
    & 1 & 2 & 3 & 0 & 3 & 2 & 1 & \\
    \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} \\
    & & & & \textcolor{lightgray}{\vdots} & & & &
\end{array}
$$

## Symmetric Sums

We get this symmetric series for the sum of even numbers
- Such that `n` is the iteration of even number

$$
\begin{array}
    & 1 & 2 & 3 & \cdots & (n-2) & (n-1) & n & 0 & n & (n-1) & (n-2) & \cdots & 3 & 2 & 1
\end{array}
$$

And now we can simplify as simply

$$
\begin{array}
    & 1 & 2 & 3 & \cdots & (n-2) & (n-1) & n & n & (n-1) & (n-2) & \cdots & 3 & 2 & 1
\end{array}
$$

Or more specifically

$$
\sum_{k=1}^{n} \underline{2k} =  1  + 2  + 3  + \cdots  + (n-2)  + (n-1) + n + n + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1
$$

---

Thus

$$
\boxed{\text{The sum of even numbers, 2k, from 1 to n, equals to an even-length symmetric sum from 1 to n}}
$$

$$
\boxed{
    \sum_{k=1}^{n} \underline{2k} =  1  + 2  + 3  + \cdots  + (n-2)  + (n-1)  + n + n  + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1
}
$$

> **Fun Fact**: The number of terms in this symmetric sum follows the last row, and since any row has even number of terms, there are even number of terms in this symmetric sum

# Sum of Even Numbers is a Consecutive Multiple

We can also attempt to simplify this equation

$$
\sum_{k=1}^{n} \underline{2k} =  1  + 2  + 3  + \cdots  + (n-2)  + (n-1)  + n + n  + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1
$$

Focusing on this part

$$
1  + 2  + 3  + \cdots  + (n-2)  + (n-1)  + n + n  + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1
$$

We realise that if we split it here

$$
\underline{1  + 2  + 3  + \cdots  + (n-2)  + (n-1) + n}  \quad \mathbb{|} \quad \underline{n + (n-1)  + (n-2)  + \cdots  + 3 + 2 + 1}
$$


It can be re-expressed like this

$$
2 \space \biggl( 1  + 2  + 3  + \cdots  + (n-2)  + (n-1) + n \biggr)
$$

Substitute the equation for the arithmetic sum from `1` to `n-1`

$$
2 \space \biggl( \dfrac{n(n+1)}{2} \biggr)
$$

The `2` cancels out

$$
\cancel{2} \space \biggl( \dfrac{n(n+1)}{\cancel{2}} \biggr)
$$

To get

$$
n(n+1)
$$

Thus, we have also proven that `the sum of even numbers is a consecutive multiple` through this way

$$
\begin{align}
    \sum_{k=1}^{n} \underline{2k} &=  1  + 2  + 3  + \cdots  + (n-2)  + (n-1)  + n + n + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1 \\
    &= n(n+1)
\end{align}
$$


> We can also prove this using summation notation

# Conclusion

Thus,

$$
\text{The sum of even numbers 2k from 1 to n}, \boxed{\text{equals to an even-length symmetric sum from 1 to n}}, \boxed{\text{which also equals to} \space n(n+1)}
$$

$$
\boxed{
    \sum_{k=1}^{n} \underline{2k} =  \underline{n(n+1)} = \underline{1  + 2  + 3  + \cdots + (n-1)  + n + n + (n-1)  + \cdots  + 3  + 2 + 1}
}
$$
