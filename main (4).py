from abc import ABC,abstractmethod
class four_wheeler(ABC):
    @abstractmethod
    def engine():
        pass
class swift(four_wheeler):
    def car_start():
        return "car is moving"
car_1=swift
ans=car_1.car_start()
print(ans)