import math # allows us to use the math.sqrt() function.

# This function checks if a number is prime or not.
def is_prime(number):
    # any number less or equal to one is de facto, not prime.
    if number <= 1:
        return False
    # Check if a number is divisible by every number between two and itself. if not return True. Meaning it is Prime.
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
    
# This function find every prime number until the given limit.
def find_primes(limit):
    primes = []
    # This for loop checks if every number from zero to the limit is prime, and appends it to list called primes. 
    for i in range(limit + 1):
        if is_prime(i):
            primes.append(i)
        else:
            continue
    return primes

# This function is set to take a list of prime numbers and finds the gaps between the primes.
def prime_gap(a_list):
    prime_gaps = []
    for i in range(1, len(a_list)):
    # using the abs() is unnecessary since the primes are always increasing. any negative number is necessarily not prime.
        prime_gaps.append(a_list[i] - a_list[i-1])
    return prime_gaps










# def find_twin_primes(list_prime_gaps):
#     # TODO
# def average_between_prime_gaps(list_prime_gaps):
#     sum = 0
#     for i in range(len(list_prime_gaps)):
#         sum += i
#     return sum / len(list_prime_gaps)

# print(find_primes(800))
print(prime_gap(find_primes(10000)))
# print(average_between_prime_gaps(prime_gap(find_primes(8000))))