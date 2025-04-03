class Car:
    def __init__(self, brand, model, year,origin_country,body_type):  # Constructor
        self.brand = brand
        self.model = model
        self.year = year
        self.origin_country = origin_country
        self.body_type = body_type


    def display_info(self):
        return f"{self.year} {self.brand} {self.model} {self.origin_country} {self.body_type}"

# Creating objects (instances)
car1 = Car("Toyota", "Corolla", 2020,"Sedan","Japan",)
car2 = Car("Honda", "Civic", 2022,"Sedan","Japan",)

print(car1.display_info())  # Output: 2020 Japan Gasoline Toyota Corolla
print(car2.display_info())  # Output: 2022 Japan Diesel Honda Civic