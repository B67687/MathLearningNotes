---
title: "Proof of the R-Formula"
source_notebook: "trigonometry/r-formula-cosine-first.ipynb"
archived_notebook: "archive/notebooks/trigonometry/r-formula-cosine-first.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Proof of the R-Formula

The main goal is to find a unifying expression for

$$
a\sin(x) \pm b\cos(x)
$$

And

$$
a\cos(x) \pm b\sin(x)
$$

where
$$
a > 0 \quad \text{and} \quad b > 0
$$

# **Cosine First**: $\mathbf{a\cos(x) \pm b\sin(x)}$


## Finding Patterns in Identities

Looking through the different trigonometric identities, we can find by that in the double-angle formula

$$
\cos(A \mp B) =
\cos(A)\cos(B) \pm \sin(A)\sin(B)
$$

Its expanded form of

$$
\textcolor{lightgray}{\cos(A \mp B)}
\textcolor{lightgray}{=}
\textcolor{green}{\cos(A)}
\cos(B)
\pm
\textcolor{blue}{\sin(A)}
\sin(B)
$$

looks quite similar to:

$$
\boxed{
    \textcolor{green}{a}\cos(x) \pm \textcolor{blue}{b}\sin(x)
}
$$

And has the unifying double-angle form of

$$
\cos(A \mp B) =
\textcolor{green}{\cos(A)}
\textcolor{lightgray}{\cos(B)}
\textcolor{lightgray}{\pm}
\textcolor{blue}{\sin(A)}
\textcolor{lightgray}{\sin(B)}
$$

## Matching Variables

To match with $cos(x)$, we can let either let $A = x$ or $B = x$

- I choose to let $B = x$

$$
\cos(A \mp x) = \cos(A)\cos(x) \pm \sin(A)\sin(x)
$$

It may seem that we can match $a$ with $\cos(A)$ and $b$ with $\sin(A)$

$$
\textcolor{green}{a}
\textcolor{lightgray}{\cos(x)}
\textcolor{lightgray}{\pm}
\textcolor{blue}{b}
\textcolor{lightgray}{\sin(x)}
\textcolor{lightgray}{=}
\textcolor{green}{\cos(A)}
\textcolor{lightgray}{\cos(x)}
\textcolor{lightgray}{\pm}
\textcolor{blue}{\sin(A)}
\textcolor{lightgray}{\sin(x)}
$$

But actually, their ranges do not match.
- $sin(A)$ and $cos(A)$ has the range of $[-1, 1]$
- While both `a` and `b` has the range of $(0, \infty)$

Therefore, we need a coefficient on the double-angle formula to make the expressions matchable.
- We can either have the coefficients individually

$$
\textcolor{gray}{p}
\textcolor{lightgray}{\cos(A)\cos(x)}
\textcolor{lightgray}{\pm}
\textcolor{gray}{q}
\textcolor{lightgray}{\sin(A)\sin(x)}
$$

- Or as we are finding unification, we can have some coefficient $R$ on the unified double-angle form, to distribute across the 2 terms

$$
R\cos(A \mp x) = R\cos(A)\cos(x) \pm R\sin(A)\sin(x)
$$

Now it can have the nice comparison of

$$
\textcolor{green}{a}
\textcolor{lightgray}{\cos(x)}
\textcolor{lightgray}{\pm}
\textcolor{blue}{b}
\textcolor{lightgray}{\sin(x)}
\textcolor{lightgray}{=}
\textcolor{green}{R\cos(A)}
\textcolor{lightgray}{\cos(x)}
\textcolor{lightgray}{\pm}
\textcolor{blue}{R\sin(A)}
\textcolor{lightgray}{\sin(x)}
$$

Therefore, we get 2 equations we can work with:

$$
\begin{align}
    a &= R\cos(A) \\
    b &= R\sin(A)
\end{align}
$$

# Solving for **A** and **R**

We want to solve for $A$ and $R$ such that we can complete the unifying formula.


## Solving for **A**

From the 2 equations, we can find $A$ by combining $\sin$ and $\cos$ into $\tan$:

$$
\frac{b}{a} = \frac{\cancel{R}\sin(A)}{\cancel{R}\cos(A)} = \tan(A).
$$

And then by taking the inverse:

$$
\boxed{
    A = \arctan\left(\frac{b}{a}\right)
}
$$

- For $\arctan$, it actually has an infinite domain, so no restrictions here
- It is not like $\arcsin$ or $\arccos$, where there is an inclusive domain
- Or $\text{arcsec}$ and $\text{arccsc}$, where there is an exclusive domain
- Also notice we could have used $\cot$ as well in the first place, and then use $\text{arccot}$

$$
\textcolor{lightgray}{
    \boxed{
        A = \text{arccot} \left(\frac{a}{b}\right)
    }
}
$$

- But this is a matter of preference

Now we have $A$, let's find $R$:

## Solving for **R**

Going back to the equations:

$$
a = R\cos(A), \quad b = R\sin(A)
$$

We can notice that $\sin(A)$ and $\cos(A)$ both exist, so we can prepare it to use the Pythagorean identity:

$$
a^2 = R^2\cos^2(A),
\quad
b^2 = R^2\sin^2(A)
$$

> **Take note here**: Because we have squared the equation, we have introduced another extraneous solution into an otherwise single-solution variable


Add these together:

$$
a^2 + b^2 = R^2\cos^2(A) + R^2\sin^2(A)
$$

Factor out $R^2$

$$
a^2 + b^2 = R^2 \biggr[ \cos^2(A) + \sin^2(A) \biggr]
$$

Using the Pythagorean identity $\cos^2(A) + \sin^2(A) = 1$:

$$
a^2 + b^2 = R^2
$$

Take the square root:

$$
R = \pm\sqrt{a^2 + b^2}
$$

Thus, right now we have:

$$
a\sin(x) \pm b\cos(x) =
R\cos(A \mp x)
$$

where:

$$
\boxed{
    A = \arctan\left(\frac{b}{a}\right)
}
\quad \quad
R = \pm\sqrt{a^2 + b^2}
$$

# Are There Restrictions Before $R^2 = a^2 + b^2$?

Before the step $R^2 = a^2 + b^2$, there is no inherent restriction that forces $R$ to be positive. The square root function $\sqrt{a^2 + b^2}$ is defined as the **non-negative root**, but the $\pm$ arises because squaring both sides of an equation introduces an inherent ambiguity.

# Resolving the Ambiguity in $R$

Notice that we still have ambiguity at $R$, where we can only choose one answer or the other. But let’s dig further:

$$
R = \pm\sqrt{a^2 + b^2}.
$$

Substituting both cases into our unified equation, we get:

$$
R\cos(A \mp x) \quad  \text{ and } \quad -R\cos(A \mp x).
$$

Zooming in on the second case, we can distribute the negative sign on $\cos$:

$$
-R\cos(A \mp x) = R \cdot -\cos(A \mp x)
$$

Using the trigonometric identity:

$$
-\cos(\theta) = \cos(\theta + \pi)
$$

We can rewrite this as:

$$
R \cdot -\cos(A \mp x) = R \cos(A \mp x + \pi).
$$

$$
R \cdot -\cos(A \mp x) = R \cos((A + \pi) \mp x).
$$

Now notice that $A$ has a period of $\pi$, meaning:

$$
A + \pi \quad \text{is functionally equivalent to} \quad A.
$$

And thus

$$
R\cos(A \mp x + \pi) = R\cos(A \mp x).
$$

We have rephrased the form with negative R, into the form with positive R
- Hence, we can always take just the positive part of R

$$
\boxed{
    R = \sqrt{a^2 + b^2}
}
$$

# Final Formula

Thus, the R-formula for $a\cos(x) \pm b\sin(x)$ is:

$$
a\cos(x) \pm b\sin(x) = R\cos(A \mp x)
$$

where:

$$
A = \arctan\left(\frac{b}{a}\right), \quad R = \sqrt{a^2 + b^2}
$$

---
### We can use the same logic to set up $a\sin(x) \pm b\cos(x)$
---
