---
title: "Binomial Expansion and Sums of Higher Powers"
source_notebook: "discrete-mathematics/series-and-sequences/sums-of-powers.ipynb"
archived_notebook: "archive/notebooks/discrete-mathematics/series-and-sequences/sums-of-powers.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Binomial Expansion and Sums of Higher Powers

We want to find a way to calculate higher powers of $k^n$

But how do we do it?

We can try to find a way to calculate higher powers by basing them on lower powers of $k^n$, such that we can slowly but surely build every new power sum from scratch
- But how do we link $k^n$ to previous sums $k^{n-1}$, $k^{n-2}$, $k^{n-3}$ etc...?

Thinking back, there is actually a series that contains all the powers of `k`, know as the binomial expansion:

$$
(k + d)^{n} =
\dbinom{n}{0}k^{n}d^{0} +
\dbinom{n}{1}k^{n-1}d^{1} +
\dbinom{n}{2}k^{n-2}d^{2} +
\cdots +
\dbinom{n}{n-2}k^{2}d^{n-2} +
\dbinom{n}{n-1}k^{1}d^{n-1} +
\dbinom{n}{n}k^{0}d^{n}
$$

We can make it reflect the number of combinations of `k` instead
- This is why binomial coefficients are symmetric

> The coefficients are symmetric around $\dfrac{n+1}{2}$, where $\dbinom{n}{m} = \dbinom{n}{n-m}$

- Also we synchronise the `number of combinations` with `k`, so more relationships are stated clearly

$$
(k + d)^{n} =
\dbinom{n}{n}k^{n}d^{0} +
\dbinom{n}{n-1}k^{n-1}d^{1} +
\dbinom{n}{n-2}k^{n-2}d^{2} +
\cdots +
\dbinom{n}{2}k^{2}d^{n-2} +
\dbinom{n}{1}k^{1}d^{n-1} +
\dbinom{n}{0}k^{0}d^{n}
$$

But the second term, `d`, still exists. Is there a way to make sure only `k` exist in this expansion?
- What kind of base would cause powers of `d` to disappear but not affect the `k` terms?
- If it were `0`, then it would eliminate every term
- If it were `1`, it would keep the `k` term, and we can get rid of the `d` terms because they would not affect the `k` terms!

$$
(k + 1)^{n} =
\dbinom{n}{n}k^{n}1^{0} +
\dbinom{n}{n-1}k^{n-1}1^{1} +
\dbinom{n}{n-2}k^{n-2}1^{2} +
\cdots +
\dbinom{n}{2}k^{2}1^{n-2} +
\dbinom{n}{1}k^{1}1^{n-1} +
\dbinom{n}{0}k^{0}1^{n}
$$

With the power of `1`s removed, is equivalent to

$$
(k + 1)^{n} =
\dbinom{n}{n}k^{n} +
\dbinom{n}{n-1}k^{n-1} +
\dbinom{n}{n-2}k^{n-2} +
\cdots +
\dbinom{n}{2}k^{2} +
\dbinom{n}{1}k^{1} +
\dbinom{n}{0}k^{0}
$$

Further simplify the combinations, plus a few minor touchups

$$
(k + 1)^{n} =
k^{n} +
nk^{n-1} +
\dbinom{n}{n-2}k^{n-2} +
\cdots +
\dbinom{n}{2}k^{2} +
nk + 1
$$

Wow! Now that we have an expression that contains $k^{n}$ and its previous powers, maybe we can start here?

# Telescoping Sums and Sums of Higher Powers

But wait, it also contains its next power, if we were to isolate $k^{n}$ directly

$$
k^{n} =
(k + 1)^{n} -
nk^{n-1} -
\dbinom{n}{n-2}k^{n-2} -
\cdots -
\dbinom{n}{2}k^{2} -
nk -
1
$$

And apply the summation, from `1` to `m`:

$$
\sum_{k=1}^m k^{n} =
\sum_{k=1}^m (k + 1)^{n} -
n \sum_{k=1}^m k^{n-1} -
\dbinom{n}{n-2} \sum_{k=1}^m k^{n-2} -
\cdots -
\dbinom{n}{2} \sum_{k=1}^m k^{2} -
n \sum_{k=1}^m k -
\sum_{k=1}^m 1
$$

Then we see that we have to find the sum of the next power in order to find the sum of the current power

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =}
\sum_{k=1}^m (k + 1)^{n}
\textcolor{lightgray}{-
    n \sum_{k=1}^m k^{n-1} -
    \dbinom{n}{n-2} \sum_{k=1}^m k^{n-2} -
    \cdots -
    \dbinom{n}{2} \sum_{k=1}^m k^{2} -
    n \sum_{k=1}^m k -
    \sum_{k=1}^m 1
}
$$

- But that defeats the whole purpose of building-up from previous powers, if we already know what the next power is

So what can we do to remove the need for the higher power?

Notice that we have these 2 terms

$$
(k + 1)^{n} \textcolor{lightgray}{=}
k^{n}
\textcolor{lightgray}{+
    nk^{n-1} +
    \dbinom{n}{n-2}k^{n-2} +
    \cdots +
    \dbinom{n}{2}k^{2} +
    nk + 1
}
$$

Thus if we take the sum of their difference, we will have a convergent result! And thus eliminates the problem of $(k+1)^n$

Taking the sum of their difference

$$
\sum_{k=1}^m (k + 1)^{n} - k^{n} =
n \sum_{k=1}^m k^{n-1} +
\dbinom{n}{n-2} \sum_{k=1}^m k^{n-2} +
\cdots +
\dbinom{n}{2} \sum_{k=1}^m k^{2} +
n \sum_{k=1}^m k +
\sum_{k=1}^m 1
$$

Focusing on this part

$$
\sum_{k=1}^m (k + 1)^{n} -
k^{n} \textcolor{lightgray}{=
    n \sum_{k=1}^m k^{n-1} +
    \dbinom{n}{n-2} \sum_{k=1}^m k^{n-2} +
    \cdots +
    \dbinom{n}{2} \sum_{k=1}^m k^{2} +
    n \sum_{k=1}^m k +
    \sum_{k=1}^m 1
}
$$

We have

$$
\begin{align*}
    \sum_{k=1}^m (k + 1)^{n} - k^{n} &= \cancel{2^{n}} - 1^{n} \\
    & + \cancel{3^{n}} - \cancel{2^{n}} \\
    & + \space \cdots - \cancel{3^{n}} \\
    & \vdots \\
    & + \cancel{m^{n}} - \cdots \\
    & + (m+1)^{n} - \cancel{m^{n}} \\
    & \\
    & = (m+1)^{n} - 1^{n} \\
    & = (m+1)^{n} - 1
\end{align*}
$$

Thus

$$
\sum_{k=1}^m (k + 1)^{n} - k^{n} = (m+1)^{n} - 1
$$

And

$$
(m+1)^{n} - 1 =
n \sum_{k=1}^m k^{n-1} +
\dbinom{n}{n-2} \sum_{k=1}^m k^{n-2} +
\cdots +
\dbinom{n}{2} \sum_{k=1}^m k^{2} +
n \sum_{k=1}^m k +
\sum_{k=1}^m 1
$$

We can simplify it a little bit

$$
(m+1)^{n} - 1 =
n \sum_{k=1}^m k^{n-1} +
\dbinom{n}{n-2} \sum_{k=1}^m k^{n-2} +
\cdots +
\dbinom{n}{2} \sum_{k=1}^m k^{2} +
n \sum_{k=1}^m k +
m
$$

And then

$$
(m+1)^{n} -
(m + 1) =
n \sum_{k=1}^m k^{n-1} +
\dbinom{n}{n-2} \sum_{k=1}^m k^{n-2} +
\cdots +
\dbinom{n}{2} \sum_{k=1}^m k^{2} +
n \sum_{k=1}^m k
$$

Wait a minute, but now we do not have any $k^n$ to work with, how are we going to find $k^n$?

# Correcting the Premise

Let us go back to this part, before we did method of difference

$$
(k + 1)^{n} =
\dbinom{n}{n}k^{n} +
\dbinom{n}{n-1}k^{n-1} +
\dbinom{n}{n-2}k^{n-2} +
\cdots +
\dbinom{n}{2}k^{2} +
\dbinom{n}{1}k^{1} +
\dbinom{n}{0}k^{0}
$$

Notice as this is the closest expression left, to $k^n$, after we do telescoping sums

$$
\textcolor{lightgray}{(k + 1)^{n} =
    \dbinom{n}{n}k^{n} +}
\dbinom{n}{n-1}k^{n-1}
\textcolor{lightgray}{+
    \dbinom{n}{n-2}k^{n-2} +
    \cdots +
    \dbinom{n}{2}k^{2} +
    \dbinom{n}{1}k^{1} +
    \dbinom{n}{0}k^{0}
}
$$

#### Perhaps we can just make this $k^n$ from the start?

In order to do that we have to increase the power by `1` throughout, and adjust the coefficients accordingly

From this

$$
(k + 1)^{n} =
\dbinom{n}{n}k^{n} +
\dbinom{n}{n-1}k^{n-1} +
\dbinom{n}{n-2}k^{n-2} +
\cdots +
\dbinom{n}{2}k^{2} +
\dbinom{n}{1}k^{1} +
\dbinom{n}{0}k^{0}
$$

To this

$$
(k + 1)^{n+1} =
\dbinom{n+1}{n+1}k^{n+1} +
\dbinom{n+1}{n}k^{n} +
\dbinom{n+1}{n-1}k^{n-1} +
\cdots +
\dbinom{n+1}{2}k^{2} +
\dbinom{n+1}{1}k^{1} +
\dbinom{n+1}{0}k^{0}
$$

# Going through the Steps

And thus when we simplify

$$
\textcolor{lightgray}{(k + 1)^{n+1}
= \space}
k^{n+1} +
(n+1)k^{n} +
\dbinom{n+1}{n-1}k^{n-1} +
\cdots +
\dbinom{n+1}{2}k^{2} +
(n+1)k + 1
$$

And take the sum

$$
\sum_{k=1}^m (k + 1)^{n+1} =
\sum_{k=1}^m k^{n+1} +
(n+1) \sum_{k=1}^m k^{n} +
\dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} +
\cdots +
\dbinom{n+1}{n-2} \sum_{k=1}^m k^{2} +
(n+1) \sum_{k=1}^m k +
\sum_{k=1}^m 1
$$

Set up the method of differences

$$
\sum_{k=1}^m (k + 1)^{n+1} -
k^{n+1} \textcolor{lightgray}{=
(n+1) \sum_{k=1}^m k^{n} +
\dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} +
\cdots +
\dbinom{n+1}{2} \sum_{k=1}^m k^{2} +
(n+1) \sum_{k=1}^m k +
\sum_{k=1}^m 1}
$$

Simplify to this

$$
(m + 1)^{n+1} - 1 \textcolor{lightgray}{=
(n+1) \sum_{k=1}^m k^{n} +
\dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} +
\cdots +
\dbinom{n+1}{2} \sum_{k=1}^m k^{2} +
(n+1) \sum_{k=1}^m k +
\sum_{k=1}^m 1}
$$

Now that we can seek to isolate the term with $k^n$

$$
\textcolor{lightgray}{(m + 1)^{n+1} - 1 =}
(n+1) \sum_{k=1}^m k^{n} \textcolor{lightgray}{+
\dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} +
\cdots +
\dbinom{n+1}{2} \sum_{k=1}^m k^{2} +
(n+1) \sum_{k=1}^m k +
\sum_{k=1}^m 1}
$$

Shift the rest of the summation over to the other side:

$$
\textcolor{lightgray}{(n+1) \sum_{k=1}^m k^{n}} =
(m + 1)^{n+1} - 1 -
\dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} -
\cdots -
\dbinom{n+1}{2} \sum_{k=1}^m k^{2} -
(n+1) \sum_{k=1}^m k +
\sum_{k=1}^m 1
$$

Then shift the coefficient to the other side

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n}} =
\dfrac{1}{n+1}
\biggr[ (m + 1)^{n+1} - 1 -
    \dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} -
    \cdots -
    \dbinom{n+1}{2} \sum_{k=1}^m k^{2} -
    (n+1) \sum_{k=1}^m k +
    \sum_{k=1}^m 1
\biggr]
$$

With the same simplification on the sum of `1`

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[ (m + 1)^{n+1} - 1 -
    \dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} -
    \cdots -
    \dbinom{n+1}{2} \sum_{k=1}^m k^{2} -
    (n+1) \sum_{k=1}^m k} +
    m
\biggr]
$$

Shift over

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[} (m + 1)^{n+1} - (m + 1) \textcolor{lightgray}{-
    \dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} -
    \cdots -
    \dbinom{n+1}{2} \sum_{k=1}^m k^{2} -
    (n+1) \sum_{k=1}^m k
\biggr]
}
$$

We get to this

$$
\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[ (m + 1)^{n+1} - (m + 1) -
    \dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} -
    \cdots -
    \dbinom{n+1}{2} \sum_{k=1}^m k^{2} -
    (n+1) \sum_{k=1}^m k
\biggr]
$$

# Compressed General Formula

Thus we have arrived at the expanded general formula to build up formulas for sums of higher powers
- It will just be tedious, but it is a gurantee to get the formulas of all the sums of higher integer powers

$$
\boxed{
    \sum_{k=1}^m k^{n} =
    \dfrac{1}{n+1} \biggr[ (m + 1)^{n+1} -
    (m+1) -
    \dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} -
    \cdots -
    \dbinom{n+1}{2} \sum_{k=1}^m k^{2} -
    (n+1) \sum_{k=1}^m k \biggr], \quad \text{for} \space  n \in \mathbf Z^{+}
    }
$$

We can compress it further

---

Notice this part are all sums of sums

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[ (m + 1)^{n+1} -
    (m+1)} -
    \dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} -
    \cdots -
    \dbinom{n+1}{2} \sum_{k=1}^m k^{2} -
    (n+1) \sum_{k=1}^m k
\biggr]
$$

When we revert it back into the form the clear combinations, bringing back the sum of $k^{0}$, and the power of $k^{1}$

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[ (m + 1)^{n+1}} -
    1 \textcolor{lightgray}{ -
    \dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} -
    \cdots -
    \dbinom{n+1}{2} \sum_{k=1}^m k^{2}} -
    \dbinom{n+1}{1} \sum_{k=1}^m k^1 -
    \dbinom{n+1}{0} \sum_{k=1}^m k^0 \textcolor{lightgray}
{\biggr], \quad \text{for n > 0}
}
$$

We have

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[
    (m + 1)^{n+1} -
    1} -
    \dbinom{n+1}{n-1} \sum_{k=1}^m k^{n-1} -
    \cdots -
    \dbinom{n+1}{2} \sum_{k=1}^m k^{2} -
    \dbinom{n+1}{1} \sum_{k=1}^m k^1 -
    \dbinom{n+1}{0} \sum_{k=1}^m k^0
\textcolor{lightgray}{\biggr]}
$$

Notice that the `combination choice` matches the `power of k` , and ranges from `n-1` to `0`

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[ (m + 1)^{n+1} -
    1} -
    \dbinom{\textcolor{lightgray}{n+1}}{n-1} \textcolor{lightgray}{\sum_{k=1}^m} k^{n-1} -
    \cdots \space -
    \dbinom{\textcolor{lightgray}{n+1}}{2} \textcolor{lightgray}{\sum_{k=1}^m} k^{2} -
    \dbinom{\textcolor{lightgray}{n+1}}{1} \textcolor{lightgray}{\sum_{k=1}^m} k^{1} -
    \dbinom{\textcolor{lightgray}{n+1}}{0} \textcolor{lightgray}{\sum_{k=1}^m} k^{0}
\textcolor{lightgray}{\biggr]}
$$

Which is the same as ranging the other way

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[ (m + 1)^{n+1} -
    1} -
    \dbinom{\textcolor{lightgray}{n+1}}{0} \textcolor{lightgray}{\sum_{k=1}^m} k^{0} -
    \dbinom{\textcolor{lightgray}{n+1}}{1} \textcolor{lightgray}{\sum_{k=1}^m} k^{1} -
    \dbinom{\textcolor{lightgray}{n+1}}{2} \textcolor{lightgray}{\sum_{k=1}^m} k^{2} -
    \cdots \space -
    \dbinom{\textcolor{lightgray}{n+1}}{n-1} \textcolor{lightgray}{\sum_{k=1}^m} k^{n-1}
\textcolor{lightgray}{\biggr]}
$$

Thus, we can compress the sums of sums such that:
- The `combination choice` and the `power of k` ranges from `0` to `n-1`

$$
\textcolor{lightgray}{\sum_{k=1}^m k^n =
    \frac{1}{n+1} \Biggl[ (m+1)^{n+1} - 1} -
    \sum_{r=0}^{n-1}  \underline{\binom{n+1}{r} \sum_{k=1}^m k^{r}} \textcolor{lightgray}{\Biggr]}
$$

Thus, we get this general formula of

$$
\boxed{
    \sum_{k=1}^m k^n =
    \frac{1}{n+1} \Biggl[ (m+1)^{n+1} - 1 -
    \sum_{r=0}^{n-1}  \underline{ \binom{n+1}{r} \sum_{k=1}^m k^{r} } \Biggr], \text{n} \in \mathbf{Z^{+}}
}
$$

# Symmetric General Formula

The symmetric and equivalent form, where the coefficients are reflected

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[ (m + 1)^{n+1} -
    (m+1)} -
    \dbinom{n+1}{2} \sum_{k=1}^m k^{n-1} -
    \cdots -
    \dbinom{n+1}{n-1} \sum_{k=1}^m k^{2} -
    (n+1) \sum_{k=1}^m k \textcolor{lightgray}
{\biggr]
}
$$

Bringing back $k^0$ once more

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[
    (m + 1)^{n+1} -
    1} -
    \dbinom{n+1}{2} \sum_{k=1}^m k^{n-1} -
    \cdots -
    \dbinom{n+1}{n-1} \sum_{k=1}^m k^{2} -
    \dbinom{n+1}{n} \sum_{k=1}^m k^1 -
    \dbinom{n+1}{n+1} \sum_{k=1}^m k^0
\textcolor{lightgray}{\biggr]}
$$

Notice that
- The `combination choice` ranges from `2` to `n+1`, while the
- The `power of k` ranges from `n-1` to `0`

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
\dfrac{1}{n+1}
\biggr[ (m + 1)^{n+1} -
    1} -
    \dbinom{\textcolor{lightgray}{n+1}}{2} \textcolor{lightgray}{\sum_{k=1}^m} k^{n-1} -
    \cdots \space -
    \dbinom{\textcolor{lightgray}{n+1}}{n-1} \textcolor{lightgray}{\sum_{k=1}^m} k^{2} -
    \dbinom{\textcolor{lightgray}{n+1}}{n} \textcolor{lightgray}{\sum_{k=1}^m} k^{1} -
    \dbinom{\textcolor{lightgray}{n+1}}{n+1} \textcolor{lightgray}{\sum_{k=1}^m} k^{0}
\textcolor{lightgray}{\biggr]}
$$


Let the sum of sums be in terms of `j`

$$
\textcolor{lightgray}{\sum_{k=1}^m k^{n} =
    \frac{1}{n+1}}
\textcolor{lightgray}{
    \Biggl[
        (m+1)^{n+1} - 1 - \sum_{j=2}^{n+1}}
            \underline{
                \binom{
                    \textcolor{lightgray}{n+1}
                }{j}
\textcolor{lightgray}{
    \sum_{k=1}^m k^{\colorbox{lightgray}{\quad}}
            } }
    \textcolor{lightgray}{\Biggr]
}
$$

As the `power of k` is nested within a sum, it has to depend on the index `j` of that outer sum
- For both the `power of k` and `combinatorial choice`, it decreases by step of `1` from some point to some point
- Which means their `difference will stay the same` throughout
- Thus, we can represent the `power of k` in terms of `j` from any part of the summation
    - Let's take from the first


To find the relationship between `combinatorial choice` and `power of k`
- We find the constant first, it is `-j + 1`
- Then the variable is simply `+n`
- Giving us `-j + 1 + n`

Rearranged, such that the negative sign is not in front,
- We have `n - j + 1` for the `power of k`

$$
\textcolor{lightgray}{\sum_{k=1}^m k^n =
    \frac{1}{n+1} \Biggl[ (m+1)^{n+1} - 1} -
    \sum_{j=2}^{n+1}  \underline{\binom{n+1}{j} \sum_{k=1}^m k^{n - j + 1}} \textcolor{lightgray}{\Biggr]}
$$


Thus, we get this symmetric general formula of

$$
\boxed{
    \sum_{k=1}^m k^n =
    \frac{1}{n+1} \Biggl[ (m+1)^{n+1} - 1 -
    \sum_{j=2}^{n+1}  \underline{ \binom{n+1}{j} \sum_{k=1}^m k^{n - j + 1} }
    \Biggr], \text{n} \in \mathbf{Z^{+}}
}
$$

- The `power of k` might look convoluted because it is nested in another sum
- When in fact it is just `1 less than n`, decreasing by `1` down to `1`

# The Symmetric Recursive Formulas

Thus, we have 2 equal and symmetric formulas for the recursive build-up of sums of powers

---

- The Direct Formula

$$
\boxed{
    \sum_{k=1}^m k^n =
    \frac{1}{n+1} \Biggl[ (m+1)^{n+1} - 1 -
    \sum_{r=0}^{n-1}  \underline{ \binom{n+1}{r} \sum_{k=1}^m k^{r} }
    \Biggr], \text{n} \in \mathbf{Z^{+}}
}
$$

- The Converse Formula

$$
\boxed{
    \sum_{k=1}^m k^n =
    \frac{1}{n+1} \Biggl[ (m+1)^{n+1} - 1 -
    \sum_{j=2}^{n+1}  \underline{ \binom{n+1}{j} \sum_{k=1}^m k^{n - j + 1} }
    \Biggr], \text{n} \in \mathbf{Z^{+}}
}
$$

# Further Compression

## From the Converse Formula

$$
\sum_{k=1}^m k^n =
    \frac{1}{n+1} \Biggl[ (m+1)^{n+1} - 1 -
    \sum_{j=2}^{n+1}  \underline{ \binom{n+1}{j} \sum_{k=1}^m k^{n - j + 1} }
    \Biggr], \text{n} \in \mathbf{Z^{+}}
$$

This can be expressed in summation form as well

$$
\textcolor{lightgray}{\sum_{k=1}^m k^n =
    \frac{1}{n+1} \Biggl[} (m+1)^{n+1} \textcolor{lightgray}{- 1 -
    \sum_{j=2}^{n+1}  \underline{ \binom{n+1}{j} \sum_{k=1}^m k^{n - j + 1} }
    \Biggr], \text{n} \in \mathbf{Z^{+}}}
$$

Expand it out and

$$
\textcolor{lightgray}{\sum_{k=1}^m k^n =
\frac{1}{n+1} \Biggl[} \sum_{p=1}^{n+1} \underline{ \dbinom{n+1}{p} m^{p} } \textcolor{lightgray}{-
\sum_{j=2}^{n+1}  \underline{\binom{n+1}{j} \sum_{k=1}^m k^{n - j + 1}}
\Biggr], \text{n} \in \mathbf{Z^{+}}}
$$

Attempt to match the other summation by factoring out the first term

$$
\textcolor{lightgray}{\sum_{k=1}^m k^n =
\frac{1}{n+1} \Biggl[} (n+1)m + \sum_{p=2}^{n+1} \underline{ \dbinom{n+1}{p} m^{p} } \textcolor{lightgray}{-
\sum_{j=2}^{n+1}  \underline{\binom{n+1}{j} \sum_{k=1}^m k^{n - j + 1}}
\Biggr], \text{n} \in \mathbf{Z^{+}}}
$$

Since now they both match in summation index

$$
\textcolor{lightgray}{\sum_{k=1}^m k^n =
\frac{1}{n+1} \Biggl[ (n+1)m} + \sum_{p=2}^{n+1} \textcolor{lightgray}{\underline{ \dbinom{n+1}{p} m^{p} }} -
\sum_{j=2}^{n+1}  \textcolor{lightgray}{\underline{\binom{n+1}{j} \sum_{k=1}^m k^{n - j + 1}}
\Biggr], \text{n} \in \mathbf{Z^{+}}}
$$

As well as one of the factors within the summation

$$
\textcolor{lightgray}{\sum_{k=1}^m k^n =
\frac{1}{n+1} \Biggl[ \sum_{p=1}^{n+1}} \underline{ \dbinom{n+1}{p} \textcolor{lightgray}{m^{p}} } \textcolor{lightgray}{-
\sum_{j=2}^{n+1}}  \underline{\binom{n+1}{j} \textcolor{lightgray}{\sum_{k=1}^m k^{n - j + 1}}}
\Biggr], \text{n} \in \mathbf{Z^{+}}
$$

We can combine it like so, keeping the index `j` as perference

$$
\sum_{k=1}^m k^n =
\frac{1}{n+1} \Biggl[ (n+1)m +
\sum_{j=2}^{n+1}  \underline{\binom{n+1}{j} \left( m^{j} - \sum_{k=1}^m k^{n - j + 1} \right)}
\Biggr], \text{n} \in \mathbf{Z^{+}}
$$

And notice these 2 `cancels out when expanded`

$$
\textcolor{lightgray}{\sum_{k=1}^m k^n =}
\frac{1}{n+1} \textcolor{lightgray}{\Biggl[} (n+1)\textcolor{lightgray}{m +
\sum_{j=2}^{n+1}  \underline{\binom{n+1}{j} \left( m^{j} - \sum_{k=1}^m k^{n - j + 1} \right)}
\Biggr], \text{n} \in \mathbf{Z^{+}}}
$$

So we expand it, and get this:

$$
\boxed{
    \sum_{k=1}^m k^n =
    m + \frac{1}{n+1}
    \sum_{j=2}^{n+1}  \underline{\binom{n+1}{j} \left( m^{j} - \sum_{k=1}^m k^{n - j + 1} \right)}
    , \text{n} \in \mathbf{Z^{+}}
}
$$

## From the Direct Formula

$$
\sum_{k=1}^m k^n =
\frac{1}{n+1} \Biggl[ (m+1)^{n+1} - 1 -
\sum_{r=0}^{n-1}  \underline{ \binom{n+1}{r} \sum_{k=1}^m k^{r} }
\Biggr], \text{n} \in \mathbf{Z^{+}}
$$

We will do a similar compression

From this

$$
\textcolor{lightgray}{\sum_{k=1}^m k^n =
\frac{1}{n+1} \Biggl[ } (n+1)m + \sum_{p=0}^{n-1} \underline{ \dbinom{n+1}{p} m^{n-p+1} } \textcolor{lightgray}{-
\sum_{r=0}^{n-1}  \underline{ \binom{n+1}{r} \sum_{k=1}^m k^{r} }
\Biggr], \text{n} \in \mathbf{Z^{+}}}
$$

To this

$$
\textcolor{lightgray}{\sum_{k=1}^m k^n =
\frac{1}{n+1} \Biggl[ (n+1)m} +
\sum_{r=0}^{n-1}  \underline{ \binom{n+1}{r} \left( m^{n-r+1} - \sum_{k=1}^m k^{r} \right) }
\Biggr], \text{n} \in \mathbf{Z^{+}}
$$

To this

$$
\boxed{
    \sum_{k=1}^m k^n =
     m + \frac{1}{n+1}
    \sum_{r=0}^{n-1}  \underline{ \binom{n+1}{r} \left( m^{n-r+1} - \sum_{k=1}^m k^{r} \right) }
    , \text{n} \in \mathbf{Z^{+}}
}
$$

# The Compressed Formulas

Thus, we have 2 equal and symmetric formulas for the recursive build-up of sums of powers

---

- The Direct Formula

$$
\boxed{
    \sum_{k=1}^m k^n =
     m + \frac{1}{n+1}
    \sum_{r=0}^{n-1}  \underline{ \binom{n+1}{r} \left( m^{n-r+1} - \sum_{k=1}^m k^{r} \right) }
    , \text{n} \in \mathbf{Z^{+}}
}
$$

- The Converse Formula

$$
\boxed{
    \sum_{k=1}^m k^n =
    m + \frac{1}{n+1}
    \sum_{j=2}^{n+1}  \underline{\binom{n+1}{j} \left( m^{j} - \sum_{k=1}^m k^{n - j + 1} \right)}
    , \text{n} \in \mathbf{Z^{+}}
}
$$

# Further Investigation

Faulhaber's Formula

$$
\sum_{k=1}^m k^n = \frac{1}{n+1} \sum_{j=0}^n \binom{n+1}{j} B_j m^{n+1-j}
$$

$$
B_0 = 1, \quad \text{and for } n \geq 1: \quad \sum_{k=0}^{n} \binom{n+1}{k} B_k = 0
$$

How do we get here?
