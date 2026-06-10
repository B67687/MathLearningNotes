---
title: "Advancements Report 21St March 2025"
source_notebook: "calculus/advancements-report-21st-march-2025.ipynb"
archived_notebook: "archive/notebooks/calculus/advancements-report-21st-march-2025.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

## Demonstrating Inequality Manipulation with Absolute Values

### Introduction

This notebook demonstrates how to manipulate inequalities involving absolute values, specifically focusing on adding constants to all parts of the inequality. We'll emphasize the importance of applying operations to *all parts* of the expanded inequality.

We'll illustrate this with an example similar to the epsilon-delta proof of $\lim_{x \to 2} x^2 = 4$.

### Example: Bounding |x + 2|

Let's say we have $|x - 2| < c$, where $c > 0$. We want to find an upper bound for $|x + 2|$.

### Step 1: Expand the Absolute Value Inequality

$|x - 2| < c$ is equivalent to:

$-c < x - 2 < c$

### Step 2: Add 4 to *All Parts*

This is the crucial step. We add 4 to *all three parts* of the inequality:

$-c + 4 < x - 2 + 4 < c + 4$

$-c + 4 < x + 2 < c + 4$

**Important Note:** We must add 4 to *every* part of the inequality to maintain its validity. We cannot just add 4 inside the absolute value without also adjusting the bounds.

### Step 3: Take the Absolute Value

Now we want to find a bound for $|x + 2|$.

Since $-c + 4 < x + 2 < c + 4$, we can say:

$|x + 2| < \max(|-c + 4|, |c + 4|)$

### Step 4: Simplify (in our case)

In our epsilon-delta proof, we typically choose a small positive value for 'c' (e.g., c=1).

If we assume $c>0$, then $c+4$ will always be positive, and therefor $|c+4| = c+4$.

If we assume $c < 4$, then $-c+4$ will be positive, and therefore $|-c+4| = -c+4$.

Since $c+4 > -c+4$ for any positive c, we can simplify:

$|x + 2| < c + 4$

---

## Keeping 1/N Direct in Limit Proofs Involving Infinity

### Introduction

This notebook explores the strategy of directly using `1/N` (or `-1/N`) in epsilon-delta-like proofs when dealing with limits that approach infinity, especially when the function is a reciprocal. We'll focus on why this is often a more direct and clear approach.

### General Principle

When proving limits that approach infinity (either positive or negative) for functions involving reciprocals (like `1/x`), it's often more intuitive to work directly with the reciprocal of the target value (`N` or `-N`).

Instead of introducing a separate `delta` and then trying to relate it to `N` later, we can often directly express `delta` or `-delta` in terms of `1/N` (or `-1/N`). This avoids unnecessary sign changes and makes the proof more straightforward.

### Example: lim (x->0-) 1/x = -infinity

Let's illustrate this with the proof of:

$$\lim_{x \to 0^-} \frac{1}{x} = -\infty$$

**Traditional Approach (with a detour):**

1.  Assume `N < 0`.
2.  Find `delta > 0` such that if `0 > x > -delta`, then `1/x < N`.
3.  We might initially try to relate `delta` to `N` indirectly, leading to more sign manipulations.

**Direct Approach (Using 1/N):**

1.  Assume `N < 0`.
2.  Let `-delta = 1/N`. This means `delta = -1/N`. Since `N < 0`, `delta > 0`.
3.  Assume `0 > x > -delta`.
4.  Substitute `-delta = 1/N`: `0 > x > 1/N`.
5.  Take the reciprocal (and flip the inequalities): `-infinity < 1/x < N`.

**Why the Direct Approach is Better:**

- **Avoids Sign Changes:** By directly setting `-delta = 1/N`, we avoid having to change the sign of `1/N` twice.
- **Clarity:** The relationship between `delta` and `N` is immediately clear.
- **Intuition:** It aligns better with the reciprocal nature of the function.

### Key Takeaway

When dealing with limits approaching infinity for reciprocal functions, consider directly using `1/N` (or `-1/N`) to express `delta` or `-delta`. This often leads to a more direct, clear, and intuitive proof.

---

## Choosing the Right Notation for Minimum in Limit Proofs

### Introduction

In mathematical proofs, particularly those involving limits and epsilon-delta arguments, clarity and simplicity are paramount. While various notations exist for representing the minimum of a set of values, the `min()` function is often the most appropriate and best practice, especially in introductory contexts.

This notebook will discuss why `min()` is generally preferred in proofs like the one shown in the image and when alternative notations might be considered.

### Why `min()` is Best Practice in Introductory Limit Proofs

- **Clarity and Simplicity:**
    - The `min()` function directly conveys the idea of selecting the smallest value from a set of options, making the proof easier to understand.
    - It avoids introducing potentially confusing or unfamiliar notations.
- **Contextual Appropriateness:**
    - Proofs like the one in the image typically involve comparing a small number of values or expressions to determine the minimum.
    - In such cases, `min()` is perfectly adequate and widely recognized.
- **Pedagogical Value:**
    - For students learning about limits and epsilon-delta proofs, `min()` is a simple and effective tool.
    - It helps them focus on the conceptual understanding of the proof rather than getting bogged down in complex notations.

### When Alternative Notations Might Be Considered

- **Large Sets:**
    - If you were dealing with the minimum of a very large or infinite set, indexed notation (e.g., $\min_{i=1}^{n} x_i$) or the infimum (inf) might be more appropriate.
- **Formal Mathematical Contexts:**
    - In advanced analysis or related fields, you might encounter other notations like the wedge symbol (∧), but these are less common in introductory settings.
- **Computer Science:**
    - In computer science, especially in algorithms or data structures, you might see indexed notation or other specialized notations.

### Example: Proof from the Image

In the proof image provided, the goal is to show:

$$\lim_{x \to 0^-} \frac{1}{x} = -\infty$$

In this proof, the choice of $\delta$ is crucial. Using `min()` to define $\delta$ is the most straightforward way to convey that we are selecting the smaller of two values to ensure the proof works.

### Conclusion

For introductory limit proofs and similar mathematical contexts, the `min()` function is generally the best practice due to its clarity, simplicity, and contextual appropriateness. It allows for greater focus on the conceptual understanding of the proof.

---

## Epsilon-Delta Proof Procedure and Variable Definition Practices

### Epsilon-Delta Proof Procedure

The epsilon-delta proof is a rigorous way to show that a limit exists. Here's a general procedure:

1.  **State the Limit:** Clearly write the limit you want to prove, e.g., $\lim_{x \to c} f(x) = L$.

2.  **State the Definition:** Recall the epsilon-delta definition: For every $\epsilon > 0$, there exists a $\delta > 0$ such that if $0 < |x - c| < \delta$, then $|f(x) - L| < \epsilon$.

3.  **Start with |f(x) - L|:** Begin by manipulating the expression $|f(x) - L|$ algebraically to relate it to $|x - c|$.

4.  **Find a Bound for |x - c|:**
    - If necessary, find a bound for other terms in the expression involving *x*. This often involves assuming a bound for $|x - c|$ (e.g., $|x - c| < 1$).
    - Use this bound to find an upper limit for the other terms.

5.  **Express |x - c| in Terms of Epsilon:**
    - Use the manipulated expression and the bounds to find a condition on $|x - c|$ that ensures $|f(x) - L| < \epsilon$.
    - This will give you an inequality of the form $|x - c| < \text{expression involving } \epsilon$.

6.  **Choose Delta:**
    - Choose $\delta$ to satisfy the condition found in the previous step.
    - If you used a preliminary bound for $|x - c|$, you might need to choose $\delta$ as the minimum of that bound and the expression involving $\epsilon$.

7.  **Verify the Condition:**
    - Show that if $0 < |x - c| < \delta$, then $|f(x) - L| < \epsilon$.

8.  **Conclusion:** State that you have shown the limit using the epsilon-delta definition.

### Common Practice: Defining Variables in Proofs

In mathematical proofs, it's essential to define variables clearly and unambiguously. Here's a common practice:

* **Direct Definition:** You can directly define a variable with its properties using set notation and inequalities. For example:
    - `c ∈ R, c > 0` (This defines 'c' as a positive real number).
    - `n ∈ Z, n > 5` (This defines 'n' as an integer greater than 5).

* **Why This Works:**
    - It is concise and removes any ambiguity.
    - It is a standard way to introduce variables in mathematical writing.

* **Optional Explicit Introduction:** If you want to be extra explicit, you can add a phrase before the direct definition:
    - "Let 'c' be a positive real number. That is, let `c ∈ R, c > 0`."

* **Clarity is Key:** Always prioritize clarity and avoid any potential misinterpretations when defining variables.

---

## Squaring Inequalities in Epsilon-Delta Proofs: A Cautionary Note

### Introduction

When working with epsilon-delta proofs, we often need to manipulate inequalities involving absolute values. A common operation is squaring the terms within an inequality. However, it's crucial to understand when this operation is valid and when it requires extra care.

### The Pitfall: Squaring Without Considering Signs

A common misconception is that if $a < b < c$, then $a^2 < b^2 < c^2$ always holds. This is **not true** in general.

**The Correct Principle:**

* If $0 \le a < b < c$, then $a^2 < b^2 < c^2$.
* However, if you have negative numbers or a mix of positive and negative numbers, you cannot simply square all parts of the inequality.

### Example: |x - 1| < c

Let's illustrate this with an example from a typical epsilon-delta proof:

1.  We start with $|x - 1| < c$, where 'c' is a positive number.
2.  This means $-c < x - 1 < c$.
3.  Adding 1 to all sides, we get $1 - c < x < 1 + c$.

**When Squaring is Safe:**

* If $c \le 1$, then $1 - c \ge 0$, and we can safely square all parts: $(1 - c)^2 < x^2 < (1 + c)^2$.
* In this case, $|x^2|$ is bounded by the larger of $(1 - c)^2$ and $(1 + c)^2$.

**When Squaring Requires Caution:**

* If $c > 1$, then $1 - c < 0$. In this case, we cannot directly square all parts.
* We need to consider the range of $x^2$ more carefully. The smallest value of $x^2$ will be 0, and the largest value will be $(1 + c)^2$.

### Context: Epsilon-Delta Proofs and Small 'c'

In epsilon-delta proofs, we typically choose 'c' (or our initial bound for |x-a|) to be a small positive number (often c = 1) to simplify the bounding process.

**Therefore, in many cases, we *can* directly square the inequality.**

### Key Takeaway

* Always consider the signs of the numbers when squaring inequalities.
* In epsilon-delta proofs, where we typically choose small positive bounds, squaring is often safe.
* However, it's essential to understand the underlying principle to avoid errors.

---

## Inequalities: The Impact of Negatives and Reciprocals

### Introduction

When working with inequalities in mathematics, it's crucial to be mindful of certain operations that can change the direction of the inequality signs. This notebook focuses on two such operations: multiplying/dividing by negatives and taking reciprocals.

### 1. Multiplying/Dividing by Negatives

**Rule:** When you multiply or divide all parts of an inequality by a negative number, you *must* reverse the direction of the inequality signs.

**Example:**

-   If $2 < 4$, then multiplying by -1 gives $-2 > -4$.
-   If $-6 < -3$, then dividing by -3 gives $2 > 1$.

**Explanation:**

Multiplying or dividing by a negative number reflects the numbers across the number line, effectively reversing their relative order.

### 2. Taking Reciprocals

**Rule:** When you take the reciprocal (1/x) of all parts of an inequality, you *must* reverse the direction of the inequality signs, but *only if* the numbers have the same sign.

**Example (Same Sign):**

-   If $2 < 4$, then taking reciprocals gives $1/2 > 1/4$.
-   If $-4 < -2$, then taking reciprocals gives $-1/4 > -1/2$.

**Example (Mixed Signs):**

-   If $-2 < 4$, you cannot simply take reciprocals. You need to consider the ranges carefully.

**Explanation:**

The reciprocal function (1/x) is a decreasing function for positive numbers and decreasing for negative numbers. This means that as a number increases, its reciprocal decreases, and vice versa.

### Key Takeaways

-   **Always be mindful of negatives** when multiplying or dividing inequalities.
-   **Always be mindful of reciprocals** when taking reciprocals of inequalities.
-   **Consider the signs of the numbers** involved to determine whether the inequality signs need to be flipped.

By remembering these points, you can accurately manipulate inequalities in your mathematical work.

---

## Interval Width and Center in Inequalities with Absolute Values

### Introduction

When manipulating inequalities with absolute values, it's crucial to understand how operations affect the interval's width and center. This notebook explores this concept and its relevance in epsilon-delta proofs.

### Interval Width and Center

Consider the inequality |a| < b, where b > 0.

-   **Center:** The interval is centered at 0.
-   **Width:** The width of the interval is 2b.

Now, consider the inequality |a - 3| < b + 3, where b > 0.

-   **Center:** The interval is centered at 3.
-   **Width:** The width of the interval is still 2b.

### Effect of Operations Inside Absolute Values

When you perform operations *inside* an absolute value (e.g., |a - 3|), you are shifting the center of the interval.

**However:**

-   The *width* of the interval remains the same.
-   In epsilon-delta proofs, we are primarily concerned with the *width* of the interval, not its center.

### Relevance in Epsilon-Delta Proofs

In epsilon-delta proofs, we often manipulate inequalities to find bounds. The shifting of the interval's center is acceptable as long as the width remains consistent.

**Example:**

-   If |x - 2| < δ, we can derive |x + 1| < δ + 3.
-   The center has shifted, but the width remains consistent.

### Key Takeaways

-   Operations inside absolute values shift the interval's center.
-   The width of the interval remains consistent.
-   In epsilon-delta proofs, we are primarily concerned with the width.

---

## Square Roots and Modulus: A Reminder

### Introduction

When taking the square root of a number, it's crucial to remember that the result is always the modulus (absolute value) of the number, unless we know the number is positive.

### Square Root and Modulus

-   The square root of a number is defined as the non-negative value that, when squared, gives the original number.
-   Therefore, the square root of x² is |x|, not x.

**Example:**

-   √((-3)²) = √9 = 3 = |-3|
-   √(3²) = √9 = 3 = |3|

### When Modulus is Not Needed

-   If we know that the number inside the square root is positive, we can omit the modulus sign.

**Example:**

-   If x > 0, then √(x²) = x

### Relevance in Limit Proofs

This concept is particularly relevant in limit proofs, especially when dealing with limits that tend to infinity.

**Example:**

-   When simplifying expressions involving square roots, always remember to include the modulus sign unless you know the number is positive.

### Reminder again

- When taking the square root of both sides of an inequality involving a squared variable, remember to use the absolute value of that variable. For example, if $M^2 > \frac{3}{N}$, then $\sqrt{M^2} > \sqrt{\frac{3}{N}}$, which leads to $|M| > \sqrt{\frac{3}{N}}$.

- You do not need the absolute value on the side of the inequality that does not contain the squared variable.

- Square roots of negative numbers are imaginary numbers. Therefore, $-\sqrt{-\frac{3}{N}}$ is an imaginary number, while $\sqrt{\frac{3}{N}}$ is a real number (assuming N is positive). Consequently, these two expressions cannot be combined or considered equal.

### Key Takeaways

-   The square root of x² is |x|.
-   Omit the modulus sign only when you know the number is positive.
-   Be mindful of this rule in limit proofs.

---

## Limits as $x$ Approaches Negative Infinity: Key Concepts

### Introduction

When dealing with limits as $x$ approaches negative infinity, there are some important concepts to remember. This notebook will outline the key things to keep in mind, especially when working with absolute values and inequalities.

### Understanding the Limit

-   When we write $\lim_{x \to -\infty} f(x) = L$, we're interested in the behavior of the function $f(x)$ as $x$ becomes increasingly negative.
-   This means we're looking for a negative number $N$ such that if $x < N$, then $f(x)$ satisfies the epsilon condition.

### Absolute Values and Inequalities

-   When dealing with inequalities involving absolute values, remember that $|x| > a$ means $x > a$ or $x < -a$.
-   In the context of limits as $x \to -\infty$, we're primarily interested in the $x < -a$ solution.

### Converting $|x| > a$ to $x < -a$

-   When you have $|x| > a$ and you're considering the limit as $x \to -\infty$, you need to convert it to $x < -a$.
-   This is because we're only interested in the negative values of $x$ that satisfy the inequality.

### Relationship Changes, Implication Holds

-   When you convert $|x| > a$ to $x < -a$, the relationship between $x$ and $a$ changes.
-   However, the implication still holds: if $x < -a$, then $|x| > a$.
-   We're not trying to preserve the exact same relationship; we're trying to find a condition on $x$ that guarantees the epsilon condition is met.

### Example: $\lim_{x \to -\infty} \frac{1}{x^2} = 0$

- In the proof of $\lim_{x \to -\infty} \frac{1}{x^2} = 0$, we encounter the inequality: $|x| > \frac{1}{\sqrt{\epsilon}}$.
- Since we're considering the limit as $x \to -\infty$, we convert this to: $x < -\frac{1}{\sqrt{\epsilon}}$.
- We then set $N = -\frac{1}{\sqrt{\epsilon}}$ to complete the proof.

### Key Takeaways

-   When dealing with limits as $x \to -\infty$, focus on the negative values of $x$.
-   Convert $|x| > a$ to $x < -a$ when appropriate.
-   Remember that the relationship changes, but the implication still holds.

---

## The "Devious" Cancellation in lim (x->0) -3/x² = -∞

### Introduction

The limit $\lim_{x \to 0} \frac{-3}{x^2} = -\infty$ presents a subtle interplay between the negative numerator and the reciprocal nature of the function. This notebook explores why this limit behaves as it does and why it can be considered "devious."

### Understanding the Limit

We are investigating the behavior of the function $f(x) = \frac{-3}{x^2}$ as $x$ approaches 0 from both sides. We want to show that for any negative number $M$ (no matter how large in magnitude), we can find a $\delta > 0$ such that if $0 < |x| < \delta$, then $\frac{-3}{x^2} < M$.

### The "Devious" Cancellation

1.  **Negative Numerator (-3):** The negative sign in the numerator ensures that the function's output is always negative for any non-zero value of $x$.

2.  **Reciprocal (1/x²):** The $x^2$ in the denominator means that as $x$ approaches 0, the denominator becomes very small, causing the magnitude of the fraction to become very large.

3.  **The Result:** The combination of these two factors leads to the function approaching negative infinity as $x$ approaches 0.

### Why It's "Devious"

-   **Counterintuitive Nature:** It might seem counterintuitive that the negative sign doesn't directly affect the limit's behavior in the same way it would in other cases.
-   **Sign Changes:** The sign changes that occur when multiplying/dividing by negative numbers and taking reciprocals can be confusing and obscure the overall trend.
-   **Focus on Magnitude:** The focus shifts to the magnitude of the function, rather than the sign, which can be misleading.

### The Key Insight

The effects of the negative sign and the reciprocal "cancel out" in terms of the limit's overall behavior.

-   The negative sign ensures that the function approaches negative infinity.
-   The reciprocal ensures that the function's magnitude becomes infinitely large.

### Conclusion

The limit $\lim_{x \to 0} \frac{-3}{x^2} = -\infty$ highlights the importance of carefully considering the interplay between different factors in a function, especially when dealing with limits involving infinity.
