---
title: "To Factor Which Part of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/factoring-the-place-units.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/number-theory/divisibility/factoring-the-place-units.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# To Factor Which Part of a Number

Since we know that a number like this

$$
\text{Number} \space = \space \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}}
$$

Can we expressed like this

$$
\text{Number} \space =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

---

In order for this to be `divisible by` some `integer j`, we must be able to factor out `j` from this `expression`

$$
\textcolor{lightgray}{\text{Number} \space =}
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

Notice that we can factor this number from `2 different parts`
- One is the `place values` of the number

$$
\underline{k \textcolor{lightgray}{\cdot 10^{n-1}}} +
\underline{m \textcolor{lightgray}{\cdot 10^{n-2}}} +
\cdots +
\underline{c \textcolor{lightgray}{\cdot 10^{2}}} +
\underline{b \textcolor{lightgray}{\cdot 10^{1}}} +
\underline{a \textcolor{lightgray}{\cdot 10^{0}}}
$$

- The other is the `powers of 10` that represents the `grouping in each place`

$$
\underline{\textcolor{lightgray}{k \space \cdot} \space 10^{n-1}} +
\underline{\textcolor{lightgray}{m \space \cdot} \space 10^{n-2}} +
\cdots +
\underline{\textcolor{lightgray}{c \space \cdot} \space 10^{2}} +
\underline{\textcolor{lightgray}{b \space \cdot} \space 10^{1}} +
\underline{\textcolor{lightgray}{a \space \cdot} \space 10^{0}}
$$

We can't do much for the `place values` since they are all just variables,

> But we can look into the `places` itself to factor out `j`!
