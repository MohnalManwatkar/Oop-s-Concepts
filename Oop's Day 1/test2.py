class person:
    def __init__(self, name, surname, email, yob):
        self.name = name
        self.surname = surname
        self.email = email
        self.yob = yob

    def age_calculate(self, current_age):
        return current_age - self.yob

rao_var = person('romesh', 'wagmare','r@gmail.com',1991)
sudh = person("sudhanshu", "kumar", "sk@g.com", 1973)
swapnil = person("swapnil", "manwatkar", "sm@g.com", 1968)
m = person("mohnal", "Manwatkar", "mm@g.com", 1999)

print(rao_var.name)
print(rao_var.surname)
print(rao_var.email)
print(rao_var.yob)

print(rao_var.name, rao_var.surname,rao_var.email, rao_var.yob)
print(sudh.name, sudh.surname,sudh.email, sudh.yob)
print(swapnil.name, swapnil.surname,swapnil.email, swapnil.yob)
print(m.name, m.surname,m.email, m.yob)

print(rao_var.age_calculate(2023))
print(sudh.age_calculate(2023))
print(swapnil.age_calculate(2023))
print(m.age_calculate(2023))