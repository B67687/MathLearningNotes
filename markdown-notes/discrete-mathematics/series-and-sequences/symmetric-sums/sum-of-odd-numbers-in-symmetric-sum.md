---
title: "Chain of Dots and Odd Numbers"
source_notebook: "discrete-mathematics/series-and-sequences/symmetric-sums/sum-of-odd-numbers-in-symmetric-sum.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Chain of Dots and Odd Numbers

Consider a starting point

$$
\bullet
$$

If we extend it from both sides

$$
\textcolor{lightgray}{\bullet} \quad \bullet \quad \textcolor{lightgray}{\bullet}
$$

We get

$$
\bullet \quad \bullet \quad \bullet
$$

We can keep extending both sides at once to get bigger and bigger sets

$$
\textcolor{lightgray}{\cdots} \quad \textcolor{lightgray}{\bullet} \quad \textcolor{lightgray}{\bullet} \quad \textcolor{lightgray}{\bullet} \quad \bullet \quad \bullet \quad \bullet \quad \textcolor{lightgray}{\bullet} \quad \textcolor{lightgray}{\bullet} \quad \textcolor{lightgray}{\bullet} \quad \textcolor{lightgray}{\cdots}
$$

Since this set of dots started from one dot

$$
\bullet
$$

It starts off as an `odd` number

$$
1
$$

And extends by `2` everytime

$$
\textcolor{lightgray}{1} \textcolor{lightgray}{+} 1 \textcolor{lightgray}{+} \textcolor{lightgray}{1}
$$

`1` from both sides

$$
\textcolor{lightgray}{1} \textcolor{lightgray}{+} 1 + 1 + 1 \textcolor{lightgray}{+} \textcolor{lightgray}{1}
$$

It continues to be odd all the way down the chain

$$
\textcolor{lightgray}{\cdots} \quad \textcolor{lightgray}{1} \textcolor{lightgray}{+} 1 + 1 + 1 + 1 + 1 \textcolor{lightgray}{+} \textcolor{lightgray}{1} \quad  \textcolor{lightgray}{\cdots}
$$

# Stack of Dots and Sum of Odd Numbers

Thus since we know now that this chain contains odd numbers,

To find the sum of odd numbers, we can stack it like so

- First Stack

$$
\begin{array}{c}
    \bullet \\
\end{array}
$$

- Second Stack

$$
\begin{array}{c}
    \bullet \\
    \bullet \quad \bullet \quad \bullet \\
\end{array}
$$

- Third Stack

$$
\begin{array}{c}
    \bullet \\
    \bullet \quad \bullet \quad \bullet \\
    \bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet \\
\end{array}
$$

- So on and so forth

$$
\begin{array}{c}
    \bullet \\
    \bullet \quad \bullet \quad \bullet \\
    \bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet \\
    \textcolor{lightgray}{\bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet} \\
    \textcolor{lightgray}{\vdots}
\end{array}
$$

## Observe the Columns

Notice how the columns of these stacks change

- First Stack

$$
\begin{array}{c}
    \bullet \\
\end{array}
$$

- Second Stack

$$
\begin{array}{c|c|c}
    & \bullet & \\
    \bullet & \bullet & \bullet \\
\end{array}
$$

- Third Stack

$$
\begin{array}{c|c|c|c|c}
    & & \bullet & & \\
    & \bullet & \bullet & \bullet & \\
    \bullet & \bullet & \bullet & \bullet & \bullet
\end{array}
$$

Every new stack
- `Introduces 1 more dot into every pre-existing column`, and
- `Introduces a column on its left and right for its new dots on its left and right`

## Convert to Numbers

It is equivalent to these sums

- First Stack

$$
\textcolor{lightgray}
{
    \begin{array}{c}
    \bullet \\
    \end{array}
}
$$

$$
1
$$

- Second Stack

$$
\textcolor{lightgray}
{
    \begin{array}{c|c|c}
    & \bullet & \\
    \bullet & \bullet & \bullet \\
    \end{array}
}
$$

$$
1 + 2 + 1
$$

- Third Stack

$$
\textcolor{lightgray}
{
    \begin{array}{c|c|c|c|c}
    & & \bullet & & \\
    & \bullet & \bullet & \bullet & \\
    \bullet & \bullet & \bullet & \bullet & \bullet
    \end{array}
}
$$

$$
1 + 2 + 3 + 2 + 1
$$

Following this pattern

$$
\begin{array}{c}
    & & & 1 & & & \\
    & & \downarrow +1 & \downarrow +1 & \downarrow +1 & & \\
    & & 1 & 2 & 1 & & \\
    & \downarrow +1 & \downarrow +1 & \downarrow +1 & \downarrow +1 & \downarrow +1 \\
    & 1 & 2 & 3 & 2 & 1 & \\
    \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} & \textcolor{lightgray}{\downarrow +1} \\
    & & & \textcolor{lightgray}{\vdots} & & &
\end{array}
$$

## Symmetric Sums

We get this symmetric series for the sum of odd numbers
- Such that `n` is the iteration of odd number

$$
\begin{array}
    & 1 & 2 & 3 & \cdots & (n-2) & (n-1) & n & (n-1) & (n-2) & \cdots & 3 & 2 & 1
\end{array}
$$

Or more specifically

$$
\sum_{k=1}^{n} \underline{2k - 1} =  1  + 2  + 3  + \cdots  + (n-2)  + (n-1)  + n  + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1
$$

---

Thus

$$
\boxed{\text{The sum of odd numbers, 2k-1, from 1 to n, equals to an odd-length symmetric sum from 1 to n}}
$$

$$
\boxed{
    \sum_{k=1}^{n} \underline{2k - 1} =  1  + 2  + 3  + \cdots  + (n-2)  + (n-1)  + n  + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1
}
$$

> **Fun Fact**: The number of terms in this symmetric sum follows the last row, and since any row has odd number of terms, there are odd number of terms in this symmetric sum

# Sum of Odd Numbers is a Square

We can also attempt to simplify this equation

$$
\sum_{k=1}^{n} \underline{2k - 1} =  1  + 2  + 3  + \cdots  + (n-2)  + (n-1)  + n  + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1
$$

Focusing on this part

$$
1  + 2  + 3  + \cdots  + (n-2)  + (n-1)  + n  + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1
$$

We realise that if we split it here

$$
\underline{1  + 2  + 3  + \cdots  + (n-2)  + (n-1)}  \quad \mathbb{|} \space\space + n  \quad \mathbb{|} \space\space \underline{+ (n-1)  + (n-2)  + \cdots  + 3 + 2 + 1}
$$


It can be re-expressed like this

$$
n + 2 \space \biggl( 1  + 2  + 3  + \cdots  + (n-2)  + (n-1) \biggr)
$$

Substitute the equation for the arithmetic sum from `1` to `n-1`

$$
n + 2 \space \biggl( \dfrac{n-1}{2} \cdot \big( 1 + \underline{n-1} \big) \biggr)
$$

We get

$$
n + 2 \space \cdot \dfrac{n(n-1)}{2}
$$

The `2` cancels out

$$
n + n(n-1)
$$

Expand

$$
n + (n^{2} - n)
$$

The `n` cancels out to get

$$
n^{2}
$$

Thus, we have also proven that `the sum of odd numbers is also a square` through this way

$$
\begin{align}
    \sum_{k=1}^{n} \underline{2k - 1} &=  1  + 2  + 3  + \cdots  + (n-2)  + (n-1)  + n  + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1 \\
    &= n^{2}
\end{align}
$$


> We can also prove this using summation notation

# Conclusion

Thus,

$$
\text{The sum of odd numbers 2k-1 from 1 to n}, \boxed{\text{equals to an odd-length symmetric sum from 1 to n}}, \boxed{\text{which also equals to} \space n^{2}}
$$

$$
\boxed{
    \sum_{k=1}^{n} \underline{2k - 1} =  \underline{n^{2}} = \underline{1  + 2  + 3  + \cdots  + (n-2)  + (n-1)  + n  + (n-1)  + (n-2)  + \cdots  + 3  + 2 + 1}
}
$$
