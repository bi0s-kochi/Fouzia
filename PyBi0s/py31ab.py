#LIST(mutable)

#acepting values as single input
marks = list(input("Enter 5 marks seperated by space : ").split()) 	
marks[0]="99.9"
print(marks)


#TUPLE(immutable)
marks = tuple(input("Enter 5 marks seperated by space : ").split())
marks[0]="99.9"
print(marks)
