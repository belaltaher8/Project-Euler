import math

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

flag = False

for a in range(1,1000):
    for b in range (a+1,1000):
        asquared = a*a
        bsquared = b*b
        csquared = asquared + bsquared
        if(is_square(csquared)):
            c = math.sqrt(csquared)
            if(a+b+c == 1000):
                flag = True
                break
            
    if flag == True:
        break
                
                
print(a)
print(b)
print(c)

print(a*b*c)
