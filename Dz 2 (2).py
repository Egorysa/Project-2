class Employee:
    def __init__(self, name ,position,salary ):
        self.name = name
        self.position = position
        self.salary = salary

    def prachivnuk(self):
        print(f"Ім'я {self.name}. Посада  {self.position}. Заробітня плата  {self.salary}")

get_salary_info = Employee(name="Антон", position="Касир", salary="27000грн")
print(get_salary_info.name)
print(get_salary_info.position)
print(get_salary_info.salary)
get_salary_info.prachivnuk()