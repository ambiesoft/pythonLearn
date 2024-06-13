# Sets: unordered, mutable, no duplicates
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# combine elements
u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

