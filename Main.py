class Person:
    def __init__(self, name, age, occupation) :
        self.name = name
        self.age = age
        self.occupation = occupation

    #getter and setter for name
    def get_name(self):
      return self._name 
    

    def set_name(self, name):
        self._name = name
    
    #getter and setter for age
    def get_age(self):
        return self._age
    

    def set_name(self, age):
        self._age = age
    

    #getter and setter for age

    def get_occupation(self):
        return self._occupation
    

    def set_occupation(self, occupation):
        self._occupation = occupation


person1 = Person("harry", 25 ,"engineer")
print("i am" + " " +person1.name)
    

class Vehicle:
    def __init__(self, brand, model, year) :
        self.brand = brand
        self.model = model
        self.year = year

    def Vehicle_details(self, brand, model, year):
        print(f"Brand  :{self.brand}")
        print(f"Model  :{self.model}")
        print(f"Year   :{self.year}")


car = Vehicle("Toyota", "Corolla", 2022)
car.Vehicle_details("Toyota", "Corolla", 2022)

        
        

