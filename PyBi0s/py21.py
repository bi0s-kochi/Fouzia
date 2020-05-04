a = int(input("Enter three numbers to find the largest of the three : \n"))
b = int(input())
c = int(input())
if a==b and b==c :
	print("All are equal")
else:
	p = a if a>b else b
	print("The largest is " + str(c if c>p else p))
