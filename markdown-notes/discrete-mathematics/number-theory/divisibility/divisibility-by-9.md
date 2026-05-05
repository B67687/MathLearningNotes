---
title: "The Composition of a Number"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-9.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# The Composition of a Number

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} =
\space \underline{k \cdot 10^{n-1}} +
\underline{m \cdot 10^{n-2}} +
\cdots +
\underline{c \cdot 10^{2}} +
\underline{b \cdot 10^{1}} +
\underline{a \cdot 10^{0}}
$$

Lets look into the `powers of 10`

# Factoring Powers of 10

From the `divisibility-by-3` notebook, we know that:

- All the `non-negative powers of 10` can be partitioned like so

$$
10^{n} = \underline{
    3^2 \cdot 10^{n-1} + 3^2 \cdot 10^{n-2} + \cdots + 3^2 \cdot 10^{1} + 3^2 \cdot 10^{0} + 1
}
$$


When we `simplify it even more` than what we did for `divisibility-by-3`, we get

$$
\boxed{
    10^{n} = 9 \cdot \underbrace{\overline{11\cdots11}}_{\text{n digits}} + 1
}
$$

We realise that `powers of 10` can be split into
- `one component divisible by 9`

$$
\textcolor{lightgray}{10^{n} =} 9 \cdot \underbrace{\overline{11\cdots11}}_{\text{n digits}} \textcolor{lightgray}{+ 1}
$$

- then the `other component of 1`

$$
\textcolor{lightgray}{10^{n} = 9 \cdot \underbrace{\overline{11\cdots11}}_{\text{n digits}}} + 1
$$

# Factoring the Number

Using the same `derivation logic` from the `divisibility-by-3` notebook, we will get

> Where $q_{n} = \underbrace{\overline{11\cdots11}}_{\text{n digits}}$

$$
\text{Number} = \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}} =
9 \biggr(
k \cdot q_{n-1} +
m \cdot q_{n-2} +
\cdots +
c \cdot q_{2} +
b\cdot q_{1}
\biggr) +
\big(
k + m + \cdots + c + b + a
\big)
$$

# Conclusion

Thus, we see that `this part` of the number is a `multiple of 9`
- Thus making it `divisible by 9`

$$
\textcolor{lightgray}{\text{Number} = }
9 \biggr(
    kq_{n-1} +
    mq_{n-2} +
    \cdots +
    cq_{2} +
    bq_{1}
\biggr)
\textcolor{lightgray}{+
\big( k + m + \cdots + c + b + a \big)}
$$

Thus for the `whole number to be divisible by 9`,  this part also has to be a `multiple of 9`

$$
\textcolor{lightgray}{\text{Number} =
9 \biggr(
    kq_{n-1} +
    mq_{n-2} +
    \cdots +
    cq_{2} +
    bq_{1}
\biggr)} +
\big( k + m + \cdots + c + b + a \big)
$$

Realise that it contains `all the digits of the number itself in order`

$$
\text{Number} \space = \space \underbrace{\overline{k \space m \space \cdots \space c \space b \space a}}_{\text{n places}}
$$

# Divisibility Rule

Thus, to determine if the `whole number is divisible by 9`,

$$
\boxed{
    \phantom{\biggr(}
        \textbf{Sum of all its the digits is a multiple of 9}
    \phantom{\biggr)}
}
$$
