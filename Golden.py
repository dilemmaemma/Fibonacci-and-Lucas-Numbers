import numpy as np
import subprocess
import platform

# Function to clear terminal
def clear_terminal():
    system = platform.system()
    if system == 'Windows':
        subprocess.run('cls', shell=True)
    elif system == 'Linux' or system == 'Darwin':  # Linux or macOS
        subprocess.run('clear', shell=True)

def fibonacci_sequence(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer for the Fibonacci sequence."

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence
    
def lucas_sequence(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer for the Lucas sequence."
    
    luc_sequence = [2, 1]
    for i in range(2, n):
        luc_sequence.append(luc_sequence[i-1] + luc_sequence[i-2])
    return luc_sequence

# Sieve of Eratasthenes
def primes(limit):
    prime_list = []
    num_list = []
    p = 2
    
    def sieve_of_eratosthenes(limit, p):
        for i in range(2, limit//p + 1):
            num_list.append(p * i)

    while p <= np.sqrt(limit):
        if p not in num_list:
            prime_list.append(p)
        sieve_of_eratosthenes(limit, p)
        p += 1

    for num in range(p, limit + 1):
        if num not in num_list:
            prime_list.append(num)

    return prime_list

# Finds perfect numbers -> sum of divisors equal the number
def perfect_numbers(limit):
    perfect_list = []
    for i in range(1, limit):
        divisors = [j for j in range(1, i) if i % j == 0]
        if sum(divisors) == i:
            perfect_list.append(i)
    return perfect_list

clear_terminal()
while True:
    fib_input = input("Fibonacci position: ")
    try: # Same as try... catch in JavaScript
        fib = int(fib_input)
        if fib <= 0:
            raise ValueError("Invalid input. Please enter a positive integer for the Fibonacci Sequence.")
        if fib > 22:
            raise ValueError("Invalid input. Please enter a value less than or equal to 22 for the Fibas Sequence.")
        fib += 1
        fib_sequence = fibonacci_sequence(fib)
        fib_prime_sequence = primes(fib_sequence[-1])
        fib_primes = []
        for num in fib_prime_sequence:
            if num in fib_sequence:
                fib_primes.append(num)
        fib_perfect_sequence = perfect_numbers(fib_sequence[-1])
        fib_perfect = []
        for num in fib_perfect_sequence:
            if num in fib_sequence:
                fib_perfect.append(num)
        break
    except ValueError as e: # Use except instead of JavaScript's catch command. ValueError is used to find an error in the actual value entered.
        print(str(e))
while True:
    luc_input = input("Lucas position: ")
    try:
        luc = int(luc_input)
        if luc <= 0:
            raise ValueError("Invalid input. Please enter a positive integer for the Lucas Sequence.")
        if luc > 20:
            raise ValueError("Invalid input. Please enter a value less than or equal to 20 for the Lucas Sequence.")
        luc += 1
        luc_sequence = lucas_sequence(luc)
        luc_prime_sequence = primes(luc_sequence[-1])
        luc_primes = []
        for num in luc_prime_sequence:
            if num in luc_sequence:
                luc_primes.append(num)
        if not luc_prime_sequence:
            luc_prime_sequence = 2
        luc_perfect_sequence = perfect_numbers(luc_sequence[-1])
        luc_perfect = []
        for num in luc_perfect_sequence:
            if num in luc_sequence:
                luc_perfect.append(num)
        break
    except ValueError as e:
        print(str(e))

clear_terminal()
print(f"\nFibonacci({fib - 1}): {fib_sequence[-1]}")
print(f"Lucas({luc - 1}): {luc_sequence[-1]}")
print(f"\nFibonacci array calculated to position {fib - 1}: {fib_sequence}")
print(f"No prime numbers found up to position {fib - 1}." if not fib_prime_sequence else f"Prime numbers calculated to position {fib - 1}: {fib_prime_sequence}") # Ternary syntax in python
print("No prime numbers found in the Fibonacci sequence." if not fib_primes else f"Prime numbers found in the Fibonacci sequence: {fib_primes}")
print(f"No perfect numbers found up to position {fib - 1}." if not fib_perfect_sequence else f"Perfect numbers calculated to position {fib - 1}: {fib_perfect_sequence}")
print("No perfect numbers found in the Fibonacci sequence.\n" if not fib_perfect else f"Perfect numbers found in the Fibonacci sequence: {fib_perfect}\n")
print(f"\nLucas array calculated to position {luc - 1}: {luc_sequence}")
print(f"Prime numbers calculated to position {luc - 1}: {luc_prime_sequence}")
print(f"Prime numbers found in the Lucas sequence: {luc_primes}")
print(f"No perfect numbers found up to position {luc - 1}." if not luc_perfect_sequence else f"Perfect numbers calculated to position {luc - 1}: {luc_perfect_sequence}")
print("No perfect numbers found in the Lucas sequence.\n" if not luc_perfect else f"Perfect numbers found in the Lucas sequence: {luc_perfect}\n\n")
print(f"The relationship between Fibonacci({fib - 1}) and Fibonacci({fib - 2}) can be used to calculate an estimation of the golden ratio: {fib_sequence[-1] / fib_sequence[-2]}")
print(f"Same with Lucas: {luc_sequence[-1] / luc_sequence[-2]}\n")
if fib == luc:
    print(f"Using a combination of Lucas and Fibonacci, the golden ratio to the power of {fib - 1} is equivalent to: {(luc_sequence[-1] + (fib_sequence[-1] * np.sqrt(5))) / 2}, with the actual value being: {((1 + np.sqrt(5))/2)**(luc - 1)}")
    print(f"Lucas({2 * (luc - 1)}): {(5*(fib_sequence[-1]**2)) + 2 * (-1**(luc - 1))}")
    print("\nThe limit of Lucas(n)/Fibonacci(n) as n approaches infinity is the square root of 5")
    print("Proof:")
    print(f"    Lucas({luc - 1})/Fibonacci({fib - 1}): {luc_sequence[-1] / fib_sequence[-1]}")
    print(f"    Square root of 5: {np.sqrt(5)}")
    