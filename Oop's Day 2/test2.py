            # Inheritence : class inside a class

class person:  # parent class

    _name = "swapnil"
    __surname = "manwatkar"
    yob = 1999

obj = person()
print((obj))

class employee(person):  # child class
    pass

obj1 = employee()

print(obj1)
print(obj.yob)
print(obj1._name)
print(obj1._person__surname)

############################################################################################################
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
############################################################################################################

            # Inheritence : class inside a class

class person:  # parent class

    _name = "swapnil"
    __surname = "manwatkar"
    yob = 1999

obj = person()
print((obj))

class employee(person):  # child class
    _name='sudhanshu'
    __surname = 'kumar'

obj1 = employee()

print(obj1)
print(obj.yob)
print(obj1._name)
print(obj1._person__surname)
print(obj1._employee__surname)