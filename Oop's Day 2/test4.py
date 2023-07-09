# import utils.util1
from utils.util1 import person1

obj = person1('chomya', 'chomi', 487987)
print(obj.yob1)

class school:
    def __init__(self, name, surname, yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

sudh = school("jaibai", "chaudhari", 1990)

print(sudh._name1)
print(sudh._school__surname1)