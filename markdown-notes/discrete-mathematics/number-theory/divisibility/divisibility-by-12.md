---
title: "Composite Numbers"
source_notebook: "discrete-mathematics/number-theory/divisibility/divisibility-by-12.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Composite Numbers

`12` is a `composite number` that is made up of `4` and `3`

$$
12 = 4 \cdot 3
$$

That means as long as a number is `divisible by 4 and 3`, it is `divisible by 12`

$$
\underline{\text{Divisible by 12}} = \boxed{\text{Divisible by 3}} \ \& \ \boxed{\text{Divisible by 4}}
$$

We have already `derived the conditions` for
- `divisibility by 3` and
- `divisibility by 4`

in earlier `jupyter notebooks`

Thus, lets just move them here

## Divisibility by 3

In order for a number to be `divisible by 3`, it has to fulfil this condition:

$$
\phantom{\biggr(}
    \textbf{Sum of all its the digits is a multiple of 3}
\phantom{\biggr)}
$$

## Divisibility by 4

In order for a number to be `divisible by 4`, it has to fulfil either of these conditions:

$$
\phantom{\biggr(}
    \textbf{The number up to the tens place has to be a multiple of 4}
\phantom{\biggr)}
$$

$$
\textbf{or}
$$

$$
\phantom{\biggr(}
    \textbf{The sum of: } \underline{\textbf{Twice of its 2nd last digit}} \textbf{ plus its } \underline{\textbf{last digit}} \textbf{, must be divisible by 4}
\phantom{\biggr)}
$$

# Conclusion

Thus, in order for a number to be `divisible by 12`, it has to `fulfil these conditions`:

---

- **Divisible by 3**

$$
\boxed{
    \phantom{\biggr(}
        \textbf{Sum of all its the digits is a multiple of 3}
    \phantom{\biggr)}
}
$$


- **Divisible by 4**

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The number up to the tens place has to be a multiple of 4}
    \phantom{\biggr)}
}
$$

$$
\textbf{or}
$$

$$
\boxed{
    \phantom{\biggr(}
        \textbf{The sum of: } \underline{\textbf{Twice of its 2nd last digit}} \textbf{ plus its } \underline{\textbf{last digit}} \textbf{, must be divisible by 4}
    \phantom{\biggr)}
}
$$

> ✅ Only when **these conditions are fulfilled** can it be **divisible by 12**
