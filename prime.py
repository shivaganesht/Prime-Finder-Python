def is_prime(num):
    """
    Check if a number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Check odd divisors up to the square root of num
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    """
    Print all prime numbers in a given range (inclusive).
    """
    print(f"Prime numbers between {start} and {end}:")
    primes = []
    
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    
    if primes:
        print(primes)
        print(f"Total prime numbers found: {len(primes)}")
    else:
        print("No prime numbers found in the given range.")
    
    return primes

def get_range_from_user():
    """
    Get the range from user input.
    """
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        if start > end:
            print("Start should be less than or equal to end. Swapping values...")
            start, end = end, start
        
        return start, end
    except ValueError:
        print("Please enter valid integers.")
        return None, None

if __name__ == "__main__":
    print("=== Prime Number Finder ===")
    
    # Method 1: Get range from user input
    start, end = get_range_from_user()
    
    if start is not None and end is not None:
        print_primes_in_range(start, end)
    
    print("\n" + "="*40)
    
    # # Method 2: Example with predefined range
    # print("Example: Prime numbers between 1 and 50:")
    # print_primes_in_range(1, 50)
    
    # print("\n" + "="*40)
    
    # # Method 3: Another example
    # print("Example: Prime numbers between 10 and 30:")
    # print_primes_in_range(10, 30)
