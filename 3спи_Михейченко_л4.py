from abc import ABC, abstractmethod
import random

class RouteStrategy(ABC):
  @abstractmethod
  def calculate_route(self, start_city, end_city):
    pass

class dorog_krat(RouteStrategy):
  def calculate_route(self, start_city, end_city):
    distance = abs(start_city['number'] - end_city['number'])
    print(f" отправка  {start_city['name']} в {end_city['name']}: короткий путь {distance} км")

class dorog_cred(RouteStrategy):
  def calculate_route(self, start_city, end_city):
    if random.choice([True, False]):
      distance = abs(start_city['number'] - end_city['number'])
      print(f"отправка  {start_city['name']} в {end_city['name']}: средний путь {distance} км")
    else:
      distance = abs(start_city['number'] - end_city['number']) * 2
      print(f"отправка {start_city['name']} в {end_city['name']}: средний путь {distance} км ")

class dorog_dlin(RouteStrategy):
  def calculate_route(self, start_city, end_city):
    distance = abs(start_city['number'] - end_city['number'])
    print(f"отправка {start_city['name']} в {end_city['name']}: Длинный путь {distance } км ")

class RouteContext:
  def __init__(self, strategy: RouteStrategy):
    self.strategy = strategy

  def find_route(self, start_city, end_city):
    self.strategy.calculate_route(start_city, end_city)

if __name__ == '__main__':
  cities = [{"name": "1", "number": 1},{"name": "2", "number": 2},{"name": "3", "number": 3},{"name": "4", "number": 4},{"name": "5", "number": 5}]

  while True:
    start_city_name = input("Введите начальный город: 1 2 3 4 5 ")
    start_city = next((city for city in cities if city['name'] == start_city_name), None)
    if start_city is None:
      print("Ошибка")
      continue

    end_city_name = input("Точка прибытия 1 2 3 4 5  ")
    end_city = next((city for city in cities if city['name'] == end_city_name), None)
    if end_city is None:
      print("Ошибка")
      continue

    strategies = [dorog_krat(), dorog_cred(), dorog_dlin()]
    strategy = random.choice(strategies)

    context = RouteContext(strategy)
    context.find_route(start_city, end_city)

    another_route = input("Новый путь + ")
    if another_route.lower() != '+':
      break