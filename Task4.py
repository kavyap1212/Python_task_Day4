# 1. Create a program class called circle with constructor which will take a list as an argument for the task.
List1 = [10,501,22,37,100,999,87,351]
class Circle:
    def __init__(self):
        self.list = List1
    def num(self):
        print(self.list)
Cir=Circle()
Cir.num()

# 2. Create proper member variables inside the task if required and use them when necessary.For example for this task create a class private variable named pi=3.141
class myClass:
    pi = 3.141;
    def __privMeth(self):
        print("I'm inside class myClass")
    def hello(self):
        print("Private Variable value: ",myClass.pi)
pv = myClass()
pv.hello()

# 3. From the given List create two class Methods Area and Perimeter which will be going to calculate the Area
class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**3.141
    def perimeter(self):
        return 2*self.radius*3.141

Cir1 = Circle(2)
print(Cir1.area())
print(Cir1.perimeter())

# 4. Convert theUML diagram into python Class & its methods
# Part A Class definition
class TV():
    brand = str
    channel = str
    price = int
    inches = float
    OnOFF_status = bool
    volume = int
    def __init__(self, brand, channel, price, inches, OnOFF_status, volume):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.OnOFF_status = False
        self.volume = volume
    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
    def set_channel(self, channel):
        if channel <= 50 and channel >= 1:
            self.channel = channel
    def reset(self):
        self.channel = 1
        self.volume = 50
    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"
# Part B Class definition
class LEDTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand, channel, price, inches, OnOFF_status, volume)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return f"{self.brand} LED TV:\n\tScreen thickness: {self.screen_thickness}\n\tEnergy usage: {self.energy_usage}\n\tLifespan: {self.lifespan}\n\tRefresh rate: {self.refresh_rate}\n\tViewing angle: {self.viewing_angle}\n\tBacklight: {self.backlight}"

class PlasmaTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, contrast_ratio):
        super().__init__(brand, channel, price, inches, OnOFF_status, volume)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.contrast_ratio = contrast_ratio

    def display_details(self):
        return f"{self.brand} Plasma TV:\n\tScreen thickness: {self.screen_thickness}\n\tEnergy usage: {self.energy_usage}\n\tLifespan: {self.lifespan}\n\tRefresh rate: {self.refresh_rate}\n\tViewing angle: {self.viewing_angle}\n\tContrast ratio: {self.contrast_ratio}"
    
brand = 'Panasonic'
volume = 75
channel = 8
price = 12000
inches = 65
OnOFF_status = False
screen_thickness = 0.5
energy_usage = 100
lifespan = 50000
refresh_rate = 120
viewing_angle = 178
backlight = "LED"
contrast_ratio = "1000000:1"
# Part A
obj_tv = TV(brand, channel, price, inches, OnOFF_status, volume)
print(obj_tv.status())
# Part B
obj_LED = LEDTV(brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight)
obj_Plasma = PlasmaTV(brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, contrast_ratio)

print("Enter the TV type to get the display details:")
TV_type = input()

if TV_type == 'LED':
    print(obj_LED.display_details())
if TV_type == 'Plasma':
    print(obj_Plasma.display_details())

