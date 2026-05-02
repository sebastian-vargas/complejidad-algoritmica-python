import time
import sys
sys.setrecursionlimit(200000)
sys.set_int_max_str_digits(1000000)

def factorial(n):
    response = 1
    while n > 1:
        response *= n
        n -= 1
    
    return response

def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1)

if __name__ == "__main__":
    n = 200000
    start_time = time.time()
    #print(factorial(n))
    final_time = time.time()
    print(f"Iterative factorial took {final_time - start_time} seconds")

    start_time = time.time()
    #print(recursive_factorial(n))
    final_time = time.time()
    print(f"Recursive factorial took {final_time - start_time} seconds")