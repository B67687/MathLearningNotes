---
title: "Fun Simulations"
source_notebook: "trigonometry/fun-simulations.ipynb"
archived_notebook: "archive/notebooks/trigonometry/fun-simulations.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

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
