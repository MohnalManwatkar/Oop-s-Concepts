            # Inheritence : class inside a class

                    # part 1

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

###############################################################################################
# --------------------------------part 2------------------------------------------------------
###############################################################################################
                    # creating functions in class and calling it

class person:  # parent class

    _name = "swapnil"
    __surname = "manwatkar"
    yob = 1999

    def _age(self, current_age):
        return current_age - self.yob

    def __age1(self, current_age):
        return current_age - self.yob

obj = person()
print((obj))
print('age:', obj._age(2023))
print('age:', obj._person__age1(2023))

class employee(person):  # child class
    pass

obj1 = employee()

print(obj1._age(2023))          # we can call "_age" function and "__age1" function in other child class also
print(obj1._person__age1(2023))

print(obj1)
print(obj.yob)
print(obj1._name)
print(obj1._person__surname)


###############################################################################################
# ----------------------------------part 3---------------------------------------------------
###############################################################################################
                        # importing test4.py file as module

import test4
print(test4)
obj3 = test4.school("jaibai", "chaudhari", 1990)  #agar import karnw wale file me '__init__()' use kiye hai to aisa execute krna padeng jab bhi usko call karenge to
print(obj3.yob1)
print(obj3._name1)
print(obj3._school__surname1)

class person:  # parent class

    _name = "swapnil"
    __surname = "manwatkar"
    yob = 1999

    def _age(self, current_age):
        return current_age - self.yob

    def __age1(self, current_age):
        return current_age - self.yob

obj = person()
print((obj))
print('age:', obj._age(2023))
print('age:', obj._person__age1(2023))

class employee(person):  # child class
    pass

obj1 = employee()

print(obj1._age(2023))          # we can call "_age" function and "__age1" function in other chile child class also
print(obj1._person__age1(2023))

print(obj1)
print(obj.yob)
print(obj1._name)
print(obj1._person__surname)