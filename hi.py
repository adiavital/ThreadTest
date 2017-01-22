from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def find_location(self):
        pass

    @abstractmethod
    def find_familiy(self):
        pass


class Risky_Entity(Entity):
    def __init__(self):
        super(Risky_Entity,self).__init__()
    @abstractmethod
    def risk_level(self):
        pass


class Girl(Entity):
    def risk_level(self):
        return "she is dangorus"

    def save(self):
        return "saved girl"

    def find_location(self):
        return "girl is here"

    def find_familiy(self):
        return "girl is a mom"


class Risky_Girl(Risky_Entity):
    def save(self):
        return "saved Risky_Girl"

    def find_location(self):
        return "Risky_Girl is here"

    def find_familiy(self):
        return "Risky_Girl is a mom"



girl_1 = Girl()
girl_2 = Risky_Girl()

print(girl_1.save())
print(girl_2.save())
print(girl_2.find_location())
print(girl_2.risk_level())