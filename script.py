# while True:
#     num1 = int(input("Enter number 1: "))
#     num2 = int(input("Enter number 2: "))
#     op = input("Enter your operation: ")

#     if(op=="+"):
#         res = num1 + num2
#         print("your result is",res)
#     elif(op=="-"):
#         res = num1 - num2
#         print("your result is", res)
#     elif(op=="*"):
#         res = num1 * num2
#         print("your result is", res)
#     elif (op == "/"):
#         res = num1 / num2
#         print("your result is", res)
#     elif (op == "**"):
#         res = num1 ** num2
#         print("your result is", res)

n = int(input("Enter the number of rows you want: "))
i = 0
j = 0

for i in range(i,n+1):
    i = i+1
    for j in range(j,i+1):
        j = j+1
        print("*")
    print("")