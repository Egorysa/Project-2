class Rectangle:
    def __init__(self, name ,prince,quantity ):
        self.name = name
        self.prince = prince
        self.quantity = quantity

    def tovar(self):
        print(f"Ім'я {self.name}. Ціна  {self.prince}. Кількість  {self.quantity}")

calculate_total_prace = Employee(name="Булка", prince="5грн", quantity="2 штуки")
print(calculate_total_prace.name)
print(calculate_total_prace.prince)
print(calculate_total_prace.quantity)
calculate_total_prace.tovar()