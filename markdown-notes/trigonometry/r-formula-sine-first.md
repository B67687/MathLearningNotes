---
title: "**Sine First**: $\\mathbf{a\\sin(x) \\pm b\\cos(x)}$"
source_notebook: "trigonometry/r-formula-sine-first.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# **Sine First**: $\mathbf{a\sin(x) \pm b\cos(x)}$

## Finding Patterns in Identities

Looking through the different trigonometric identities, we can find by that in the double-angle formula

$$
\sin(A \pm B) = \sin(A)\cos(B) \pm \cos(A)\sin(B)
$$

Its expanded form of

$$
\begin{aligned}
    \textcolor{lightgray}{\sin(A \pm B)}
    &= \sin(A) \textcolor{green}{\cos(B)} \pm \cos(A) \textcolor{blue}{\sin(B)} \\
    &= \textcolor{green}{\cos(B)} \sin(A) \pm \textcolor{blue}{\sin(B)} \cos(A)
\end{aligned}
$$

looks quite similar to:

$$
\boxed{
    \textcolor{green}{a}\sin(x) \pm \textcolor{blue}{b}\cos(x)
}
$$

And has the unifying double-angle form of

$$
\sin(A \pm B)
\textcolor{lightgray}{=}
\textcolor{green}{\cos(B)}
\textcolor{lightgray}{\sin(A)}
\textcolor{lightgray}{\pm}
\textcolor{blue}{\sin(B)}
\textcolor{lightgray}{\cos(A)}
$$

## Matching Variables

To match with $sin(x)$ and $cos(x)$, we can let either let $A = x$ or $B = x$

- I choose to let $A = x$ instead

$$
\sin(x \pm B) = \cos(B)\sin(x) \pm \sin(B)\cos(x)
$$

It may seem that we can match $a$ with $\cos(A)$ and $b$ with $\sin(A)$

$$
\textcolor{green}{a}
\textcolor{lightgray}{\sin(x)}
\textcolor{lightgray}{\pm}
\textcolor{blue}{b}
\textcolor{lightgray}{\cos(x)} =
\textcolor{green}{\cos(B)}
\textcolor{lightgray}{\sin(x)}
\textcolor{lightgray}{\pm}
\textcolor{blue}{\sin(B)}
\textcolor{lightgray}{\cos(x)}
$$

But actually, their ranges do not match.
- $cos(B)$ and $sin(B)$ has the range of $[-1, 1]$
- While both `a` and `b` has the range of $(0, \infty)$

Therefore, we need a coefficient on the double-angle formula to make the expressions matchable.
- We can either have the coefficients individually

$$
\textcolor{gray}{p}
\textcolor{lightgray}{\cos(B)\sin(x)}
\textcolor{lightgray}{\pm}
\textcolor{gray}{q}
\textcolor{lightgray}{\sin(B)\cos(x)}
$$

- Or as we are finding unification, we can have some coefficient $R$ on the unified double-angle form, to distribute across the 2 terms

$$
R\sin(x \pm B) = R\cos(B)\sin(x) \pm R\sin(B)\cos(x)
$$

Now it can have the nice comparison of

$$
\textcolor{green}{a}
\textcolor{lightgray}{\sin(x)}
\textcolor{lightgray}{\pm}
\textcolor{blue}{b}
\textcolor{lightgray}{\cos(x)}
\textcolor{lightgray}{=}
\textcolor{green}{R\cos(B)}
\textcolor{lightgray}{\sin(x)}
\textcolor{lightgray}{\pm}
\textcolor{blue}{R\sin(B)}
\textcolor{lightgray}{\cos(x)}
$$

Therefore, we get 2 equations we can work with:

$$
\begin{align}
    a &= R\cos(B) \\
    b &= R\sin(B)
\end{align}
$$

# Solving for **A** and **R**

We want to solve for $A$ and $R$ such that we can complete the unifying formula.

## Solving for **A**

From the 2 equations, we can find $A$ by combining $\sin$ and $\cos$ into $\tan$:

$$
\frac{b}{a} = \frac{\cancel{R}\sin(B)}{\cancel{R}\cos(B)} = \tan(B).
$$

And then by taking the inverse:

$$
\boxed{
    B = \arctan\left(\frac{b}{a}\right)
}
$$

- For $\arctan$, it actually has an infinite domain, so no restrictions here
- It is not like $\arcsin$ or $\arccos$, where there is an inclusive range
- Or $\text{arcsec}$ and $\text{arccsc}$, where there is an exclusive range
- Also notice we could have used $\cot$ as well in the first place, and then use $\text{arccot}$

$$
\textcolor{lightgray}{
    \boxed{
        B = \text{arccot} \left(\frac{a}{b}\right)
    }
}
$$

- But this is a matter of preference
Now we have $B$, let's find $R$:

## Solving for **R**

Going back to the equations:

$$
a = R\cos(B), \quad b = R\sin(B)
$$

We can notice that $\sin(B)$ and $\cos(B)$ both exist, so we can prepare it to use the Pythagorean identity:

$$
a^2 = R^2\cos^2(B), \quad b^2 = R^2\sin^2(B)
$$

>**Take note here**: Because we have squared the equation, we have introduced another extraneous solution into an otherwise single-solution variable

Add these together:

$$
a^2 + b^2 = R^2\cos^2(B) + R^2\sin^2(B)
$$

Factor out $R^2$

$$
a^2 + b^2 = R^2 \biggr[ \cos^2(B) + \sin^2(B) \biggr]
$$

Using the Pythagorean identity $\cos^2(B) + \sin^2(B) = 1$:

$$
a^2 + b^2 = R^2
$$

Take the square root:

$$
R = \pm\sqrt{a^2 + b^2}
$$

Thus, right now we have:

$$
a\sin(x) \pm b\cos(x) = R\sin(x \pm B)
$$

where:

$$
\boxed{
    B = \arctan\left(\frac{b}{a}\right)
}\quad \quad R = \pm\sqrt{a^2 + b^2}
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
R\sin(x \pm B) \quad  \text{ and } \quad -R\sin(x \pm B)
$$

Zooming in on the second case:

$$
\textcolor{lightgray}{R\sin(x \pm B) \quad  \text{ and }} \quad -R\sin(x \pm B)
$$

We can distribute the negative sign on $\sin$:

$$
-R\sin(x \pm B) = R \cdot -\sin(x \pm B)
$$

Using the trigonometric identity:

$$
-\sin(\theta) = \sin(\theta + \pi)
$$

We can rewrite this as:

$$
R \cdot -\sin(x \pm B) = R \sin(x \pm B + \pi)
$$

$$
R \cdot -\sin(x \pm B) = R \sin(x \pm (B + \pi))
$$

Now notice that $B$ has a period of $\pi$, meaning:

$$
B + \pi \quad \text{is functionally equivalent to} \quad B
$$

And thus

$$
R\cos(B \mp x + \pi) = R\cos(B \mp x).
$$

We have rephrased the form with negative R, into the form with positive R
- Hence, we can always take just the positive part of R

$$
\boxed{
    R = \sqrt{a^2 + b^2}
}
$$

# Final Formula

Thus, the R-formula for $a\sin(x) \pm b\cos(x)$ is:

$$
a\sin(x) \pm b\cos(x) = R\sin(x \pm B)
$$

where:

$$
B = \arctan\left(\frac{b}{a}\right), \quad R = \sqrt{a^2 + b^2}
$$

---
### We can use the same logic to set up $a\cos(x) \pm b\sin(x)$
---
