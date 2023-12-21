# Fibonacci and Lucas Numbers

## Purpose

I am delving into Python development, particularly with Flask, to build backend applications. This program serves as a refresher on Python's core foundations, emphasizing terminal-controlled outputs.

## Usage

This program calculates Fibonacci numbers up to 22 and Lucas numbers up to 20. It employs the Sieve of Eratosthenes to find prime numbers from 2 to the array limit, including all perfect numbers within that range. Additionally, it establishes a relationship to estimate the golden ratio. If identical values are set for both Fibonacci and Lucas calculations, it computes the golden ratio to the power of n, compares it to a combination of the Lucas and Fibonacci theorems, and provides a mathematical limit proof as values approach infinity.

## Theorems

- \(Fibonacci_n = Fibonacci_{n - 1} + Fibonacci_{n - 2}\)
- \(Lucas_n = Lucas_{n - 1} + Lucas_{n - 2}\)
- Golden Ratio (\(\phi\)) = \(\frac{1 + \sqrt{5}}{2}\)
  - \(\frac{Fibonacci_n}{Fibonacci_{n - 1}} \approx \phi\)
  - \(\frac{Lucas_n}{Lucas_{n - 1}} \approx \phi\)
  - \(\phi^n \approx \frac{Lucas_n + Fibonacci_n \cdot \sqrt{5}}{2}\)
  - \(Lucas_{2n} = 5 \cdot (Fibonacci_n)^2 + 2 \cdot (-1)^{n - 1}\)
  - \(\lim_{{x \to \infty}} \frac{Lucas_n}{Fibonacci_n} = \sqrt{5}\)
