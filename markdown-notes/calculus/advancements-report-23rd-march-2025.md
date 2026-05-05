---
title: "Finding Derivatives Using the Limit Definition"
source_notebook: "calculus/advancements-report-23rd-march-2025.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Finding Derivatives Using the Limit Definition

This notebook demonstrates how to find derivatives of functions using the limit definition.

## Limit Definition of a Derivative

The derivative of a function $f(x)$ is defined as:

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

We'll work through a few examples to illustrate the process.

### $f(x) = x^2$

1.  **Apply the limit definition:**

    $$f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h}$$

2.  **Expand the expression:**

    $$f'(x) = \lim_{h \to 0} \frac{x^2 + 2xh + h^2 - x^2}{h}$$

3.  **Simplify:**

    $$f'(x) = \lim_{h \to 0} \frac{2xh + h^2}{h}$$

4.  **Factor out $h$:**

    $$f'(x) = \lim_{h \to 0} \frac{h(2x + h)}{h}$$

5.  **Cancel $h$:**

    $$f'(x) = \lim_{h \to 0} (2x + h)$$

6.  **Evaluate the limit:**

    $$f'(x) = 2x$$

---

### $f(x) = \frac{1}{x}$

1.  **Apply the limit definition:**

    $$f'(x) = \lim_{h \to 0} \frac{\frac{1}{x + h} - \frac{1}{x}}{h}$$

2.  **Find a common denominator in the numerator:**

    $$f'(x) = \lim_{h \to 0} \frac{\frac{x - (x + h)}{x(x + h)}}{h}$$

3.  **Simplify the numerator:**

    $$f'(x) = \lim_{h \to 0} \frac{\frac{-h}{x(x + h)}}{h}$$

4.  **Rewrite the expression:**

    $$f'(x) = \lim_{h \to 0} \frac{-h}{h x(x + h)}$$

5.  **Cancel $h$:**

    $$f'(x) = \lim_{h \to 0} \frac{-1}{x(x + h)}$$

6.  **Evaluate the limit:**

    $$f'(x) = \frac{-1}{x^2}$$

---

### $f(x) = \sqrt{x}$

1.  **Apply the limit definition:**

    $$f'(x) = \lim_{h \to 0} \frac{\sqrt{x + h} - \sqrt{x}}{h}$$

2.  **Rationalize the numerator by multiplying by the conjugate:**

    $$f'(x) = \lim_{h \to 0} \frac{(\sqrt{x + h} - \sqrt{x})(\sqrt{x + h} + \sqrt{x})}{h(\sqrt{x + h} + \sqrt{x})}$$

3.  **Simplify the numerator using the difference of squares:**

    $$f'(x) = \lim_{h \to 0} \frac{(x + h) - x}{h(\sqrt{x + h} + \sqrt{x})}$$

4.  **Simplify further:**

    $$f'(x) = \lim_{h \to 0} \frac{h}{h(\sqrt{x + h} + \sqrt{x})}$$

5.  **Cancel $h$:**

    $$f'(x) = \lim_{h \to 0} \frac{1}{\sqrt{x + h} + \sqrt{x}}$$

6.  **Evaluate the limit:**

    $$f'(x) = \frac{1}{2\sqrt{x}}$$

---

## $ f(x) = x + \sqrt x $

**1. Derivative Definition:**

-   The derivative of a function $f(x)$ is defined as:
    $$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

**2. Applying the Definition to f(x) = x + √x:**

-   We found $f(x + h) = (x + h) + \sqrt{x + h}$.
-   Plugging into the derivative definition:
    $$f'(x) = \lim_{h \to 0} \frac{[(x + h) + \sqrt{x + h}] - [x + \sqrt{x}]}{h}$$

**3. Simplifying the Expression:**

-   Simplifying the numerator:
    $$f'(x) = \lim_{h \to 0} \frac{h + \sqrt{x + h} - \sqrt{x}}{h}$$

**4. Separating the Limit:**

-   We separated the limit into two parts:
    $$f'(x) = \lim_{h \to 0} \frac{h}{h} + \lim_{h \to 0} \frac{\sqrt{x + h} - \sqrt{x}}{h}$$
-   The first limit is 1:
    $$f'(x) = 1 + \lim_{h \to 0} \frac{\sqrt{x + h} - \sqrt{x}}{h}$$

**5. Rationalizing the Numerator:**

-   We rationalized the numerator of the second limit:
    $$f'(x) = 1 + \lim_{h \to 0} \frac{(\sqrt{x + h} - \sqrt{x})(\sqrt{x + h} + \sqrt{x})}{h(\sqrt{x + h} + \sqrt{x})}$$
    $$f'(x) = 1 + \lim_{h \to 0} \frac{h}{h(\sqrt{x + h} + \sqrt{x})}$$

**6. Canceling h and Evaluating the Limit:**

-   Canceling $h$ and substituting $h = 0$:
    $$f'(x) = 1 + \frac{1}{2\sqrt{x}}$$

**7. Key Learnings:**

-   Separating the limit into parts can be a useful technique when dealing with complex expressions.
-   Rationalization is a powerful tool for simplifying expressions with radicals, but it must be applied strategically.
-   Rationalization to remove the h can only happen in some circumstances, and we must either make the circumstances or see that we can utilize it.
-   In this case, separating the fraction before rationalizing allowed us to simplify the limit effectively.

---

## $ g(x) = \frac{4}{\sqrt{1 - x}} $

This notebook cell demonstrates how to find the derivative of $g(x) = \frac{4}{\sqrt{1 - x}}$ using the definition of the derivative.

**1. Definition of the Derivative:**

-   The derivative of a function $g(x)$ is defined as:
    $$g'(x) = \lim_{h \to 0} \frac{g(x + h) - g(x)}{h}$$

**2. Applying the Definition:**

-   Given $g(x) = \frac{4}{\sqrt{1 - x}}$, we find $g(x + h)$:
    $$g(x + h) = \frac{4}{\sqrt{1 - (x + h)}}$$
-   Plugging $g(x + h)$ and $g(x)$ into the derivative definition:
    $$g'(x) = \lim_{h \to 0} \frac{\frac{4}{\sqrt{1 - (x + h)}} - \frac{4}{\sqrt{1 - x}}}{h}$$

**3. Simplifying the Numerator:**

-   Finding a common denominator for the fractions in the numerator:
    $$g'(x) = \lim_{h \to 0} \frac{\frac{4\sqrt{1 - x} - 4\sqrt{1 - (x + h)}}{\sqrt{1 - (x + h)} \sqrt{1 - x}}}{h}$$
    $$g'(x) = \lim_{h \to 0} \frac{4(\sqrt{1 - x} - \sqrt{1 - x - h})}{h \sqrt{1 - (x + h)} \sqrt{1 - x}}$$

**4. Rationalizing the Numerator:**

-   Multiplying by the conjugate to rationalize the numerator:
    $$g'(x) = \lim_{h \to 0} \frac{4(\sqrt{1 - x} - \sqrt{1 - x - h})}{h \sqrt{1 - (x + h)} \sqrt{1 - x}} \cdot \frac{\sqrt{1 - x} + \sqrt{1 - x - h}}{\sqrt{1 - x} + \sqrt{1 - x - h}}$$
    $$g'(x) = \lim_{h \to 0} \frac{4[(1 - x) - (1 - x - h)]}{h \sqrt{1 - (x + h)} \sqrt{1 - x} (\sqrt{1 - x} + \sqrt{1 - x - h})}$$
    $$g'(x) = \lim_{h \to 0} \frac{4h}{h \sqrt{1 - (x + h)} \sqrt{1 - x} (\sqrt{1 - x} + \sqrt{1 - x - h})}$$

**5. Canceling h and Evaluating the Limit:**

-   Canceling the $h$ terms:
    $$g'(x) = \lim_{h \to 0} \frac{4}{\sqrt{1 - (x + h)} \sqrt{1 - x} (\sqrt{1 - x} + \sqrt{1 - x - h})}$$
-   Substituting $h = 0$:
    $$g'(x) = \frac{4}{\sqrt{1 - x} \sqrt{1 - x} (\sqrt{1 - x} + \sqrt{1 - x})}$$
    $$g'(x) = \frac{4}{(1 - x) (2\sqrt{1 - x})}$$
    $$g'(x) = \frac{2}{(1 - x)^{3/2}}$$

**Conclusion:**

-   The derivative of $g(x) = \frac{4}{\sqrt{1 - x}}$ is:
    $$g'(x) = \frac{2}{(1 - x)^{3/2}}$$

---

## Conclusion

These examples demonstrate how to find derivatives using the limit definition. The key is to manipulate the expression to eliminate the $h$ in the denominator before evaluating the limit.

---

# Derivatives and Limits: A Deeper Dive

This notebook expands on our understanding of derivatives and their relationship to limits, building on the previous concepts.

### Derivative as a Special Limit
-   The derivative of a function $f(x)$ at a point $x = a$ is defined as:
        $$f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$$
-   This is a specific type of limit that measures the *instantaneous rate of change* or the slope of the tangent line.

### Limit of the Slope vs. Derivative Function

-   The limit of the slope (the limit of the difference quotient) can approach infinity.
-   However, the derivative $f'(x)$ is itself a function.
-   Functions must have real number outputs for real number inputs.
-   Infinity is not a real number.
-   Therefore, the derivative function $f'(x)$ is undefined (or "does not exist") at points where the limit of the slope is infinite.
-   Example: $f(x) = x^{2/3}$ at $x = 0$. The limit of the slope is infinite, but the derivative function does not exist.

### One-Sided Limits and Derivatives
-   When dealing with functions like $f(x) = |x|$, we must consider one-sided limits to determine if the derivative exists.
-   If the left-hand limit ($\lim_{h \to 0^-}$) and the right-hand limit ($\lim_{h \to 0^+}$) are different, the general limit does not exist, and therefore the derivative does not exist.

#### Example: Derivative of f(x) = |x| at x = 0
-   The derivative of $f(x) = |x|$ at $x = 0$ does not exist.
-   This is because the one-sided limits are:
    -   $\lim_{h \to 0^-} \frac{|h|}{h} = -1$
    -   $\lim_{h \to 0^+} \frac{|h|}{h} = 1$
-   Since $-1 \neq 1$, the limit $\lim_{h \to 0} \frac{|h|}{h}$ does not exist, and thus $f'(0)$ does not exist.

### General Limits vs. Derivative Limits
-   General limits (e.g., $\lim_{x \to a} f(x)$) describe the behavior of a function near a point.
-   Derivative limits specifically measure the rate of change.
-   The existence of a general limit does not guarantee the existence of a derivative.
-   However, if the derivative exists, the limit defining it *must* exist.
-   Conversely, if the limit that defines the derivative doesn't exist, the derivative doesn't exist.

### Limits at Infinity (Plateau Limits)
-   These limits (e.g., $\lim_{x \to \infty} f(x)$) describe the long-term behavior of a function.
-   They reveal horizontal asymptotes or "plateaus."

### Limits of Sequences
-   These limits describe the behavior of sequences as the index approaches infinity.

## Conclusion

We've reinforced the critical distinction between general limits and the specific limits that define derivatives. We've also highlighted the importance of one-sided limits when dealing with functions that have discontinuities or sharp changes.

---

## Continuity vs. Smoothness and Differentiability

This notebook cell summarizes the important distinction between continuity, smoothness, and differentiability, building upon our previous discussions.

**1. Continuity:**

-   A function $f(x)$ is **continuous at a point x = a** if and only if:
    -   $f(a)$ is defined.
    -   $\lim_{x \to a} f(x)$ exists (left-hand and right-hand limits are equal).
    -   $\lim_{x \to a} f(x) = f(a)$.
-   Continuity is about the function being "connected" without breaks, jumps, or holes.

**2. Smoothness:**

-   A function is **smooth** if it has a well-defined derivative (i.e., a tangent line) at every point.
-   Smoothness implies that the function has no sharp corners or cusps.

**3. Differentiability:**

-   A function is **differentiable at a point x = a** if its derivative $f'(a)$ exists.
-   Differentiability implies smoothness.

**4. Relationships:**

-   **Differentiatiable => Smooth => Continuous:** Differentiability implies smoothness, which implies continuity.
-   **Continuous $ \ne $ Smooth:** Continuity does not imply smoothness. Functions like $f(x) = |x|$ and $f(x) = x^{2/3}$ are continuous but not smooth.
-   **Continuous $ \ne $ Differentiatiable:** Continuity does not imply differentiability. The Weierstrass function is continuous everywhere but differentiable nowhere.

**5. Why the Distinction Matters:**

-   It clarifies the hierarchy of "niceness" of functions.
-   It emphasizes that differentiability is a stronger condition than continuity.
-   It highlights that smoothness is an intermediate step between differentiability and continuity.

**6. Importance of Formal Definition:**

-   The intuitive understanding of continuity as "being able to draw the function without lifting your pencil" is not sufficient.
-   The formal definition of continuity is crucial for a deeper understanding of calculus.
-   The distinction between continuity and smoothness is often not emphasized enough in calculus teachings.

---

## Sudden Changes and Non-Differentiability

This notebook cell documents the learning about why points of sudden change in a function cannot have a derivative.

**1. Points of Sudden Change:**

-   Points of sudden change in a function's graph are points where the function has:
    -   Sharp corners (e.g., $f(x) = |x|$ at $x = 0$)
    -   Cusps (e.g., $f(x) = x^{2/3}$ at $x = 0$)
    -   Vertical tangents

**2. Infinite Slope:**

-   At these points, the slope of the tangent line becomes infinitely steep.
-   This means the change in y over the change in x approaches infinity.

**3. Derivative as Slope:**

-   The derivative $f'(x)$ represents the slope of the tangent line.

**4. Derivative Function:**

-   The derivative $f'(x)$ is itself a function.
-   Functions must have real number outputs for real number inputs.

**5. Infinity is Not a Real Number:**

-   Therefore, if the slope is infinite, the derivative function is undefined at that point.

**6. Conclusion:**

-   Points of sudden change have an infinite slope.
-   The derivative function cannot have an infinite value.
-   Therefore, functions with sudden changes are not differentiable at those points.

**7. Examples:**

-   $f(x) = |x|$ at $x = 0$: sharp corner, undefined derivative.
-   $f(x) = x^{2/3}$ at $x = 0$: cusp, undefined derivative.
-   Vertical tangents: infinite slope, undefined derivative.

---

## Proof: Differentiability Implies Continuity

This notebook cell explains the proof provided in the image that demonstrates that if a function $f(x)$ is differentiable at $x=a$, then it is also continuous at $x=a$.

**Proof Breakdown:**

1.  **Given:** We are given that $f(x)$ is differentiable at $x=a$. This means that the limit:
    $$f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$
    exists.

2.  **Manipulation of f(x) - f(a):**
    -   We can rewrite $f(x) - f(a)$ as:
        $$f(x) - f(a) = \frac{f(x) - f(a)}{x - a} (x - a)$$

3.  **Taking the Limit:**
    -   Taking the limit of both sides as $x \to a$:
        $$\lim_{x \to a} (f(x) - f(a)) = \lim_{x \to a} \left[ \frac{f(x) - f(a)}{x - a} (x - a) \right]$$
    -   Using limit properties:
        $$\lim_{x \to a} (f(x) - f(a)) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a} \cdot \lim_{x \to a} (x - a)$$
    -   Since $\lim_{x \to a} \frac{f(x) - f(a)}{x - a} = f'(a)$ (from step 1) and $\lim_{x \to a} (x - a) = 0$, we have:
        $$\lim_{x \to a} (f(x) - f(a)) = f'(a) \cdot 0 = 0$$

4.  **Connecting to Continuity:**
    -   We want to show that $\lim_{x \to a} f(x) = f(a)$, which is the definition of continuity.
    -   We can rewrite $\lim_{x \to a} f(x)$ as:
        $$\lim_{x \to a} f(x) = \lim_{x \to a} [f(a) + (f(x) - f(a))]$$
    -   Using limit properties:
        $$\lim_{x \to a} f(x) = \lim_{x \to a} f(a) + \lim_{x \to a} (f(x) - f(a))$$
    -   Since $\lim_{x \to a} f(a) = f(a)$ (because $f(a)$ is a constant) and $\lim_{x \to a} (f(x) - f(a)) = 0$ (from step 3), we have:
        $$\lim_{x \to a} f(x) = f(a) + 0 = f(a)$$

5.  **Conclusion:**
    -   We have shown that $\lim_{x \to a} f(x) = f(a)$, which is the definition of continuity at $x=a$.
    -   Therefore, if $f(x)$ is differentiable at $x=a$, it is also continuous at $x=a$.

## Conceptual Understanding vs. Formal Proof

-   While the formal proof in the image is mathematically sound, it can appear convoluted due to its reliance on algebraic manipulation and seemingly arbitrary steps.
-   A more intuitive understanding can be gained by recognizing that differentiability implies the existence of a limit of the difference quotient, which is a stronger condition than continuity.
-   Differentiability also implies smoothness, which in turn implies continuity.
-   The conceptual understanding, which connects differentiability to smoothness and continuity, is often more direct and easier to grasp.
-   The formal proof essentially demonstrates the same concept using rigorous algebraic steps, but the connection might be less apparent.

---

## Order of Writing Limit Expressions

This notebook cell documents the discussion about the order of writing limit expressions and its implications for clarity and readability.

**1. Standard Practice:**

-   The standard practice in mathematics is to write the limit notation *to the left* of the expression.
    -   $ lim_{x \to a} f(x) $
-   This is generally considered the most common and widely accepted notation in mathematics textbooks and academic writing.
-   This practice aids reading by immediately indicating that a limit is being taken.

**2. Alternative Approach (Expression First):**

-   An alternative approach is to write the expression first and then the limit notation.
    -   $ f(x)  lim_{x \to a} $
-   This approach is not technically incorrect, but it is not the standard practice.
-   It might be considered less conventional or even confusing by some readers who are accustomed to the standard notation.

**3. Rationale for Alternative Approach:**

-   The rationale behind writing the expression first is to emphasize the function's behavior, which is the core concept of limits and derivatives.
-   In derivatives, we're examining the *rate of change* of the function, which is captured by the expression $\frac{f(x + h) - f(x)}{h}$ or $\frac{f(x) - f(a)}{x - a}$.
-   Writing this expression first allows us to perform algebraic manipulations before considering the limit itself.

**4. Why Standard Practice is Preferred:**

-   **Readability:** The standard notation allows for a smoother flow of reading, as the reader immediately understands the context of the expression.
-   **Consistency:** Consistent notation is essential for clear communication in mathematics.
-   **Established Convention:** Mathematical notation is often based on established conventions that have evolved over time.

**5. Recommendation:**

-   It is recommended to follow the standard practice of writing the limit notation to the left of the expression.
-   This ensures that your notation is consistent with common mathematical conventions and avoids potential confusion.
-   If you prefer writing the expression first, you can leave a space for the limit notation to the left, but ultimately the limit notation should be placed to the left.

# Nowhere Differentiable Functions: A Mathematical Dichotomy

## Key Insight
Functions that are **continuous everywhere** but **differentiable nowhere** achieve this property through one of two fundamental approaches:

1. **Infinite Regularity** (Fractal/Self-Similar)
2. **Chaos/Randomness**

---

## 1. Infinite Regularity (Fractal Self-Similarity)

### Principle
- Deterministic construction using infinite series
- Self-similar oscillations at all scales
- "Too much structure" - patterns repeat infinitely when zooming in
- Every point exhibits the same "rough" behavior at every magnification

### Examples

#### Weierstrass Function
```
f(x) = Σ(n=0 to ∞) aⁿ cos(bⁿπx)
```
- Where 0 < a < 1, b is odd integer, ab > 1 + 3π/2
- Uses sine/cosine waves with increasing frequency, decreasing amplitude

#### Van der Waerden Function
- Similar to Weierstrass but uses sawtooth waves instead of trigonometric functions
- Same principle: infinite superposition of oscillating functions

#### Takagi Function (Blancmange)
```
f(x) = Σ(n=0 to ∞) (1/2)ⁿ t(2ⁿx)
```
- Where t(x) is the tent function
- Self-similar construction using tent functions

### Why It Works
- Each term adds oscillations at a different scale
- No matter how much you zoom in, new oscillations appear
- Prevents formation of tangent lines at any point

---

## 2. Chaos/Randomness

### Principle
- Stochastic/probabilistic construction
- Fundamental unpredictability at all scales
- "Too little structure" - no coherent pattern emerges
- Irregularity comes from inherent randomness

### Examples

#### Brownian Motion
- Continuous random walk in the limit
- Nowhere differentiable with probability 1
- Models random particle motion

#### Random Series
- Functions built using random coefficients
- Probabilistic superposition creates universal non-differentiability

### Why It Works
- Randomness prevents any point from developing coherent local behavior
- No predictable pattern means no linear approximation possible
- Statistical properties ensure non-differentiability everywhere

---

## The Mathematical Dichotomy

### Two Extremes Leading to the Same Result

| **Infinite Regularity** | **Chaos/Randomness** |
|-------------------------|----------------------|
| Perfect deterministic order | Perfect disorder |
| Self-similarity at all scales | Unpredictability at all scales |
| Too much structure | Too little structure |
| Predictable construction | Stochastic construction |

### The Paradox
Both **perfect order** (infinite self-similarity) and **perfect disorder** (chaos) destroy differentiability through opposite means:

- **Fractals**: So regular they become irregular
- **Chaos**: Fundamentally irregular from the start

---

## Contrast with Isolated Non-Differentiability

### Functions Differentiable "Somewhere"
For functions that are non-differentiable at only isolated points or countable sets:

- **Geometric corners**: |x| (corner at x=0)
- **Cusps**: x^(1/3) (vertical tangent at x=0)
- **Piecewise functions**: Deliberate breaks in smoothness

### Why These Don't Work for "Nowhere"
- Only create finite/countable non-differentiable points
- Cannot systematically break differentiability everywhere
- Need either infinite regularity or chaos for universal non-differentiability

---

## Philosophical Conclusion

To achieve continuity with nowhere differentiability, mathematics reveals a profound duality:

> **The middle ground of "moderate complexity" typically yields differentiable functions. Only the extremes - infinite deterministic complexity or pure randomness - can systematically prevent differentiability at every point.**

This represents one of the most elegant examples of how mathematical extremes can converge to similar pathological behavior through fundamentally different mechanisms.
