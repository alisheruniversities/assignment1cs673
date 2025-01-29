def compute_fibonacci(n):
    fibonacci_numbers = [1, 1]
    while len(fibonacci_numbers) < n:
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fib)
    return fibonacci_numbers

def main():
    fibonacci_numbers = compute_fibonacci(100)
    print(f"The first 100 Fibonacci numbers are: {fibonacci_numbers}")

if __name__ == "__main__":
    main()