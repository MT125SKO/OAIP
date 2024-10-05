from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Машина едет (брбрбр)")

class bike(Transport):
    def move(self):
        print("Велосипед едет (тдтдтд)")

class Plane(Transport):
    def move(self):
        print("Самолет летит (вжух)")

class Transport_Factory:
    @staticmethod
    def create_transport(transport_type):
        if transport_type == "car":
            return Car()
        elif transport_type == "bike":
            return bike()
        elif transport_type == "plane":
            return Plane()
        else:
            raise ValueError(f"Ошибка {transport_type}")
if __name__ == "__main__":
    while True:
        transport_type = input("Средство передвижения car, bike, plane, выход (1) ")
        if transport_type == "1":
            break

        try:
            transport = Transport_Factory.create_transport(transport_type)
            transport.move()
        except ValueError as e:
            print(e)