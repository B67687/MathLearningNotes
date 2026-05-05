---
title: "Odd-Length Symmetric Sum of Even Numbers"
source_notebook: "discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-even-numbers.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Odd-Length Symmetric Sum of Even Numbers

$$
2 + 4 + \cdots  \boxed{2n - 2} + \boxed{2n} + \boxed{2n - 2} \cdots + 4 + 2
$$

Realise it is equal to

$$
2 \Biggr( 1 + 2 + \cdots  \boxed{n - 1} + \boxed{n} + \boxed{n - 1} \cdots + 2 + 1 \Biggr)
$$

---

## From the `sum-of-odd-numbers-in-symmetric-sum` notebook

We have realised this is equal to the `sum of odd numbers`

$$
\textcolor{lightgray}{2} \sum_{k=1}^n \underline{2k-1}
$$

Which is also equal to the `square at that point`

$$
\textcolor{lightgray}{2} n^{2}
$$

---

Thus

$$
\boxed{
    \phantom{\Biggr(} 2 + 4 + \cdots  \boxed{2n - 2} + \boxed{2n} + \boxed{2n - 2} \cdots + 4 + 2 = 2n^2 \phantom{\Biggr)}
}
$$

# Identity

Realise that the `odd-length symmetric sum of even numbers` is equal to the `even-length symmetric sum of odd numbers`

$$
\boxed{
    \phantom{\biggr(} \underline{2 + 4 + \cdots  \boxed{2n - 2} + \boxed{2n} + \boxed{2n - 2} \cdots + 4 + 2} \phantom{\biggr)} = \underline{2n^2} = \phantom{\biggr(} \underline{1 + 3 + \cdots  \boxed{2n - 3} + \boxed{2n-1} + \boxed{2n-1} + \boxed{2n - 3} \cdots + 3 + 1} \phantom{\biggr)}
}
$$

# Even-Length Symmetric Sum of Even Numbers

$$
2 + 4 + \cdots  \boxed{2n - 2} + \boxed{2n}  + \boxed{2n} + \boxed{2n - 2} \cdots + 4 + 2
$$

Realise it is equal to

$$
2 \Biggr( 1 + 2 + \cdots  \boxed{n - 1} + \boxed{n} + \boxed{n} + \boxed{n - 1} \cdots + 2 + 1 \Biggr)
$$

---

## From the `sum-of-even-numbers-in-symmetric-sum` notebook

We have realised this is equal to the `sum of even numbers`

$$
\textcolor{lightgray}{2} \sum_{k=1}^n \underline{2k}
$$

Which is also equal to the `consecutive multiple`

$$
\textcolor{lightgray}{2} n(n+1)
$$

---


Thus,

$$
\boxed{
    \phantom{\Biggr(} 2 + 4 + \cdots  \boxed{2n - 2} + \boxed{2n}  + \boxed{2n} + \boxed{2n - 2} \cdots + 4 + 2 = 2n(n+1) \phantom{\Biggr)}
}
$$
