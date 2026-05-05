---
title: "My Math Learnings"
source_notebook: "calculus/advancements-report-14th-march-2025.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# My Math Learnings

## Lesson 1: Limits and Continuity
- A limit $ \lim_{x \to a} f(x) $ evaluates the value $ f(x) $ approaches as $ x $ nears $ a $.
- If $ f(x) $ is continuous at $ a $ (no jumps or undefined points), $ \lim_{x \to a} f(x) = f(a) $.
- For discontinuities (e.g., $ \frac{0}{0} $), check one-sided limits ($ x \to a^- $, $ x \to a^+ $).
- Example: $ \lim_{z \to 1} \frac{10z - 9 - z^2}{z^2 - 1} = 4 $ (after factoring).
- Strategy: Use values near $ a $ (e.g., 1.01, 0.99) to estimate if discontinuous.

## Lesson 2: One-Sided Limits and Discontinuities
- Limits differ if left ($ x \to a^- $) and right ($ x \to a^+ $) values disagree (e.g., jump at $ x = 0 $ for $ \frac{|x|}{x} $).
- Example: $ \lim_{x \to 0} \frac{|x|}{x} = -1 $ ($ x \to 0^- $), 1 ($ x \to 0^+ $) → limit doesn’t exist.
- Check both sides for asymptotes (e.g., $ \frac{1}{x-2} \to -\infty, \infty $) or oscillations (e.g., $ \sin\left(\frac{1}{x}\right) $).

## Lesson 3: Absolute Value and Trigonometric Limits
- Absolute value (e.g., $ |x - a| $) creates kinks; check both sides at the kink (e.g., $ \lim_{x \to 2} \frac{|x-2|}{x-2} $).
- Trig limits use identities: $ \lim_{x \to 0} \frac{\sin(x)}{x} = 1 $, $ \lim_{x \to 0} \frac{\cos(x)-1}{x} = 0 $.
- Example: $ \lim_{\theta \to 4} \frac{\cos(\theta-4)-1}{2\theta-8} = 0 $ (using substitution $ u = \theta - 4 $).
- Oscillation (e.g., $ \sin\left(\frac{1}{x}\right) $) prevents limits at 0.

## Lesson 4: Pseudopoints and Scale-Dependent Continuity
- Pseudopoint: Tiny interval (e.g., $ |x - a| < 10^{-35} $) where $ f(x) $ is continuous, despite discontinuities outside.
- Limit depends on the pseudopoint: $ \lim_{x \to 0} x $ (for $ |x| < 10^{-35} $) = 0, ignoring outer chaos.
- Physical link: At Planck length ($ 10^{-35} $ m), pseudopoints model continuity in quantum foam.

## Lesson 5: Solving Equations (Squares and Exponentials)
- $ a^2 = b \to |a| = \sqrt{b} $ ($ b \geq 0 $), so $ a = \pm \sqrt{b} $.
- $ a^2 = b^2 \to |a| = |b| $, so $ a = b $ or $ a = -b $.
- One-to-one functions (e.g., $ e^x $, $ x^5 $): If $ f(x) = f(y) $, then $ x = y $.
- Example: $ e^x = e^{2x-1} \to x = 1 $; $ x^5 = (2x-3)^5 \to x = 3 $ (real).

## Lesson 6: Complex Roots and nth Roots
- Fundamental Theorem of Algebra: Degree $ n $ polynomial has $ n $ roots (real/complex).
- Monomial $ z^n = w $: $ z = w^{1/n} e^{2\pi i k / n} $, $ k = 0 $ to $ n-1 $.
- Example: $ z^3 = -8 \to z = 2 e^{i(\pi + 2\pi k)/3} $, $ k = 0,1,2 $.
- General polynomials ($ n \geq 5 $) lack radical formulas (Abel-Ruffini).

## Lesson 7: Non-Functions and Equating
- Non-function: One $ x $ maps to multiple $ y $ (fails vertical line test).
- Examples: Circle ($ x^2 + y^2 = 1 $), Parabola ($ y^2 = x $), Inverse sin ($ x = \sin(y) $).
- Equating trick fails if $ y $-sets overlap (e.g., circle).
- Works for distinct sets (e.g., $ y^2 = x $, $ y = \pm \sqrt{x} $ per $ x $).

## Lesson 8: Domain Specification and Complex Numbers
- Specify domain (real/complex) for solutions: $ x^2 = -1 $ has no real roots, but $ x = \pm i $ (complex).
- Imaginary numbers ($ i = \sqrt{-1} $) extend reals, used in quantum wave equations.
- Example: Specify real roots for $ x^5 = (2x-3)^5 $ gives $ x = 3 $; complex roots need nth root formula.

## Lesson 9: Binomial Linear Conjugates and Complex Conjugates
- Sum or difference of conjugates divided by 2 extracts terms: $ (a + b) + (a - b) = 2a \to a = [(a + b) + (a - b)]/2 $.
- Extended to binomial linear conjugates (e.g., $ (x + y) $ and $ (x - y) $), but for complex conjugates $ z = a + bi $, $ \overline{z} = a - bi $:
  - $ \text{Re}(z) = \frac{z + \overline{z}}{2} $, $ \text{Im}(z) = \frac{z - \overline{z}}{2i} $.
- Nuance: Works for conjugate pairs where the operation (e.g., $ + $ or $ - $) defines the pair; generalizes to linear binomials.

## Lesson 10: Product of Complex Conjugates and Modulus
- Product of complex conjugates: $ z \overline{z} = (a + bi)(a - bi) = a^2 + b^2 = |z|^2 $.
- $ |z| $ is the modulus of $ z $, so the product equals the square of the modulus.
- Neat property: Connects algebraic ($ z \overline{z} $) and geometric ($ |z|^2 $) interpretations.

## Lesson 11: Square Root as a Definition

- Square root $ \sqrt{x} $ (for $ x \geq 0 $) is the non-negative $ y $ where $ y^2 = x $.
- Reason is $ y \geq 0 $ ensures $ \sqrt{x} $ is a function (one output), e.g., $ \sqrt{4} = 2 $, not $ \pm 2 $.
- Solving $ x^2 = 4 $ gives $ x = \pm 2 $, but $ \sqrt{4} = 2 $ by definition.
- Implication:
    - For $|z| \geq |\text{Re}(z)|$,
    - $\sqrt{\text{Re}(z)^2}\ = |\text{Re}(z)|$
    - not $\text{Re}(z)$, due to this rule.

## Lesson 12: Modulus of $ z $ and Conjugate $ \overline{z} $ via Pythagorean Theorem
- Modulus $ |z| = \sqrt{(\text{Re}(z))^2 + (\text{Im}(z))^2} $, same as $ |\overline{z}| = \sqrt{(\text{Re}(z))^2 + (\text{Im}(z))^2} $, by Pythagorean theorem.
- $ z = a + bi $, $ \overline{z} = a - bi $; $ |z| = |\overline{z}| = \sqrt{a^2 + b^2} $ as distances in the complex plane.
- Insight: Reflects geometric symmetry; ties to $ z \overline{z} = |z|^2 $.

## Lesson 13: Modulus Properties of Complex Multiplication
- Property: $ |z_1 z_2| = |z_1| |z_2| $, proven by $ |z_1 z_2|^2 = (z_1 z_2)(\overline{z_1} \overline{z_2}) = |z_1|^2 |z_2|^2 $.
- Intuitive: Magnitudes multiply under complex multiplication (geometric scaling).
- Property: $ |-z| = |z| $, as $ |-z| = \sqrt{(-\text{Re}(z))^2 + (-\text{Im}(z))^2} = \sqrt{(\text{Re}(z))^2 + (\text{Im}(z))^2} = |z| $.
- Note: Not trivial by definition (unlike real $ |-a| = |a| $); follows from modulus symmetry, but pretty trivial once understood.

## Lesson 14: Triangle Inequality for Complex Numbers
- **Property**: $ |z_1 + z_2| \leq |z_1| + |z_2| $, the triangle inequality.
- **Geometric Derivation**: In the complex plane, $ z_1 $ and $ z_2 $ are vectors from $ (0, 0) $ to $ (\text{Re}(z_1), \text{Im}(z_1)) $ and $ (\text{Re}(z_2), \text{Im}(z_2)) $. Adding $ z_1 + z_2 $ gives a vector to $ (\text{Re}(z_1) + \text{Re}(z_2), \text{Im}(z_1) + \text{Im}(z_2)) $. The triangle formed by $ 0 $, $ z_1 $, and $ z_1 + z_2 $ has sides $ |z_1| $, $ |z_2| $, and $ |z_1 + z_2| $. The triangle inequality states $ |z_1 + z_2| \leq |z_1| + |z_2| $, as the direct path is at most the sum of the other two sides.
- **Why the Triangle Inequality Holds**: In Euclidean geometry, the shortest path between two points (e.g., $ 0 $ to $ z_1 + z_2 $) is a straight line ($ |z_1 + z_2| $). The path via $ z_1 $ (length $ |z_1| + |z_2| $) must be at least as long, because a detour cannot be shorter than the direct path.
- **Degenerate Case**: Equality holds when the points are collinear ($ z_2 = k z_1 $, $ k \geq 0 $), forming a degenerate triangle (area = 0). A triangle is formally a set of three points with edges connecting them, including collinear cases for consistency in definitions and to handle limiting cases (e.g., when a triangle’s area approaches 0). While not a "conventional" triangle with area, it’s included as a boundary case, aligning with the user’s insight that it’s about the set of points, not the shape.
- **Alternative Insight**: Drawing a triangle with components $ \text{Re}(z_1) $, $ \text{Re}(z_2) $, $ \text{Im}(z_1) $, $ \text{Im}(z_2) $ suggested a bound, refined to $ |\text{Re}(z_1)| + |\text{Re}(z_2)| + |\text{Im}(z_1)| + |\text{Im}(z_2)| \geq |z_1 + z_2| $, a looser bound than the standard inequality.
- **Example**: $ z_1 = 3 $, $ z_2 = 4i $, $ |z_1 + z_2| = 5 $, $ |z_1| + |z_2| = 7 $, so $ 5 \leq 7 $.

## Lesson 15: Bounding the Modulus with Components
- **Exploration**: $ |\text{Re}(z_1)| + |\text{Re}(z_2)| + |\text{Im}(z_1)| + |\text{Im}(z_2)| \geq |z_1 + z_2| $ is a valid bound.
- **Insight**: Each $ |z_i| \leq |\text{Re}(z_i)| + |\text{Im}(z_i)| $, so their sum bounds $ |z_1 + z_2| $ via the triangle inequality.
- **Connection**: This is a looser bound than $ |z_1| + |z_2| $, but still reflects the geometric idea of summing component magnitudes.
- **Example**: $ z_1 = 1 + i $, $ z_2 = 1 + i $, left side = 4, $ |z_1 + z_2| = 2\sqrt{2} \approx 2.828 $, so $ 4 \geq 2.828 $.
