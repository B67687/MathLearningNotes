---
title: "**Reflections**"
source_notebook: "trigonometry/getting-definitions-right.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# **Reflections**
Wow so I really just refined my understanding of trigonometry, I really didnt understand it before huh! Especially about learning that the standard position where we take reference for all angles, which is really the main break through for me. And then also realising this fact about reference angles that is a neat way to reason about trigonometric functions of greater than acute angles.

I dont know if I had needed to go through so much readjustment if I had learnt this correctly from the start given the right resources and attitude and schedule, alas it hard to find and take the most direct path in learning, sometimes we gotta stumble here and there and back finally to the correct understanding. I am very satisfied now but also feel sad for the lost time trying to understand trigonometry through the wrong perspective of its definition

## **Conclusion**
* An angle is defined through its rotation away from the positive `x-axis` on a Unit Circle (the **standard position**)
    * Therefore an angle doesn't exactly refer to an acute angle, but one *rotated from standard position*
* Angles greater than $90\degree$, can also be referenced by their acute angle to the `x-axis`, defined as the **reference angle**, which gives us a neat and convenient way to reason about trig functions of degrees larger than a quarter rotation


### **Do you really understand?**
- How would you find the reference angles for angles in every quadrant?
- How would you take the $sin(234\degree)$?

# **Insights on Trigonometry- Reasoning about definition**

My initial reasoning is that the height and base stays the same through about the whole angles, but it might not have worked for greater than 180 degrees because my reasoning bases very strongly on drawing a euclidean right angled triangle relative to the standard position.

BUT the definition is actually much more simple and by extension flexible idea - instead of needing the triangle for the height and base, the height and base itself will be sufficient. Using cartesian plane centered at the origin to model change from original position, we can equate the base and height to position (x,y), thereby simplifying the relationship between ratio of sides to angle.

'What about the hypotenuse of the triangle?' I thought, 'Would it seem that it is not included in this simplification?' as I continued thinking, then it dawned on me that the hypoetenuse is directly related to the height and base, it is not as fundamental as height and base in right-triangle building as I had previously assumed.
* Given, base x and height y, the hypotenuse is $\sqrt{x^2 + y^2}$, using pythagorean theorem

#### In fact, digging further, height and base ARE the FUNDAMENTAL constructs of a right-angle triangle.

Notice the right-angled triangle tie has been loosened, going from strictly right-triangle to just the points in space from the origin.

So now the free parameters now are
* An angle - its rotation from standard position, angles range from $-2\pi$ to $2\pi$, and angles outside these ranges are coterminal with angles within this range
* Height and base - (x, y)
    * Hypotenuse - $\sqrt{x^2 + y^2}$

As a consequence - we can bring the right-angled triangle to all 4 quadrants, forming on the `x-axis` because well `x-axis` is where we defined the base to be at,

meaning **4 angles** now **correspond to the same absolute ratio between the sides of a triangle**
* The angles are - where $\theta$ is acute:
   * Quadrant 1: $\theta$
   * Quadrant 2: 180 - $\theta$
   * Quadrant 3: 180 + $\theta$
   * Quadrant 4: 360 - $\theta$

*Now the exact ratios will have **polarity** because of our construct in the cartesian plane, which correspond to the orientation of the right-angle triangle's construct from the origin*

#### Hence, we can conclude that the trigonometric functions of *any* angle, can now output the combination of the **polarity** with **absolute ratio** between x, y and $\sqrt{x^2 + y^2}$, all based on the original construct of the right-angle triangle with the absolute angle
* We can tell polarity of trigonometric functions by looking at the quadrant it resides
* We can tell the absolute ratio of sides of the triangle through the construct of the right-angle triangle **with positive angle**

##### Determining the trig functions of any angle is now systematic and well-defined, by going through logical derivation of this definition
* You might eventually find this to be straightforward when you are well-handled with the flow of logic
* In practice - of course - we skip a lot of steps based on implicit understanding for speed and accuracy, but if any of those implicit understanding becomes cloudy, refer back to this full explanation to maintain your understanding - or improve on it!


### Points of Breakthrough
* Defining the premise of angles on a cartesian plane, representing direction and magnitude of change from the origin, rotated from positive `x-axis`
* Loosening the current perception that trigonometric functions depend solely on the right angle triangle construct, thereby **highlighting height and base as the most fundamental constructs of a right-angle triangle**, and by extension trigonometry
    * by atomising the direct parameters for the ratios - height and base - we shift the perception of height and base strictly tied to a drawable triangle to points in space relative to the point where the acute angle is, giving us freedom to explore greater-than-acute angles
* With this definition solidifed, and newfound freedom through paramtrisation, we were able to connect the trigonometric function of ANY angle to sides of a triangle constructed with its associated positive acute angle.
    * Associated positive acute angle is otherwise formally known as the `reference angle`

### Approach to Evaluating Trig Functions of Large Angles
Armed with the knowledge and experience (work it out personally) of derivation, this is the practical way to determine the equivalent trigonometric functions of large angles

Three things to check in this order
- Trigonometric Function (constant)
- Reference Angle
- Polarity
    - Find the determining factor, since hypotenuse is always positive, the determining factors are the `height` and `base`
    - for example determining factor of $\cos$ is the `x-axis`, and determining factor of $\sin$ is the `y-axis`, and the determinig factor of $\tan$ is both `x and y-axis`. Then the polarity of the axis is the polarity of the whole term.

## An extension of definition to trigonometric identities
Extending from the above derivation, now we can look at how to make it even simpler given these newfound understandings
* `Height` and `Base` are the fundamental constructs of a right-angle triangle
* Hypotenuse is defined by `height` and `base`, which by its definition, is always positive. See definition of radicals if unsure why.
* Trigonometric functions are based off of the relationship between `height`, `base`, and `hypotenuse`

Now we are thinking how to link the fundamental trigonometric ratios to the `height` and `base`.

$\sin\theta=\frac{height}{hyp}$

$\cos\theta=\frac{base}{hyp}$

$\tan\theta=\frac{height}{base}$

We see the hypotenuse present in all three of the basic trigonometric functions, but only 2 of those - $\sin\theta$ and $\cos\theta$ contains the `height` and `base` as the primary determining factor, while they are both determining factors in $\tan\theta$.

We will focus on those 2.

Given the constancy of hypotenuse in both functions, we can make the hypotenuse into a simpler constant, 1, that allows us to simplify the relationship between $\sin\theta$ and `height` and between $\cos\theta$ and `base` to:

$\sin\theta=height$

$\cos\theta=base$

Now that we have based the most fundamental properties of `height` and `base` to their respective trigonometric functions, we can draw it out. You will see that the constant hypotenuse would trace a circle of radius 1.
* This is called the **Unit Circle**

<img src="unit-circle.png" style="width: 230px">

On the `Unit Circle` we can directly see how $\cos$ is directly related to the `x-axis` and $\sin$ is directly related to the `y-axis`

We can further use extension of that drawing to derive several identities such as these

<div style="text-align: center;">
    <img src="unit-circle-derivations-1.png" style="width: 280px">
    <img src="unit-circle-derivations-2.png" style="width: 280px">
    <img src="unit-circle-derivations-3.png" style="width: 340px; height: 290px">
</div>

These are the identities of
* $\sin^2\theta + \cos^2\theta = 1$
* $\tan^2\theta + 1 = \sec^2\theta$
* $\cot^2\theta + 1 = \csc^2\theta$


derived from similar triangle properties

## Relative minor points worth addressing
* Reference angles are by definition **absolute acute** (positive). Therefore continue using its positive counterpart when dealing with evaluating trigonometric functions of negative angles.
* The `slope` of a triangle is different from the `hypotenuse` of the triangle.
    * The `hypotenuse` represents the absolute length of the slope. It has dimension.
    * The `slope` represents the **change** of y relative to the change in x of the hypotenuse, highlighting the relationship between x and y through quantifying their change relative to each other. It is thus dimensionless.
* The relationship between the `height`, `base`, and the `hypotenuse` is two-way, it is not restricted to height-base to hypotenuse which may be a misconception derived from reading the derivation of trigonometric definition above

```python
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
import ipywidgets as widgets

def plot_unit_circle(theta_deg):
    # Convert to radians
    theta_rad = np.radians(theta_deg)
    cos_theta = np.cos(theta_rad)
    sin_theta = np.sin(theta_rad)

    # Round values to avoid floating-point errors in display
    cos_theta_rounded = round(cos_theta, 3)
    sin_theta_rounded = round(sin_theta, 3)

    # Determine the quadrant and reference angle
    theta_deg = theta_deg % 360  # Normalize to 0-360
    if 0 <= theta_deg <= 90:
        quadrant = 1
        ref_angle = theta_deg
    elif 90 < theta_deg <= 180:
        quadrant = 2
        ref_angle = 180 - theta_deg
    elif 180 < theta_deg <= 270:
        quadrant = 3
        ref_angle = theta_deg - 180
    else:
        quadrant = 4
        ref_angle = 360 - theta_deg

    # Round reference angle for display
    ref_angle_rounded = round(ref_angle, 3)

    # Round absolute angle for display
    theta_deg_rounded = round(theta_deg, 3)

    # Plot the unit circle
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label='Unit Circle', color='blue')

    # Plot the angle and triangle
    plt.plot([0, cos_theta], [0, sin_theta], 'r-', label='Hypotenuse (r=1)')
    plt.plot([0, cos_theta], [0, 0], 'g-', label=f'Base (cos θ = {cos_theta_rounded})')
    plt.plot([cos_theta, cos_theta], [0, sin_theta], 'm-', label=f'Height (sin θ = {sin_theta_rounded})')
    plt.plot(cos_theta, sin_theta, 'ko', label=f'Point ({cos_theta_rounded}, {sin_theta_rounded})')

    # Add labels and grid
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.title(f'Angle: {theta_deg_rounded}° (Quadrant {quadrant}, Reference Angle: {ref_angle_rounded}°)')
    plt.show()

# Interactive slider for theta
interact(plot_unit_circle, theta_deg=widgets.FloatSlider(min=-720, max=720, step=1, value=45))
```

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data for a 3D helix
t = np.linspace(0, 10 * np.pi, 100)
x = np.cos(t)
y = np.sin(t)
z = t

# Plot the helix
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Helix: (cos(t), sin(t), t)')
ax.set_xlabel('X (cos(t))')
ax.set_ylabel('Y (sin(t))')
ax.set_zlabel('Z (t)')
ax.legend()
plt.title('3D Helix Using Trigonometric Functions')
plt.show()
```

```python
import sympy as sp

# Define the variable
theta = sp.Symbol('theta')

# Define trigonometric functions
sin_theta = sp.sin(theta)
cos_theta = sp.cos(theta)

# Verify the Pythagorean identity: sin^2(θ) + cos^2(θ) = 1
identity1 = sin_theta**2 + cos_theta**2
print("sin^2(θ) + cos^2(θ) =", sp.simplify(identity1))

# Verify another identity: tan^2(θ) + 1 = sec^2(θ)
tan_theta = sp.tan(theta)
sec_theta = 1 / cos_theta
identity2 = tan_theta**2 + 1 - sec_theta**2
print("tan^2(θ) + 1 - sec^2(θ) =", sp.simplify(identity2))

# Verify angle addition formula: sin(θ + φ) = sin(θ)cos(φ) + cos(θ)sin(φ)
phi = sp.Symbol('phi')
sin_addition = sp.sin(theta + phi) - (sp.sin(theta) * sp.cos(phi) + sp.cos(theta) * sp.sin(phi))
print("sin(θ + φ) - (sin(θ)cos(φ) + cos(θ)sin(φ)) =", sp.simplify(sin_addition))
```

# **Reflections on Emotional Response and Logical Thinking**
this is an amazing breakthrough, but it taught me:

- to catch habit of negative thinking, stopping a potential downward spiral, then turning to optimistic thinking to expand my resourcefulness, and start applying the logical steps below

- to find the most direct connections between things, to link them to other things, that's the most basic way to look at a thing

- to revisit my strong perceptions and work them out by doing point 1, see if one thing leads to another, this requires noticing then meticulous work, but meta-realisation is doing it the next time I encounter a problem

These are the cornerstone thinking skills to get out of half-knowledge ditches where I was, and to do it less painfully by acknowledging the pain, calming down, switch to optimism, and then switch to logical thinking

Emotional Responses are quite direct brain stimuli to situations that has posed problems in the past, that is hard to control exact amount of.

Emotional responses are old and unreliable systems that require refinement and new version, which unfortunately, cannot keep pace with the change from the environment that it lives in. A tool that is difficult to control, therefore requiring analogue regulation.

The best use of it then, is therefore to treat it as a general response, once you acknowledge the response exist, tune down the response, shove it in the other direction with some force so that it goes back to baseline, start thinking more logically.
While that happens you can find the problem that caused this response,  while the logic centre takes over to break down the situation to its fundamental parts, find the interconnections between things, question the hidden relationships, and formulate a response. You might not be right the first time, but that is to be expected, continue in this loop, rest when needed, stop when needed. But ultimately learning something novel, anything from it, from yourself, is a win. Count your wins. Don't fret the win being too small, do it everyday and the win compounds on your previous progress, and you will find one day you have come so far from your previous self.
