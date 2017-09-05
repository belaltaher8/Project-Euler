sum = 0

firstNum = 1
secondNum = 2
flag = True
listOfFib = []

listOfFib.append(firstNum)


while flag is True:
    
    listOfFib.append(secondNum)

    nextFib = firstNum + secondNum
    firstNum = secondNum
    secondNum = nextFib

    if(secondNum > 4000000):
        flag = False

for i in listOfFib:
    if(i%2==0):
        sum = sum + i

print(sum)
    
    
    
