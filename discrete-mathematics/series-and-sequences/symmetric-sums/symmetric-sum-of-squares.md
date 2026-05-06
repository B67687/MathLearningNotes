---
title: "Odd-Length Symmetric Sum of Squares"
source_notebook: "discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-squares.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-squares.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Odd-Length Symmetric Sum of Squares

$$
1^{2}  + 2^{2}  + 3^{2}  + \cdots  + (n-2)^{2} + (n-1)^{2} + n^{2} + (n-1)^{2} + (n-2)^{2} + \cdots + 3^{2} + 2^{2} + 1^{2}
$$

We realise that if we split it here

$$
\underline{1^{2}  + 2^{2}  + 3^{2}  + \cdots  + (n-2)^{2} + (n-1)^{2}}  \quad \mathbb{|} \space\space + n^{2}  \quad \mathbb{|} \space\space \underline{+ (n-1)^{2} + (n-2)^{2} + \cdots + 3^{2} + 2^{2} + 1^{2}}
$$


It can be re-expressed like this

$$
n^2 + 2 \space \biggl( 1^{2}  + 2^{2}  + 3^{2}  + \cdots  + (n-2)^{2} + (n-1)^{2} \biggr)
$$

Substitute the equation for the `sum of squares` from `1` to `n-1`

$$
n^2 + 2 \space \biggl( \dfrac{\boxed{n-1}(\boxed{n-1}+1)(2\boxed{n-1}+1)}{6} \biggr)
$$

Which through much simplification

$$
\begin{align}
    n^2 + \dfrac{(n-1)n(2n-2+1)}{3} &= \dfrac{3n^2}{3} + \dfrac{n(n-1)(2n-1)}{3} \\
    &= \dfrac{n}{3} \biggr( 3n + (n-1)(2n-1) \biggr) \\
    &= \dfrac{n}{3} (3n + 2n^{2} - n - 2n + 1) \\
    &= \dfrac{n(2n^{2} + 1)}{3}
\end{align}
$$

Thus

$$
\boxed{
    1^{2}  + 2^{2}  + 3^{2}  + \cdots  + (n-2)^{2} + (n-1)^{2} + n^{2} + (n-1)^{2} + (n-2)^{2} + \cdots + 3^{2} + 2^{2} + 1^{2} = \dfrac{n(2n^{2} + 1)}{3}
}
$$

# Even-Length Symmetric Sum of Squares

$$
1^{2}  + 2^{2}  + 3^{2}  + \cdots  + (n-2)^{2} + (n-1)^{2} + n^{2} + n^{2} + (n-1)^{2} + (n-2)^{2} + \cdots + 3^{2} + 2^{2} + 1^{2}
$$

We realise that if we split it here

$$
\underline{1^{2}  + 2^{2}  + 3^{2}  + \cdots  + (n-2)^{2} + (n-1)^{2} + n^{2}}  \quad \mathbb{|} \quad \underline{n^{2} + (n-1)^{2} + (n-2)^{2} + \cdots + 3^{2} + 2^{2} + 1^{2}}
$$


It can be re-expressed like this

$$
2 \space \biggl( \dfrac{n(n+1)(2n+1)}{6} \biggr)
$$

Which is this

$$
\dfrac{n(n+1)(2n+1)}{3}
$$

Thus,

$$
\boxed{
    1^{2}  + 2^{2}  + 3^{2}  + \cdots  + (n-2)^{2} + (n-1)^{2} + n^{2} + n^{2} + (n-1)^{2} + (n-2)^{2} + \cdots + 3^{2} + 2^{2} + 1^{2} = \dfrac{n(n+1)(2n+1)}{3}
}
$$
