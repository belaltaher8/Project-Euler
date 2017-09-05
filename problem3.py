largestPrime = 0

num = 600851475143

primeFactors = []
divider = 2

while num is not 1:
    if(num%divider == 0):
        num = num/divider
        primeFactors.append(divider)
        print(divider)
    else:
        divider = divider + 1

print(primeFactors)
