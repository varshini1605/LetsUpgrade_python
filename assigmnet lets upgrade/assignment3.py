#1.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

#2.
b = car.keys()

print(b)

#3.
car.pop("model")

print(car)

#4.
car.update({"color": "pink"})

print(car)

#5.
d = car.values()

print(d)

