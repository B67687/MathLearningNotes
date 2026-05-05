---
title: "One-to-one Function Equivalence Relation"
source_notebook: "algebra/general-properties.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

## Properties of Equality

### Reflexive
Anything is equal to itself

$$
a = a
$$

### Symmetric
Order of equivalence is interchangeable

$$
\text{If } a = b, \text{ then } b = a
$$

### Transitive
Equivalence holds true between any object in the equivalence link

$$
a = b \quad \text{ and } \quad b = c
$$

$$
a = c
$$

Hence
$$
a = b = c
$$

### Additive Operations
Adding the same value to both sides of an equation maintains equality

$$
a = b
$$

$$
a + c = b + c
$$

Subtracting the same value from both sides of an equation also maintains equality

$$
a = b
$$

$$
a - c = b - c
$$

### Multiplicative Operation
Multiplying both sides of an equation by the same value maintains equality

$$
a = b
$$

$$
a \cdot c = b \cdot c
$$

Dividing both sides of an equation by the same **non-zero value** also maintains equality

For $a \ne 0$

$$
a = b
$$

$$
\dfrac{a}{c} = \dfrac{b}{c}
$$

### Substitution Property
In any equation or expression, a quantity can be replaced by its equal

$$
\text{If } a = b, \text{ then 'a' can be substituted for 'b' (or 'b' for 'a') in any equation or expression.}
$$

Example
$$ y = 4x $$
$$ 3x + y = 9  $$
Thus
$$ 3x + (4x) = 9  $$
$$ 7x = 9  $$
$$ x = \dfrac{9}{7}  $$

# One-to-one Function Equivalence Relation

This demonstrates the property that for a one-to-one function, if the output for two inputs is the same, then the inputs must also be the same. Mathematically, this is expressed as:

$$
\text{If } f(a) = f(b), \text{ then } a = b
$$

### Positive Example: $y = x^3$

Consider the function $f(x) = x^3$. Let's see if it satisfies the one-to-one property:

$$
\text{Assume } f(a) = f(b)
$$
$$
a^3 = b^3
$$

Taking the cube root of both sides, we get:

$$
\sqrt[3]{a^3} = \sqrt[3]{b^3}
$$
$$
a = b
$$

Since $f(a) = f(b)$ implies $a = b$, the function $y = x^3$ is one-to-one.

### Negative Example: $y = x^2$

Consider the function $f(x) = x^2$. Let's see if it satisfies the one-to-one property:

$$
\text{Assume } f(a) = f(b)
$$
$$
a^2 = b^2
$$

Let's take specific values for $a$ and $b$:

$$
\text{If } a = 2 \text{ and } b = -2
$$

Then,

$$
f(2) = 2^2 = 4
$$
$$
f(-2) = (-2)^2 = 4
$$

Here, we have $f(2) = f(-2)$ (since $4 = 4$), but:

$$
2 \ne -2
$$

Since we found a case where $f(a) = f(b)$ but $a \neq b$, the function $y = x^2$ is not one-to-one.

# Restrictions for Equations and Checking Solutions

-  Whenever we multiply the entire equation by a variable, or we do some operation on both sides of an equation, we are bound to introduce some extra solutions.
-  When encountering a radical, a fraction, an absolute value, trigonometric functions, write down the restrictions and combine them into 1 single restriction so you can check your answers against it.

# Division by Zero

-  Multiplication by 0 will give zero, but division by 0 doesn’t have one defined answer (the answer can be anything. I.e. it can be 1 ,2, 3, …), this inconsistency causes division by zero to remain undefined in its formal definition.

# Solving Equations with Fractions

-  Always assume denominators are non-zero to avoid division by zero, it is defined within the mathematical definition of division to avoid inconsistencies.

# Numerator Comparison - The Cross-Multiplication Trick

-  While solving an algebraic equation, very often we might get 2 fractions equalling each other.

$$ \frac{2x}{x+1} = \frac{2x-1}{x}, \text{ where } x-1, x \neq 0 $$
-  If you don’t understand why we need to have these conditions everytime we solve an equation with fractions, look here

-  To equalise the fractions for easier comparison, while keeping the expressions the same value, we can do this:

$$ \frac{2x}{x+1} \cdot \frac{x}{x} = \frac{2x-1}{x} \cdot \frac{x+1}{x+1} $$
$$ \frac{2x^2}{x(x+1)} = \frac{(2x-1)(x+1)}{x(x+1)} $$

-  Now we can compare just the numerators because in an equation where either the denominators/numerators are equal, and the expressions on both sides are equal, then the numerators/denominators must also be equal

$$ 2x^2 = (2x-1)(x+1) $$

-  So as it seems this is equivalent to just taking the denominator of each side and having the other side multiply by it, while removing the denominators on both sides.
-  This trick is known as cross-multiplication.

$$ \frac{2x}{x+1} = \frac{2x-1}{x} $$

-  …after cross-multiplication

$$ (2x)(x) = (2x-1)(x+1) $$
$$ 2x^2 = (2x-1)(x+1) $$

-  After solving, check that your solution doesn’t violate the axiom of division

-  For example, let’s continue solving:

$$ 2x^2 = 2x^2 + 2x - x - 1 $$
$$ 0 = 2x - x - 1 $$
$$ 0 = x - 1 $$
$$ x = 1 $$

-  Luckily, $x = 1$ does not violate $x-1, x \neq 0$. Therefore, it is a solution!

# Conclusion

-  Now you know why the cross-multiplication trick works, it is because of pattern spotting done on that original process, and optimising it and it happened to be very intuitive.

-  Therefore, cross-multiplication works because of the reasoning behind it, not just by chance.
-  Just always remember this is a trick, not the most direct property of algebraic manipulation


# Common Range Restrictions

## Domain Restrictions

-  Denominator $\neq 0$, (see Division by Zero)
-  Even Radicands $\geq 0$, If even radicand in denominator, Radicand > 0
-  The reason is that odd radicands can be negative because the radicands base can be negative, thus giving negative answers at odd powers. This is untrue for even powers because whatever real value the base is the result will always be positive. Check Positive Range for Even Powers

## Proof that cube root of negative numbers are negative cube roots of their absolute value

-  $\sqrt[3]{-x}$, where x is positive → $\sqrt[3]{-1} \cdot \sqrt[3]{x}$ → $(-1)\sqrt[3]{x}$ → $-\sqrt[3]{x}$

-  Therefore, $\sqrt[3]{-x} = -\sqrt[3]{x}$

## Range Restrictions

-  $x^2 \geq 0$, and by extension any even power

-  $|x| \geq 0$, by definition

-  $b^x > 0$, thus $b^x = p > 0$ in $\log_b{p}$
-  However, $\log_b{p} \in \mathbb{R}$, since any power is possible

-  $-1 \leq \sin(x) \leq 1$  ----- $\sin(x)^{-1} \geq 1$, $\sin(x) \leq 1$
-  $-1 \leq \cos(x) \leq 1$ ----- $\cos(x)^{-1} \geq 1$, $\cos(x) \leq 1$

# Parameters and Variables

-  In something like $y = mx + c$
    -  $m$, $c$ are parameters
    -  $x$, $y$ are the variables

-  Even though in the general sense they are all variables, x,y are variables the whole way through but m, c become constants once they are defined.

# General Notes

-  Whenever requiring to do operations on in both directions, get the required fraction through the first operation and then wont need to recalculate it the second time
-  If the signs of a bracket is positive, then the brackets are ignorable
-  Remember that subtraction is literally for finding the difference. It is easier to find the absolute difference and then add the direction to the difference.

# Identity Definition / General-Equation Properties

-  When we define general equations to represent something such as the distinct rational terms for partial fractions, we are creating an identity. It means this is a general equation, it holds true for all x. This will come to be very helpful when you need to find the value of undefined constant, and you can substitute convenient values of x to remove big bracketed factors to just 1 or 0 depending on your needs

# Triangle Inequality

-  $a + b \geq c$ where c is the longest side, a and b are the other 2 sides of ANY Triangle

# Pythagorean Theorem

-  $a^2 + b^2 = c^2$ where c is the longest side, a and b are the other 2 sides of a Right-Angled Triangle

-  Here is a list of pythagorean triples that’s good to keep in mind
    -  (3, 4, 5)
    -  (5, 12, 13)
    -  (8, 15, 17)
    -  (7, 24, 25)
    -  (9, 40, 41)
    -  (11, 60, 61)
    -  (12, 35, 37)
    -  (13, 84, 85)
    -  (16, 63, 65)
    -  (20, 21, 29)

# Isosceles Triangle Properties

-  NOTE: Equilateral Triangles are also isosceles triangles, they are just isosceles 2 ways
-  In an isosceles triangle, the angle bisector of the vertex angle is the perpendicular bisector of the base.

# Completing the square

$x^2 + ax = \left[x^2 + 2x\left(\frac{a}{2}\right) + \left(\frac{a}{2}\right)^2\right] - \left(\frac{a}{2}\right)^2 = \left(x + \frac{a}{2}\right)^2 - \left(\frac{a}{2}\right)^2$
-  Hence $x^2 + ax = \left(x + \frac{a}{2}\right)^2 - \left(\frac{a}{2}\right)^2$, do the entire expansion if you aren’t COMPLETELY confident why the left equals the right side

-  When collapsing completing the square, read the first term and the sign after it, and then read the last term's base. That would be efficient and mistake-proof.

# Inverses and Reciprocals

-  An Inverse is a general concept where it undoes something.
    -  Addition and Subtraction are perfect inverses
    -  Multiplication and Division are imperfect inverses if taken generally due to inconsistencies of division by 0
    -  Exponential Function, Power Functions to Radicals, Logarithms are imperfect inverses if we take the whole domain and range of those functions, because they don’t match. However, within limited domain and range they can be perfect inverses

-  A Reciprocal is a kind of inverse, a multiplicative inverse, which is basically division by that specific value to which we multiply
    -  If x is the multiple, then the multiplicative inverse, is $\frac{1}{x}$.
    -  $\frac{1}{x}$ is also called the reciprocal of x while x is also called the reciprocal of $\frac{1}{x}$.

# Opposite-sign Solution Pairs

-  When we get something like x=2, then y=-x, we actually get y= 2. Negative sign flips the sign, and for we have to remember to flip the signs in Opposite Sign Pair Notation to preserve this opposite relationship between x and y whenever they are opposites of each other

-  It can also be beneficial to use opposite-sign pairs during calculation to do conjugate calculations together, just remember to flip the signs when necessary.

-  List the solutions using opposite-sign pair notation is not as clear when it is both .
-  It is therefore recommended to just expand out all the solutions when doing so.

# Number of Common Zeros of n Polynomials / Bézout's Theorem

-  The maximum number of common zeros equals the product of the degrees of the polynomials
-  It isn’t exactly that number because of repeated zeros

-  $xy = 4$  (Degree 2)

-  $\frac{x^2}{4} + \frac{y^2}{25} = 1$  (Degree 2)

-  Maximum Number of Common Zeroes=2*2=4

## Refresher

-  The degree of a polynomial is the largest degree among all the terms
-  The degree of a term is found by summing the exponents of all unique variables present in that term

# Parametric Form

-  It is a simplification of parameters by restating every equation in terms of one other parameter allowing one parameter to be substituted into all the relevant equations
