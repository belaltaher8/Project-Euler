sum = 0;
for i in range(101):
    sum = sum + i
sum = sum * sum

smallerSum = 0

for i in range(101):
    k = i * i
    smallerSum = smallerSum + k

print(sum - smallerSum)
