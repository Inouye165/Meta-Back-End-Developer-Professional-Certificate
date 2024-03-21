# This excercise demonstrated the use of abstract classes in Python.

# "If you remove the @abstractmethod decorator, the code still functions, 
# but you lose the guarantee that derived classes will implement the 
# specified methods. This introduces potential for runtime issues if a 
# derived class is used without providing the expected behavior. By using 
# the decorator, you enforce the interface contract defined by the abstract 
# , catching these inconsistencies at instantiation time rather than facing 
# unexpected behavior later."



from abc import ABC, abstractmethod

class Pet(ABC):
	@abstractmethod # This is the abstract method decorator. 
	def make_sound():
		pass
class Dog(Pet):	
	def make_sound(self):
		print("Woof")
class Cat(Pet):
	def make_sound(self): # For better understanding, I comment out this method and run the code. You will see an error message.
		print("Meow")   # TypeError: Can't instantiate abstract class Cat with abstract methods make_sound. Without abc you will not get this error message.

class Bird(Pet):
	def make_sound(self):
		print("Tweet")

dobby = Dog()
kitty = Cat()
tweety = Bird()

dobby.make_sound()
kitty.make_sound()
tweety.make_sound()