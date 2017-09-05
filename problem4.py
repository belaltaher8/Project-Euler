x = 0

for i in range (1000,800,-1):
    for k in range (1000,800,-1):
        checking = i*k
        stringForProduct = str(checking)
        reversedString = stringForProduct[::-1]
        if stringForProduct == reversedString:
            if checking > x:
                x = checking
                print(x)
