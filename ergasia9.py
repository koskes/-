def repeat(s):
    num = s
    k = num * 3
    w = k + 1
    l = [int(y) for y in str(w)]
    s = sum(l)
    return s


num1 = int(input('Enter a number  '))
num2 = 3
y = num1 * num2
z = y + 1
u = [int(x) for x in str(z)]
s = sum(u)
while s > 9:
    s = repeat(s)
print(s)

