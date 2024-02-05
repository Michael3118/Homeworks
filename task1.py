import asyncio
import multiprocessing
import time

async def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


async def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


async def calculate_square(n):
    return n * n


async def calculate_cubic(n):
    return n * n * n


async def main():
    numbers = list(range(1, 11))

    fibonacci_results = await asyncio.gather(*(calculate_fibonacci(n) for n in numbers))
    factorial_results = await asyncio.gather(*(calculate_factorial(n) for n in numbers))
    square_results = await asyncio.gather(*(calculate_square(n) for n in numbers))
    cubic_results = await asyncio.gather(*(calculate_cubic(n) for n in numbers))

    print("Fibonacci:", fibonacci_results)
    print("Factorial:", factorial_results)
    print("Square:", square_results)
    print("Cubic:", cubic_results)


if __name__ == "__main__":
    asyncio.run(main())




def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_square(n):
    return n * n

def calculate_cubic(n):
    return n * n * n

def main():
    numbers = list(range(1, 11))

    with multiprocessing.Pool() as pool:
        start_time = time.time()

        fibonacci_results = pool.map(calculate_fibonacci, numbers)
        factorial_results = pool.map(calculate_factorial, numbers)
        square_results = pool.map(calculate_square, numbers)
        cubic_results = pool.map(calculate_cubic, numbers)

        end_time = time.time()

    print("Fibonacci:", fibonacci_results)
    print("Factorial:", factorial_results)
    print("Square:", square_results)
    print("Cubic:", cubic_results)
    print("Execution Time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()
