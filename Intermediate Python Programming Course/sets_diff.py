setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

diff = setB.difference(setA)
print(diff)

diff = setA.symmetric_difference(setB)
print(diff)

diff = setB.symmetric_difference(setA)
print(diff)
