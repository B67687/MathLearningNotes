---
title: "Difference Quotient"
source_notebook: "calculus/derivative-proofs.ipynb"
archived_notebook: "archive/notebooks/calculus/derivative-proofs.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Difference Quotient

$$
\boxed{
    \phantom{\Biggr(}
        \dfrac{f(x+h)-f(x)}{h}
    \phantom{\Biggr)}
}
$$

# Derivative

$$
\boxed{
    \phantom{\Biggr(}
        \dfrac{d}{dx} f(x) = \lim_{h \to 0} \dfrac{f(x+h)-f(x)}{h} = f'
    \phantom{\Biggr)}
}
$$

# Constant Derivative
$$
\boxed{
    \phantom{\biggr(}
        \frac{d}{dx} \big[ \space c \space \big] = 0
    \phantom{\biggr)}
}
$$

$
\textbf{Proof:}
$
$$
\begin{align*}
    f'(x) &= \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} \\
    &= \lim_{h \to 0} \frac{c - c}{h} \\
    &= \lim_{h \to 0} \frac{0}{h} \\
    &= 0
\end{align*}
$$

# Power Derivative

$$
\boxed{
    \phantom{\biggr(}
        \frac{d}{dx} x^n = n x^{n-1}
    \phantom{\biggr)}
}
$$

$
\textbf{Proof:}
$

$$
f(x) = x^n
$$

$$
f'(x) = \lim_{h \to 0} \dfrac{(x+h)^n - x^n}{h}
$$


Focusing on

$$
\textcolor{lightgray}{f'(x) = \lim_{h \to 0}} \dfrac{(x+h)^n - x^n}{h}
$$

We get

$$
\dfrac{(x^n + n x^{n-1} h + \cdots + h^n) - x^n}{h}
$$

$$
\dfrac{\cancel{x^n} + n x^{n-1} h + \cdots + h^n - \cancel{x^n}}{h}
$$

$$
\dfrac{n x^{n-1} h + n x^{n-2} h^2 +\cdots + h^n}{h}
$$

$$
\dfrac{n x^{n-1} \cancel{h}}{\cancel{h}} + \dfrac{n x^{n-2} h \cdot \cancel{h}}{\cancel{h}} +\cdots + \dfrac{h^{n-1} \cdot \cancel{h}}{{\cancel{h}}}
$$

$$
n x^{n-1} + nx^{n-2} h + nx^{n-3} h^2 + \cdots + h^{n-1}
$$

Thus,

$$
f'(x) = \lim_{h \to 0} \biggr( \space n x^{n-1} + nx^{n-2} h + nx^{n-3} h^2 + \cdots + h^{n-1} \biggr)
$$

As h tends to 0, all the terms with h tend to 0:

$$
nx^{n-1} + \cancel{n x^{n-2} h} + \cancel{n x^{n-3} h^2} + \cdots + \cancel{h^{n-1}}
$$

Leaving us with:

$$
nx^{n-1}
$$

# Product Derivative

$$
\boxed{
    \phantom{\Biggr(}
        (fg)' = f'g + fg'
    \phantom{\Biggr)}
}
$$

$
\textbf{Proof:}
$

$$
(fg)' = \lim_{h \to 0} \dfrac{f(x+h)g(x+h)-f(x)g(x)}{h}
$$

Focusing on

$$
\textcolor{lightgray}{(fg)' =} \lim_{h \to 0} \dfrac{f(x+h)g(x+h)-f(x)g(x)}{h}
$$

> We want to express it in a form we can understand, which is the **difference quotient**

So we can do that by trying to introduce terms that contain parts of both expressions, so that we can factor out on both sides
> Making sure that the expression still stays the same, we need to do **opposite operations**
>
> Lets say $f(x+h)g(x)$

$$
\lim_{h \to 0} \dfrac{f(x+h)g(x+h) - \boxed{ \phantom{\big(} f(x+h)g(x) \phantom{\big)}} + \boxed{ \phantom{\big(} f(x+h)g(x) \phantom{\big(}} - f(x)g(x)}{h}
$$

> Note that this will also work with $f(x)g(x+h)$

Then we split it

$$
\lim_{h \to 0} \dfrac{f(x+h)g(x+h) - f(x+h)g(x)}{h} + \lim_{h \to 0} \dfrac{f(x+h)g(x) - f(x)g(x)}{h}
$$

And take out the factors

$$
\lim_{h \to 0} f(x+h) \dfrac{g(x+h) - g(x)}{h} + \lim_{h \to 0} g(x) \dfrac{f(x+h) - f(x)}{h}
$$

Then we distribute the limit

$$
\Biggr( \lim_{h \to 0} f(x+h) \Biggr) \Biggr( \lim_{h \to 0} \dfrac{g(x+h) - g(x)}{h} \Biggr) + \Biggr( \lim_{h \to 0} g(x) \Biggr) \Biggr( \lim_{h \to 0} \dfrac{f(x+h) - f(x)}{h} \Biggr)
$$

Which we can easily evaluate as

$$
f(x) g'(x) + g(x) f'(x)
$$

Which we can write simply as

$$
fg' + f'g
$$

Or if we want the term with `f derivative` to come first

$$
f'g + fg'
$$

# Quotient Derivative

$$
\boxed{
    \phantom{\Biggr(}
    \biggr( \dfrac{f}{g} \biggr) ^\prime = \dfrac{f'g - fg'}{g^2}
    \phantom{\Biggr)}
}
$$

$
\textbf{Proof:}
$

$$
\frac{d}{dx} \dfrac{f(x)}{g(x)} = \lim_{h \to 0} \dfrac{\dfrac{f(x+h)}{g(x+h)}-\dfrac{f(x)}{g(x)}}{h}
$$

Focusing on

$$
\textcolor{lightgray}{\frac{d}{dx} \dfrac{f(x)}{g(x)} = } \lim_{h \to 0} \dfrac{\dfrac{f(x+h)}{g(x+h)}-\dfrac{f(x)}{g(x)}}{h}
$$

Simplify it

$$
\lim_{h \to 0} \dfrac{1}{h} \Biggr( \dfrac{f(x+h)}{g(x+h)}-\dfrac{f(x)}{g(x)} \Biggr)
$$

Turn that into one fraction

$$
\lim_{h \to 0} \Biggr( \dfrac{1}{h} \cdot \dfrac{f(x+h)g(x)-f(x)g(x+h)}{g(x)g(x+h)} \Biggr)
$$

Realise we are quite close to the form where we can get `difference quotients`
> Now we just exchange the denominators

$$
\lim_{h \to 0} \Biggr( \dfrac{1}{g(x)g(x+h)} \cdot \dfrac{f(x+h)g(x)-f(x)g(x+h)}{h} \Biggr)
$$

Share the limit

$$
\Biggr( \lim_{h \to 0} \dfrac{1}{g(x)g(x+h)} \Biggr) \Biggr( \lim_{h \to 0} \dfrac{f(x+h)g(x)-f(x)g(x+h)}{h} \Biggr)
$$

Evaluate the simpler one

$$
\dfrac{1}{g(x)g(x)} \Biggr( \lim_{h \to 0} \dfrac{f(x+h)g(x)-f(x)g(x+h)}{h} \Biggr)
$$

Simplify

$$
\dfrac{1}{g^2} \lim_{h \to 0} \dfrac{f(x+h)g(x)-f(x)g(x+h)}{h}
$$

Lets focus on this part

$$
\textcolor{lightgray}{\dfrac{1}{g^2}} \lim_{h \to 0} \dfrac{f(x+h)g(x)-f(x)g(x+h)}{h}
$$

> Similar to how we did derived the product rule, we want to express it in a form we can understand, which is the **difference quotient**

So we can do that by trying to introduce terms that contain parts of both expressions, so that we can factor out on both sides
> Making sure that the expression still stays the same, we need to do **opposite operations**
>
> Lets say $f(x)g(x)$

$$
\lim_{h \to 0} \dfrac{f(x+h)g(x) - \boxed{ \phantom{\big(} f(x)g(x) \phantom{\big(}} + \boxed{ \phantom{\big(} f(x)g(x) \phantom{\big)}} - f(x)g(x+h)}{h}
$$

> Note that this will also work with $f(x+h)g(x+h)$

Then we split it

$$
\lim_{h \to 0} \dfrac{f(x+h)g(x) - f(x)g(x)}{h} + \lim_{h \to 0} \dfrac{f(x)g(x) - f(x)g(x+h)}{h}
$$

And take out the factors

$$
\lim_{h \to 0} \Biggr( g(x) \dfrac{f(x+h) - f(x)}{h} \Biggr) + \lim_{h \to 0} \Biggr( f(x) \dfrac{g(x) - g(x+h)}{h} \Biggr)
$$

And switch the second expression into a `difference quotient` through `negation`

$$
\lim_{h \to 0} \Biggr( g(x) \dfrac{f(x+h) - f(x)}{h} \Biggr) - \lim_{h \to 0} \Biggr( f(x) \dfrac{g(x+h)- g(x)}{h} \Biggr)
$$

Then we split it by `limits`

$$
\Biggr( \lim_{h \to 0} g(x) \Biggr) \Biggr( \lim_{h \to 0} \dfrac{f(x+h) - f(x)}{h} \Biggr) - \Biggr( \lim_{h \to 0} f(x) \Biggr) \Biggr( \lim_{h \to 0} \dfrac{g(x+h)- g(x)}{h} \Biggr)
$$

Which we can easily evaluate as

$$
gf' - fg'
$$

And if we want to standardise `f` to be the first `variable`

$$
f'g - fg'
$$

Now we sub this back to this

$$
\dfrac{1}{g^2} \textcolor{lightgray}{ \lim_{h \to 0} \dfrac{f(x+h)g(x)-f(x)g(x+h)}{h}}
$$

To get

$$
\dfrac{1}{g^2} \Biggr( f'g - fg' \Biggr)
$$

And thus we get

$$
\dfrac{f'g - fg'}{g^2}
$$
