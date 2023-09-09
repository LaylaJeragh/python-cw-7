class Person :
    #attributes:
    Name = "Layla"
    Age = 15
    #method:
class Person:
    def __init__(self, Name, Age):
      self.Name = Name
      self.Age = Age
    

    def is_adult(self):
        if self.Age > 18:
            return("You have too much responsibilities")
        elif self.Age<18:
            return("Lucky you!!!")
        else:
            return("invalid age")

    def __str__(self):
       return f"My name is {self.Name}and I am {self.Age} years old "
   
First_Person = Person("Layla",15)
print(First_Person.Name)
print(First_Person.Age)
print(First_Person.is_adult())
print(First_Person)
