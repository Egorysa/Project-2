class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def brumbrum(self):
        print(f"Марка машини {self.make}. Модель машини {self.model}. Рік винаходження {self.year}")

one_car = Car(make="BMW", model="M5", year="1986")
print(one_car.make)
print(one_car.model)
print(one_car.year)
one_car.brumbrum()