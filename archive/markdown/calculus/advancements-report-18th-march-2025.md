---
title: "My Learning Summary: Logarithms, Exponents, and Reality"
source_notebook: "calculus/advancements-report-18th-march-2025.ipynb"
archived_notebook: "archive/notebooks/calculus/advancements-report-18th-march-2025.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# My Learning Summary: Logarithms, Exponents, and Reality

## Starting Point: Logarithms and Limits
- **Observation**: Logarithms of small numbers (e.g., $\ln(0.01) = -4.6$) give big negative numbers because they’re exponents, and small numbers come from negative exponents (e.g., $e^{-4.6} \approx 0.01$).
- **Limit Question**: Solving $\lim_{x \to 0^-} \ln(-x)$.
  - As $x \to 0^-$, $-x \to 0^+$, so $\ln(-x) \to -\infty$, not 0 as I first thought.
  - Why? $e^p$ never hits 0; $p$ must dive to $-\infty$.
- **New Insight**: For $\lim_{x \to 0^+} \ln(-x)$, $-x$ becomes negative (e.g., $-0.1$ when $x = 0.1$), and $\ln$ requires a positive argument. Since it’s undefined for $x > 0$, the limit "does not exist". I thought "undefined," but "does not exist" is the correct limit term due to domain issues.
- **New Example**: For $h(z) = \ln|z|$, evaluate limits:
  - (a) $\lim_{z \to 0^-} \ln|z|$: $|z| \to 0^+$, so $\ln|z| \to -\infty$.
  - (b) $\lim_{z \to 0^+} \ln|z|$: $|z| \to 0^+$, so $\ln|z| \to -\infty$.
  - (c) $\lim_{z \to -3} \ln|z|$: $|z| = |-3| = 3$, so $\ln|z| = \ln 3 \approx 1.0986$.
  - **Note**: (a) and (b) both $\to -\infty$, so the two-sided $\lim_{z \to 0} \ln|z|$ is $-\infty$ (asymptotic behavior), while (c) is finite.

## Exponents: Why $a^0 = 1$?
- **Intuition**: If exponents are "multiples," $a^0$ = "0 multiples" = 0?
- **Test**: $5^2 / 5^2 = 5^{2-2} = 5^0 = 1$, not 0. Rules ($a^m / a^n = a^{m-n}$) need $a^0 = 1$.
- **Alternative**: If $a^0 = 0$, $5^1 \cdot 5^0 = 5 \cdot 0 = 0$, but $5^{1+0} = 5$. Inconsistent.

## Philosophical Insight
- **Nothingness (0)**: Non-existence. Can’t start from it—$0 \cdot a = 0$, no change possible.
- **Undifferentiated State (1)**: The unit, a starting point with potential.
- **Reality**: Can’t begin from nothing (paradox: how does nothing spark something?). Must be eternal, no start/end.

## New Learning: Vertical Asymptotes
- **Definition**: Vertical asymptotes occur where a function is undefined, typically when the denominator is zero (e.g., rational functions like $f(x)$ or $g(x)$).
- **Example 1**: For $f(x) = \frac{7x}{(10 - 3x)^4}$, set denominator to zero: $(10 - 3x)^4 = 0$ $\to$ $10 - 3x = 0$ $\to$ $x = \frac{10}{3}$. Vertical asymptote at $x = \frac{10}{3}$.
- **Example 2**: For $g(x) = \frac{8}{(x + 5)(x - 9)}$, set denominator to zero: $(x + 5)(x - 9) = 0$ $\to$ $x = -5$ or $x = 9$. Vertical asymptotes at $x = -5$ and $x = 9$.
- **New Insight: Even vs. Odd Powers**:
  - For $g(x) = \frac{-4}{(x - 1)^2}$:
    - (a) $\lim_{x \to 1^-} g(x)$: $(x - 1)^2 \to 0^+$, so $g(x) \to \frac{-4}{0^+} = -\infty$.
    - (b) $\lim_{x \to 1^+} g(x)$: $(x - 1)^2 \to 0^+$, so $g(x) \to \frac{-4}{0^+} = -\infty$.
    - (c) $\lim_{x \to 1} g(x)$: Both sides $-\infty$, but as a two-sided limit, it "does not exist" (though often noted as $-\infty$ for asymptotes).
  - **Pattern**: Terms like $(x - a)^{\text{even}}$ (e.g., $(x - 1)^2$) yield the same infinity on both sides if the numerator is consistent, due to the even power ensuring positivity. Odd powers (e.g., $x - 1$) or mixed terms (e.g., $(x + 5)(x - 9)$) can lead to opposite infinities, so the two-sided limit typically DNE.
  - **Refinement**: The "even power trick" applies to forms like $(a - b)^{\text{even}}$, but not universally. For $(a + b)$ or complex denominators, the sign and power of each factor must be evaluated carefully on both sides.
  - **Polarity**: The function’s sign (e.g., $-4$ gives $-\infty$) sets the infinity direction.
- **New Technique: Evaluating Limits Near Asymptotes**:
  - For rational functions, as $x$ approaches the asymptote (e.g., $x = a$):
    - Left ($x \to a^-$): $x - a$ is a small negative number.
    - Right ($x \to a^+$): $x - a$ is a small positive number.
    - If the denominator is an even power (e.g., $(x - a)^2$), it’s $0^+$ on both sides.
    - If the denominator is an odd power (e.g., $x - a$), it changes sign.
  - **Rule**: If the denominator is infinitesimally small ($0^+$ or $0^-$), and the numerator is finite:
    - $\frac{\text{big}}{\text{small}}$ (positive numerator, $0^+$) $\to +\infty$.
    - $\frac{\text{negative}}{\text{small}}$ (negative numerator, $0^+$) $\to -\infty$.
    - If both sides tend to the same number, the difference is infinitesimally small, making the denominator tiny, so the function goes to $\pm\infty$ based on the numerator.
  - **Example Check**: For $g(x) = \frac{-4}{(x - 1)^2}$, both sides $\to -\infty$ due to the negative numerator and tiny positive denominator.
- **Connection**: This mirrors $\lim_{x \to 0^+} \ln(-x)$ not existing due to an undefined domain, reinforcing that math needs a defined "something" to operate.

## Conclusion
- $a^0 = 1$ reflects reality starting from "something," not nothing.
- $\ln(-x) \to -\infty$ (for $x \to 0^-$) shows existence stretching, not collapsing to 0.
- $\lim_{x \to 0^+} \ln(-x)$ does not exist due to negative arguments, and vertical asymptotes occur where functions are undefined (denominator zero).
- Even-powered terms like $(x - a)^{\text{even}}$ can lead to consistent infinity limits if the numerator aligns, while odd or mixed terms require careful evaluation, often resulting in DNE.
- Limits near asymptotes depend on denominator size and sign, with infinitesimally small denominators driving the function to $\pm\infty$ based on the numerator.
- For $h(z) = \ln|z|$, $\lim_{z \to 0^-}$ and $\lim_{z \to 0^+}$ both $\to -\infty$, while $\lim_{z \to -3} = \ln 3$, showing finite vs. infinite behavior.
- Nothingness can’t exist logically; reality begins from 1, the "empty slate."
