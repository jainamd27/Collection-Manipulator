n = 5

for i in range(1, n+1):
    for j in range(1, i+1):
        if((i+1)%2==0):
            print(j, end=" ")
        else:
            print("*", end=" ")
    print("")

print("\n")
print("Program 2\n")
# program 2

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print("")