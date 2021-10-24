#Object Oriented Programming 
#Creating Class

class Man:
    def __init__(self):
        #here __init__ is called as Constructor which donot need to call whenever any Object is created 
        #here self is an Object which refers to Man1 ...
        print("THis is __init__ Function in the Man Class")

    #Second Function
    def secondFunc(self):
        print("Second Function is Called")


Man1 = Man()
Man1.secondFunc()
#Man2 = Man()
 
