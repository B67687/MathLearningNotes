# MathLearningNotes

Repository for mathematics learning notes, covering topics like trigonometry, precalculus, calculus, and discrete math.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Jupyter Notebooks](#jupyter-notebooks)
  - [Root Directory Notebooks](#root-directory-notebooks)
  - [Algebra](#algebra)
  - [Calculus](#calculus)
  - [Discrete Mathematics](#discrete-mathematics)
    - [Combinatorics](#combinatorics)
    - [Logic](#logic)
    - [Series and Sequences](#series-and-sequences)
  - [Fractals](#fractals)
  - [Trigonometry](#trigonometry)
  - [Translated Notebooks](#translated-notebooks)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains a collection of Jupyter notebooks documenting various mathematical concepts, proofs, and explorations. The notebooks are organized by mathematical discipline and include both theoretical explanations and practical examples.

## Installation

To use these notebooks, you'll need to have Jupyter installed. You can set up the environment using either the provided `environment.yml` file (for conda) or `requirements.txt` (for pip).

### Using Conda

```bash
conda env create -f environment.yml
conda activate math-learning
```

### Using Pip

```bash
pip install -r requirements.txt
```

## Jupyter Notebooks

### Root Directory Notebooks

| Notebook | Description |
|----------|-------------|
| [Math-Lessons.ipynb](Math-Lessons.ipynb) | Main notebook with comprehensive math lessons compiled from previous Google Docs |
| [Template_Notebook.ipynb](Template_Notebook.ipynb) | Template for creating new detailed notes |
| [Template_QUICKNOTE.ipynb](Template_QUICKNOTE.ipynb) | Template for creating quick notes |

### Algebra

| Notebook | Description |
|----------|-------------|
| [general-properties.ipynb](algebra/general-properties.ipynb) | General properties of algebraic operations |

### Calculus

The calculus section contains a series of advancement reports documenting progress in learning calculus concepts, as well as specific topic notebooks.

| Notebook | Description |
|----------|-------------|
| [derivative-proofs.ipynb](calculus/derivative-proofs.ipynb) | Proofs related to derivatives |
| [advancements-report-*.ipynb](calculus/) | Daily/weekly progress reports from March-April 2025 |

### Discrete Mathematics

#### Combinatorics

| Notebook | Description |
|----------|-------------|
| [binomial-expansion.ipynb](discrete-mathematics/combinatorics/binomial-expansion.ipynb) | Binomial expansion formulas and applications |
| [pascals-triangle.ipynb](discrete-mathematics/combinatorics/pascals-triangle.ipynb) | Pascal's triangle properties and applications |
| [permutation-and-combination.ipynb](discrete-mathematics/combinatorics/permutation-and-combination.ipynb) | Permutation and combination concepts |

#### Logic

| Notebook | Description |
|----------|-------------|
| [if-p-then-q-explained.ipynb](discrete-mathematics/logic/if-p-then-q-explained.ipynb) | Explanation of conditional statements in logic |
| [learnings-1st-april.ipynb](discrete-mathematics/logic/learnings-1st-april.ipynb) | Logic concepts learned on April 1st, 2025 |

#### Series and Sequences

| Notebook | Description |
|----------|-------------|
| [arithmetic-sum-generalisation.ipynb](discrete-mathematics/series-and-sequences/arithmetic-sum-generalisation.ipynb) | Generalizations of arithmetic sum formulas |
| [arithmetic-sum.ipynb](discrete-mathematics/series-and-sequences/arithmetic-sum.ipynb) | Basic arithmetic sum concepts and formulas |
| [cubes-as-sum-of-consecutive-odd-numbers.ipynb](discrete-mathematics/series-and-sequences/cubes-as-sum-of-consecutive-odd-numbers.ipynb) | Representing cubes as sums of consecutive odd numbers |
| [geometric-sum.ipynb](discrete-mathematics/series-and-sequences/geometric-sum.ipynb) | Geometric series concepts and formulas |
| [sharing-and-splitting.ipynb](discrete-mathematics/series-and-sequences/sharing-and-splitting.ipynb) | Problems involving sharing and splitting sequences |
| [sum-of-consecutive-multiples.ipynb](discrete-mathematics/series-and-sequences/sum-of-consecutive-multiples.ipynb) | Sums of consecutive multiples |
| [sum-of-cubes-with-arithmetic-sum-old.ipynb](discrete-mathematics/series-and-sequences/sum-of-cubes-with-arithmetic-sum-old.ipynb) | Old approach to sum of cubes using arithmetic sums |
| [sum-of-cubes-with-arithmetic-sum.ipynb](discrete-mathematics/series-and-sequences/sum-of-cubes-with-arithmetic-sum.ipynb) | Sum of cubes using arithmetic sum formulas |
| [sum-of-cubes-with-sum-of-squares.ipynb](discrete-mathematics/series-and-sequences/sum-of-cubes-with-sum-of-squares.ipynb) | Relationship between sum of cubes and sum of squares |
| [sum-of-cubes-with-symmetric-sums.ipynb](discrete-mathematics/series-and-sequences/sum-of-cubes-with-symmetric-sums.ipynb) | Sum of cubes using symmetric sum approach |
| [sum-of-even-numbers.ipynb](discrete-mathematics/series-and-sequences/sum-of-even-numbers.ipynb) | Formulas for sum of even numbers |
| [sum-of-odd-numbers-is-square.ipynb](discrete-mathematics/series-and-sequences/sum-of-odd-numbers-is-square.ipynb) | Proof that sum of odd numbers equals perfect squares |
| [sum-of-positive-integers-to-odd-or-even-integer.ipynb](discrete-mathematics/series-and-sequences/sum-of-positive-integers-to-odd-or-even-integer.ipynb) | Sum formulas for positive integers up to odd or even numbers |
| [sum-of-reciprocal-consecutive-multiples.ipynb](discrete-mathematics/series-and-sequences/sum-of-reciprocal-consecutive-multiples.ipynb) | Sums of reciprocals of consecutive multiples |
| [symmetric-sum-of-even-numbers.ipynb](discrete-mathematics/series-and-sequences/symmetric-sum-of-even-numbers.ipynb) | Symmetric approach to summing even numbers |
| [symmetric-sum-of-odd-numbers.ipynb](discrete-mathematics/series-and-sequences/symmetric-sum-of-odd-numbers.ipynb) | Symmetric approach to summing odd numbers |

### Fractals

| Notebook | Description |
|----------|-------------|
| [mandelbrot.ipynb](fractals/mandelbrot.ipynb) | Mandelbrot fractal exploration and visualization |

### Trigonometry

| Notebook | Description |
|----------|-------------|
| [fun-simulations.ipynb](trigonometry/fun-simulations.ipynb) | Trigonometric function simulations |
| [getting-definitions-right.ipynb](trigonometry/getting-definitions-right.ipynb) | Precise definitions of trigonometric concepts |
| [r-formula.ipynb](trigonometry/r-formula.ipynb) | R-formula in trigonometry |
| [the-way-is-to-simplify-case-study.ipynb](trigonometry/the-way-is-to-simplify-case-study.ipynb) | Case study on simplification techniques |
| [advancements-report-*.ipynb](trigonometry/) | Progress reports from March 2025 |

### Translated Notebooks

The `translated-notebooks` directory contains translated versions of various notebooks, primarily in Chinese. These translations are generated using the `translate_notebooks.py` script.

## Usage

To use these notebooks:

1. Clone the repository:
   ```bash
   git clone https://github.com/B67687/MathLearningNotes.git
   ```

2. Set up the environment as described in the [Installation](#installation) section.

3. Launch Jupyter Notebook or Jupyter Lab:
   ```bash
   jupyter notebook
   # or
   jupyter lab
   ```

4. Navigate to the notebook of interest and open it.

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a new branch for your feature
3. Add your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

