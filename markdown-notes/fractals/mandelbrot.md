---
title: "Mandelbrot"
source_notebook: "fractals/mandelbrot.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

```python
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(h, w, max_iter):
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y*1j
    z = c
    divtime = max_iter + np.zeros(z.shape, dtype=int)
    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        divtime[diverge] = i
        z[diverge] = 2
    return divtime

plt.imshow(mandelbrot(400, 400, 100), cmap='hot')
plt.show()
```
