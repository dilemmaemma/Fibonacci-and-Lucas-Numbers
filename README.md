# Fibonacci and Lucas Numbers

## Purpose

I am delving into Python development, particularly with Flask, to build backend applications. This program serves as a refresher on Python's core foundations, emphasizing terminal-controlled outputs.

## Usage

This program calculates Fibonacci numbers up to 22 and Lucas numbers up to 20. It employs the Sieve of Eratosthenes to find prime numbers from 2 to the array limit, including all perfect numbers within that range. Additionally, it establishes a relationship to estimate the golden ratio. If identical values are set for both Fibonacci and Lucas calculations, it computes the golden ratio to the power of n, compares it to a combination of the Lucas and Fibonacci theorems, and provides a mathematical limit proof as values approach infinity.

## Theorems

- Fibonacci<sub>n</sub> = Fibonacci<sub>n - 1</sub> + Fibonacci<sub>n - 2</sub>
- Lucas<sub>n</sub> = Lucas<sub>n - 1</sub> + Lucas<sub>n - 2</sub>
- Golden Ratio (&phi;) = <math><mfrac><mrow><mi>1</mi><mo>+</mo><mn>&radic;5</mn></mrow><mrow><mo>2</mo></mrow></mfrac></math>
<br/>
- <math><mfrac><mrow><mi><i>F</i></mi><mo><sub>n</sub></mo></mrow><mrow><mi><i>F</i><mo><sub>n - 1</sub></mo></mrow></mfrac></math> &cong; &phi;
- <math><mfrac><mrow><mi><i>L</i></mi><mo><sub>n</sub></mo></mrow><mrow><mi><i>L</i><mo><sub>n - 1</sub></mo></mrow></mfrac></math> &cong; &phi;
- &phi;<sup>n</sup> &cong; <math><mfrac><mrow><mi><i>L</i><sub>n</sub></mi><mo>+</mo><mn><i>F</i><sub>n</sub> * &radic;5</mn></mrow><mrow><mo>2</mo></mrow></mfrac></math>
- <i>L</i><sub>2n</sub> = 5(<i>F</i><sub>n</sub>)<sup>2</sup> + 2(-1)<sup><i>n - 1</i></sup>
- lim(<strong>x→∞</strong>) <math><mfrac><mrow><mo><i>L</i><sub>n</sub></mo></mrow><mrow><mo><i>F</i><sub>n</sub></mo></mrow></mfrac></math> = &radic;5
