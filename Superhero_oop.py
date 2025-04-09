# Base class
class Superhero:
    def __init__(self, hero_name, home, power_level):#Parameters 
        self._name = hero_name  #Attributes of the superhero , name , origin, power level 
        self.origin = home
        self.power_level = power_level

    def use_power(self):#funtions :Describes what happens when the super hero uses their powers 
        return f"{self._name} uses their default superpower!"

    def get_identity(self): #Gets the superhero name and where they come from 
        return f"Superhero: {self._name}, Origin: {self.origin}"

# Subclass 1
class FlyingHero(Superhero):#This class inherits from hero 
    def __init__(self, hero_name, home, power_level, flight_speed):#It calls the Superhero constructor using super().__init__() to reuse the name, origin, and power level setup.
        super().__init__(hero_name, home, power_level) #This method overrides the original use_power() method in the parent class. #Instead of the generic message, it now describes flying, using the flight_speed value.

        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self._name} pierces through the sky at {self.flight_speed} km/h!"

# Subclass 2
class TechHero(Superhero):#Like FlyingHero, this class inherits from Superhero. #It uses the same super().__init__() call to set up the basic attributes.
    def __init__(self, hero_name, home, power_level, gadgets):#Then it adds a new one: gadgets, which is a list of tools or weapons the hero uses.
        super().__init__(hero_name, home, power_level)
        self.gadgets = gadgets

    def use_power(self):
        return f"{self._name} uses amazing gadgets like {', '.join(self.gadgets)}!"

# Example usage
hero1 = FlyingHero("SuperGirl", "River Side", 90, 300)
hero2 = TechHero("Blade", "Rose Park", 85, ["Rope", "Arrow", "Blade and Shield"])

print(hero1.get_identity()) #Prints identity: name and origin.
print(hero1.use_power())#Prints their power (flying at 300 km/h).

print(hero2.get_identity()) #Prints identity: name and origin
print(hero2.use_power()) #Prints their power (flying at 300 km/h).
