---
title: "Factoring Quadratics"
source_notebook: "algebra/quadratic-slide-and-divide.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Factoring Quadratics

When we need to factor a quadratic equation in the form like

$$
\large{
    x^2 + 2x - 15
}
$$

It can be easily seen that the factors of $15$ that makes $2x$ will be $+5$ and $-3$

$$
\large{
    (x+5)(x-3)
}
$$

But sometimes we get a quadratic formula like

$$
\large{
    6x^2 - 15x + 9
}
$$

Which can be difficult to factor instantly without a little bit of practice or guessing
- Because now we have to pair the possible factors of the amount of $\large{x^2}$ to the possible factors of the **constant** to get the correct combination that will lead to the amount of $\large{x}$

$$
\large{
    (3x - 3)(2x - 3)
}
$$

# Trick

But there is a kind of a trick where you can shift the coefficient of $\large{x^2}$ over to multiply by the constant, and factor for $ax$ instead

$$
\large{
    (6x)^2 - 15(6x) + 54
}
$$

So we have

$$
\large{
    (6x-6)(6x-9)
}
$$

Which simplifies like this

$$
\large{
    2 \cdot (3x-3) \cdot 3 \cdot (2x-3)
}
$$

To this

$$
\large{
    6 \cdot (3x-3)(2x-3)
}
$$

Which we see that changing the equation to be in terms of $\large{ax}$, is equivalent to $\large{a}$ times the original expression

$$
\large{
    6 \cdot (6x^2 - 15x + 9)
}
$$

# Solving for Roots

This trick is especially useful when solving for roots of a quadratic equation where you want to turn it into an easier form to see the factorisation for

$$
\large{
    6x^2 - 15x + 9 = 0
}
$$

$$
\large{
    (6x)^2 - 15(6x) + 9 \cdot 6 = 0
}
$$

$$
\large{
    (6x - 6)(6x + 9) = 0
}
$$

$$
\large{
    6x - 6 = 0 \qquad \text{or} \qquad 6x + 9 = 0
}
$$

$$
\large{
    6x = 6 \qquad \text{or} \qquad 6x = -9
}
$$

$$
\large{
    x = \dfrac{6}{6} \qquad \text{or} \qquad x = \dfrac{-9}{6}
}
$$

$$
\large{
    x = 1 \qquad \text{or} \qquad x = -\dfrac{3}{2}
}
$$

# Why this works

The motivation here is to turn this quadratic formulas that look like this form

$$
\large{
    ax^2 + bx + c, \quad a \ne 1
}
$$

To this form

$$
\large{
    x^2 + bx + c
}
$$

Basically we eliminate the coefficient on the leading term $\large{x^2}$ for easier factorisation

BUT we want to keep the entire expression unchanged

In order to eliminate the coefficient on $\large{x^2}$, we can just take the coefficient and the $\large{x}$ of $\large{x^2}$ together as a new variable

$$
\large{
    (ax)^2 \textcolor{lightgray}{+ bx + c}
}
$$

This expression is different from the original expression, because it is now this

$$
\large{
    a^2 x^2 \textcolor{lightgray}{+ bx + c}
}
$$


So if we want to get to this form while keeping the original expression the same, we have to counteract additional effect of multiplying by $a$ to at the same time dividing by $a$

$$
\large{
    \dfrac{1}{a}(a^2 x^2) \textcolor{lightgray}{+ bx + c}
}
$$

For which we get this

$$
\large{
    \dfrac{1}{a} \cdot (ax)^2 \textcolor{lightgray}{+ bx + c}
}
$$

Now, we want the rest of the variables to be also in terms of $\large{ax}$ too, so we do the balancing correspondingly

$$
\large{
    \dfrac{1}{a} \cdot (ax)^2 + b \cdot \dfrac{1}{a} \cdot ax + c
}
$$

Simplify to get this

$$
\large{
    \dfrac{1}{a} \cdot (ax)^2 + \dfrac{1}{a} \cdot b(ax) + c
}
$$

Since we dont want the leading variable to have a coefficient, and it seems like $\large{c}$ is the only variable missing to do factoring here, we shall do it to $\large{c}$ as well

$$
\large{
    \dfrac{1}{a} \cdot (ax)^2 + \dfrac{1}{a} \cdot b(ax) + \dfrac{1}{a} \cdot ac
}
$$

Then we factor $\dfrac{1}{a}$ out

$$
\large{
    \dfrac{1}{a} \biggr[ (ax)^2 + b(ax) + ac \biggr]
}
$$

This is the equivalent form to the original of $\large{ax^2 + bx + c}$

# Demonstration

Now solving for its roots

$$
\large{
    ax^2 + bx + c = 0
}
$$

Since it it equivalent to this

$$
\large{
    \dfrac{1}{a} \biggr[ (ax)^2 + b(ax) + ac \biggr] = 0
}
$$

By the zero-product property, we have

$$
\large{
    \dfrac{1}{a} = 0 \qquad \text{or} \qquad (ax)^2 + b(ax) + ac = 0
}
$$

Since, $\dfrac{1}{a} = 0$ is impossible, we are left solving for the other side

$$
\large{
    \textcolor{lightgray}{\dfrac{1}{a} = 0} \space \text{(rej. because impossible)}\qquad \text{or} \qquad (ax)^2 + b(ax) + ac = 0
}
$$

So we are left with basically solving this to find the roots of $\large{ax^2 + bx + c}$

$$
\large{
    (ax)^2 + b(ax) + ac = 0
}
$$
> Notice this form is equivalent to moving $\large{a}$ over to multiply by $\large{c}$ then turning the variables from $\large{x}$ to $\large{ax}$

Once we find the roots of $\large{ax}$ through factorisation, lets say $\large{q_1}$ and $\large{q_2}$

$$
\vdots
$$

$$
\large{
    ax = r_1 \qquad \text{or} \qquad ax = r_2
}
$$

We get

$$
\large{
    x = \dfrac{r_1}{a} \qquad \text{or} \qquad x = \dfrac{r_2}{a}
}
$$

# Summary

Thus for any quadratic in the form

$$
\large{
    ax^2 + bx + c
}
$$

For which we want to make into

$$
\large{
    (x\prime) ^2 + b(x\prime) + c\prime
}
$$
> So its easier to factorise and find the roots for

We simply multiply $\large{c}$ by $\large{a}$, and change the variables to solve for $ax$


$$
\large{
    (ax)^2 + b(ax) + ac
}
$$

Once we accomplish the factorisation, we will get the form of

$$
\large{
    ax = r_1 \qquad \text{or} \qquad ax = r_2
}
$$

And easily solve for x

$$
\large{
    x = \dfrac{r_1}{a} \qquad \text{or} \qquad x = \dfrac{r_2}{a}
}
$$

# Re-demonstration

$$
\large{
    6x^2 - 15x + 9 = 0
}
$$

$$
\large{
    (6x)^2 - 15(6x) + 9 \cdot 6 = 0
}
$$

$$
\large{
    (6x - 6)(6x + 9) = 0
}
$$

$$
\large{
    6x - 6 = 0 \qquad \text{or} \qquad 6x + 9 = 0
}
$$

$$
\large{
    6x = 6 \qquad \text{or} \qquad 6x = -9
}
$$

$$
\large{
    x = \dfrac{6}{6} \qquad \text{or} \qquad x = \dfrac{-9}{6}
}
$$

$$
\large{
    x = 1 \qquad \text{or} \qquad x = -\dfrac{3}{2}
}
$$

# Another Demonstration
$$
\large{
    8x^2 + 10x - 3 = 0
}
$$

$$
\large{
    (8x)^2 + 10(8x) - 3 \cdot 8 = 0
}
$$

$$
\large{
    (8x)^2 + 10(8x) - 24 = 0
}
$$

$$
\large{
    (8x + 12)(8x - 2) = 0
}
$$

$$
\large{
    8x + 12 = 0 \qquad \text{or} \qquad 8x - 2 = 0
}
$$

$$
\large{
    8x = -12 \qquad \text{or} \qquad 8x = 2
}
$$

$$
\large{
    x = \dfrac{-12}{8} \qquad \text{or} \qquad x = \dfrac{2}{8}
}
$$

$$
\large{
    x = -\dfrac{3}{2} \qquad \text{or} \qquad x = \dfrac{1}{4}
}
$$
