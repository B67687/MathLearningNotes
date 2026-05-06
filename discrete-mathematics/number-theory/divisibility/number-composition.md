---
title: "Decomposition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/number-composition.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/number-theory/divisibility/number-composition.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Decomposition of a Number

Any number can be represented in its `base-10` form like so
- Where the variables range from `0` to `9`

$$
\text{Number} \space = \space \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}}
$$

When each place is expanded out, we get

$$
\underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} \space =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

Thus

$$
\text{Number} \space =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$
