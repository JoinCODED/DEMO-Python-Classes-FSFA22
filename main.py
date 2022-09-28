# # THIS IS A BLUEPRINT
# class Car:
#     # CONSTRUCTOR METHOD
#     def __init__(self, model, year, color, dates_of_service):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.dates_of_service = dates_of_service

#     def greet(self):
#         print("VROOOOOM")

#     def print_service_dates(self):
#         for date in self.dates_of_service:
#             print(date)


# cars = []

# while len(cars) < 2:
#     model = input("Wht brand do you want? ")
#     year = input("What year? ")
#     color = input("What color? ")
#     services = []

#     new_car = Car(model, year, color, services)
#     cars.append(new_car)

#     print(cars)

# print("We're full")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi")

    def __str__(self):
        return f"Hi I'm {self.name}, and I'm {self.age} years old"


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f"{super().__str__()} and my grade is {self.grade}"


person_one = Person("Laila", 25)

print(person_one)
student_one = Student("Abbas", 55, 100)

print(student_one)
