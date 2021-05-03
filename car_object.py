class Car:
  def __init__(self, make, color, year, name, transmission, isOn=True):
    self.make = make
    self.color = color
    self.year = year
    self.name = name
    self.transmission = transmission
    self.isOn = isOn

  def car_make(self):
    print("This " + self.name + " make is " + self.make)

  def checkStatus(self):
    return self.isOn

  def turnOn(self):
    status = self.checkStatus()
    print(status)
    if status == False:
      self.isOn = True
      print("Just turn car on, zoom off!!!")
    else:
      print("The car is on and ready")

  def turnOff(self):
    status = self.checkStatus()
    if status:
      self.isOn = False
    else:
      print("The car is already off")


car_A = Car("Mercedez Benz", "Black", 2021, "car_A", "Auto")

print(car_A.name + " name is " + car_A.make)
print(car_A.name + " color is " + car_A.color)
# car_A.isOn = True

car_A.turnOn()

# car_A.make = "Benz"
# car_A.color = "Red"
# car_A.name = "car_A"

# print(car_A.make)
# print(car_A.color)


car_B = Car("Audi", "Blue", 2023, "car_B", "Manual", False)
print(car_B.name + " year is " + str(car_B.year))
print(car_B.name + " transmission is " + car_B.transmission)

car_B.turnOff()

# car_B.make = "Audi"
# car_B.color = "Red"
# car_B.name = "car_B"
