#Car CLass
class  Car:
    def __init__(self,modelName,Year):
        self.modelName = modelName
        self.Year = Year
        self.Model = "Top Model"

    def display(self):
        print(self.modelName,self.Year,self.Model)
        print("This is Display Function")

C1 = Car("Toyota",2020)
C1.display()
 
