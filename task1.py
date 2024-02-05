import math
import concurrent.futures

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def check_primes_with_threadpool():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, NUMBERS))
    return results

def check_primes_with_processpool():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, NUMBERS))
    return results

if __name__ == "__main__":
    threadpool_results = check_primes_with_threadpool()
    processpool_results = check_primes_with_processpool()

    print("Results with ThreadPoolExecutor:")
    print(threadpool_results)

    print("\nResults with ProcessPoolExecutor:")
    print(processpool_results)
