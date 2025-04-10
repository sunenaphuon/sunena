n = int(input("Enter number: "))
s = 0
temp = n
while temp > 0:
    d = temp % 10
    s += d**len(str(n))
    temp //= 10
if s == n:
    print("Armstrong")
else:
    print("Not Armstrong")
