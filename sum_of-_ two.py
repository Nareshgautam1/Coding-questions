A = [1,4,5,6,7,8]
b = 14
c= []
i = 0
j= i+1
for i in range (len(A)):
    for j in range(len(A)):
         if A[i]+A[j] == b:
             c.append(i)
             c.append(j)

print(c)