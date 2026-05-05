---
title: "Special Case for the Base"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-10.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Special Case for the Base

Since we are `dividing by the base` itself, the number itself is built on bases,
- How we represent number in bases is basically by `grouping a quantity` by that number

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

- Then `grouping groups by the same number` on and on and on till it suffices

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space c \space b \space \textcolor{lightgray}{a}}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} \textcolor{lightgray}{+
\underline{a \cdot 10^{0}}}
$$

Thus, in order to know if a number is `divisible by its base`,
- We only need to check whether the `grouping is whole`, or in other words
- Whether there are `no remainders`, i.e. **nothing in the ones place**

$$
\text{Number} = \underbrace{\overline{\textcolor{lightgray}{k \space m \space \cdots \space c \space b} \space a}}_{\text{n places}} =
\textcolor{lightgray}{\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}}} +
\underline{a \cdot 10^{0}}
$$

# Divisibility Rule

Thus, to determine if a number is `divisible by 10`

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The digit in the ones place has to be 0}
    \phantom{\biggr)}
}
$$
