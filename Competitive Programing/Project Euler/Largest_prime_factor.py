def largest_prime_factor(n):
    largest_prime = 1

   
    while n % 2 == 0:
        largest_prime = 2
        n //= 2

    
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            largest_prime = factor
            n //= factor
        else:
            factor += 2 

    if n > 1:
        largest_prime = n

    return largest_prime


number = 600851475143
result = largest_prime_factor(number)

print("The largest prime factor of", number, "is", result)
