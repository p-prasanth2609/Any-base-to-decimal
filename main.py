n = int(input())
b = int(input())
a = str(n)[::-1]
sum = 0
for i in range(len(a)):
    sum += int(a[i]) * (b ** i)
print(sum)
