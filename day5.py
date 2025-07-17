# for i in range(1,5):
#     for j in range(10,16):
#         print("*", end=" ")
#     print("")

# for i in range(1, 5):
#     for j in range(10, 16):
#         print(j, end=" ")
#     print("")

n = int(input("Enter the number of rows you want: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print("")