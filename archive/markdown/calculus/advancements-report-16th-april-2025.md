---
title: "Proving $\\lim_{\\theta \\to 0} \\frac{\\sin \\theta}{\\theta} = 1$"
source_notebook: "calculus/advancements-report-16th-april-2025.ipynb"
archived_notebook: "archive/notebooks/calculus/advancements-report-16th-april-2025.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Proving $\lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1$

We aim to prove $\lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1$ using the Squeeze Theorem and a geometric approach on a unit circle. Since $\sin \theta$ depends on the angle $\theta$, we’ll analyze $\theta$ in a range where trigonometric functions are well-defined.

## Step 1: Define the Range
To ensure $\sin \theta$, $\cos \theta$, and $\tan \theta$ are well-behaved, we choose the range $0 < |\theta| < \pi/2$. This:
- Excludes $\theta = 0$, where $\frac{\sin \theta}{\theta}$ is undefined (we take the limit as $\theta \to 0$).
- Excludes $|\theta| = \pi/2$, where $\tan \theta$ is undefined.
- Ensures $\sin |\theta| > 0$ and $\cos |\theta| > 0$, facilitating division operations.

## Step 2: Geometric Setup
Consider a unit circle centered at $O(0, 0)$ with radius 1. Define:
- Point $A$ at $(1, 0)$.
- Point $B$ at $(\cos \theta, \sin \theta)$ for $0 < \theta < \pi/2$.

The arc $AB$ has length $\theta$ (since radius = 1). The chord $AB$ is the straight line from $A$ to $B$. We’ll derive inequalities by comparing $\sin \theta$, $\theta$, and $\tan \theta$.

### Lower Bound: $\sin \theta \leq \theta$
Form right triangle $OBC$, where:
- $C$ is at $(0, \sin \theta)$, the projection of $B$ onto the y-axis.
- $OB = 1$ (hypotenuse).
- $BC = \sin \theta$ (opposite).
- $OC = \cos \theta$ (adjacent).

The arc $AB$ has length $\theta$. The chord $AB$ has length:
$$
AB = \sqrt{(1 - \cos \theta)^2 + (\sin \theta)^2} = \sqrt{2 - 2 \cos \theta} = 2 \sin\left(\frac{\theta}{2}\right)
$$
Since the straight line is the shortest path:
$$
\text{Length of chord } AB \leq \text{Length of arc } AB = \theta
$$
To relate $\sin \theta$ to $\theta$, compare areas:
- Area of triangle $OBA = \frac{1}{2} \cdot 1 \cdot 1 \cdot \sin \theta = \frac{\sin \theta}{2}$.
- Area of sector $OAB = \frac{1}{2} \cdot 1^2 \cdot \theta = \frac{\theta}{2}$.
- Since triangle $OBA$ is inside sector $OAB$:
$$
\frac{\sin \theta}{2} \leq \frac{\theta}{2} \implies \sin \theta \leq \theta
$$
For $0 < \theta < \pi/2$, $\sin \theta < \theta$ (equality at $\theta \to 0^+$).

### Upper Bound: $\theta \leq \tan \theta$
Construct points:
- $D$ at $(1, \tan \theta)$, on the line $x = 1$.
- $E$ at $(0, 1)$, forming triangle $CDE$.

Line $AD$ has length:
$$
AD = \sqrt{(1 - 1)^2 + (\tan \theta - 0)^2} = \tan \theta
$$
We aim to show $\tan \theta \geq \theta$. Form triangle $CDE$:
- $C = (0, \sin \theta)$, $D = (1, \tan \theta)$, $E = (0, 1)$.
- $CE = 1 - \sin \theta$.
- $CD = \sqrt{(1 - 0)^2 + (\tan \theta - \sin \theta)^2}$.

In a right triangle, the hypotenuse is longer than any leg. Assume $CDE$ is right-angled (we’ll check coordinates). Instead, use the tangent line at $B$ for clarity, but adapt to your construction. The line from $O$ through $B$ to $x = 1$ gives $D = (1, \tan \theta)$. To confirm $\theta \leq \tan \theta$, test:
$$
f(\theta) = \tan \theta - \theta, \quad f'(\theta) = \sec^2 \theta - 1 > 0 \text{ for } 0 < \theta < \pi/2
$$
Since $f(0^+) = 0$ and $f'(\theta) > 0$, $\tan \theta > \theta$ for $\theta > 0$. For the limit, use:
$$
\theta \leq \tan \theta
$$
Thus, for $0 < |\theta| < \pi/2$:
$$
\sin |\theta| \leq |\theta| \leq \tan |\theta|
$$

## Step 3: Apply Absolute Value
For $\theta > 0$, $|\theta| = \theta$. For $\theta < 0$, $|\theta| = -\theta$, and since $\sin(-\theta) = -\sin \theta$, $\tan(-\theta) = -\tan \theta$, the inequality holds:
$$
\sin |\theta| \leq |\theta| \leq \tan |\theta|
$$

## Step 4: Derive the Squeeze Inequality
For $0 < |\theta| < \pi/2$, divide by $\sin |\theta|$ (since $\sin |\theta| > 0$):
$$
1 \leq \frac{|\theta|}{\sin |\theta|} \leq \frac{\tan |\theta|}{\sin |\theta|} = \frac{\sin |\theta|}{\cos |\theta| \cdot \sin |\theta|} = \frac{1}{\cos |\theta|}
$$
Take reciprocals, reversing inequalities:
$$
1 \geq \frac{\sin |\theta|}{|\theta|} \geq \cos |\theta|
$$
Or:
$$
\cos |\theta| \leq \frac{\sin |\theta|}{|\theta|} \leq 1
$$

## Step 5: Apply the Squeeze Theorem
Take the limit as $\theta \to 0$:
$$
\lim_{\theta \to 0} \cos |\theta| \leq \lim_{\theta \to 0} \frac{\sin |\theta|}{|\theta|} \leq \lim_{\theta \to 0} 1
$$
- $\lim_{\theta \to 0} 1 = 1$.
- $\lim_{\theta \to 0} \cos |\theta|$:
  - For $\theta \to 0^+$, $|\theta| = \theta$, $\cos \theta \to 1$.
  - For $\theta \to 0^-$, $|\theta| = -\theta$, $\cos(-\theta) = \cos \theta \to 1$.
  Thus, $\lim_{\theta \to 0} \cos |\theta| = 1$.

So:
$$
1 \leq \lim_{\theta \to 0} \frac{\sin |\theta|}{|\theta|} \leq 1 \implies \lim_{\theta \to 0} \frac{\sin |\theta|}{|\theta|} = 1
$$

## Step 6: Relate to Original Limit
For $\theta \neq 0$:
$$
\frac{\sin |\theta|}{|\theta|} =
\begin{cases}
\frac{\sin \theta}{\theta} & \text{if } \theta > 0 \\
\frac{\sin (-\theta)}{-\theta} = \frac{\sin \theta}{\theta} & \text{if } \theta < 0
\end{cases}
$$
Thus:
$$
\frac{\sin |\theta|}{|\theta|} = \frac{\sin \theta}{\theta}
$$
Therefore:
$$
\lim_{\theta \to 0} \frac{\sin |\theta|}{|\theta|} = \lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1
$$

## Conclusion
Using the geometric inequality $\sin |\theta| \leq |\theta| \leq \tan |\theta|$ for $0 < |\theta| < \pi/2$, we derived $\cos |\theta| \leq \frac{\sin |\theta|}{|\theta|} \leq 1$. The Squeeze Theorem confirms:
$$
\lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1
$$
The diagram’s triangles $OBC$ and $CDE$ support the bounds, ensuring the limit holds for both positive and negative $\theta$.

# Summary of Key Calculus Insights: Sign-Switching in Derivatives

## 1. Core Concepts

### Periodic Functions (Trigonometric)
- **Behavior**: Oscillate between positive/negative values with fixed periods.
- **Key Examples**:
  - `sin(x)` → Zeros at `x = nπ`, flips sign at every zero.
  - `cos(x)` → Zeros at `x = π/2 + nπ`, flips sign at every zero.

### Polynomials
- **Behavior**: Sign-switching depends on root multiplicity:
  - **Odd powers**: Flip sign at roots (e.g., `(x-2)^3`).
  - **Even powers**: No sign flip (e.g., `(x-1)^2`).

## 2. Your Derivative Analysis (`f'(x) = -4sin(x) - 1`)

### Step-by-Step Strategy
1. **Find zeros**: Solve `-4sin(x) - 1 = 0` → `sin(x) = -1/4`.
   - Solutions: `x ≈ -0.25268 + 2πn` or `x ≈ 3.3943 + 2πn` (n ∈ ℤ).
2. **Determine starting sign**:
   - At `x = -2`: `sin(-2) < -1/4` → `f'(-2) > 0`.
3. **Flip signs at each zero**:
   - After `x ≈ -0.25268`: `f'(x) < 0`.
   - After `x ≈ 3.3943`: `f'(x) > 0`, etc.

## 3. Key Takeaways
- **Trig Derivatives**: Sign-switching is guaranteed at zeros due to periodicity.
- **Polynomials**: Sign-switching only at odd-multiplicity roots.
- **Efficient Workflow**:
  1. Find all critical points (zeros).
  2. Determine the sign in one interval.
  3. Alternate signs at each zero.

## 4. Pro Tips
- **For `sin(x)`/`cos(x)`**: Use the unit circle to predict sign patterns.
- **For polynomials**: Factor completely to identify root multiplicities.
- **Visualization**: Always plot to confirm analytical results!
