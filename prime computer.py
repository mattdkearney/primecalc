upper_bound = int(input('Input an upper bound: '))

prime_list = [2]

for numbers in range(3, upper_bound + 1):
    results_list = []
    for primes in prime_list:
        remainder = numbers%primes
        divisible = remainder == 0
        results_list.append(divisible)
    results_set = set(results_list)
    if len(results_set) == 1:
        prime_list.append(numbers)
    else:
        pass

print(prime_list)
