# MathLearningNotes

Repository for mathematics learning notes, covering topics like trigonometry, precalculus, calculus, and discrete math.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Markdown Notes](#markdown-notes)
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

This repository contains a collection of Markdown notes documenting various mathematical concepts, proofs, and explorations. The notes are organized by mathematical discipline and include both theoretical explanations and practical examples. Additionally, this repository includes Chinese translations of many notes to make the content accessible to Chinese-speaking learners.

## Installation

To work with the archived notebooks, you'll need to have Jupyter installed. You can set up the environment using either the provided `environment.yml` file (for conda) or `requirements.txt` (for pip).

### Using Conda

```bash
conda env create -f environment.yml
conda activate math-learning
```

### Using Pip

```bash
pip install -r requirements.txt
```

## Markdown Notes

### Root Directory Notes

| Note                                           | Description                                                                  |
| ---------------------------------------------- | ---------------------------------------------------------------------------- |
| [Math-Lessons.md](Math-Lessons.md)             | Main note with comprehensive math lessons compiled from previous Google Docs |
| [Template_Notebook.md](Template_Notebook.md)   | Template for creating new detailed notes                                     |
| [Template_QUICKNOTE.md](Template_QUICKNOTE.md) | Template for creating quick notes                                            |

### Algebra

| Note                                                   | Description                                |
| ------------------------------------------------------ | ------------------------------------------ |
| [general-properties.md](algebra/general-properties.md) | General properties of algebraic operations |

### Calculus

The calculus section contains a series of advancement reports documenting progress in learning calculus concepts, as well as specific topic notes.

| Note                                                                                                  | Description                                                |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [derivative-proofs.md](calculus/derivative-proofs.md)                                                 | Proofs related to derivatives                              |
| [advancements-report-14th-march-2025.md](calculus/advancements-report-14th-march-2025.md)             | Progress report from March 14, 2025                        |
| [advancements-report-15th-march.md](calculus/advancements-report-15th-march--Properties-of-Limits.md) | Progress report from March 15, 2025 — Properties of Limits |
| [advancements-report-16th-april-2025.md](calculus/advancements-report-16th-april-2025.md)             | Progress report from April 16, 2025                        |
| [advancements-report-16th-march-2025.md](calculus/advancements-report-16th-march-2025.md)             | Progress report from March 16, 2025                        |
| [advancements-report-17th-march-2025.md](calculus/advancements-report-17th-march-2025.md)             | Progress report from March 17, 2025                        |
| [advancements-report-18th-march-2025.md](calculus/advancements-report-18th-march-2025.md)             | Progress report from March 18, 2025                        |
| [advancements-report-19th-march-2025.md](calculus/advancements-report-19th-march-2025.md)             | Progress report from March 19, 2025                        |
| [advancements-report-20th-march-2025.md](calculus/advancements-report-20th-march-2025.md)             | Progress report from March 20, 2025                        |
| [advancements-report-21st-march-2025.md](calculus/advancements-report-21st-march-2025.md)             | Progress report from March 21, 2025                        |
| [advancements-report-23rd-march-2025.md](calculus/advancements-report-23rd-march-2025.md)             | Progress report from March 23, 2025                        |
| [advancements-report-25th-march-2025.md](calculus/advancements-report-25th-march-2025.md)             | Progress report from March 25, 2025                        |
| [advancements-report-27th-march-2025.md](calculus/advancements-report-27th-march-2025.md)             | Progress report from March 27, 2025                        |

### Discrete Mathematics

#### Combinatorics

| Note                                                                                                | Description                                   |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| [binomial-expansion.md](discrete-mathematics/combinatorics/binomial-expansion.md)                   | Binomial expansion formulas and applications  |
| [pascals-triangle.md](discrete-mathematics/combinatorics/pascals-triangle.md)                       | Pascal's triangle properties and applications |
| [permutation-and-combination.md](discrete-mathematics/combinatorics/permutation-and-combination.md) | Permutation and combination concepts          |

#### Logic

| Note                                                                            | Description                                    |
| ------------------------------------------------------------------------------- | ---------------------------------------------- |
| [if-p-then-q-explained.md](discrete-mathematics/logic/if-p-then-q-explained.md) | Explanation of conditional statements in logic |
| [learnings-1st-april.md](discrete-mathematics/logic/learnings-1st-april.md)     | Logic concepts learned on April 1st, 2025      |

#### Series and Sequences

##### Arithmetic Sum

| Note                                                                                                                          | Description                                |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [arithmetic-sum-generalisation.md](discrete-mathematics/series-and-sequences/arithmetic-sum/arithmetic-sum-generalisation.md) | Generalizations of arithmetic sum formulas |
| [arithmetic-sum.md](discrete-mathematics/series-and-sequences/arithmetic-sum/arithmetic-sum.md)                               | Basic arithmetic sum concepts and formulas |
| [sum-of-consecutive-multiples.md](discrete-mathematics/series-and-sequences/sum-of-consecutive-multiples.md)                  | Sums of consecutive multiples              |

##### Sum of Cubes

| Note                                                                                                                                                        | Description                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| [cubes-as-sum-of-consecutive-odd-numbers.md](discrete-mathematics/series-and-sequences/cubes-as-sum-of-consecutive-odd-numbers.md)                          | Representing cubes as sums of consecutive odd numbers    |
| [sum-of-cubes-with-arithmetic-sum (compressed).md](discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-arithmetic-sum (compressed).md) | Compressed version of sum of cubes using arithmetic sums |
| [sum-of-cubes-with-arithmetic-sum.md](discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-arithmetic-sum.md)                           | Sum of cubes using arithmetic sum formulas               |
| [sum-of-cubes-with-sum-of-squares.md](discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-sum-of-squares.md)                           | Relationship between sum of cubes and sum of squares     |

##### Sum of Squares

| Note                                                                                                                                    | Description                                  |
| --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [sum-of-squares-with-arithmetic-sum.md](discrete-mathematics/series-and-sequences/sum-of-squares/sum-of-squares-with-arithmetic-sum.md) | Sum of squares using arithmetic sum formulas |
| [sum-of-squares-with-symmetric-sum.md](discrete-mathematics/series-and-sequences/sum-of-squares/sum-of-squares-with-symmetric-sum.md)   | Sum of squares using symmetric sum approach  |

##### Symmetric Sums

| Note                                                                                                                              | Description                                |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [sum-of-cubes-with-symmetric-sums.md](discrete-mathematics/series-and-sequences/sum-of-cubes/sum-of-cubes-with-symmetric-sums.md) | Sum of cubes using symmetric sum approach  |
| [symmetric-sum-of-even-numbers.md](discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-even-numbers.md)     | Symmetric approach to summing even numbers |
| [symmetric-sum-of-odd-numbers.md](discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-odd-numbers.md)       | Symmetric approach to summing odd numbers  |
| [symmetric-sum-of-squares.md](discrete-mathematics/series-and-sequences/symmetric-sums/symmetric-sum-of-squares.md)               | Symmetric approach to summing squares      |

##### Other Series and Sequences

| Note                                                                                                                                                              | Description                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| [geometric-sum.md](discrete-mathematics/series-and-sequences/geometric-sum.md)                                                                                    | Geometric series concepts and formulas                       |
| [sharing-and-splitting.md](discrete-mathematics/series-and-sequences/sharing-and-splitting.md)                                                                    | Problems involving sharing and splitting sequences           |
| [sum-of-consecutive-multiples.md](discrete-mathematics/series-and-sequences/sum-of-consecutive-multiples.md)                                                      | Sums of consecutive multiples                                |
| [sum-of-even-numbers-is-consecutive-multiple.md](discrete-mathematics/series-and-sequences/sum-of-even-numbers-is-consecutive-multiple.md)                        | Even numbers as consecutive multiples                        |
| [sum-of-odd-numbers-is-square.md](discrete-mathematics/series-and-sequences/sum-of-odd-numbers-is-square.md)                                                      | Proof that sum of odd numbers equals perfect squares         |
| [sum-of-odd-and-even-squares.md](discrete-mathematics/series-and-sequences/sum-of-odd-and-even-squares.md)                                                        | Sum of odd and even squares                                  |
| [sum-of-positive-integers-to-odd-or-even-integer.md](discrete-mathematics/series-and-sequences/arithmetic-sum/sum-of-positive-integers-to-odd-or-even-integer.md) | Sum formulas for positive integers up to odd or even numbers |
| [sum-of-reciprocal-consecutive-multiples.md](discrete-mathematics/series-and-sequences/sum-of-reciprocal-consecutive-multiples.md)                                | Sums of reciprocals of consecutive multiples                 |
| [sum-of-reciprocal-triangle-numbers.md](discrete-mathematics/series-and-sequences/sum-of-reciprocal-triangle-numbers.md)                                          | Sums of reciprocals of triangular numbers                    |
| [cubes-as-sum-of-consecutive-odd-numbers.md](discrete-mathematics/series-and-sequences/cubes-as-sum-of-consecutive-odd-numbers.md)                                | Cubes as sum of consecutive odd numbers                      |
| [telescoping-series.md](discrete-mathematics/series-and-sequences/telescoping-series.md)                                                                          | Telescoping series concepts and formulas                     |
| [sums-of-powers.md](discrete-mathematics/series-and-sequences/sums-of-powers.md)                                                                                  | Sums of powers formulas                                      |
| [triangular-numbers-and-their-sum.md](discrete-mathematics/series-and-sequences/triangular-numbers-and-their-sum.md)                                              | Triangular numbers and their sum formulas                    |

#### Number Theory

| Note                                                                                                             | Description                                         |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [divisibility-by-1.md](discrete-mathematics/number-theory/divisibility/divisibility-by-1.md)                     | Rules and properties of divisibility by 1           |
| [divisibility-by-2.md](discrete-mathematics/number-theory/divisibility/divisibility-by-2.md)                     | Rules and properties of divisibility by 2           |
| [divisibility-by-3.md](discrete-mathematics/number-theory/divisibility/divisibility-by-3.md)                     | Rules and properties of divisibility by 3           |
| [divisibility-by-4.md](discrete-mathematics/number-theory/divisibility/divisibility-by-4.md)                     | Rules and properties of divisibility by 4           |
| [divisibility-by-5.md](discrete-mathematics/number-theory/divisibility/divisibility-by-5.md)                     | Rules and properties of divisibility by 5           |
| [divisibility-by-6.md](discrete-mathematics/number-theory/divisibility/divisibility-by-6.md)                     | Rules and properties of divisibility by 6           |
| [divisibility-by-8.md](discrete-mathematics/number-theory/divisibility/divisibility-by-8.md)                     | Rules and properties of divisibility by 8           |
| [divisibility-by-9.md](discrete-mathematics/number-theory/divisibility/divisibility-by-9.md)                     | Rules and properties of divisibility by 9           |
| [divisibility-by-10.md](discrete-mathematics/number-theory/divisibility/divisibility-by-10.md)                   | Rules and properties of divisibility by 10          |
| [divisibility-by-11.md](discrete-mathematics/number-theory/divisibility/divisibility-by-11.md)                   | Alternating sum divisibility rule for 11            |
| [divisibility-by-12.md](discrete-mathematics/number-theory/divisibility/divisibility-by-12.md)                   | Divisibility by 12                                  |
| [divisibility-by-13.md](discrete-mathematics/number-theory/divisibility/divisibility-by-13.md)                   | Divisibility by 13                                  |
| [divisibility-by-powers-of-2.md](discrete-mathematics/number-theory/divisibility/divisibility-by-powers-of-2.md) | Divisibility by powers of 2                         |
| [divisibility-nomenclature.md](discrete-mathematics/number-theory/divisibility/divisibility-nomenclature.md)     | Terminology and definitions related to divisibility |

### Fractals

| Note                                    | Description                                      |
| --------------------------------------- | ------------------------------------------------ |
| [mandelbrot.md](fractals/mandelbrot.md) | Mandelbrot fractal exploration and visualization |

### Trigonometry

| Note                                                                                          | Description                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------- |
| [fun-simulations.md](trigonometry/fun-simulations.md)                                         | Trigonometric function simulations            |
| [getting-definitions-right.md](trigonometry/getting-definitions-right.md)                     | Precise definitions of trigonometric concepts |
| [r-formula-cosine-first.md](trigonometry/r-formula-cosine-first.md)                           | R-formula in trigonometry (cosine-first)      |
| [r-formula-sine-first.md](trigonometry/r-formula-sine-first.md)                               | R-formula in trigonometry (sine-first)        |
| [the-way-is-to-simplify-case-study.md](trigonometry/the-way-is-to-simplify-case-study.md)     | Case study on simplification techniques       |
| [advancements-report-4th-march-2025.md](trigonometry/advancements-report-4th-march-2025.md)   | Progress report from March 4, 2025            |
| [advancements-report-8th-march-2025.md](trigonometry/advancements-report-8th-march-2025.md)   | Progress report from March 8, 2025            |
| [advancements-report-10th-march-2025.md](trigonometry/advancements-report-10th-march-2025.md) | Progress report from March 10, 2025           |

### Translated Notes (中文翻译笔记)

The `translated-notebooks` directory contains Chinese translations of various notes, making the mathematical content accessible to Chinese-speaking learners. Older translations are preserved from the notebook workflow; future canonical work should prefer Markdown.

#### Discrete Mathematics (离散数学)

##### Combinatorics (组合学)

| Note                                                                | Description                                                          |
| ------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [二项展开式.md](translated-notebooks/离散数学/组合学/二项展开式.md) | 二项展开式公式与应用 (Binomial expansion formulas and applications)  |
| [排列与组合.md](translated-notebooks/离散数学/组合学/排列与组合.md) | 排列与组合概念 (Permutation and combination concepts)                |
| [杨辉三角.md](translated-notebooks/离散数学/组合学/杨辉三角.md)     | 杨辉三角的性质与应用 (Pascal's triangle properties and applications) |

##### Series and Sequences (数列与级数)

| Note                                                                                                                          | Description                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [三角形数与之求和.md](translated-notebooks/离散数学/数列与级数/三角形数与之求和.md)                                           | 三角形数及其求和公式 (Triangular numbers and their sum formulas)                            |
| [几何级数.md](translated-notebooks/离散数学/数列与级数/等比数列求和.md)                                                       | 几何级数概念与公式 (Geometric series concepts and formulas)                                 |
| [奇数之和为平方数.md](translated-notebooks/离散数学/数列与级数/奇数之和是平方数.md)                                           | 奇数之和等于平方数的证明 (Proof that sum of odd numbers equals perfect squares)             |
| [偶数之和.md](translated-notebooks/离散数学/数列与级数/偶数之和.md)                                                           | 偶数之和公式 (Formulas for sum of even numbers)                                             |
| [正整数之和为奇数或偶数.md](translated-notebooks/离散数学/数列与级数/等差数列求和/等差数列至奇数乃偶数之求和.md)              | 正整数之和为奇数或偶数的公式 (Sum formulas for positive integers up to odd or even numbers) |
| [连续倍数之和.md](translated-notebooks/离散数学/数列与级数/连续整数乘积求和.md)                                               | 连续倍数之和 (Sums of consecutive multiples)                                                |
| [连续倍数倒数之和.md](translated-notebooks/离散数学/数列与级数/连续乘积倒数求和.md)                                           | 连续倍数倒数之和 (Sums of reciprocals of consecutive multiples)                             |
| [算术级数.md](translated-notebooks/离散数学/数列与级数/等差数列求和/等差数列求和.md)                                          | 算术级数概念与公式 (Basic arithmetic sum concepts and formulas)                             |
| [算术级数推广.md](translated-notebooks/离散数学/数列与级数/等差数列求和/等差数列求和之广义化.md)                              | 算术级数推广 (Generalizations of arithmetic sum formulas)                                   |
| [立方数之和与算术级数 (压缩版).md](translated-notebooks/离散数学/数列与级数/立方数列求和/立方和的等差数列之推导（压缩版）.md) | 立方数之和与算术级数 (压缩版) (Compressed version of sum of cubes using arithmetic sums)    |
| [立方数之和与算术级数.md](translated-notebooks/离散数学/数列与级数/立方数列求和/立方和的等差数列之推导.md)                    | 立方数之和与算术级数 (Sum of cubes using arithmetic sum formulas)                           |
| [立方数之和与平方数之和.md](translated-notebooks/离散数学/数列与级数/立方数列求和/立方和的平方和之推导.md)                    | 立方数之和与平方数之和的关系 (Relationship between sum of cubes and sum of squares)         |
| [立方数之和与对称和.md](translated-notebooks/离散数学/数列与级数/立方数列求和/立方和的对称和之推导.md)                        | 立方数之和与对称和 (Sum of cubes using symmetric sum approach)                              |
| [平方数之和与算术级数.md](translated-notebooks/离散数学/数列与级数/平方数列求和/平方和的等差数列之推导.md)                    | 平方数之和与算术级数 (Sum of squares using arithmetic sum formulas)                         |
| [平方数之和与对称和.md](translated-notebooks/离散数学/数列与级数/对称之和/平方求和之对称之和.md)                              | 平方数之和与对称和 (Sum of squares using symmetric sum approach)                            |
| [偶数对称和.md](translated-notebooks/离散数学/数列与级数/对称之和/偶数之对称之和.md)                                          | 偶数对称和 (Symmetric approach to summing even numbers)                                     |
| [奇数对称和.md](translated-notebooks/离散数学/数列与级数/对称之和/奇数之对称之和.md)                                          | 奇数对称和 (Symmetric approach to summing odd numbers)                                      |
| [平方和的对称和之推导.md](translated-notebooks/离散数学/数列与级数/平方数列求和/平方和的对称和之推导.md)                      | 平方和的对称和之推导 (Derivation of sum of squares using symmetric sum)                     |

## Usage

To work with the archived notebooks:

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
