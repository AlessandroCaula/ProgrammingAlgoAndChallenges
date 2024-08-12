# Day 41

## Only Words with Vowels

'''
Create a function called words_with_vowels, this function takes a string of words and returns a list of only words that have vowels in them. 
For example 'You have no rhythm' should return ['You','have', 'no']. 
'''

def words_with_vowels(string):
    string_split = string.split(' ')
    only_vowels = [word for word in string_split if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word]
    return only_vowels

string = 'You have no rhythm'
print(words_with_vowels(string))

print()

## Extra Challenge

'''
Create three classes of three car brands – Ford, BMW, and Tesla. The attributes of the car's objects will be, model, color, year, transmission, and whether the car is electric or not (Boolean value.) 
Consider using inheritance in your answer. 

You will create one object for each car brand:

bmw1 : model: x6, Color: silver, Year: 2018, Transmission: Auto, Electric: False  
tesla1:  model: S, Color: beige, Year: 2017, Transmission: Auto, Electric: True 
ford1 :  model:  focus, Color: white, Year: 2020, Transmission: Auto, Electric: False 

You will create a class method, called print_cars that will be able to print out objects of the class. 
For example, if you call the method on the ford1 object of the Ford class, your function should be able to print out car info in this exact format:
car_model = focus 
Color = White  
Year = 2020  
Transmission = Auto  
Electric = False 
'''

class Car():
    def __init__(self, model, color, year, transmission, electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric
    
    def print_cars(self):
        print(f"Car model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Year: {self.year}")
        print(f"Transmission: {self.transmission}")
        print(f"Electric: {self.electric}")
        

class Ford(Car):
    def __init__(self, model, color, year, transmission, electric):
        super().__init__(model, color, year, transmission, electric)    # The super() function that will make the child class inherit all the methods and properties from its parent.
                                                                        # By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
class BMW(Car):
    pass    # Use the pass keyword when you do not want to add any other properties or methods to the class.

class Tesla(Car):
    def __init__(self, model, color, year, transmission, electric):
        Car.__init__(self, model, color, year, transmission, electric)  # Adding the call to the parent, to keep the inheritance of the parent's __init__() function.


bmw1 = BMW(model="x6", color="silver", year=2018, transmission="Auto", electric=False)
tesla1 = Tesla(model="S", color="beige", year=2017, transmission="Auto", electric=True)
ford1 = Ford(model="focus", color="white", year=2020, transmission="Auto", electric=False)

ford1.print_cars()