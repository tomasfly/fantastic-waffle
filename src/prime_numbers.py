# prime_numbers.py

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_numbers(limit):
    """
    Generate prime numbers up to a given limit.
    """
    prime_numbers = []
    for num in range(2, limit + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers