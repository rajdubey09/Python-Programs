#Exception Handling in Python

try:
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    c = a/b
    print("Division is ",c)
    
except Exception as e:
    print(Exception)
    print("can't divide by Zero")
    print(e) 
else:
    print("else Block")
finally:
    print("always run wheather there is any exeption occured or not")
