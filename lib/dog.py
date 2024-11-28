#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name     
        self.breed = breed 

    def bark(self):
        print("Woof!") 
    
    def sit(self):
        print("The dog is sitting.") 

fido = Dog("Fido", "Beagle")  
print(fido.name) 
print(fido.breed)  
fido.bark() 
fido.sit() 

buddy = Dog("Buddy")
print(buddy.name)
print(buddy.breed) 
buddy.bark() 
buddy.sit()  

