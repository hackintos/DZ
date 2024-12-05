
class TechnicalSpecs:
    def __init__(self, processor, ram, storage):
        self.processor = processor
        self.ram = ram
        self.storage = storage 

    def show_specs(self):
        return f"Processor: {self.processor}, RAM: {self.ram} GB, Storage: {self.storage} GB"


class Display:
    def __init__(self, size, resolution):
        self.size = size
        self.resolution = resolution

    def show_display(self):
        return f"Display: {self.size}\" ({self.resolution})"



class Battery:
    def __init__(self, capacity, battery_life):
        self.capacity = capacity
        self.battery_life = battery_life

    def show_battery(self):
        return f"Battery: {self.capacity} mAh, Battery Life: {self.battery_life} hours"


class Laptop(TechnicalSpecs, Display, Battery):
    def __init__(self, brand, model, processor, ram, storage, size, resolution, capacity, battery_life):
        TechnicalSpecs.__init__(self, processor, ram, storage)
        Display.__init__(self, size, resolution)
        Battery.__init__(self, capacity, battery_life)

        self.brand = brand
        self.model = model

    def show_full_details(self):
        details = f"Brand: {self.brand}, Model: {self.model}\n"
        details += self.show_specs() + "\n"
        details += self.show_display() + "\n"
        details += self.show_battery()
        return details



laptop = Laptop(
    brand="Lenovo",
    model="ideapad 3-15ITL6",
    processor="Intel Core i3",
    ram=8,
    storage=256,
    size=15,
    resolution="1920x1080",
    capacity=7500,
    battery_life=6
)

print(laptop.show_full_details())
