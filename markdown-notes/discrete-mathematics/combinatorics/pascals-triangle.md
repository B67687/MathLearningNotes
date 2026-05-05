---
title: "Pascal's Triangle"
source_notebook: "discrete-mathematics/combinatorics/pascals-triangle.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Pascal's Triangle

This is the Pascal's Triangle:

$$
\begin{array}
    & & & & & & 1 & & & & & &\\
    & & & & 1 & & 1 & & & &\\
    & & & 1 & & 2 & & 1 & & &\\
    & & 1 & & 3 & & 3 & & 1 & &\\
    & 1 & & 4 & & 6 & & 4 & & 1 &\\
    1 & & 5 & & 10 & & 10 & & 5 & & 1\\
\end{array}
$$

Each number, bar `1`, is equal to the 2 numbers right above it added together

`1` is usually stated as the starting point of a Pascals Triangle, and the rest of the numbers are simply made of the 2 numbers above it added together
- For the sides of the triangle, it is simply `1 + 0`, therefore it is always `1`

We also know of its relevance in binomial distribution such that each row corresponds to the coefficients of each term in a binomial expansion
- The coefficients are also expressible in terms of combinations, in forms like ${}^{2}C_1$,  ${}^{4}C_3$,  ${}^{8}C_2$ etc etc

This begs a few questions
- Does this mean the Pascal's Triangle can also be formed in combinatorially?
- Does this bring about a earlier premise that might explain how even `1` came about?
- How does this connect to the addition properties of the Pascal's Triangle that we know?

Let's find out

# The Types of Choices

To clarify what choose means here, it is

$$
\dbinom{n}{k}, \text{where n is the total size, k is the the size of your choice}
$$

---
#### Choose **less than nothing**, there is **no way**
- The premise of choosing is to find ways to group `k` things together out of some pile of `n` things. Thus, to group less than nothing, is not possible.

#### Choose **nothing**, there is exactly **1 way**
- Nothing else, except to choose a set of 0 things, can be done

#### Choose **from 1 to n**, we have **some ways**
- Some number > 1

#### Choose **everything**, there is exactly **1 way**
- Nothing else, except to choose the full set, can be done

#### Choose **more than n**, then there is **no way**
- Because there is no way to choose more than the total.

---

# Re-building the Pascals Triangle

Now that we know of these general patterns, we can rebuild Pascal's Triangle from the ground up

To start off, we have nothing, thus to start building the triangle is to start choosing.

From nothing, we can only choose nothing

$$
\dbinom{0}{0} = 1
$$

Now that we have 1 thing, we have 1 more option to choose. We can choose nothing `i.e. 0` or we can choose `1`.
- Thus this is `2` options total

$$
\begin{array}{ccccccc}
    & \dbinom{0}{0} = 1 &\\
    \dbinom{1}{0} = 1 & & \dbinom{1}{1} = 1\\
\end{array}
$$

We may continue this pattern of choosing from the previous choices so on and so forth

$$
\begin{array}{ccccccc}
    & & & \dbinom{0}{0} = 1 & & & \\
    & & \dbinom{1}{0} = 1 & & \dbinom{1}{1} = 1 & &\\
    & \dbinom{2}{0} = 1 & & \dbinom{2}{1} = 2 & & \dbinom{2}{2} = 1 &\\
    \dbinom{3}{0} = 1 & & \dbinom{3}{1} = 3 & & \dbinom{3}{2} = 3 & & \dbinom{3}{3} = 1
\end{array}
$$

How exactly we calculate the choices is explained in combinations and permutations chapter

# What is the Relevance?

But what relevance does combination have to do with addition?

Why does

$$
\dbinom{0}{0} = \dbinom{1}{0} = \dbinom{1}{1} = \dbinom{n}{0} = \dbinom{n}{1}
$$

Why does

$$
\dbinom{1}{0} + \dbinom{1}{1} = \dbinom{2}{1}, \quad \dbinom{2}{1} + \dbinom{2}{2} = \dbinom{3}{2}, \quad \text{etc etc}
$$

There seems to be no relevance?

- There is!

When we add one more thing to the total, we have 2 choices for that new thing, either it is chosen as part of the choice, or it is not chosen as part of the choice.

# Take These Examples
---

## 8 Choose 3

From a premise of `7 choose 3`, if we have one more thing, we have `8 choose 3`

- Either the 8th choice is chosen, or it is not chosen.

Thus `8 choose 3` consists of these scenarios:

- If it is chosen

$$
\text{(8th choice chosen), (remaining 7 choices has to choose 2 more)} \longrightarrow \dbinom{1}{1} \space \text{then} \space \dbinom{7}{2} \longrightarrow \dbinom{1}{1} \cdot \dbinom{7}{2}
$$

- If it is not chosen

$$
\text{(8th choice not chosen), (remaining 7 choices has to choose 3)} \longrightarrow \dbinom{1}{0} \space \text{then} \space \dbinom{7}{3} \longrightarrow \dbinom{1}{0} \cdot \dbinom{7}{3}
$$

Thus, for `8 choose 2` we have the combination of these 2 scenarios

$$
\underline{
    \dbinom{8}{3} = \dbinom{1}{1} \dbinom{7}{2} + \dbinom{1}{0} \dbinom{7}{3}
}
$$

Which can be simplified to just

$$
\underline{
    \dbinom{8}{3} = \dbinom{7}{2} + \dbinom{7}{3}
}
$$

As `1 choose 1` is `1`, and `anything choose 0` is `1`

---

Well, what if we choose nothing?

## 8 Choose 0

From a premise of `7 choose 0`, if we have one more thing, we have `8 choose 0`

- Now the 8th choice is definitely not chosen, because the we are choosing nothing

$$
0
$$

- Hence from the remaining `7` things, to choose `0` things, there is only `1` way

$$
\dbinom{7}{0} = 1
$$


Thus

$$
\dbinom{8}{0} = 0 + \dbinom{7}{0} = 1
$$


Thus `8 choose 0` is still `1`

$$
\underline{\dbinom{8}{0} = 1}
$$

Although we know that `anything choose 0` is 1, we have gone through this logic to prove that it will continue to be `1` throughout

Such that even `negative integers choose 0`, would equal to `1`

$$
\underline{\dbinom{n}{0}}, \space \text{for} \space n \in \mathbf Z
$$

---

What if we want to choose everything? How can that we explained in this way?

## 8 Choose 8

Let us start from the premise of `7 choose 8`, if we have one more thing, we have `8 choose 8`

Now we have `2` choices for the 8th choice, either it is chosen or it is not:

- If it is chosen

$$
\text{(8th choice chosen), (remaining 7 choices has to choose 7 more)} \longrightarrow \dbinom{1}{1} \space \text{then} \space \dbinom{7}{7} \longrightarrow \dbinom{1}{1} \cdot \dbinom{7}{7}
$$

- If it is not chosen

$$
\text{(8th choice nto chosen), (remaining 7 choices has to choose 8 more)} \longrightarrow \dbinom{1}{0} \space \text{then} \space \dbinom{7}{8} \longrightarrow \dbinom{1}{0} \cdot \dbinom{7}{8}
$$

Thus, for `8 choose 8`, we have

$$
\dbinom{8}{8} = \dbinom{1}{1} \dbinom{7}{7} + \dbinom{1}{0} \dbinom{7}{8}
$$

- We know that $\dbinom{7}{7}$ is `1`, because if we choose everything, there is also only `1` way to do it
- We also know that $\dbinom{7}{8}$ is `0`, because we cannot choose more than what we have

Thus

$$
\begin{align}
    \dbinom{8}{8} &= \dbinom{1}{1} \dbinom{7}{7} + \dbinom{1}{0} \dbinom{7}{8} \\
    & = \dbinom{1}{1} (1) + \dbinom{1}{0} (0) \\
    & = 1(1) + 1(0) \\
    & = 1 \\
\end{align}
$$

We can extend this explanation to any `non-negative integer n`, choose itself, to be equal to `1`.

$$
\underline{\dbinom{n}{n} = 1}, \space \text{for} \space n \in \mathbf{Z}_{\ge 0}
$$

Thus we have explained through this continuation method of how `n choose n equals 1`

---

# Generalised Addition of Choice

Thus, we can generalise the process of increasing the total choices into this, where `n` is the total number of things and we choose `m` items from it

From `n choose m` to `n+1 choose m`, we have:
$$
\dbinom{n}{m} \longrightarrow \dbinom{n+1}{m} = \underline{\dbinom{1}{1} \dbinom{n}{m-1} + \dbinom{1}{0} \dbinom{n}{m}} = \underline{\dbinom{n}{m-1} + \dbinom{n}{m}}
$$

We can thus also generalise for any $\dbinom{n}{m}$ such that

$$
\begin{align}
    \dbinom{n}{m} & = \dbinom{1}{1} \dbinom{n-1}{m-1} + \dbinom{1}{0} \dbinom{n-1}{m} \\
    & = \textcolor{lightgray}{(1)} \dbinom{n-1}{m-1} + \textcolor{lightgray}{(1)} \dbinom{n-1}{m} \\
    & = \dbinom{n-1}{m-1} + \dbinom{n}{m}
\end{align}
$$

Thus from

$$
\boxed{
    \dbinom{n}{m} = \dbinom{1}{1} \dbinom{n-1}{m-1} + \dbinom{1}{0} \dbinom{n-1}{m}
}
$$

Emerges

$$\underline{
    \dbinom{n}{m} = \dbinom{n-1}{m-1} + \dbinom{n-1}{m}
}
$$

# Test the Formula
Lets test this again on the extreme cases

- When n choose 0

$$
\begin{align}
    \dbinom{n}{0} & = \dbinom{1}{1} \dbinom{n-1}{-1} + \dbinom{1}{0} \dbinom{n-1}{0} \\
    & = \dbinom{n-1}{-1} + \dbinom{n-1}{0} \\
    & = 0 + 1 \\
    & = 1
\end{align}
$$

This works!

- When n choose n

$$
\begin{align}
    \dbinom{n}{n} & = \dbinom{1}{1} \dbinom{n-1}{n-1} + \dbinom{1}{0} \dbinom{n-1}{n} \\
    & = \dbinom{n-1}{n-1} + \dbinom{n-1}{n} \\
    & = 1 + 0 \\
    & = 1
\end{align}
$$

This works too!

---

# Conclusion

In conclusion, we start from the action of choosing to generate the tree of combinations

$$
\begin{array}{ccccccc}
    & & & \dbinom{0}{0} = 1 & & & \\
    & & \dbinom{1}{0} = 1 & & \dbinom{1}{1} = 1 & & \\
    & \dbinom{2}{0} = 1 & & \dbinom{2}{1} = 2 & & \dbinom{2}{2} = 1 & \\
    \dbinom{3}{0} = 1 & & \dbinom{3}{1} = 3 & & \dbinom{3}{2} = 3 & & \dbinom{3}{3} = 1 \\
    &&& \vdots &&&
\end{array}
$$

And through the principle of addition

$$
\dbinom{n}{m} \longrightarrow \dbinom{n+1}{m} = \boxed{\dbinom{1}{1} \dbinom{n}{m-1} + \dbinom{1}{0} \dbinom{n}{m}} = \underline{\dbinom{n}{m-1} + \dbinom{n}{m}}
$$

We get the property of the the next number created from the previous the 2 numbers above it added together

- And thus we get the simplified version, known as the pascals triangle

$$
\begin{array}
    & & & & & & 1 & & & & & &\\
    & & & & 1 & & 1 & & & &\\
    & & & 1 & & 2 & & 1 & & &\\
    & & 1 & & 3 & & 3 & & 1 & &\\
    & 1 & & 4 & & 6 & & 4 & & 1 &\\
    1 & & 5 & & 10 & & 10 & & 5 & & 1\\
    &&&&& \vdots &&&&&
\end{array}
$$

---

# Remarks

- The simplified version would have seemed to presuppose `1`
- And thus it would have seemed that addition is the only rule
- But now we know more!

# Total choices

As for each choice it is either `chosen` or `not chosen`, the total choices presents as such

$$
\underbrace{\underline{2} \times \underline{2} \times \underline{2} \times \cdots \times \underline{2}}_{\text{n choices}}
$$

Total choices is thus

$$
\underline{2^{n}}
$$

Thus, this is true

$$
\boxed{
    \dbinom{n}{0} + \dbinom{n}{1} + \dbinom{n}{2} + \dbinom{n}{3} + \cdots + \dbinom{n}{n-1} + \dbinom{n}{n} = 2^{n}
}
$$
