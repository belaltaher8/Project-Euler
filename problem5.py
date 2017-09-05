def primeFactorize(num):
    returningArray = []

    if int(num) is 1:
        returningArray = [1]
        return returningArray

    while int(num) is not 1:
        for i in range(2,int(num)+1):
            if(num%i == 0):
                returningArray.append(i)
                newNum = num / i
                num = newNum
                break
    return(returningArray)


        
        
finalArray = []
for i in range (1,21):
    arrayToAdd = primeFactorize(i)
    finalArray.append(arrayToAdd)

print(finalArray)





##for i in range(1, len(finalArray)):
##        print(finalArray[i])
##        for j in range(0, len(finalArray[i])):
##            arrayToExtract = finalArray[i]
##            numToMultiply = arrayToExtract[j]
##            newProduct = int(product) * int(numToMultiply)
##            product = newProduct
##
##print(newProduct)

##########flag = True
##########numToCheck = 2520
##########while flag is True:
##########    flag = False
##########    for i in range(1,20):
##########        if(numToCheck%i is not 0):
##########            flag = True
##########    numToCheck = numToCheck + 20
##########    print(numToCheck)
##########    
##########print(numToCheck)













