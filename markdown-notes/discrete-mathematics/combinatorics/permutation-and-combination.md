---
title: "To Choose"
source_notebook: "discrete-mathematics/combinatorics/permutation-and-combination.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# To Choose

If we have a thing

$$
\_\_\_
$$

It is either chosen

$$
\underline{a}
$$

Or not chosen

$$
\underline{\textcolor{lightgray}{a}}
$$

# To Choose from A Set of Things

When we have `n` items,

$$
\underbrace{\_ \quad \_ \quad \_ \quad \_ \space \cdots \space \_ \quad \_ \quad \_}_{n}
$$

And we want to choose `m` items out of it

$$
\underbrace{\_ \quad \_ \quad \_ \quad \_ \space}_{m} \cdots \space \_ \quad \_ \quad \_
$$


So how many ways can we choose `m` things from `n` things?

---

When we choose things, we can build our total choices one by one.

- There are `n` ways to choose the `first` item

$$
\underline{n} \quad \_ \quad \_ \space \cdots \space \_ \quad \_ \quad \_
$$

If you need to choose one more
- There is now `1` less way to choose for the next item,

$$
\underline{n}, \space \underline{n-1}, \space \_ \space \cdots \space \_ \quad \_ \quad \_
$$

If you need to choose one more
- There is now `1` less way to choose for the next item,

$$
\underline{n}, \space \underline{n-1}, \space \underline{n-2}, \space \cdots \space \_ \quad \_ \quad \_
$$

We can continue on and on until the maximum number of choices, which is the total choice presented!

$$
\underline{n}, \space \underline{n-1}, \space \underline{n-2}, \space \cdots \space \underline{3}, \space \underline{2}, \space \underline{1}
$$

# Exploring the Edge Cases

#### What if we choose more than the total?
- We cannot choose more than what we have
- The amount of ways to choose more than the total is `0`

#### What if we choose everything `i.e, n`?
- Then there is only `1` way, to choose everything

#### What if we choose nothing?
- There is still only `1` way, because there is only `1` way to get nothing from anything, which is to make the choice then get nothing in return.

#### What if we choose less than no choice?
- We can think of choosing less than nothing as to give that amount to the selection of things to choose from.
- But the premise of choosing is to start from nothing, you cannot give anything if you do not have anything to start off with
- Thus the amount of ways to choose negative things is `0`.

---
#### Thus for any valid choice `non-zero`, the size of the choice must be

$$
0 \le m \le n
$$

---

# How We Choose

Let's find the total ways to choose everything!

Since we have this

$$
\underline{n}, \space \underline{n-1}, \space \underline{n-2}, \cdots , \space \underline{3}, \space \underline{2}, \space \underline{1}
$$

The total ways to choose everything is thus

$$
n \cdot (n-1) \cdot (n-2) \cdots 3 \cdot 2 \cdot 1
$$

We could represent this by the product notation as such

- Ascending Form
$$
\prod_{k=1}^{n} k
$$

- Descending Form
$$
\prod_{k=0}^{n-1}(n-k) \quad \text{or with index adjusted} \quad \prod_{k=1}^{n}(n-k+1)
$$

---

But as this is such a simple operation, a new notation has been invented to describe this patterned operation:

---

The `factorial`, or more specifically the special case of the `falling factorial`, where it falls `n` times
- Falling factorial up to `n` times

$$
n^{\underline{n}}
$$

- Is represented by a exclamation mark

$$
n!
$$

- Such that each term decreases by exactly `1` from the previous term, all the way down to `1`

$$
n! = n \cdot (n-1) \cdot (n-2) \cdots 3 \cdot 2 \cdot 1
$$

---

Thus, to find the total ways to choose m items is to choose the part of the factorial here

$$
\underbrace{\underline{n}, \space \underline{n-1}, \space \underline{n-2}, \cdots}_{m} \cdots , \space \underline{3}, \space \underline{2}, \space \underline{1}
$$


But how do we get that part, `m`, out of `n!`?

# Permutation

We could of course just use the `falling factorial` notation

$$
n^{\underline{m}}
$$

This means we multiply up to `m` terms downwards, one term by one term

---

We can also represent it fully in terms of `!`


Factorials contains other factorials
- This is inherent because of how factorials build upon the previous one

$$
n! = n \times (n-1)!
$$

Thus to get the part `m`

$$
\underbrace{\underline{n}, \space \underline{n-1}, \space \underline{n-2}, \cdots \space \underline{n - m + 1} \space}_{m} \textcolor{lightgray}{\cdots \space \underline{3}, \space \underline{2}, \space \underline{1}}
$$

We can take the total

$$
\underbrace{\underline{n}, \space \underline{n-1}, \space \underline{n-2}, \cdots \space \underline{n - m + 1} \space \cdots \space \underline{3}, \space \underline{2}, \space \underline{1}}_{n}
$$

Remove away the corresponding part, which is `n - m`

$$
\textcolor{lightgray}{\underline{n}, \space \underline{n-1}, \space \underline{n-2}, \cdots \space \underline{n - m + 1} \space} \underbrace{\cdots \space \underline{3}, \space \underline{2}, \space \underline{1}}_{n-m}
$$

This removal involves division instead of substraction because factorials are multiplicative, thus its inverse oepration is division

Thus to choose `m` items from `n` things raw is as such

$$
n \cdot (n-1) \cdot (n-2) \cdots (n - m + 1)
$$

That is like this

$$
\dfrac{
    n \cdot (n-1) \cdot (n-2) \cdots (n - m + 1) (n - m) \cdots 3 \cdot 2 \cdot 1
}{
    (n - m) \cdots 3 \cdot 2 \cdot 1
}
$$

Which simplifies notationally to

$$
\dfrac{n!}{(n-m)!}
$$

Thus

$$
n \cdot (n-1) \cdot (n-2) \cdots (n - m + 1) = \dfrac{n!}{(n-m)!}
$$

Thus! We have found the way to choose `m` items from `n` things!


$$
\text{Choose m items from n things} = \dfrac{n!}{(n-m)!}
$$


This kind of choice where we just choose raw, is called a `Permutation`, meaning total arrangements
- That comes with its notation

$$
{}^n P_m
$$

In conclusion,

$$
\boxed{{}^n P_m = n^{\underline{m}} = \dfrac{n!}{(n-m)!}}
$$

# Combination

In permutations, we chose those number of things raw
- It means that any item can be picked anywhere from the `1st` to the `m-th` place

But what if we do not care for what place the item could be picked from, but instead that it is picked within the `1st` and `m-th` place?

- In other words, we do not care for how many different ways these `m` things can be picked, just that `m` things are picked

---

Thus we need to go back to how many ways `m` things can be `arranged`

When we arrange things, we can consider one thing by one thing

- There are `m` ways to put any item into the 1st slot

$$
\underline{m} \quad \_ \quad \_ \space \cdots \space \_ \quad \_ \quad \_
$$

- And `m-1` ways to put any one of the remaining items into the 2nd slot

$$
\underline{m}, \space \underline{m-1}, \space \_ \space \cdots \space \_ \quad \_ \quad \_
$$

- And `m-2` ways to put any one of the remaining items into the 3rd slot

$$
\underline{m}, \space \underline{m-1},  \space \underline{m-2}, \space \_ \space \cdots \space \_ \quad \_ \quad \_
$$

So on and so forth!
- Thus we realise this actually is an application of choice again!

Where

$$
m! = \underline{m}, \space \underline{m-1}, \space \underline{m-2}, \space \cdots \space \underline{3}, \space \underline{2}, \space \underline{1}
$$

Thus, since we want to remove the duplicate arrangements, we simply divide by the number of ways we can arrange `m` things
- Which is to take the number of permutations and divide by `m!`


$$
\dfrac{1}{m!} \space \space \text{of} \space \space {}^nP_m
$$

Substitute in what that is

$$
\dfrac{1}{m!} \cdot \dfrac{n!}{(n-m)!}
$$

Combine

$$
\dfrac{n!}{m!(n-m)!}
$$

Therefore, we have the combinations of choosing `m` things out of `n` items as:

$$
\boxed{
    {}^nC_m = \dfrac{n^{\underline{m}}}{m!} = \dfrac{n!}{m!(n-m)!}
}
$$

# Conclusion

These are the 2 ways we can choose `m` things from `n` items

---

#### Permutation
- Choose raw `(thus with different arrangements included)`

$$
\boxed{{}^n P_m = n^{\underline{m}} = \dfrac{n!}{(n-m)!}}
$$

#### Combination
- Choose without arrangement

$$
\boxed{
    {}^nC_m = \dfrac{n^{\underline{m}}}{m!} = \dfrac{n!}{m!(n-m)!}
}
$$
