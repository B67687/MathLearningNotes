---
title: "Best Practices for Limit Evaluation and Related Concepts"
source_notebook: "calculus/advancements-report-17th-march-2025.ipynb"
archived_notebook: "archive/notebooks/calculus/advancements-report-17th-march-2025.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Best Practices for Limit Evaluation and Related Concepts

## 1. Prioritize Standard Notation and Methods
   - Use $ \lim_{x \to a^-} f(x) $ for left-hand limits and $ \lim_{x \to a^+} f(x) $ for right-hand limits.
   - Avoid unconventional symbols to ensure consistency.

## 2. Evaluate Limits Using One-Sided Limits
   - For $ \lim_{x \to a} f(x) $ to exist, check $ \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) $.
   - If they differ, the limit does not exist (D.N.E.).

## 3. Handle Piecewise Functions Carefully
   - Use only the expressions defined near $ x = a $.
   - Ignore irrelevant pieces.

## 4. Understand Behavior of Absolute Functions in Limits
   - For $ \frac{|x|}{x} $ or $ \frac{1}{|x|} $, expect D.N.E. at $ x = 0 $.
   - For $ \frac{x - a}{|x - a|^n} $ (odd $ n $), results like $ \pm 1 $ or $ \pm \infty $ often lead to D.N.E.

## 5. Rationalizing the Denominator: Key Insights
   - Rationalizing doesn’t fix division by zero without cancellation.
   - If the denominator still approaches zero, the limit may be undefined or infinite.

## 6. Seek Cancellation in Indeterminate Forms
   - Simplify $ \frac{0}{0} $ forms by factoring or rationalizing to cancel terms.
   - If no cancellation occurs, check for infinity or D.N.E.

## 7. Balance Conciseness with Clarity
   - Favor accuracy and standard methods over shortcuts.
   - Alternative formats (e.g., matrices) are fine if correct and clear.

## 8. Formalize Insights for Broader Application
   - Test ideas with examples.
   - Define variables and justify steps for rigor.

## 9. Evaluate Limits Formally
   - Always compute one-sided limits to confirm D.N.E., especially at discontinuities.

---

# Comprehensive Notes on Limit Evaluation and Related Concepts

## Guidelines and Preferences

These notes reflect your learning journey and preferences as of March 17, 2025, with a focus on mathematical correctness, standard notation, and conciseness, tailored for a computer science context.

- **Preference for Mathematical Correctness and Standard Notation**:
  - Always assess whether a method or notation is:
    - **Mathematically Standard**: Widely accepted in formal mathematics (e.g., $ \lim $, $ = $).
    - **Mathematically Correct/Notational Correct**: Logically valid, even if not standard.
    - **Non-Standard/Custom**: Requires definition and isn’t formally recognized, limiting portability.
  - Engage ideas optimistically but ground them in reality to avoid pursuing unfeasible paths.

- **Avoiding Personal Habits**:
  - Prioritize standard methods to avoid forming habits with non-standard notations, ensuring long-term consistency and portability (e.g., for exams, academic submissions).

- **Conciseness and Elegance**:
  - Seek concise and elegant presentations where possible, balancing with correctness and acceptability.

- **Contextual Use**:
  - In a computer science context, alternative presentations (e.g., matrix alignment) are more tolerated if the workings are correct, suitable for assignments where a TA may accept equivalent methods.

## Limits and Piecewise Functions

### Introduction

This section covers the concepts of left-hand and right-hand limits, how to determine if a limit exists, and the correct notation to use, especially when dealing with piecewise functions.

### Left-Hand and Right-Hand Limits

When evaluating the limit of a function $ f(x) $ as $ x $ approaches a value $ a $, we need to consider both the left-hand and right-hand limits.

- **Left-Hand Limit**: The limit of $ f(x) $ as $ x $ approaches $ a $ from the left (i.e., $ x < a $) is denoted as:
  - $ \lim_{x \to a^-} f(x) $ or $ \lim_{x \uparrow a} f(x) $
- **Right-Hand Limit**: The limit of $ f(x) $ as $ x $ approaches $ a $ from the right (i.e., $ x > a $) is denoted as:
  - $ \lim_{x \to a^+} f(x) $ or $ \lim_{x \downarrow a} f(x) $

### Limit Existence

For the limit of $ f(x) $ as $ x $ approaches $ a $ to exist, both the left-hand and right-hand limits must exist and be equal.

- $ \lim_{x \to a} f(x) $ exists if and only if $ \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) $.

If the left-hand and right-hand limits are not equal, the limit does not exist (D.N.E.).

### Correct Notation

- Use $ \lim_{x \to a^-} f(x) $ and $ \lim_{x \to a^+} f(x) $ to denote left-hand and right-hand limits, respectively.
- **Do not** use the logical conjunction symbol "$ \land $" to connect numerical values when evaluating limits. "$ \land $" is for logical "AND" operations, not for showing equality of values.
- When stating that a limit does not exist, use "D.N.E." or "The limit does not exist."

### Absolute Functions in Fractions and Limit Behavior

You’ve noticed that many limits involving absolute functions in fractions (e.g., $ \frac{|x|}{x} $, $ \frac{1}{|x|} $) result in D.N.E., especially in your recent work with problems 27–30. This pattern arises because:

- **Discontinuities**: Absolute values like $ |x| $ are piecewise ($ x $ for $ x \geq 0 $, $ -x $ for $ x < 0 $), and when in a denominator or tied to a root (e.g., $ \frac{1}{|x|} $, $ \frac{|x - a|}{x - a} $), they become undefined or switch signs at $ x = a $, often leading to different left-hand and right-hand limits.
  - Example: $ \lim_{x \to 0} \frac{1}{|x|} $
    - $ \lim_{x \to 0^-} = \frac{1}{-x} \to -\infty $
    - $ \lim_{x \to 0^+} = \frac{1}{x} \to +\infty $
    - D.N.E. since $ -\infty \neq +\infty $.

- **Sign Changes**: When the absolute value is in the numerator or denominator (e.g., $ \frac{|x|}{x} $), the switch at $ x = 0 $ or $ x = a $ can cause a mismatch.
  - Example: $ \lim_{x \to 0} \frac{|x|}{x} $
    - $ \lim_{x \to 0^-} = \frac{-x}{x} = -1 $
    - $ \lim_{x \to 0^+} = \frac{x}{x} = 1 $
    - D.N.E. since $ -1 \neq 1 $.

- **Refined Hypothesis: Odd Powers and Symmetry**: You’ve refined this for absolute functions with odd powers in fractions, where the limit is taken at $ x \to a $, $ a \neq 0 $. For functions like $ f(x) = \frac{x - a}{|x - a|^n} $ with $ n $ odd:
  - For $ n = 1 $: $ \lim_{x \to a} \frac{x - a}{|x - a|} $ gives $ -1 $ and $ 1 $, D.N.E., symmetric.
  - For $ n = 3 $: $ \lim_{x \to a} \frac{x - a}{|x - a|^3} $ gives $ -\infty $ and $ +\infty $, D.N.E., symmetric.
  - This holds for this form, supporting your pattern from problems 27–30.

- **Counterexample**: Not all such limits are D.N.E. If balanced, the limit can exist.
  - Example: $ \lim_{x \to 0} \frac{|x|}{x + 1} $
    - $ \lim_{x \to 0^-} = \frac{-x}{x + 1} \to 0 $
    - $ \lim_{x \to 0^+} = \frac{x}{x + 1} \to 0 $
    - Exists and equals 0.

- **Practical Note**: Even if you suspect D.N.E., evaluate formally to confirm, catch exceptions, and build intuition.

**Conclusion**: Absolute functions in fractions often result in D.N.E. due to discontinuities or sign changes, especially at $ x = a $. Your hypothesis about odd-powered forms like $ \frac{x - a}{|x - a|^n} $ (with $ a \neq 0 $) shows symmetric D.N.E., as seen in problems 27–30.

### Rationalizing the Denominator and Division by Zero

You’ve observed that rationalizing the denominator doesn’t seem to eliminate the division-by-zero problem in limits, and you’ve refined this to suggest it only works with cancellation. Let’s analyze this, focusing on rationalizing the denominator, to confirm your insight.

- **Why Rationalizing the Denominator Doesn’t Inherently Eliminate Division by Zero**:
  - Rationalizing rewrites the denominator to eliminate radicals (e.g., $ \frac{1}{\sqrt{x} - 2} \to \frac{\sqrt{x} + 2}{x - 4} $), but the denominator’s root persists (e.g., $ x - 4 = 0 $ at $ x = 4 $).
  - After rationalizing, the denominator often becomes a difference of squares (e.g., $ (\sqrt{x} - a)(\sqrt{x} + a) = x - a^2 $), which equals 0 when $ x = a^2 $, as you noted with $ x + a = 0 $ or $ x - a = 0 $ leading to $ x^2 - a^2 = 0 $.
  - If no cancellation occurs, the division-by-zero problem persists.
  - Example: $ \lim_{x \to 4} \frac{1}{\sqrt{x} - 2} $:
    - After rationalizing: $ \lim_{x \to 4} \frac{\sqrt{x} + 2}{x - 4} $.
    - Numerator: $ \sqrt{x} + 2 \to 4 $.
    - Denominator: $ x - 4 \to 0 $.
    - Result: $ \frac{4}{0} $, D.N.E. as a finite limit.

- **When Rationalizing the Denominator Eliminates Division by Zero**:
  - In $ \frac{0}{0} $ indeterminate forms, rationalizing the denominator can resolve the issue if the numerator provides a factor to cancel with the new denominator (e.g., $ x - a^2 $).
  - Example: $ \lim_{x \to 9} \frac{x - 9}{\sqrt{x} - 3} $:
    - Rationalize denominator: $ \frac{(x - 9)(\sqrt{x} + 3)}{(\sqrt{x} - 3)(\sqrt{x} + 3)} = \frac{(x - 9)(\sqrt{x} + 3)}{x - 9} = \sqrt{x} + 3 \quad (x \neq 9) $.
    - Limit: $ \lim_{x \to 9} (\sqrt{x} + 3) = 6 $.
    - The cancellation of $ x - 9 $ removed the division by zero.

- **Your Insight**:
  - You’ve concluded that rationalizing the denominator doesn’t inherently eliminate division by zero—it requires cancellation. Without it, the denominator $ x - a^2 = 0 $ at $ x = a^2 $ persists, maintaining the problem.
  - This is confirmed: the technique’s success depends on the numerator matching the denominator’s form post-rationalization.

**Conclusion**: Rationalizing the denominator doesn’t inherently eliminate the division-by-zero problem; it only does so when a cancellation occurs that removes the term (e.g., $ x - a^2 $) causing the denominator to approach zero, as you’ve insightfully concluded.

---

## 1. Limit Evaluation (Two-Sided Limits)

### Optimized Standard Method (Preferred)

To evaluate $ \lim_{x \to a} g(x) $, compute the one-sided limits separately using standard notation, followed by an explicit comparison. This is the conventional approach in calculus and your preferred method as of March 17, 2025.

- **Assessment**:
  - **Mathematically Correct/Notational Correct**: Yes, it follows the standard rule that a two-sided limit exists if the one-sided limits are equal.
  - **Mathematically Standard**: Yes, this is the widely accepted method in textbooks.
- **Steps**:
  1. State the limit:
     $ \lim_{x \to a} g(x) $
  2. Compute each one-sided limit separately:
     $ \lim_{x \to a^-} g(x) = \text{[expression at } x \to a^-] = \text{[simplified value]} $
     $ \lim_{x \to a^+} g(x) = \text{[expression at } x \to a^+] = \text{[simplified value]} $
  3. Compare and conclude:
     - If equal ($ L_1 = L_2 $), then $ \lim_{x \to a} g(x) = L_1 $.
     - If different ($ L_1 \neq L_2 $), then $ \lim_{x \to a} g(x) \text{ D.N.E.} $.

### Refined Matrix Approach (Optional, Explored)

For a concise presentation suitable in a computer science context, you previously explored a matrix-like alignment to compute one-sided limits side by side. This is retained as an optional method for reference.

- **Assessment**:
  - **Mathematically Correct/Notational Correct**: Yes, it computes one-sided limits accurately and applies the standard rule for two-sided limits.
  - **Mathematically Standard**: No, the table format is not standard for limit evaluations (typically used for matrices or data), but it’s a valid personal adaptation.
  - **Acceptability**: Acceptable for personal use and CS assignments, especially if the TA recognizes the identical workings. Include a note if submitting formally (e.g., “Matrix shows parallel one-sided limit computations”).
- **Steps**:
  1. State the limit and present the one-sided limit computations in a side-by-side array:
     $ \lim_{x \to a} g(x) \quad \begin{array}{c|c}
     \lim_{x \to a^-} g(x) & \lim_{x \to a^+} g(x) \\
     \text{[expression at } x \to a^-] \to \text{[simplified value]} & \text{[expression at } x \to a^+] \to \text{[simplified value]}
     \end{array} $
  2. Compare the final values and conclude:
     - If equal, the limit exists.
     - If different, the limit D.N.E.

### Inspirational $ \wedge $ Approach (Explored, Non-Standard)

You explored an elegant $ \wedge $ notation for personal inspiration. Define $ \wedge $ as simultaneous evaluation of one-sided limits.

- **Assessment**:
  - **Mathematically Correct/Notational Correct**: Yes, with the definition, it’s correct and elegant.
  - **Mathematically Standard**: No, $ \wedge $ is not a standard operator for limits (used for logical AND or set intersection instead).
  - **Acceptability**: Acceptable for personal notes with a definition, but not for formal use due to your goal of avoiding non-standard habits.
- **Steps**:
  1. Define and compute:
     $ \lim_{x \to a} g(x) = \lim_{x \to a^-} g(x) \wedge \lim_{x \to a^+} g(x) $
     (Where $ \wedge $ means "the two-sided limit exists if the one-sided limits are equal, or D.N.E. if different.")
  2. Substitute and simplify, then compare.
  3.

### Initial $ = $ Method (Explored, Partially Standard)

You initially used a one-liner with $ = $ to evaluate limits, which evolved over time.

- **Assessment**:
  - **Mathematically Correct/Notational Correct**: Yes, the method is correct. It states the condition that a two-sided limit exists if the one-sided limits are equal.
  - **Mathematically Standard**: Partially. The equality $ \lim_{x \to a^-} g(x) = \lim_{x \to a^+} g(x) $ is standard, but the one-liner format with $ = $ carried through all steps is not typical, and $ = $ is overloaded (condition and computation).
  - **Acceptability**: Moved away from this due to overloading concerns and your preference for standard notation.
- **Steps**:
  1. Start with:
     $ \lim_{x \to a} g(x) : \lim_{x \to a^-} g(x) = \lim_{x \to a^+} g(x) $
  2. Compute by substituting and simplifying, carrying $ = $ through.
  3. Compare and conclude based on equality.

## 2. Piecewise Function Context

Limits are often evaluated for piecewise functions, where the expression changes based on the value of $ x $.

- **Definition**: A piecewise function $ g(x) $ is defined as:
  $ g(x) = \begin{cases}
  \text{expression 1} & \text{if condition 1} \\
  \text{expression 2} & \text{if condition 2} \\
  \text{expression 3} & \text{if condition 3}
  \end{cases} $
- **Limit Evaluation**: Use the appropriate expression for each one-sided limit based on the piecewise definition. Only the pieces relevant to the limit point $ x = a $ are used, determined by the intervals immediately to the left and right of $ a $.
- **Insight on Continuity and Predictability**: If the function were continuous at $ x = a $, all relevant pieces would yield the same limit value. Distant pieces are irrelevant due to their distance from the limit point.
- **Examples**:
  - $ g(x) = 5x + 24 $ for $ x < -3 $, $ x^2 - 3 $ for $ -3 \leq x < 4 $, $ 1 - 2x $ for $ x \geq 4 $.
  - $ f(x) = x^2 $ for $ x < 1 $, $ 2x - 1 $ for $ x \geq 1 $.
  - $ g(t) = t^2 - t^3 $ for $ t < 2 $, $ 5t - 14 $ for $ t \geq 2 $.
  - $ h(z) = 6z $ for $ z < -4 $, $ -9z $ for $ z \geq -4 $.

## 3. Notation Experiments

You explored various notations to achieve conciseness and elegance:
- **$ = $ Method**: Initially used a one-liner with $ = $, which was correct but overloaded (partially standard).
- **$ \wedge $ Exploration**: Proposed $ \lim_{x \to a} g(x) = \lim_{x \to a^-} g(x) \wedge \lim_{x \to a^+} g(x) $, elegant and correct with a definition, but non-standard.
- **Matrix Approach**: Evolved into the refined matrix method, balancing conciseness and correctness, acceptable in CS but not standard, now retained as an optional exploration.

---

## Examples Across Topics

### Example 1: Piecewise Function (Limit Exists)
Consider the piecewise function:

$ f(x) = \begin{cases}
x^2 & \text{if } x < 1 \\
2x - 1 & \text{if } x \geq 1
\end{cases} $

Find $ \lim_{x \to 1} f(x) $.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to 1} f(x) $
    $ \lim_{x \to 1^-} f(x) = x^2 = 1^2 = 1 $
    $ \lim_{x \to 1^+} f(x) = 2x - 1 = 2(1) - 1 = 1 $
  - **Compare and Conclude**:
    $ 1 = 1 $, so $ \lim_{x \to 1} f(x) = 1 $


### Example 2: Limit Does Not Exist (D.N.E.)
Consider the function:

$ g(t) = \begin{cases}
t^2 - t^3 & \text{if } t < 2 \\
5t - 14 & \text{if } t \geq 2
\end{cases} $

Find $ \lim_{t \to 2} g(t) $.

**Correction Note**: The intended function (from prior discussions) is $ t^2 - t $, evaluating to $ 2 $, leading to D.N.E.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{t \to 2} g(t) $
    $ \lim_{t \to 2^-} g(t) = t^2 - t = 2^2 - 2 = 4 - 2 = 2 $
    $ \lim_{t \to 2^+} g(t) = 5t - 14 = 5(2) - 14 = 10 - 14 = -4 $
  - **Compare and Conclude**:
    $ 2 \neq -4 $, so $ \lim_{t \to 2} g(t) \text{ D.N.E.} $

### Example 3: Showing D.N.E. with Absolute Function
Consider the function with an absolute value:

$ h(x) = \frac{|x|}{x} $

Find $ \lim_{x \to 0} h(x) $.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to 0} \frac{|x|}{x} $
    $ \lim_{x \to 0^-} \frac{|x|}{x} = \frac{-x}{x} = -1 \quad (\text{since } |x| = -x \text{ for } x < 0) $
    $ \lim_{x \to 0^+} \frac{|x|}{x} = \frac{x}{x} = 1 \quad (\text{since } |x| = x \text{ for } x > 0) $
  - **Compare and Conclude**:
    $ -1 \neq 1 $, so $ \lim_{x \to 0} \frac{|x|}{x} \text{ D.N.E.} $

### Example 4: Limit of $ g(x) $ at $ x = -3 $
Consider the piecewise function:

$ g(x) = \begin{cases}
5x + 24 & \text{if } x < -3 \\
x^2 - 3 & \text{if } -3 \leq x < 4 \\
1 - 2x & \text{if } x \geq 4
\end{cases} $

Find $ \lim_{x \to -3} g(x) $.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to -3} g(x) $
    $ \lim_{x \to -3^-} g(x) = 5x + 24 = 5(-3) + 24 = -15 + 24 = 9 $
    $ \lim_{x \to -3^+} g(x) = x^2 - 3 = (-3)^2 - 3 = 9 - 3 = 6 $
  - **Compare and Conclude**:
    $ 9 \neq 6 $, so $ \lim_{x \to -3} g(x) \text{ D.N.E.} $

### Example 5: Limit Where Absolute Function Allows Existence
Consider the function:

$ f(x) = \frac{|x|}{x + 1} $

Find $ \lim_{x \to 0} f(x) $.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to 0} \frac{|x|}{x + 1} $
    $ \lim_{x \to 0^-} \frac{|x|}{x + 1} = \frac{-x}{x + 1} \to \frac{0}{1} = 0 \quad (\text{since } |x| = -x \text{ for } x < 0) $
    $ \lim_{x \to 0^+} \frac{|x|}{x + 1} = \frac{x}{x + 1} \to \frac{0}{1} = 0 \quad (\text{since } |x| = x \text{ for } x > 0) $
  - **Compare and Conclude**:
    $ 0 = 0 $, so $ \lim_{x \to 0} \frac{|x|}{x + 1} = 0 $

### Example 6: Absolute Function with Odd Power, Symmetric D.N.E.
Consider the function:

$ k(x) = \frac{x - 2}{|x - 2|^3} $

Find $ \lim_{x \to 2} k(x) $.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to 2} \frac{x - 2}{|x - 2|^3} $
    $ \lim_{x \to 2^-} \frac{x - 2}{|x - 2|^3} = \frac{x - 2}{(2 - x)^3} = \frac{-(2 - x)}{(2 - x)^3} = \frac{-1}{(2 - x)^2} \to -\infty $
    $ \lim_{x \to 2^+} \frac{x - 2}{|x - 2|^3} = \frac{x - 2}{(x - 2)^3} = \frac{1}{(x - 2)^2} \to +\infty $
  - **Compare and Conclude**:
    $ -\infty \neq +\infty $, so $ \lim_{x \to 2} \frac{x - 2}{|x - 2|^3} \text{ D.N.E.} $

### Example 7: Problem 27 - $ \lim_{h \to 0} \frac{|h|}{h} $
- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{h \to 0} \frac{|h|}{h} $
    $ \lim_{h \to 0^-} \frac{|h|}{h} = \frac{-h}{h} = -1 $
    $ \lim_{h \to 0^+} \frac{|h|}{h} = \frac{h}{h} = 1 $
  - **Compare and Conclude**:
    $ -1 \neq 1 $, so $ \lim_{h \to 0} \frac{|h|}{h} \text{ D.N.E.} $

### Example 8: Problem 28 - $ \lim_{t \to 2} \frac{2 - t}{|t - 2|} $
- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{t \to 2} \frac{2 - t}{|t - 2|} $
    $ \lim_{t \to 2^-} \frac{2 - t}{|t - 2|} = \frac{2 - t}{2 - t} = 1 $
    $ \lim_{t \to 2^+} \frac{2 - t}{|t - 2|} = \frac{2 - t}{t - 2} = \frac{-(t - 2)}{t - 2} = -1 $
  - **Compare and Conclude**:
    $ 1 \neq -1 $, so $ \lim_{t \to 2} \frac{2 - t}{|t - 2|} \text{ D.N.E.} $

### Example 9: Problem 29 - $ \lim_{w \to -5} \frac{|2w + 10|}{w + 5} $
- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{w \to -5} \frac{|2w + 10|}{w + 5} $
    $ \lim_{w \to -5^-} \frac{|2w + 10|}{w + 5} = \frac{-2w - 10}{w + 5} = \frac{-2(w + 5)}{w + 5} = -2 $
    $ \lim_{w \to -5^+} \frac{|2w + 10|}{w + 5} = \frac{2w + 10}{w + 5} = \frac{2(w + 5)}{w + 5} = 2 $
  - **Compare and Conclude**:
    $ -2 \neq 2 $, so $ \lim_{w \to -5} \frac{|2w + 10|}{w + 5} \text{ D.N.E.} $

### Example 10: Problem 30 - $ \lim_{x \to 4} \frac{|x - 4|}{x^2 - 16} $
- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to 4} \frac{|x - 4|}{x^2 - 16} $
    $ \lim_{x \to 4^-} \frac{|x - 4|}{x^2 - 16} = \frac{4 - x}{(x - 4)(x + 4)} = \frac{-1}{x + 4} \to \frac{-1}{8} $
    $ \lim_{x \to 4^+} \frac{|x - 4|}{x^2 - 16} = \frac{x - 4}{(x - 4)(x + 4)} = \frac{1}{x + 4} \to \frac{1}{8} $
  - **Compare and Conclude**:
    $ \frac{-1}{8} \neq \frac{1}{8} $, so $ \lim_{x \to 4} \frac{|x - 4|}{x^2 - 16} \text{ D.N.E.} $

### Example 11: Rationalizing Denominator Doesn’t Resolve Division by Zero
Consider the function:

$ f(x) = \frac{1}{\sqrt{x} - 2} $

Find $ \lim_{x \to 4} f(x) $.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to 4} \frac{1}{\sqrt{x} - 2} $
    - Rationalize denominator: $ \frac{1}{\sqrt{x} - 2} \cdot \frac{\sqrt{x} + 2}{\sqrt{x} + 2} = \frac{\sqrt{x} + 2}{x - 4} $.
    - $ \lim_{x \to 4^-} \frac{\sqrt{x} + 2}{x - 4} $:
      - Numerator: $ \sqrt{x} + 2 \to 4 $.
      - Denominator: $ x - 4 \to 0^- $, so $ \frac{4}{0^-} \to -\infty $.
    - $ \lim_{x \to 4^+} \frac{\sqrt{x} + 2}{x - 4} $:
      - Numerator: $ \sqrt{x} + 2 \to 4 $.
      - Denominator: $ x - 4 \to 0^+ $, so $ \frac{4}{0^+} \to +\infty $.
  - **Compare and Conclude**:
    $ -\infty \neq +\infty $, so $ \lim_{x \to 4} \frac{1}{\sqrt{x} - 2} \text{ D.N.E.} $
  - **Note**: Rationalizing the denominator didn’t eliminate the division by zero; the denominator $ x - 4 \to 0 $.

### Example 12: Rationalizing Denominator Resolves Division by Zero
Consider the function:

$ f(x) = \frac{x - 9}{\sqrt{x} - 3} $

Find $ \lim_{x \to 9} f(x) $.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to 9} \frac{x - 9}{\sqrt{x} - 3} $
    - Rationalize denominator: $ \frac{(x - 9)(\sqrt{x} + 3)}{(\sqrt{x} - 3)(\sqrt{x} + 3)} = \frac{(x - 9)(\sqrt{x} + 3)}{x - 9} = \sqrt{x} + 3 \quad (x \neq 9) $.
    - $ \lim_{x \to 9} (\sqrt{x} + 3) = \sqrt{9} + 3 = 6 $.
  - **Compare and Conclude**:
    $ \lim_{x \to 9} \frac{x - 9}{\sqrt{x} - 3} = 6 $
  - **Note**: Rationalizing the denominator resolved the division by zero by canceling the $ x - 9 $, leaving an expression with no denominator approaching 0.

### Example 13: Rationalizing Denominator Doesn’t Resolve Division by Zero
Consider the function:

$ f(x) = \frac{x + 1}{\sqrt{x} - 1} $

Find $ \lim_{x \to 1} f(x) $.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to 1} \frac{x + 1}{\sqrt{x} - 1} $
    - Rationalize denominator: $ \frac{(x + 1)(\sqrt{x} + 1)}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \frac{(x + 1)(\sqrt{x} + 1)}{x - 1} $.
    - $ \lim_{x \to 1^-} \frac{(x + 1)(\sqrt{x} + 1)}{x - 1} $:
      - Numerator: $ (x + 1)(\sqrt{x} + 1) \to 4 $.
      - Denominator: $ x - 1 \to 0^- $, so $ \frac{4}{0^-} \to -\infty $.
    - $ \lim_{x \to 1^+} \frac{(x + 1)(\sqrt{x} + 1)}{x - 1} $:
      - Numerator: $ (x + 1)(\sqrt{x} + 1) \to 4 $.
      - Denominator: $ x - 1 \to 0^+ $, so $ \frac{4}{0^+} \to +\infty $.
  - **Compare and Conclude**:
    $ -\infty \neq +\infty $, so $ \lim_{x \to 1} \frac{x + 1}{\sqrt{x} - 1} \text{ D.N.E.} $
  - **Note**: Rationalizing the denominator didn’t eliminate the division by zero because there was no cancellation with $ x - 1 $.

### Example 14: Limit of $ g(x) $ at $ x = 4 $
Consider the piecewise function:

$ g(x) = \begin{cases}
5x + 24 & \text{if } x < -3 \\
x^2 - 3 & \text{if } -3 \leq x < 4 \\
1 - 2x & \text{if } x \geq 4
\end{cases} $

Find $ \lim_{x \to 4} g(x) $.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to 4} g(x) $
    $ \lim_{x \to 4^-} g(x) = x^2 - 3 = 4^2 - 3 = 16 - 3 = 13 $
    $ \lim_{x \to 4^+} g(x) = 1 - 2x = 1 - 2(4) = 1 - 8 = -7 $
  - **Compare and Conclude**:
    $ 13 \neq -7 $, so $ \lim_{x \to 4} g(x) \text{ D.N.E.} $

### Example 15: Limit of $ g(x) $ at $ x = 12 $
Consider the same function:

$ g(x) = \begin{cases}
5x + 24 & \text{if } x < -3 \\
x^2 - 3 & \text{if } -3 \leq x < 4 \\
1 - 2x & \text{if } x \geq 4
\end{cases} $

Find $ \lim_{x \to 12} g(x) $.

- **Standard Method (Preferred)**:
  - **Definition and Computation**:
    $ \lim_{x \to 12} g(x) $
    $ \lim_{x \to 12^-} g(x) = 1 - 2x = 1 - 2(12) = 1 - 24 = -23 $
    $ \lim_{x \to 12^+} g(x) = 1 - 2x = 1 - 2(12) = 1 - 24 = -23 $
  - **Compare and Conclude**:
    $ -23 = -23 $, so $ \lim_{x \to 12} g(x) = -23 $

## Conclusion

Understanding left-hand and right-hand limits is crucial for evaluating limits, especially for piecewise functions and those involving discontinuities. Rationalizing the denominator doesn’t inherently eliminate division by zero—it requires a cancellation to remove the term (e.g., $ x - a^2 $) causing the denominator to approach zero, as you’ve insightfully concluded. Your work with absolute functions (problems 27–30) highlights patterns like symmetric D.N.E., while your exploration of rationalizing the denominator deepens the understanding of limit techniques.

## Notes
- **Piecewise Context**: All examples assume piecewise definitions based on given expressions.
- **Proof Interpretation**: The method acts as a proof by contradiction when the limit does not exist, and as a direct proof when the limit exists.
- **Rationale**: The standard method (4 lines) is your preferred choice for its alignment with formal mathematics.
- **Learning Journey**: This notebook consolidates your exploration of limit methods, piecewise functions, absolute functions, and rationalizing, reflecting your growth.
