# Fibonacci and Lucas Numbers

## Purpose
  I am interested in opening up my skills into Python development, especially developing with Flask to create backend Python applications. I made this program to help me recall the core foundations of Python and how to code with it, with output being controlled within the confines of the terminal.

## Usage
  This program can be used to calculate the Fibonacci and Lucas numbers up to 22 and 20, respectively. Additionally, the application uses the Sieve of Eratastenes to calculate all of the prime numbers from 2 to the array limit and includes all perfect numbers within the array and from 1 to the array limit. Finally, a relationship is derived from the data to estimate the golden ratio and, if identical values are set for both Fibonacci and Lucas calculation, the golden ratio to the power of n is calculated and compared to a combination of the Lucas and Fibonacci theorems and lists the mathematical limit proof of the values as they approach infinity.

## Theorems
  - Fibonacci<sub>n</sub> = Fibonacci<sub>n - 1</sub> + Fibonacci<sub>n - 2</sub>
  - Lucas<sub>n</sub> = Lucas<sub>n - 1</sub> + Lucas<sub>n - 2</sub>
  - Golden Ratio(&phi;) = <math><mfrac><mrow><mi>1</mi><mo>+</mo><mn>&radic;5</mn></mrow><mrow><mo>2</mo></mrow></mfrac></math>
  <br/>
  - <math><mfrac><mrow><mi><i>F</i></mi><mo><sub>n</sub></mo></mrow><mrow><mi><i>F</i><mo><sub>n - 1</sub></mo></mrow></mfrac></math> &cong; &phi;
  - <math><mfrac><mrow><mi><i>L</i></mi><mo><sub>n</sub></mo></mrow><mrow><mi><i>L</i><mo><sub>n - 1</sub></mo></mrow></mfrac></math> &cong; &phi;
  - &phi;<sup>n</sup> &cong; <math><mfrac><mrow><mi><i>L</i><sub>n</sub></mi><mo>+</mo><mn><i>F</i><sub>n</sub> * &radic;5</mn></mrow><mrow><mo>2</mo></mrow></mfrac></math>
  - <i>L</i><sub>2n</sub> = 5(<i>F</i><sub>n</sub>)<sup>2</sup> + 2(-1)<sup><i>n - 1</i></sup>
  - lim(<strong>x→∞</strong>) <math><mfrac><mrow><mo><i>L</i><sub>n</sub></mo></mrow><mrow><mo><i>F</i><sub>n</sub></mo></mrow></mfrac></math> = &radic;5
