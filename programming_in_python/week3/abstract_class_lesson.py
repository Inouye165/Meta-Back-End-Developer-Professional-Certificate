# lesson from https://www.coursera.org/learn/programming-in-python/lecture/rh0lN/abstract-classes-and-methods
form abc import ABC, abstractmethod
class AbstractCoffee(ABC):
    @abstractmethod
    def donate(self):
        pass
