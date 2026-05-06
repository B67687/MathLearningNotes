---
title: "Understanding Limits: Concepts and Problem Solving"
source_notebook: "calculus/advancements-report-15th-march--Properties-of-Limits.ipynb"
archived_notebook: "archive/notebooks/calculus/advancements-report-15th-march--Properties-of-Limits.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Understanding Limits: Concepts and Problem Solving

This notebook compiles key concepts about limits, observations, study cases, and answers to questions about limits and continuity, incorporating philosophical insights on approximation and the nature of redefining discontinuities.

### 1. Two-Sided Limits Require Both Sides to Match
- In 1D, a two-sided limit $ \lim_{x \to a} f(x) $ exists only if the left-hand limit ($ \lim_{x \to a^-} f(x) $) and right-hand limit ($ \lim_{x \to a^+} f(x) $) exist and are equal.
- If the values from the left and right approach different numbers, the two-sided limit does not exist.

### 2. Single-Sided Limits
- Single-sided limits (left-hand or right-hand) only consider the function’s behavior from one direction.
- They can exist independently, even if the two-sided limit does not exist.
- **Notation Clarification**: The notation $ \lim_{x \to a} f(x) $ inherently refers to a two-sided limit. To specify a one-sided limit, we must use:
  - $ \lim_{x \to a^-} f(x) $: Left-hand limit (approaching from $ x < a $).
  - $ \lim_{x \to a^+} f(x) $: Right-hand limit (approaching from $ x > a $).

### 3. Limits in Higher Dimensions
- In 2D, to find $ \lim_{(x, y) \to (a, b)} f(x, y) $, the function must approach the same value along **all possible paths** (not just along the axes).
- In 3D or higher, the same rule applies: the limit exists only if the function converges to the same value along every path to the point.
- Practically, we test a few key paths (e.g., along axes, lines, curves) to check for consistency.

### 4. Limits Don’t Depend on the Function’s Value at the Point
- The value of a limit $ \lim_{x \to a} f(x) $ depends only on the values of $ f(x) $ **around** $ x = a $, not at $ x = a $.
- Often, the limit and the function’s value at the point are different, especially if the function is undefined at that point or has a discontinuity.

### 5. Starting with Small Deviations and Multiple Substitutions
- When estimating limits numerically, starting with small deviations from the point (e.g., 0.001 or 0.0001) helps, as the limit’s behavior is determined by values very close to the point.
- **Insight**: Using at least two or more substitutions on each side of the point (e.g., left: $ a - 0.001, a - 0.0001 $; right: $ a + 0.001, a + 0.0001 $) is crucial to identify the direction and confirm the limit. With only two points (one on each side), the trend might be unclear, especially if signs differ or the function oscillates.
- Always check both sides for a two-sided limit to ensure they converge to the same value.

### 6. Continuity and Polynomials
- A function $ f(x) $ is **continuous at $ x = a $** if:
  1. $ f(a) $ is defined.
  2. $ \lim_{x \to a} f(x) $ exists.
  3. $ \lim_{x \to a} f(x) = f(a) $.
- A function is **continuous on an interval** if it is continuous at every point in that interval.
- **Determining Continuity Analytically**:
  1. **Identify the Domain**: Where is the function defined?
     - Example: $ f(x) = \frac{1}{x} $ has domain $ x \neq 0 $.
  2. **Check for Potential Discontinuities**:
     - **Infinite Discontinuities**: Points where the denominator is zero or the function approaches infinity (e.g., $ f(x) = \frac{1}{x} $ at $ x = 0 $).
     - **Jump Discontinuities**: For piecewise functions, check where definitions change (e.g., $ f(x) = \begin{cases} 1 & \text{if } x \geq 0 \\ -1 & \text{if } x < 0 \end{cases} $ at $ x = 0 $).
     - **Removable Discontinuities**: Points where $ \lim_{x \to a} f(x) $ exists but $ f(a) $ is undefined or differs (e.g., $ f(x) = \frac{x^2 - 1}{x - 1} $ at $ x = 1 $, where $ \lim_{x \to 1} f(x) = 2 $, and redefining $ f(1) = 2 $ removes it).
  3. **Classify**:
     - **Fully Continuous**: Continuous everywhere in its domain (e.g., $ f(x) = x^2 $).
     - **Partially Continuous**: Continuous on some intervals (e.g., $ f(x) = \frac{1}{x} $, continuous except at $ x = 0 $).
     - **Discontinuous Everywhere**: No intervals of continuity (e.g., Dirichlet function: $ f(x) = 1 $ if $ x $ is rational, 0 if irrational).
- **Polynomials**: Continuous everywhere because they are defined for all $ x $, built from continuous operations (addition, multiplication, powers), and have no breaks.

### 7. Indeterminate Forms and the \( 0/0 \) Distinction
- **Indeterminate Forms**: An indeterminate form (e.g., $ 0/0 $, $ \infty/\infty $, $ 0 \cdot \infty $) occurs when substituting the limit value into an expression doesn’t immediately determine the limit. It indicates not enough information is available yet, requiring further analysis (e.g., factoring, L’Hôpital’s rule). Examples:
  - $ \lim_{x \to 0} \frac{x}{x} = 1 $ (simplifies to 1).
  - $ \lim_{x \to 0} \frac{x^2}{x} = 0 $ (simplifies to $ x $).
  - $ \lim_{x \to 0} \frac{\sin x}{x} = 1 $ (requires known result or L’Hôpital’s rule).

- **Why \( 0/0 \) Is Indeterminate, Not Undefined**:
  - **In Algebra**: $ \frac{0}{0} $ is undefined because there’s no unique real number $ k $ such that $ 0 \cdot k = 0 $—any number satisfies this, so the operation has no specific value.
  - **In Limits**: When $ \lim_{x \to a} f(x) = 0 $ and $ \lim_{x \to a} g(x) = 0 $, substitution gives $ \frac{0}{0} $, but the limit $ \lim_{x \to a} \frac{f(x)}{g(x)} $ depends on the behavior of $ f(x) $ and $ g(x) $ near $ x = a $, not at $ x = a $. The outcome varies:
    - $ \lim_{x \to 0} \frac{x}{x} = 1 $.
    - $ \lim_{x \to 0} \frac{x^2}{x} = 0 $.
    - $ \lim_{x \to 0} \frac{x}{x^3} = \frac{1}{x^2} \to \infty $.
    - $ \lim_{x \to 0} \frac{|x|}{x} $ doesn’t exist (1 from the right, -1 from the left).

  - **Why Not Just Undefined?**: If we called $ 0/0 $ "undefined" in the limit context, we’d conclude the limit doesn’t exist, which would be incorrect in cases where it does (e.g., $ \lim_{x \to 0} \frac{x}{x} = 1 $). The term "indeterminate" reflects that the limit’s value is not yet determined—it could be finite, infinite, or nonexistent, depending on the relative rates at which the numerator and denominator approach 0.

- **Why It’s a Roadblock**: The $ 0/0 $ form stops us from using direct substitution to find the limit immediately. It’s a signal that the limit’s value depends on the function’s behavior near the point, requiring further analysis (e.g., simplifying, factoring, or using L’Hôpital’s rule). Unlike a clearly undefined limit (e.g., $ \lim_{x \to 0} \frac{1}{x} $, which diverges to $ \pm \infty $), $ 0/0 $ leaves the outcome ambiguous until we investigate further.

- **Why We Don’t Go Further with \( \frac{\text{nonzero}}{0} \)-Type Forms**:
  - When substitution yields a form like $ \frac{1}{0} $ (or $ \frac{L}{0} $ where $ L \neq 0 $), it indicates the denominator approaches 0 while the numerator approaches a nonzero value. This typically means the limit is infinite or doesn’t exist in the finite sense:
    - Example: $ \lim_{x \to 0} \frac{1}{x} $: As $ x \to 0^+ $, $ \frac{1}{x} \to +\infty $; as $ x \to 0^- $, $ \frac{1}{x} \to -\infty $. The two-sided limit doesn’t exist.
    - Example: $ \lim_{x \to 0} \frac{3}{x^2} $: As $ x \to 0 $, $ \frac{3}{x^2} \to +\infty $ from both sides.

  - **Clear Behavior**: Unlike $ 0/0 $, where the limit could be finite, a $ \frac{\text{nonzero}}{0} $ form indicates divergence to $ \pm \infty $ or nonexistence due to differing one-sided limits. The relative rates are clear: the denominator approaches 0 faster than the numerator approaches 0 (since the numerator approaches a nonzero value), leading to a predictable outcome. We don’t need to go further to resolve ambiguity because the behavior is already determined:
    - If both one-sided limits are $ +\infty $ (or $ -\infty $), the limit is described as $ +\infty $ (or $ -\infty $), though not a real number.
    - If one-sided limits differ (e.g., $ +\infty $ and $ -\infty $), the two-sided limit doesn’t exist.


  - **The Role of Relative Rates**: In $ 0/0 $, both numerator and denominator approach 0, so their relative rates determine the limit, requiring further analysis (e.g., comparing how fast each term shrinks). In $ \frac{\text{nonzero}}{0} $, the denominator’s rate of approach to 0 dominates, leading to divergence—no further analysis is needed to find a finite limit. This explains why some relative rates are conclusive, allowing you to skip detailed analysis and determine the final outcome (e.g., \( \pm \infty \) or nonexistence) directly from substitution and a quick check of one-sided limits.

- **Implication**: The indeterminacy of $ 0/0 $ reflects the need to compare rates, while a $ \frac{\text{nonzero}}{0} $ form provides a clear conclusion about the limit’s behavior, leveraging the conclusive nature of the relative rates.

### 8. Meaning of "Equals" in Limits and the Philosophy of Approximation
- **Non-Calculus**: $ a = b $ means $ a $ is exactly $ b $ (e.g., $ 2 + 2 = 4 $), a perfect special case for discrete mathematics and finite values.
- **In Limits**: $ \lim_{x \to a} f(x) = L $ means $ f(x) $ gets arbitrarily close to $ L $ as $ x $ gets arbitrarily close to $ a $ (but $ x \neq a $), formalized by:
  - For any $ \epsilon > 0 $, there exists $ \delta > 0 $ such that if $ 0 < |x - a| < \delta $, then $ |f(x) - L| < \epsilon $.
- **Philosophical Insight**: Calculus accepts that we can’t always know the full truth (e.g., at discontinuities or infinity), but "knowing enough" through limits is sufficient. This redefines "equals" as convergence, a broader definition encompassing algebraic equality as a subset for continuous or discrete cases where $ \lim_{x \to a} f(x) = f(a) $. The calculus approach handles real-world complexities where perfect certainty is elusive, making it the definitive framework for infinite processes.
- **Practical Success**: This approximation (e.g., limits, derivatives, integrals) models reality effectively, so diverging to demand perfect knowledge isn’t worth it.

### 9. Connection to Removable Discontinuities
- Removable discontinuities (e.g., $ f(x) = \frac{x^2 - 1}{x - 1} $ at $ x = 1 $, where $ \lim_{x \to 1} f(x) = 2 $ but $ f(1) $ is undefined) reflect this philosophy. The limit provides "enough" knowledge to redefine $ f(1) = 2 $, removing the discontinuity, showcasing calculus’s focus on approximation over perfect truth.
- **Redefinition as a Choice**: Redefining $ f(a) $ to match the limit isn’t a mathematical necessity but a pragmatic choice. We can:
  - Keep the discontinuity, acknowledging the gap (valid for contexts where the undefined point has meaning).
  - Redefine $ f(a) $ to remove the discontinuity, creating a new continuous function (useful for simplifying analysis, e.g., differentiation).
- **Less of a Mathematical Definition**: The act of removing a discontinuity feels less like a strict mathematical rule because it’s a human decision driven by utility, not a fundamental requirement. The limit’s definition is rigorous, but choosing to redefine $ f(a) $ prioritizes practicality, aligning with the idea of "knowing enough."

### 10. Limit Properties and Their Rationale
Assume $ \lim_{x \to a} f(x) $ and $ \lim_{x \to a} g(x) $ exist, and $ c $ is a constant. Here’s why the following properties hold:

- **1. Constant Multiple**: $ \lim_{x \to a} [c f(x)] = c \lim_{x \to a} f(x) $
  - **Why**: Multiplying $ f(x) $ by $ c $ scales its limit. If $ \lim_{x \to a} f(x) = L $, then $ c f(x) \to c L $ because the epsilon-delta condition scales by $ c $ (e.g., if $ |f(x) - L| < \epsilon/|c| $, then $ |c f(x) - c L| < \epsilon $).

- **2. Sum/Difference**: $ \lim_{x \to a} [f(x) \pm g(x)] = \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x) $
  - **Why**: If $ f(x) \to L $ and $ g(x) \to M $, the sum/difference approaches $ L \pm M $ because small errors in $ f(x) $ and $ g(x) $ add up to a small error in $ f(x) \pm g(x) $ (e.g., $ |(f(x) + g(x)) - (L + M)| \leq |f(x) - L| + |g(x) - M| $).

- **3. Product**: $ \lim_{x \to a} [f(x) g(x)] = \lim_{x \to a} f(x) \lim_{x \to a} g(x) $
  - **Why**: The product of two converging functions converges to the product of their limits. Using $ |f(x) g(x) - L M| \leq |f(x) - L| |g(x)| + |L| |g(x) - M| $, and since $ g(x) $ is bounded near $ a $, the limit holds.

- **4. Quotient**: $ \lim_{x \to a} \left[\frac{f(x)}{g(x)}\right] = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)} $, provided $ \lim_{x \to a} g(x) \neq 0 $
  - **Why**: If $ g(x) \to M \neq 0 $, it’s bounded away from zero, avoiding division by zero. The limit follows from manipulating $ \left|\frac{f(x)}{g(x)} - \frac{L}{M}\right| $ using the difference of fractions.

- **5. Power**: $ \lim_{x \to a} [f(x)]^n = [\lim_{x \to a} f(x)]^n $, where $ n $ is any real number
  - **Why**: For integer $ n $, use the product rule repeatedly. For real $ n $, use $ [f(x)]^n = e^{n \ln f(x)} $, leveraging continuity of exponentiation as $ f(x) \to L > 0 $.

- **6. Root**: $ \lim_{x \to a} [n \sqrt{f(x)}] = n \sqrt{\lim_{x \to a} f(x)} $
  - **Why**: A special case of the power rule with $ n = 1/n $, holding if $ \lim_{x \to a} f(x) > 0 $.

- **7. Constant**: $ \lim_{x \to a} c = c $, where $ c $ is any real number
  - **Why**: A constant function doesn’t change, so its limit is itself (e.g., $ |c - c| = 0 < \epsilon $).

- **8. Identity**: $ \lim_{x \to a} x = a $
  - **Why**: The function $ f(x) = x $ approaches $ a $ as $ x \to a $ (e.g., $ |x - a| < \epsilon $).

- **9. Power of \( x \)**: $ \lim_{x \to a} x^n = a^n $
  - **Why**: Apply the power rule with $ f(x) = x $, so $ \lim_{x \to a} x^n = [\lim_{x \to a} x]^n = a^n $.

### Why These Properties Hold: A Deeper Perspective
- **Surface-Level Insight**: These properties work because the operations (e.g., addition, multiplication) don’t introduce new discontinuities or continuities—they preserve the existing behavior of $ f(x) $ and $ g(x) $. If $ \lim_{x \to a} f(x) $ and $ \lim_{x \to a} g(x) $ exist, the combined function (e.g., $ f(x) + g(x) $) reflects the same type of behavior (continuous or discontinuous) as the individual limits dictate. Since these operations are continuous, we can split the limit into individual parts and recombine them, simplifying the process instead of evaluating the entire expression directly.
- **Simplification Through Substitution**: As noted, applying these properties allows us to substitute the limit values (e.g., $ \lim_{x \to a} f(x) = L $, $ \lim_{x \to a} g(x) = M $) and perform simple algebraic manipulation and arithmetic (e.g., $ L + M $, $ L \cdot M $). This "dumbs down" the process to basic computations once the individual limits are known, making limit evaluation efficient and accessible. For example, $ \lim_{x \to 2} [(3x + 1)(x^2 - 4)] = (\lim_{x \to 2} (3x + 1)) \cdot (\lim_{x \to 2} (x^2 - 4)) = 7 \cdot 0 = 0 $, reducing it to multiplication.
- **Hypothetical Counterexample**: If an operation $ \zeta(f(x), g(x)) $ could create discontinuities or continuities unexpectedly (e.g., $ \zeta(f(x), g(x)) = 0 $ if $ f(x) = g(x) $, else 1), the limit $ \lim_{x \to a} \zeta(f(x), g(x)) $ might not equal $ \zeta(\lim_{x \to a} f(x), \lim_{x \to a} g(x)) $, breaking these properties. Standard operations don’t do this, ensuring the properties hold.


- **The Fundamental Reason: Epsilon-Delta and Completeness of $ \mathbb{R} $**:
  - **Epsilon-Delta Definition**: The limit $ \lim_{x \to a} f(x) = L $ means: for every $ \epsilon > 0 $, there exists $ \delta > 0 $ such that if $ 0 < |x - a| < \delta $, then $ |f(x) - L| < \epsilon $. This ensures limits are well-defined and can be manipulated algebraically. The continuity of operations (e.g., addition, multiplication) allows substitution: if $ f(x) \to L $ and $ g(x) \to M $, then $ f(x) + g(x) \to L + M $, justifying the algebraic approach.
  - **Completeness of $ \mathbb{R} $**: The real numbers are complete—every Cauchy sequence converges to a real number. This ensures that $ L $ and $ M $ are real numbers, enabling straightforward arithmetic (e.g., $ L + M $) without gaps or undefined results. Without completeness (e.g., in $ \mathbb{Q} $), some limits might not exist.
  - **Why This Is Fundamental**: The epsilon-delta definition and completeness of $ \mathbb{R} $ provide the rigorous foundation that makes substitution and algebraic manipulation valid. The continuity of operations ensures the process is reliable, while completeness guarantees the results are well-defined in $ \mathbb{R} $.

---

## **Observation: Numerical Behavior of $ g(\theta) $**

Consider the function:

$ g(\theta) = \frac{\cos(\theta - 4) - 1}{2\theta - 8} $

### Numerical Evaluation
- **Left of 4**:
  - $ \theta = 3.999 $: $ g(3.999) \approx 0.00025000 $
  - $ \theta = 3.9999 $: $ g(3.9999) = 2.5 \times 10^{-5} $
- **Right of 4**:
  - $ \theta = 4.001 $: $ g(4.001) \approx -0.00025000 $
  - $ \theta = 4.0001 $: $ g(4.0001) = -2.5 \times 10^{-5} $

### Analysis
- With multiple points, the magnitudes decrease toward 0, confirming $ \lim_{\theta \to 4} g(\theta) = 0 $.
- Multiple substitutions clarify the direction.

### Algebraic Confirmation
Let $ u = \theta - 4 $, so as $ \theta \to 4 $, $ u \to 0 $:
$ g(\theta) = \frac{\cos(u) - 1}{2u} $
$ \lim_{\theta \to 4} g(\theta) = \lim_{u \to 0} \frac{\cos(u) - 1}{2u} = 0 $
The limit is 0.

## Study Case: Limit vs. Function Value at the Point

### Problem Description
Consider the function $ f(x) $ with the given graph:

<img src="discontinuity-graph.png">

- The graph shows a closed dot at $ x = -8 $, $ y = -3 $, indicating $ f(-8) = -3 $.
- The function approaches $ y = -6 $ as $ x \to -8 $ from both sides.

### Analysis
- **Function Value**: $ f(-8) = -3 $.
- **Limit**: $ \lim_{x \to -8} f(x) = -6 $.

The limit depends on values around $ x = -8 $, not at $ x = -8 $.

---

## **New Questions and Answers**

### 7. Explain in your own words what each of the following equations means: $ \lim_{x \to -8^-} f(x) = 3 $ and $ \lim_{x \to -8^+} f(x) = -1 $
- **Explanation**:
  - $ \lim_{x \to -8^-} f(x) = 3 $: As $ x $ approaches $ -8 $ from the left (values less than $ -8 $,
    like $ -8.1, -8.01 $), $ f(x) $ gets closer to 3.
  - $ \lim_{x \to -8^+} f(x) = -1 $: As $ x $ approaches $ -8 $ from the right (values greater
    than $ -8 $, like $ -7.9, -7.99 $), $ f(x) $ gets closer to $ -1 $.
  - Since the left-hand limit ($ 3 $) and right-hand limit ($ -1 $) differ, the two-sided
    limit $ \lim_{x \to -8} f(x) $ does not exist.
- **Your Answer**: "Approach $ x = 8 $ from negative side is 3, from positive side is -1,
  no overall limit."
  - **Analysis**: Correct reasoning—you noted the left-hand limit is 3, the right-hand
    limit is -1, and thus the two-sided limit doesn’t exist. There’s a typo (you wrote
    $ x = 8 $ instead of $ x \to -8 $), but assuming that’s a slip, your answer aligns
    with the explanation.

### 8. Suppose we know that $ \lim_{x \to -7} f(x) = 18 $. If possible, determine the value
of $ \lim_{x \to -7^-} f(x) $ and the value of $ \lim_{x \to -7^+} f(x) $. If it is not
possible to determine one or both of these values, explain why not.
- **Explanation**:
  - The two-sided limit $ \lim_{x \to -7} f(x) = 18 $ means the left-hand and right-hand
    limits must both exist and equal 18.
  - Thus, $ \lim_{x \to -7^-} f(x) = 18 $ and $ \lim_{x \to -7^+} f(x) = 18 $.
- **Your Answer**: "Yes, because it inherently means that all ways to approach that value
  results in that limit."
  - **Analysis**: Correct! You recognized that a two-sided limit existing implies both
    one-sided limits match it, so both are 18. Your explanation captures the core idea,
    even without explicitly stating the values.

### 9. Suppose we know that $ f(6) = -53 $. If possible, determine the value of
$ \lim_{z \to 6^-} f(z) $ and the value of $ \lim_{z \to 6^+} f(z) $. If it is not
possible to determine one or both of these values, explain why not.
- **Explanation**:
  - $ f(6) = -53 $ gives the function’s value at $ z = 6 $, but limits depend on the
    behavior of $ f(z) $ as $ z $ approaches 6, not at 6.
  - Without knowing $ f(z) $ for $ z \neq 6 $, we can’t determine the limits. For
    example, if $ f(z) = -53 $ for all $ z $, both limits are $ -53 $; if $ f(z) = 0 $
    for $ z \neq 6 $, both are 0.
  - Since we only know $ f(6) $, the limits cannot be determined without more information.
- **Your Answer**: "No. This point may be discontinuous, if we can also prove it is
  continuous then yes."
  - **Analysis**: Correct! You noted that $ f(6) = -53 $ doesn’t provide enough to find
    the limits, as the point may be discontinuous. You also correctly stated that if the
    function is continuous at $ z = 6 $, the limits would be $ -53 $, but without that
    information, we can’t conclude.

### 10. Is it possible to have $ \lim_{x \to 1} f(x) = -23 $ and $ f(1) = 107 $?
Yes, if the function is discontinuous at $ x = 1 $. The limit $ \lim_{x \to 1} f(x) = -23 $
means $ f(x) $ approaches $ -23 $ as $ x $ approaches 1, but $ f(1) = 107 $ creates a
removable discontinuity. Redefining $ f(1) = -23 $ would make it continuous. Example:
$ f(x) = \begin{cases} -23 & \text{if } x \neq 1 \\ 107 & \text{if } x = 1 \end{cases} $
This can be visualized as a function that is $ -23 $ everywhere except at $ x = 1 $,
where it jumps to $ 107 $, illustrating a clear break that the limit ignores.

---

## **Practice Problems: Applying Limit Properties**

### Problem 4: Compute $ \lim_{x \to -1} (3x^2 - 9x + 2) $
- **Solution**:
  - Using limit properties: $ \lim_{x \to -1} (3x^2 - 9x + 2) = \lim_{x \to -1} (3x^2) - \lim_{x \to -1} (9x) + \lim_{x \to -1} 2 $.
  - $ \lim_{x \to -1} (3x^2) = 3 (\lim_{x \to -1} x)^2 = 3(-1)^2 = 3 \cdot 1 = 3 $.
  - $ \lim_{x \to -1} (9x) = 9 \lim_{x \to -1} x = 9(-1) = -9 $.
  - $ \lim_{x \to -1} 2 = 2 $.
  - Combine: $ 3 - (-9) + 2 = 3 + 9 + 2 = 14 $.
  - Alternatively, since it’s a polynomial (continuous), substitute: $ 3(-1)^2 - 9(-1) + 2 = 3 + 9 + 2 = 14 $.
- **Result**: $ \lim_{x \to -1} (3x^2 - 9x + 2) = 14 $.

### Problem 5: Compute $ \lim_{w \to -1} (w - (w^2 + 3)^2) $
- **Solution**:
  - $ \lim_{w \to -1} (w - (w^2 + 3)^2) = \lim_{w \to -1} w - \lim_{w \to -1} (w^2 + 3)^2 $.
  - $ \lim_{w \to -1} w = -1 $.
  - $ \lim_{w \to -1} (w^2 + 3) = (\lim_{w \to -1} w)^2 + 3 = (-1)^2 + 3 = 4 $.
  - $ \lim_{w \to -1} (w^2 + 3)^2 = [\lim_{w \to -1} (w^2 + 3)]^2 = 4^2 = 16 $.
  - Combine: $ -1 - 16 = -17 $.
- **Result**: $ \lim_{w \to -1} (w - (w^2 + 3)^2) = -17 $.

### Problem 6: Compute $ \lim_{t \to 0} (t^4 - 4t^2 + 12t - 8) $
- **Solution**:
  - $ \lim_{t \to 0} (t^4 - 4t^2 + 12t - 8) = \lim_{t \to 0} t^4 - \lim_{t \to 0} (4t^2) + \lim_{t \to 0} (12t) - \lim_{t \to 0} 8 $.
  - $ \lim_{t \to 0} t^4 = 0 $.
  - $ \lim_{t \to 0} (4t^2) = 4 \cdot 0 = 0 $.
  - $ \lim_{t \to 0} (12t) = 12 \cdot 0 = 0 $.
  - $ \lim_{t \to 0} 8 = 8 $.
  - Combine: $ 0 - 0 + 0 - 8 = -8 $.
  - Alternatively, substitute: $ 0^4 - 4(0)^2 + 12(0) - 8 = -8 $.
- **Result**: $ \lim_{t \to 0} (t^4 - 4t^2 + 12t - 8) = -8 $.

### Problem 7: Compute $ \lim_{z \to 2} \frac{10 + z^2}{3 - 4z} $
- **Solution**:
  - Numerator: $ \lim_{z \to 2} (10 + z^2) = 10 + 2^2 = 14 $.
  - Denominator: $ \lim_{z \to 2} (3 - 4z) = 3 - 4 \cdot 2 = 3 - 8 = -5 $.
  - Quotient: $ \frac{14}{-5} = -\frac{14}{5} $.
- **Result**: $ \lim_{z \to 2} \frac{10 + z^2}{3 - 4z} = -\frac{14}{5} $.

### Problem 8: Compute $ \lim_{x \to 7} \frac{8x}{x^2 - 14x + 49} $
- **Solution**:
  - Simplify: $ x^2 - 14x + 49 = (x - 7)^2 $, so the expression is $ \frac{8x}{(x - 7)^2} $.
  - Numerator: $ \lim_{x \to 7} (8x) = 8 \cdot 7 = 56 $.
  - Denominator: $ \lim_{x \to 7} (x - 7)^2 = (7 - 7)^2 = 0 $.
  - This gives $ \frac{56}{0} $, a $ \frac{\text{nonzero}}{0} $ form. The denominator approaches 0 positively, and the numerator is positive, so the limit approaches $ +\infty $.
- **Result**: $ \lim_{x \to 7} \frac{8x}{x^2 - 14x + 49} = +\infty $ (not finite, may need clarification).

### Problem 9: Compute $ \lim_{y \to 3} \frac{y^3 - 20y + 4}{y^2 + 8y - 1} $
- **Solution**:
  - Numerator: $ \lim_{y \to 3} (y^3 - 20y + 4) = 3^3 - 20 \cdot 3 + 4 = 27 - 60 + 4 = -29 $.
  - Denominator: $ \lim_{y \to 3} (y^2 + 8y - 1) = 3^2 + 8 \cdot 3 - 1 = 9 + 24 - 1 = 32 $.
  - Quotient: $ \frac{-29}{32} = -\frac{29}{32} $.
- **Result**: $ \lim_{y \to 3} \frac{y^3 - 20y + 4}{y^2 + 8y - 1} = -\frac{29}{32} $.

### Problem 10: Compute $ \lim_{w \to -6} \sqrt[3]{8 + 7w} $
- **Solution**:
  - Inside: $ \lim_{w \to -6} (8 + 7w) = 8 + 7(-6) = 8 - 42 = -34 $.
  - Root: $ \lim_{w \to -6} \sqrt[3]{8 + 7w} = \sqrt[3]{-34} $.
- **Result**: $ \lim_{w \to -6} \sqrt[3]{8 + 7w} = \sqrt[3]{-34} $.

### Problem 11: Compute $ \lim_{t \to 1} (4t^2 - \sqrt{8t + 1}) $
- **Solution**:
  - $ \lim_{t \to 1} (4t^2 - \sqrt{8t + 1}) = \lim_{t \to 1} (4t^2) - \lim_{t \to 1} \sqrt{8t + 1} $.
  - $ \lim_{t \to 1} (4t^2) = 4 \cdot 1^2 = 4 $.
  - $ \lim_{t \to 1} (8t + 1) = 8 \cdot 1 + 1 = 9 $, so $ \lim_{t \to 1} \sqrt{8t + 1} = \sqrt{9} = 3 $.
  - Combine: $ 4 - 3 = 1 $.
- **Result**: $ \lim_{t \to 1} (4t^2 - \sqrt{8t + 1}) = 1 $.

### Problem 12: Compute $ \lim_{z \to -8} (\sqrt{3z - 8} + \sqrt[3]{9 + 2z}) $
- **Solution**:
  - $ \lim_{z \to -8} (\sqrt{3z - 8} + \sqrt[3]{9 + 2z}) = \lim_{z \to -8} \sqrt{3z - 8} + \lim_{z \to -8} \sqrt[3]{9 + 2z} $.
  - $ \lim_{z \to -8} (3z - 8) = 3(-8) - 8 = -32 $, so $ \lim_{z \to -8} \sqrt{3z - 8} = \sqrt{-32} $, which is imaginary.
  - $ \lim_{z \to -8} (9 + 2z) = 9 + 2(-8) = -7 $, so $ \lim_{z \to -8} \sqrt[3]{9 + 2z} = \sqrt[3]{-7} $.
  - The square root term is not real, so the limit is not defined in the real numbers.
- **Result**: Not defined in the real numbers; if complex numbers are allowed, it’s $ \sqrt{32}i + \sqrt[3]{-7} $.
