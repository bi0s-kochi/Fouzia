a = int(input("Enter two numbers to perform swapping : "))
b = int(input())
print("Before swapping : \nA ="+str(a)+"\tB = "+str(b))
a = a + b
b = a - b
a = a - b
print("After swapping : \nA ="+str(a)+"\tB = "+str(b))
