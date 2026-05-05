---
title: "Decomposition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/sum-of-digits-is-less-than-or-equal-to-its-number.ipynb"
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
\space \underline{k \cdot 10^{n}} +
\underline{m \cdot 10^{n-1}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

And its sum of digits is simply

$$
\text{Sum of digits} =
\space \underline{k \phantom{\cdot 10^{n.1}}}+
\underline{m \phantom{\cdot 10^{n-1.1}}} +
\cdots +
\underline{c \phantom{\cdot 10^{3^1}}} +
\underline{b \phantom{\cdot 10^{2^1}}} +
\underline{a \phantom{\cdot 10^{1^1}}}
$$

# Place Value Comparison

Notice that for `every place bigger than the ones place`, the `place value contribution` is always bigger than the `place value`
- Given that the `variables` ranges from `1` to `9`

### $n$-th place

$$
\textcolor{lightgray}{\underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} \space =
\space} \underline{k \cdot 10^{n}} \textcolor{lightgray}{+
\underline{m \cdot 10^{n-1}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}}
$$

$$
\textcolor{lightgray}{\text{Sum of digits} =
\space} \underline{k \phantom{\cdot 10^{n.1}}} \textcolor{lightgray}{+
\underline{m \phantom{\cdot 10^{n-1.1}}} +
\cdots +
\underline{c \phantom{\cdot 10^{2^1}}} +
\underline{b \phantom{\cdot 10^{1^1}}} +
\underline{a \phantom{\cdot 10^{0^1}}}}
$$

---

$$
k\cdot 10^n > k
$$

---

### $(n-1)$-th place

$$
\textcolor{lightgray}{\underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} \space =
\space \underline{k \cdot 10^{n}}} +
\underline{m \cdot 10^{n-1}} \textcolor{lightgray}{+
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}}
$$

$$
\textcolor{lightgray}{\text{Sum of digits} =
\space \underline{k \phantom{\cdot 10^{n.1}}}} +
\underline{m \phantom{\cdot 10^{n-1.1}}} \textcolor{lightgray}{+
\cdots +
\underline{c \phantom{\cdot 10^{2^1}}} +
\underline{b \phantom{\cdot 10^{1^1}}} +
\underline{a \phantom{\cdot 10^{0^1}}}}
$$

---

$$
m\cdot 10^{n-1} > m
$$

---

### 3rd place `(Hundreds)`

$$
\textcolor{lightgray}{\underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} \space =
\space \underline{k \cdot 10^{n}} +
\underline{m \cdot 10^{n-1}} +
\cdots} +
\underline{c \cdot 10^{2}} \textcolor{lightgray}{+
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}}
$$

$$
\textcolor{lightgray}{\text{Sum of digits} =
\space \underline{k \phantom{\cdot 10^{n.1}}}+
\underline{m \phantom{\cdot 10^{n-1.1}}} +
\cdots} +
\underline{c \phantom{\cdot 10^{2^1}}} \textcolor{lightgray}{+
\underline{b \phantom{\cdot 10^{1^1}}} +
\underline{a \phantom{\cdot 10^{0^1}}}}
$$

---

$$
c\cdot 10^2 > c
$$

---


### 2nd place `(Tens)`

$$
\textcolor{lightgray}{\underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} \space =
\space \underline{k \cdot 10^{n}} +
\underline{m \cdot 10^{n-1}} +
\cdots +
\underline{c \cdot 10^{2}}} +
\underline{b \cdot 10^{1}} \textcolor{lightgray}{+
\underline{a \cdot 10^{0}}}
$$

$$
\textcolor{lightgray}{\text{Sum of digits} =
\space \underline{k \phantom{\cdot 10^{n.1}}}+
\underline{m \phantom{\cdot 10^{n-1.1}}} +
\cdots +
\underline{c \phantom{\cdot 10^{2^1}}}} +
\underline{b \phantom{\cdot 10^{1^1}}} \textcolor{lightgray}{+
\underline{a \phantom{\cdot 10^{0^1}}}}
$$

---

$$
b\cdot 10^1 > b
$$

---

### 1st place `(Ones)`

$$
\textcolor{lightgray}{\underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} \space =
\space \underline{k \cdot 10^{n}} +
\underline{m \cdot 10^{n-1}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}}} +
\underline{a \cdot 10^{0}}
$$

$$
\textcolor{lightgray}{\text{Sum of digits} =
\space \underline{k \phantom{\cdot 10^{n.1}}}+
\underline{m \phantom{\cdot 10^{n-1.1}}} +
\cdots +
\underline{c \phantom{\cdot 10^{2^1}}} +
\underline{b \phantom{\cdot 10^{1^1}}}} +
\underline{a \phantom{\cdot 10^{0^1}}}
$$

---

$$
a\cdot 10^0 = a
$$

---

# Conclusion

Thus for numbers with only `one digit`

$$
\boxed{
    \text{Number = Sum of digits}
}
$$

For numbers with `more than one digit`,
- The contributions of the `bigger places` will cause the `number` to be a lot greater than the `sum of its digits`

$$
\boxed{
    \text{Number >> Sum of digits}
}
$$
