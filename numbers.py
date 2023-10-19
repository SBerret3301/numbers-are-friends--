x = int(input("enter a number : "))
y = int(input("enter another one : "))
a = 0
b = 0
for i in range(2,x) :
    if (x % i == 0) :
        a += i
for i in range(2,y) :
    if (y % i == 0) :
        b += i
if a == y and b == x :
    print("the two numbers are friends")
else :
    print("the two numbers aren't friends")

