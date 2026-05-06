---
title: "Odd-Length Symmetric Sum of Cubes"
source_notebook: "discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-cubes.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-cubes.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Odd-Length Symmetric Sum of Cubes

$$
1^{3}  + 2^{3}  + 3^{3}  + \cdots  + (n-2)^{3} + (n-1)^{3} + n^{3} + (n-1)^{3} + (n-2)^{3} + \cdots + 3^{3} + 2^{3} + 1^{3}
$$

We realise that if we split it here

$$
\underline{1^{3}  + 2^{3}  + 3^{3}  + \cdots  + (n-2)^{3} + (n-1)^{3}}  \quad \mathbb{|} \space\space + n^{3}  \quad \mathbb{|} \space\space \underline{+ (n-1)^{3} + (n-2)^{3} + \cdots + 3^{3} + 2^{3} + 1^{3}}
$$

It can be re-expressed like this

$$
n^3 + 2 \space \biggl( 1^{3}  + 2^{3}  + 3^{3}  + \cdots  + (n-2)^{3} + (n-1)^{3} \biggr)
$$

Substitute the equation for the `sum of cubes` from `1` to `n-1`

$$
n^3 + 2 \space \biggl( \dfrac{\boxed{n-1}(\boxed{n-1}+1)}{2} \biggr)^{2}
$$

Which through much simplification

$$
\begin{align}
    n^3 + 2 \biggl( \dfrac{n(n-1)}{2} \biggr) ^ {2} &= n^3 + 2 \cdot \dfrac{n^{2}(n-1)^{2}}{4} \\
    &= \dfrac{2n^3}{2} + \dfrac{n^{2}(n-1)^{2}}{2} \\
    &= \dfrac{n^2}{2} \biggr( 2n + (n-1)^2 \biggr) \\
    &= \dfrac{n^2}{2} \biggr( 2n + \underline{n^2 - 2n + 1} \biggr) \\
    &= \dfrac{n^2}{2} \biggr( n^2 + 1 \biggr) \\
    &= \dfrac{n^{2} (n^{2} + 1)}{2} \\
\end{align}
$$

Thus

$$
\boxed{
   1^{3}  + 2^{3}  + 3^{3}  + \cdots  + (n-2)^{3} + (n-1)^{3} + n^{3} + (n-1)^{3} + (n-2)^{3} + \cdots + 3^{3} + 2^{3} + 1^{3} = \dfrac{n^{2} (n^{2} + 1)}{2}
}
$$

# Even-Length Symmetric Sum of Cubes

$$
1^{3}  + 2^{3}  + 3^{3}  + \cdots  + (n-2)^{3} + (n-1)^{3} + n^{3} + (n-1)^{3} + (n-2)^{3} + \cdots + 3^{3} + 2^{3} + 1^{3}
$$

We realise that if we split it here

$$
\underline{1^{2}  + 2^{2}  + 3^{2}  + \cdots  + (n-2)^{2} + (n-1)^{2} + n^{2}} \quad \mathbb{|} \quad \underline{n^{2} + (n-1)^{2} + (n-2)^{2} + \cdots + 3^{2} + 2^{2} + 1^{2}}
$$


It can be re-expressed like this

$$
2 \space \biggl( \dfrac{n(n+1)}{2} \biggr) ^ {2}
$$

Simplify

$$
2 \cdot \dfrac{n^{2} (n+1)^{2}}{4}
$$

To get this

$$
\dfrac{n^{2} (n+1)^{2}}{2}
$$

Thus,

$$
\boxed{
    1^{2}  + 2^{2}  + 3^{2}  + \cdots  + (n-2)^{2} + (n-1)^{2} + n^{2} + n^{2} + (n-1)^{2} + (n-2)^{2} + \cdots + 3^{2} + 2^{2} + 1^{2} = \dfrac{n^{2} (n+1)^{2}}{2}
}
$$
