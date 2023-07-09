class person:
    def __init__(self, name, surname, email, dob):
        self.name = name
        self.surname = surname
        self.email = email
        self.dob = dob

rao_var = person('romesh', 'wagmare','r@gmail.com',3)
sudh = person("sudhanshu", "kumar", "sk@g.com", 22)
swapnil = person("swapnil", "manwatkar", "sm@g.com", 1)
m = person("mohnal", "Manwatkar", "mm@g.com", 1)

    '''
        class variables = rao_var, sudh, swapnil, m
        objects are nothing but a class variables
    '''

print(rao_var.name)
print(rao_var.surname)
print(rao_var.email)
print(rao_var.dob)

print(rao_var.name, rao_var.surname,rao_var.email, rao_var.dob)
print(sudh.name, sudh.surname,sudh.email, sudh.dob)
print(swapnil.name, swapnil.surname,swapnil.email, swapnil.dob)
print(m.name, m.surname,m.email, m.dob)
