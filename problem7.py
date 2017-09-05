def checkIfPrime(num):
    returning = True
    for i in range(2,int(num)):
        if(int(num)%i == 0):
            returning = False
            break

    return returning
    

currentPrimeIndex = 6
currentNum = 13

while currentPrimeIndex < 10001:
    currentNum = currentNum +1
    if(checkIfPrime(currentNum) is True):
        currentPrimeIndex = currentPrimeIndex + 1
        print(currentPrimeIndex)


print(currentNum)
    
    
