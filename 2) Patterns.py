n=int(input("Enter number of rows: "))

print("Square")
if n>0:
    for i in range(1, n+1):
        print("* " * n)
else:
    print("Please enter a positive integer.")

print() 

print("Triangle")
for i in range(1, n+1):
    print(" " * (n - i) + "* " * i)

print() 

print("Inverted Triangle")
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

print() 

print("Right Aligned Triangle")
for i in range(1, n+1):
    print("* " * i)

print() 

print("Left Aligned Triangle")
for i in range(n, 0, -1):
    print("* " * i)

print() 

print("Hollow Square")
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ") #end=" " to stay on the same line (Like print in Java)
        else:
            print(" ", end=" ")
    print()

print() 

print("Hollow Triangle")
for i in range (1, n+1):
    for j in range (1, i+1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
