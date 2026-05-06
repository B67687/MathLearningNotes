---
title: "**Summary of Math Concepts Learned**"
source_notebook: "trigonometry/advancements-report-10th-march-2025.ipynb"
archived_notebook: "archive/notebooks/trigonometry/advancements-report-10th-march-2025.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# **Summary of Math Concepts Learned**

## I. Foundations & Pre-Calculus

- **Vectors Before Calculus:** Strong recommendation to study **vectors before starting calculus**, especially for fields like physics, engineering, CS, and AI. Vectors build a crucial geometric foundation for multivariable calculus.
- **Solid Math Foundation:** Emphasized the importance of a **solid math foundation** (trigonometry and geometry) for vectors and advanced math. Conceptual understanding is key, not just memorization.

## II. Polar Coordinates

- **Polar Coordinates:** Explored **polar coordinates** and their relationship to Cartesian coordinates.

## III. Trigonometric Functions: Deep Dive

- **Transformations & Periodicity:** Explored coefficients' effects on polar equations and function periods:
    - **Inside Coefficients (Angular Frequency) (e.g., $\cos(k\theta)$):** Change **periodicity** (tracing speed w.r.t. $\theta$) and **angular frequency**. $k > 1$ faster (shorter period), $0 < k < 1$ slower (longer period). Period becomes $2\pi/|k|$.
    - **Outside Coefficients (Radial Scale/Amplitude) (e.g., $C \cos(\theta)$):** Change **radial scale** or **amplitude**, affecting the overall size of the curve.
- **Special Polar Forms:**
    - **$r = a \sec(\theta)$ and $r = a \csc(\theta)$:** Represent **straight lines** ($x = a$ and $y = a$ in Cartesian). "Flat vertex" appearance in polar form is inherent to straight lines.
- **Fundamental Properties:**
    - **Even/Odd Functions:**
        - **Cosine ($\cos \theta$): Even Function.** $\cos(-\theta) = \cos(\theta)$. Geometrically explained by x-coordinate invariance under x-axis reflection on the unit circle.
        - **Sine ($\sin \theta$): Odd Function.** $\sin(-\theta) = -\sin(\theta)$. Geometrically explained by y-coordinate sign flip under x-axis reflection on the unit circle.
        - **Tangent ($\tan \theta$): Odd Function.** $\tan(-\theta) = -\tan(\theta)$.

    - **Deriving from First Principles:** Value of **deriving formulas** (e.g., cosine double-angle to get $\cos^2(x)$ and $\sin^2(x)$). Enhances understanding and retention.
    - **Refined Periodicity Understanding:** $2\pi$ period is inherent to the **trig function itself** (cosine, sine) regarding its *input angle*. Coefficients scale this period in terms of input $\theta$ for functions like $\cos(k\theta)$.
    - **Ranges of Trigonometric Functions:**
        - **Sine ($\sin \theta$) and Cosine ($\cos \theta$): Bounded Range $[-1, 1]$.**  The values of $\sin \theta$ and $\cos \theta$ are *always* between -1 and 1, inclusive.  This is fundamentally due to their definition on the unit circle as ratios of sides in a right triangle or as coordinates on the unit circle.  This bounded range is crucial in understanding the behavior of these functions and solving trigonometric equations.
        - **Secant ($\sec \theta$) and Cosecant ($\csc \theta$): Unbounded Range $(-\infty, -1] \cup [1, \infty)$.** The values of $\sec \theta$ and $\csc \theta$ are *always* outside the interval $(-1, 1)$.  Their absolute values are always greater than or equal to 1 ($|\sec \theta| \ge 1$, $|\csc \theta| \ge 1$). This is because they are reciprocals of cosine and sine respectively, and when $\cos \theta$ or $\sin \theta$ are close to zero, their reciprocals become very large (in magnitude).  Therefore, they have a *minimal absolute value* of 1 and extend to infinity. This is in *direct contrast* to the bounded nature of sine and cosine.

## IV. Inverse Trigonometric Functions

- **Inverse vs. Direct Trig Functions:**
    - **Trigonometric Functions ($\sin$, $\cos$, $\tan$): Angle $\rightarrow$ Ratio.** Take an **angle** as input and output a **ratio**.
    - **Inverse Trigonometric Functions ($\arcsin$, $\arccos$, $\arctan$): Ratio $\rightarrow$ Angle.** Take a **ratio** as input and output an **angle**. "Arc-" prefix signifies finding the *arc* on the unit circle.
- **Crucial Note: Principal Domains and Ranges for Inverse Trig Functions:**
    - **Inverse trig functions have *principal ranges* to ensure they are well-defined functions (single output for each input).**
    - **Always be mindful of these principal ranges when working with inverse trig functions to provide the *principal value* of the angle.**
        - **Arccosine ($\arccos$ or $\cos^{-1}$): Principal Range is $[0, \pi]$ (or $[0^\circ, 180^\circ]$).**
        - **Arcsine ($\arcsin$ or $\sin^{-1}$): Principal Range is $[-\pi/2, \pi/2]$ (or $[-90^\circ, 90^\circ]$).**
        - **Arctangent ($\arctan$ or $\tan^{-1}$): Principal Range is $(-\pi/2, \pi/2)$ (or $(-90^\circ, 90^\circ)$).**
- **Arccosine ($\arccos$ or $\cos^{-1}$): Neither Even nor Odd.** $\arccos(-x) = \pi - \arccos(x)$. Loses even property due to domain restriction $[0, \pi]$ needed for inverse function definition (cosine is not one-to-one over its full domain).
- **Arcsine ($\arcsin$ or $\sin^{-1}$) & Arctangent ($\arctan$ or $\tan^{-1}$): Odd Functions.** $\arcsin(-x) = -\arcsin(x)$, $\arctan(-x) = -\arctan(x)$. Domain restrictions for sine and tangent to define inverses preserve odd symmetry.

## V. Solving Trigonometric Equations & Problem-Solving

- **Principal vs. Reference Angles:** Essential for finding trig values in all quadrants. Reference angles relate angles back to Quadrant I. **Always explicitly write down the reference angle** when finding solutions.
- **Considering All Quadrants:** **Crucial to consider all four quadrants** to find complete solutions for trigonometric equations.
- **Quadrant Signs (ASTC Rule):** Mastery of ASTC rule for determining signs of trigonometric functions in each quadrant.
- **Zero Product Property:** Applied **zero product property** via factoring to solve trig equations.
- **Quadratic Equations in Trigonometry:** Quadratic equations frequently arise and require quadratic formula or factoring techniques.
- **Range Awareness:** Importance of knowing function **ranges**. **Be aware that sine and cosine functions always have a range within $[-1, 1]$**. Use this to identify impossible equations and valid solutions quickly.
- **Adjusting Interval for Trigonometric Equations with Coefficients:**
    - When solving equations like $\text{trig\_function}(kt) = \text{value}$ for $t$ in a given interval $[a, b]$, adjust the interval for the *argument* ($kt$) at the beginning using the Step-by-Step Interval Adjustment Process (see below). The given interval is always for the variable you are solving for ($t$), not directly for the angle inside the trigonometric function ($kt$).
    - Crucially, when given a negative interval, visualize angles rotating *clockwise* from the positive x-axis.


## Step-by-Step Interval Adjustment Process for Trigonometric Equations

- **1. Identify Given Interval for $t$:** Given interval for $t$: $a \le t \le b$ (or $t \in [a, b]$).
- **2. Identify Argument:** Argument of the trigonometric function: $kt$.
- **3. Transform Interval for Argument $kt$:** Transform interval for $t$ to interval for $kt$: Multiply all parts of $a \le t \le b$ by $k$ (assume $k > 0$). For division, divide all parts.
- **4. Solve for Argument $kt$ in Transformed Interval:** Solve trig equation for $kt$ in interval $ka \le kt \le kb$. Find all solutions for $kt$ using periodicity & reference angles.
- **5. Solve for Original Variable $t$:** Solve for $t$ by dividing each solution for $kt$ by $k$: $t = kt/k$.

    *Benefit:* Ensures correct number of solutions. Simplifies solving.

- **Technique: Common Denominator for Range Check:** When working with fractional angles and intervals, **convert interval boundaries to have a common denominator** (related to angle fractions) to simplify comparison and range verification. This makes it easier to see if solutions fall within the correct range.
- **Strategy: Step-by-Step Operations:** For complex algebraic manipulations, **perform one operation at a time across all parts of the equation**, writing out each step explicitly. This reduces cognitive load and significantly increases accuracy, especially with signs and fractions. **Write your own division explicitly** instead of relying solely on mental calculation for each step.
- **Integer Nature of 'n' in Periodicity:** Remember that in general solutions involving periodicity ($+ 2\pi n, n \in \mathbb{Z}$), **$n$ can *only* be integers**, not continuous real numbers. This is crucial when finding specific solutions within an interval.

- **Notation Clarity: Interval Notation vs. Set Notation:**
    - **Interval Notation (e.g., $[1, 2]$, $(a, \infty)$):** Represents a **continuous range** of real numbers. Uses $[ ]$ for included endpoints, $( )$ for excluded

## Step-by-Step Process for Trigonometric Equations

- **1. Write out the question in its totality**, remembering that the interval points to the variable itself.
- **2. Balance the equation to get an isolated trigonometric function on one side**, conventionally left.
- **3. Check the range of the trigonometric function**:
  - For **sin** and **cos**, it’s within absolute 1.
  - For **sec** and **csc**, it’s without absolute 1.
  - **Why those are the ranges comes down to how they are defined:**
    - The **hypotenuse** is the longest length in a right-angled triangle, hence defining a ratio of its other sides against the hypotenuse means that it will only ever be as close as 1.
    - Even though in a conventional sense, the ratio won’t be 1 but we realized that by altering the opposite and adjacent sides, we can push its limits to not only 1, but also -1, within a point of reference (i.e., the origin of a Cartesian plane).
    - This is why the range of **sin** and **cos** is within the absolute range of 1.
    - Likewise, we can deduce **sec** and **csc**, because putting the longest side against all its sides means that it will always be bigger than the other sides, making the ratios of hypotenuse against its other 2 sides always more than $|ratio| < 1$.
    - Extending to the Cartesian plane, we can see that it can also take on a negative aspect, which depicts its direction.
    - Thereby making the range of **sec** and **csc** without the absolute range of 1, i.e., $|ratio| > 1$.
- **4. Find the angle of reference and note it down**:
  - This is always the inverse trigonometric function of the ratio.
  - Some inverses have reasonable ways to write it out, and it has been narrowed down to the 45-45-90 triangle and the 30-60-90 triangle.
  - **Remember those ratios and its relevant angles**, or **derive on the spot**.
- **5. Find the quadrants for which the angle resides and note it down**:
  - By looking at the trigonometric function to find its relevant axes and match it with its polarity
- **6. Write down the relevant angles within principle range $0 \leq \theta \leq 2\pi$** so that we have a nice point of reference from something we know.
  - Finding relevant angles is the angle drawn from standard position to the angle drawn away from the x-axis; you can check out the previous notes for its explanation if you fail to derive the relevant quadrant angles or are unconvinced of your logic guiding there.
- **7. Equate the quadrant angles with the angle inside the trigonometric function**
- **8. Now modify the relevant interval notation for the variable to include the angle that your variable is a part of and describes**.
- **9. Modify it again, such that the intervals have the same denominator as your stated principle angles** so that it is easy to check whether periodic angles of those principle angles fall within the correct range; recommendation is to use mixed fractions at the numerator if required.
- **10. Now extend forwards and backwards from principle angles by their respective periodic cycle**:
  - $2\pi$ for **sin**, **cos**, and their reciprocals **csc**, **sec**.
  - $\pi$ for **tan** and its reciprocal **cot**.
  - It will be easy to check now that you have the interval notation readable; we can find all the angles that fit within that interval with the respective periods.
  - **An easy way to add and subtract periods is to add and subtract the denominator to the numerator**; if $2\pi$ is involved, then we advance or de-advance by twice the denominator. Let the angles have the fraction of $\frac{a}{b}$, which is a common form for angles. We will get newer angles for $\sin$, $\cos$ and their reciprocals $\csc$, $\csc$ by simply doing $\frac{a + 2b}{b}$ and $\frac{a - 2b}{b}$, to quickly expand to all the angles within the interval.
  - Likewise for $\tan$, and its reciprocal $\cot$, we get new angles by doing $\frac{a + 2b}{b}$ and $\frac{a - 2b}{b}$
  - You will find sometimes that the angles stated from the principle range are outside the intervals; it’s possible for that to happen, so simply cancel it out from the final result. Its use was just for a point of reference that you can easily start off with, whether or not it remains is up to the interval.
  - If the no range is stated, append $+2\pi n$ for $x \in \mathbb{Z}$ to account for all the periodic extensions of the quadrant angles
- **11. Now you can rebalance the equation on each angle one operation by one operation to minimize mistakes made**, and there you have it! All the angle answers to that variable!

<div style="text-align: center;">
    <img src="trigonometric-equations-solving-example.jpg">
