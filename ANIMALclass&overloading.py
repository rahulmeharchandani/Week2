class animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
        
    def sounds(self):
        return(f"{self.name} make a {self.sound} sound.")
    
class dog(animal):
    def __init__(self, name):
        super().__init__(name,"bark")
        
class lion(animal):        
    def __init__(self,name):
        super().__init__(name,"roar")
        
Dog=dog("Dogesh")
Lion=lion("loin")
print(Dog.sounds())
print(Lion.sounds())
            
class book:
    def __init__(self,price):
        self.price=price
    def __add__(self,other):
        return book(self.price+other.price)
    def __str__(self):
        return(f"Book price = {self.price}")
    
Book1=book(500)
Book2=book(700)
total=Book1+Book2
print(total)                    
            
    