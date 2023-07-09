class car:

    def __init__(self, body, engin, tyre):
        self.body = body
        self.engin = engin
        self.tyre = tyre

    def milage(self):
        print("Milage of the car")

c = car('solid', 'v4', 'radial')
print(c)
print(c.body)
print(c.milage())

class tata(car):
    pass

t = tata('soliid_1', 'v4_1', 'radial_1')
print(t)

print(t.body)
print(t.engin)
print(t.tyre)

print(t.milage())