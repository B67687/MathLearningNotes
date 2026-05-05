---
title: "Odd-Length Symmetric Sum of Odd Numbers"
source_notebook: "discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-odd-numbers.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Odd-Length Symmetric Sum of Odd Numbers

$$
1 + 3 + \cdots  \boxed{2n - 3} + \boxed{2n-1} + \boxed{2n - 3} \cdots + 3 + 1
$$

Since every term is `2n-1` of each of the `natural numbers` in the `symmetric sum of natural numbers`
- It also means it is

$$
2 \Biggr(  \underbrace{1 + 2 + \cdots  \boxed{n - 1} + \boxed{n} + \boxed{n - 1} \cdots + 2 + 1}_{\text{2n-1 terms}} \Biggr) - \underbrace{(1 + 1 + \cdots + 1 + 1)}_{\text{2n-1 terms}}
$$

Simplify

$$
2 \Biggr( 1 + 2 + \cdots  \boxed{n - 1} + \boxed{n} + \boxed{n - 1} \cdots + 2 + 1 \Biggr) - (2n-1)
$$

---

## From the `sum-of-odd-numbers-in-symmetric-sum` notebook

We have realised this is equal to the `sum of odd numbers`

$$
\textcolor{lightgray}{2} \space \boxed{\sum_{k=1}^n \underline{2k-1}} \textcolor{lightgray}{- (2n-1)}
$$

Which is also equal to the `square at that point`

$$
\textcolor{lightgray}{2} n^{2} \textcolor{lightgray}{- (2n-1)}
$$

---

When we simplify

$$
2n^{2} - 2n + 1
$$

We get

$$
2n(n - 1) + 1
$$

Thus

$$
\boxed{
    \phantom{\Biggr(} 1 + 3 + \cdots  \boxed{2n - 3} + \boxed{2n-1} + \boxed{2n - 3} \cdots + 3 + 1 = 2n(n - 1) + 1 \phantom{\Biggr)}
}
$$

# Even-Length Symmetric Sum of Odd Numbers

$$
1 + 3 + \cdots  \boxed{2n - 3} + \boxed{2n-1} + \boxed{2n-1} + \boxed{2n - 3} \cdots + 3 + 1
$$

Since every term is `2n-1` of each of the `natural numbers` in the `symmetric sum of natural numbers`
- It also means it is

$$
2 \Biggr(  \underbrace{1 + 2 + \cdots  \boxed{n - 1} + \boxed{n} + \boxed{n} + \boxed{n - 1} \cdots + 2 + 1}_{\text{2n terms}} \Biggr) - \underbrace{(1 + 1 + \cdots + 1 + 1)}_{\text{2n terms}}
$$

Simplify

$$
2 \Biggr( 1 + 2 + \cdots  \boxed{n - 1} + \boxed{n} + \boxed{n} + \boxed{n - 1} \cdots + 2 + 1 \Biggr) - 2n
$$

---

## From the `sum-of-even-numbers-in-symmetric-sum` notebook

We have realised this is equal to the `sum of even numbers`

$$
\textcolor{lightgray}{2} \space \boxed{\sum_{k=1}^n \underline{2k}} \textcolor{lightgray}{-2n}
$$

Which is also equal to the `square at that point`

$$
\textcolor{lightgray}{2} n(n+1) \textcolor{lightgray}{-2n}
$$

---

When we simplify

$$
2n^{2} + 2n -2n
$$

We get

$$
2n^2
$$

Thus

$$
\boxed{
    \phantom{\Biggr(} 1 + 3 + \cdots  \boxed{2n - 3} + \boxed{2n-1} + \boxed{2n-1} + \boxed{2n - 3} \cdots + 3 + 1 = 2n^2 \phantom{\Biggr)}
}
$$

# Identity

Realise that the `even-length symmetric sum of odd numbers` is equal to the `odd-length symmetric sum of even numbers`

$$
\boxed{
    \phantom{\biggr(} \underline{1 + 3 + \cdots  \boxed{2n - 3} + \boxed{2n-1} + \boxed{2n-1} + \boxed{2n - 3} \cdots + 3 + 1} \phantom{\biggr)} = \underline{2n^2} = \phantom{\biggr(} \underline{2 + 4 + \cdots  \boxed{2n - 2} + \boxed{2n} + \boxed{2n - 2} \cdots + 4 + 2} \phantom{\biggr)}
}
$$
