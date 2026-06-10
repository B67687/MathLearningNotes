# MathLearningNotes

Repository for mathematics learning notes in Jupyter Notebook format, covering topics like trigonometry, precalculus, calculus, and discrete math.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Notes](#notes)
  - [Root Directory Notes](#root-directory-notes)
  - [Algebra](#algebra)
  - [Calculus](#calculus)
  - [Discrete Mathematics](#discrete-mathematics)
    - [Combinatorics](#combinatorics)
    - [Logic](#logic)
    - [Series and Sequences](#series-and-sequences)
      - [Arithmetic Sum](#arithmetic-sum)
      - [Sum of Cubes](#sum-of-cubes)
      - [Sum of Squares](#sum-of-squares)
      - [Symmetric Sums](#symmetric-sums)
    - [Number Theory](#number-theory)
  - [Fractals](#fractals)
  - [Trigonometry](#trigonometry)
  - [Translated Notes (中文翻译笔记)](#translated-notes-中文翻译笔记)
    - [Discrete Mathematics (离散数学)](#discrete-mathematics-离散数学)
      - [Combinatorics (组合学)](#combinatorics-组合学)
      - [Series and Sequences (数列与级数)](#series-and-sequences-数列与级数)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains a collection of Jupyter Notebooks documenting various mathematical concepts, proofs, and explorations. The notes are organized by mathematical discipline and include both theoretical explanations and practical examples. Additionally, this repository includes Chinese translations of many notes to make the content accessible to Chinese-speaking learners.

Most notes are in **Jupyter Notebook (.ipynb)** format, which renders natively in GitHub with full MathJax support for LaTeX equations. A small number of notes are in **Markdown (.md)** format — these are marked with a † symbol.

## Installation

To work with the notes locally, you'll need Jupyter installed. Set up the environment using either the provided `environment.yml` file (for conda) or `requirements.txt` (for pip).

### Using Conda

```bash
conda env create -f environment.yml
conda activate math-learning
```

### Using Pip

```bash
pip install -r requirements.txt
```

## Notes

### Root Directory Notes

| Note                                                 | Description                                                                      |
| ---------------------------------------------------- | -------------------------------------------------------------------------------- |
| [Math-Lessons.ipynb](Math-Lessons.ipynb)             | Main notebook with comprehensive math lessons compiled from previous Google Docs |
| [Template_Notebook.ipynb](Template_Notebook.ipynb)   | Template for creating new detailed notes                                         |
| [Template_QUICKNOTE.ipynb](Template_QUICKNOTE.ipynb) | Template for creating quick notes                                                |

### Algebra

| Note                                                                         | Description                                |
| ---------------------------------------------------------------------------- | ------------------------------------------ |
| [general-properties.ipynb](algebra/general-properties.ipynb)                 | General properties of algebraic operations |
| [quadratic-slide-and-divide.ipynb](algebra/quadratic-slide-and-divide.ipynb) | AC method of quadratic factorisation       |

### Calculus

The calculus section contains a series of advancement reports documenting progress in learning calculus concepts, as well as specific topic notes.

| Note                                                                                                        | Description                                                |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [derivative-proofs.ipynb](calculus/derivative-proofs.ipynb)                                                 | Proofs related to derivatives                              |
| [advancements-report-14th-march-2025.ipynb](calculus/advancements-report-14th-march-2025.ipynb)             | Progress report from March 14, 2025                        |
| [advancements-report-15th-march.ipynb](calculus/advancements-report-15th-march--Properties-of-Limits.ipynb) | Progress report from March 15, 2025 — Properties of Limits |
| [advancements-report-16th-april-2025.ipynb](calculus/advancements-report-16th-april-2025.ipynb)             | Progress report from April 16, 2025                        |
| [advancements-report-16th-march-2025.ipynb](calculus/advancements-report-16th-march-2025.ipynb)             | Progress report from March 16, 2025                        |
| [advancements-report-17th-march-2025.ipynb](calculus/advancements-report-17th-march-2025.ipynb)             | Progress report from March 17, 2025                        |
| [advancements-report-18th-march-2025.ipynb](calculus/advancements-report-18th-march-2025.ipynb)             | Progress report from March 18, 2025                        |
| [advancements-report-19th-march-2025.ipynb](calculus/advancements-report-19th-march-2025.ipynb)             | Progress report from March 19, 2025                        |
| [advancements-report-20th-march-2025.ipynb](calculus/advancements-report-20th-march-2025.ipynb)             | Progress report from March 20, 2025                        |
| [advancements-report-21st-march-2025.ipynb](calculus/advancements-report-21st-march-2025.ipynb)             | Progress report from March 21, 2025                        |
| [advancements-report-23rd-march-2025.ipynb](calculus/advancements-report-23rd-march-2025.ipynb)             | Progress report from March 23, 2025                        |
| [advancements-report-25th-march-2025.ipynb](calculus/advancements-report-25th-march-2025.ipynb)             | Progress report from March 25, 2025                        |
| [advancements-report-27th-march-2025.ipynb](calculus/advancements-report-27th-march-2025.ipynb)             | Progress report from March 27, 2025                        |

### Discrete Mathematics

#### Combinatorics

| Note                                                                                                      | Description                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| [binomial-expansion.ipynb](discrete-mathematics/combinatorics/binomial-expansion.ipynb)                   | Binomial expansion formulas and applications  |
| [pascals-triangle.ipynb](discrete-mathematics/combinatorics/pascals-triangle.ipynb)                       | Pascal's triangle properties and applications |
| [permutation-and-combination.ipynb](discrete-mathematics/combinatorics/permutation-and-combination.ipynb) | Permutation and combination concepts          |
| [circular-arrangements.md](discrete-mathematics/combinatorics/circular-arrangements.md) †                 | Circular arrangement problems                 |
| [stars-and-bars.md](discrete-mathematics/combinatorics/stars-and-bars.md) †                               | Stars and bars combinatorics method           |

#### Logic

| Note                                                                                                                                        | Description                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [consecutive-integer-multiples-are-divisible-by-2.ipynb](discrete-mathematics/logic/consecutive-integer-multiples-are-divisible-by-2.ipynb) | Proof that consecutive integer products are even |
| [if-p-then-q-explained.ipynb](discrete-mathematics/logic/if-p-then-q-explained.ipynb)                                                       | Explanation of conditional statements in logic   |
| [learnings-1st-april.ipynb](discrete-mathematics/logic/learnings-1st-april.ipynb)                                                           | Logic concepts learned on April 1st, 2025        |
| [proof-by-induction.md](discrete-mathematics/logic/proof-by-induction.md) †                                                                 | Mathematical induction explained                 |
| [triangle-inequality.md](discrete-mathematics/logic/triangle-inequality.md) †                                                               | Triangle inequality concepts and proofs          |

#### Series and Sequences

##### Arithmetic Sum

| Note                                                                                                                                                                    | Description                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| [arithmetic-sum-generalisation.ipynb](discrete-mathematics/series-and-sequences/arithmetic-sum/arithmetic-sum-generalisation.ipynb)                                     | Generalizations of arithmetic sum formulas                   |
| [arithmetic-sum.ipynb](discrete-mathematics/series-and-sequences/arithmetic-sum/arithmetic-sum.ipynb)                                                                   | Basic arithmetic sum concepts and formulas                   |
| [sum-of-positive-integers-to-odd-or-even-integer.ipynb](discrete-mathematics/series-and-sequences/arithmetic-sum/sum-of-positive-integers-to-odd-or-even-integer.ipynb) | Sum formulas for positive integers up to odd or even numbers |

##### Sum of Cubes

| Note                                                                                                                                                                  | Description                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| [cubes-as-sum-of-consecutive-odd-numbers.ipynb](discrete-mathematics/series-and-sequences/cubes-as-sum-of-consecutive-odd-numbers.ipynb)                              | Representing cubes as sums of consecutive odd numbers    |
| [sum-of-cubes-with-arithmetic-sum (compressed).ipynb](<discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-arithmetic-sum%20(compressed).ipynb>) | Compressed version of sum of cubes using arithmetic sums |
| [sum-of-cubes-with-arithmetic-sum.ipynb](discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-arithmetic-sum.ipynb)                               | Sum of cubes using arithmetic sum formulas               |
| [sum-of-cubes-with-sum-of-squares.ipynb](discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-sum-of-squares.ipynb)                               | Relationship between sum of cubes and sum of squares     |
| [sum-of-cubes-with-symmetric-sums.ipynb](discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-symmetric-sums.ipynb)                               | Sum of cubes using symmetric sum approach                |

##### Sum of Squares

| Note                                                                                                                                                            | Description                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [sum-of-squares-with-arithmetic-sum.ipynb](discrete-mathematics/series-and-sequences/sum-of-squares/sum-of-squares-with-arithmetic-sum.ipynb)                   | Sum of squares using arithmetic sum formulas |
| [sum-of-squares-with-stack-of-symmetric-sums.ipynb](discrete-mathematics/series-and-sequences/sum-of-squares/sum-of-squares-with-stack-of-symmetric-sums.ipynb) | Sum of squares using stacked symmetric sums  |
| [sum-of-squares-with-symmetric-sum.ipynb](discrete-mathematics/series-and-sequences/sum-of-squares/sum-of-squares-with-symmetric-sum.ipynb)                     | Sum of squares using symmetric sum approach  |

##### Symmetric Sums

| Note                                                                                                                                              | Description                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [sum-of-even-numbers-in-symmetric-sum.ipynb](discrete-mathematics/series-and-sequences/symmetric-sums/sum-of-even-numbers-in-symmetric-sum.ipynb) | Symmetric approach to summing even numbers |
| [sum-of-odd-numbers-in-symmetric-sum.ipynb](discrete-mathematics/series-and-sequences/symmetric-sums/sum-of-odd-numbers-in-symmetric-sum.ipynb)   | Symmetric approach to summing odd numbers  |
| [symmetric-sum-of-cubes.ipynb](discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-cubes.ipynb)                             | Symmetric approach to summing cubes        |
| [symmetric-sum-of-even-numbers.ipynb](discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-even-numbers.ipynb)               | Symmetric approach to summing even numbers |
| [symmetric-sum-of-odd-numbers.ipynb](discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-odd-numbers.ipynb)                 | Symmetric approach to summing odd numbers  |
| [symmetric-sum-of-squares.ipynb](discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-squares.ipynb)                         | Symmetric approach to summing squares      |

##### Other Series and Sequences

| Note                                                                                                                                             | Description                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| [geometric-sum.ipynb](discrete-mathematics/series-and-sequences/geometric-sum.ipynb)                                                             | Geometric series concepts and formulas               |
| [sharing-and-splitting.ipynb](discrete-mathematics/series-and-sequences/sharing-and-splitting.ipynb)                                             | Problems involving sharing and splitting sequences   |
| [sum-of-consecutive-multiples.ipynb](discrete-mathematics/series-and-sequences/sum-of-consecutive-multiples.ipynb)                               | Sums of consecutive multiples                        |
| [sum-of-even-numbers-is-consecutive-multiple.ipynb](discrete-mathematics/series-and-sequences/sum-of-even-numbers-is-consecutive-multiple.ipynb) | Even numbers as consecutive multiples                |
| [sum-of-odd-numbers-is-square.ipynb](discrete-mathematics/series-and-sequences/sum-of-odd-numbers-is-square.ipynb)                               | Proof that sum of odd numbers equals perfect squares |
| [sum-of-odd-and-even-squares.ipynb](discrete-mathematics/series-and-sequences/sum-of-odd-and-even-squares.ipynb)                                 | Sum of odd and even squares                          |
| [sum-of-reciprocal-consecutive-multiples.ipynb](discrete-mathematics/series-and-sequences/sum-of-reciprocal-consecutive-multiples.ipynb)         | Sums of reciprocals of consecutive multiples         |
| [sum-of-reciprocal-triangle-numbers.ipynb](discrete-mathematics/series-and-sequences/sum-of-reciprocal-triangle-numbers.ipynb)                   | Sums of reciprocals of triangular numbers            |
| [telescoping-series.ipynb](discrete-mathematics/series-and-sequences/telescoping-series.ipynb)                                                   | Telescoping series concepts and formulas             |
| [sums-of-powers.ipynb](discrete-mathematics/series-and-sequences/sums-of-powers.ipynb)                                                           | Sums of powers formulas                              |
| [triangular-numbers-and-their-sum.ipynb](discrete-mathematics/series-and-sequences/triangular-numbers-and-their-sum.ipynb)                       | Triangular numbers and their sum formulas            |

#### Number Theory

| Note                                                                                                                                                               | Description                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| [fun-facts-about-factors.ipynb](discrete-mathematics/number-theory/fun-facts-about-factors.ipynb)                                                                  | Interesting properties of factors                   |
| [modular-arithmetic.md](discrete-mathematics/number-theory/modular-arithmetic.md) †                                                                                | Modular arithmetic concepts                         |
| **Divisibility**                                                                                                                                                   |                                                     |
| [divisibility-by-1.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-1.ipynb)                                                                 | Rules and properties of divisibility by 1           |
| [divisibility-by-2.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-2.ipynb)                                                                 | Rules and properties of divisibility by 2           |
| [divisibility-by-3.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-3.ipynb)                                                                 | Rules and properties of divisibility by 3           |
| [divisibility-by-4.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-4.ipynb)                                                                 | Rules and properties of divisibility by 4           |
| [divisibility-by-5.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-5.ipynb)                                                                 | Rules and properties of divisibility by 5           |
| [divisibility-by-6.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-6.ipynb)                                                                 | Rules and properties of divisibility by 6           |
| [divisibility-by-7.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-7.ipynb)                                                                 | Rules and properties of divisibility by 7           |
| [divisibility-by-8.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-8.ipynb)                                                                 | Rules and properties of divisibility by 8           |
| [divisibility-by-9.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-9.ipynb)                                                                 | Rules and properties of divisibility by 9           |
| [divisibility-by-10.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-10.ipynb)                                                               | Rules and properties of divisibility by 10          |
| [divisibility-by-11.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-11.ipynb)                                                               | Alternating sum divisibility rule for 11            |
| [divisibility-by-12.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-12.ipynb)                                                               | Divisibility by 12                                  |
| [divisibility-by-13.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-13.ipynb)                                                               | Divisibility by 13                                  |
| [divisibility-by-powers-of-2.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-by-powers-of-2.ipynb)                                             | Divisibility by powers of 2                         |
| [divisibility-nomenclature.ipynb](discrete-mathematics/number-theory/divisibility/divisibility-nomenclature.ipynb)                                                 | Terminology and definitions related to divisibility |
| [factoring-the-place-units.ipynb](discrete-mathematics/number-theory/divisibility/factoring-the-place-units.ipynb)                                                 | Factoring by place units                            |
| [number-composition.ipynb](discrete-mathematics/number-theory/divisibility/number-composition.ipynb)                                                               | Number composition and decomposition                |
| [sum-of-digits-is-less-than-or-equal-to-its-number.ipynb](discrete-mathematics/number-theory/divisibility/sum-of-digits-is-less-than-or-equal-to-its-number.ipynb) | Sum of digits vs the number itself                  |

### Fractals

| Note                                          | Description                                      |
| --------------------------------------------- | ------------------------------------------------ |
| [mandelbrot.ipynb](fractals/mandelbrot.ipynb) | Mandelbrot fractal exploration and visualization |

### Trigonometry

| Note                                                                                                | Description                                   |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| [fun-simulations.ipynb](trigonometry/fun-simulations.ipynb)                                         | Trigonometric function simulations            |
| [getting-definitions-right.ipynb](trigonometry/getting-definitions-right.ipynb)                     | Precise definitions of trigonometric concepts |
| [r-formula-cosine-first.ipynb](trigonometry/r-formula-cosine-first.ipynb)                           | R-formula in trigonometry (cosine-first)      |
| [r-formula-sine-first.ipynb](trigonometry/r-formula-sine-first.ipynb)                               | R-formula in trigonometry (sine-first)        |
| [the-way-is-to-simplify-case-study.ipynb](trigonometry/the-way-is-to-simplify-case-study.ipynb)     | Case study on simplification techniques       |
| [advancements-report-4th-march-2025.ipynb](trigonometry/advancements-report-4th-march-2025.ipynb)   | Progress report from March 4, 2025            |
| [advancements-report-8th-march-2025.ipynb](trigonometry/advancements-report-8th-march-2025.ipynb)   | Progress report from March 8, 2025            |
| [advancements-report-10th-march-2025.ipynb](trigonometry/advancements-report-10th-march-2025.ipynb) | Progress report from March 10, 2025           |

### Translated Notes (中文翻译笔记)

The `translated-notebooks` directory contains Chinese translations of various notes, making the mathematical content accessible to Chinese-speaking learners.

#### Discrete Mathematics (离散数学)

##### Combinatorics (组合学)

| Note                                                                      | Description                                                          |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [二项展开式.ipynb](translated-notebooks/离散数学/组合学/二项展开式.ipynb) | 二项展开式公式与应用 (Binomial expansion formulas and applications)  |
| [排列与组合.ipynb](translated-notebooks/离散数学/组合学/排列与组合.ipynb) | 排列与组合概念 (Permutation and combination concepts)                |
| [杨辉三角.ipynb](translated-notebooks/离散数学/组合学/杨辉三角.ipynb)     | 杨辉三角的性质与应用 (Pascal's triangle properties and applications) |

##### Series and Sequences (数列与级数)

| Note                                                                                                                                   | Description                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [三角形数与之求和.ipynb](translated-notebooks/离散数学/数列与级数/三角形数与之求和.ipynb)                                              | 三角形数及其求和公式 (Triangular numbers and their sum formulas)                            |
| [等比数列求和.ipynb](translated-notebooks/离散数学/数列与级数/等比数列求和.ipynb)                                                      | 几何级数概念与公式 (Geometric series concepts and formulas)                                 |
| [奇数之和是平方数.ipynb](translated-notebooks/离散数学/数列与级数/奇数之和是平方数.ipynb)                                              | 奇数之和等于平方数的证明 (Proof that sum of odd numbers equals perfect squares)             |
| [偶数之和.ipynb](translated-notebooks/离散数学/数列与级数/偶数之和.ipynb)                                                              | 偶数之和公式 (Formulas for sum of even numbers)                                             |
| [等差数列至奇数乃偶数之求和.ipynb](translated-notebooks/离散数学/数列与级数/等差数列求和/等差数列至奇数乃偶数之求和.ipynb)             | 正整数之和为奇数或偶数的公式 (Sum formulas for positive integers up to odd or even numbers) |
| [连续整数乘积求和.ipynb](translated-notebooks/离散数学/数列与级数/连续整数乘积求和.ipynb)                                              | 连续倍数之和 (Sums of consecutive multiples)                                                |
| [连续乘积倒数求和.ipynb](translated-notebooks/离散数学/数列与级数/连续乘积倒数求和.ipynb)                                              | 连续倍数倒数之和 (Sums of reciprocals of consecutive multiples)                             |
| [等差数列求和.ipynb](translated-notebooks/离散数学/数列与级数/等差数列求和/等差数列求和.ipynb)                                         | 算术级数概念与公式 (Basic arithmetic sum concepts and formulas)                             |
| [等差数列求和之广义化.ipynb](translated-notebooks/离散数学/数列与级数/等差数列求和/等差数列求和之广义化.ipynb)                         | 算术级数推广 (Generalizations of arithmetic sum formulas)                                   |
| [立方和的等差数列之推导（压缩版）.ipynb](translated-notebooks/离散数学/数列与级数/立方数列求和/立方和的等差数列之推导（压缩版）.ipynb) | 立方数之和与算术级数 (压缩版) (Compressed version of sum of cubes using arithmetic sums)    |
| [立方和的等差数列之推导.ipynb](translated-notebooks/离散数学/数列与级数/立方数列求和/立方和的等差数列之推导.ipynb)                     | 立方数之和与算术级数 (Sum of cubes using arithmetic sum formulas)                           |
| [立方和的平方和之推导.ipynb](translated-notebooks/离散数学/数列与级数/立方数列求和/立方和的平方和之推导.ipynb)                         | 立方数之和与平方数之和的关系 (Relationship between sum of cubes and sum of squares)         |
| [立方和的对称和之推导.ipynb](translated-notebooks/离散数学/数列与级数/立方数列求和/立方和的对称和之推导.ipynb)                         | 立方数之和与对称和 (Sum of cubes using symmetric sum approach)                              |
| [平方和的等差数列之推导.ipynb](translated-notebooks/离散数学/数列与级数/平方数列求和/平方和的等差数列之推导.ipynb)                     | 平方数之和与算术级数 (Sum of squares using arithmetic sum formulas)                         |
| [平方求和之对称之和.ipynb](translated-notebooks/离散数学/数列与级数/对称之和/平方求和之对称之和.ipynb)                                 | 平方数之和与对称和 (Sum of squares using symmetric sum approach)                            |
| [偶数之对称之和.ipynb](translated-notebooks/离散数学/数列与级数/对称之和/偶数之对称之和.ipynb)                                         | 偶数对称和 (Symmetric approach to summing even numbers)                                     |
| [奇数之对称之和.ipynb](translated-notebooks/离散数学/数列与级数/对称之和/奇数之对称之和.ipynb)                                         | 奇数对称和 (Symmetric approach to summing odd numbers)                                      |
| [平方和的对称和之推导.ipynb](translated-notebooks/离散数学/数列与级数/平方数列求和/平方和的对称和之推导.ipynb)                         | 平方和的对称和之推导 (Derivation of sum of squares using symmetric sum)                     |

† = Markdown-only notes (no notebook original)

## Usage

The notes are **Jupyter Notebooks (.ipynb)** which render natively in your browser on GitHub with full LaTeX support. To work with them locally:

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

You can also browse the notebooks directly on GitHub — it renders them with MathJax for proper LaTeX display.

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a new branch for your feature
3. Add your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
