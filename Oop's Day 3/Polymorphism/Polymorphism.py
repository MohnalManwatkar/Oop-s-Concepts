
# polymorphism

class ineuron:
    def students(self):
        print("print a student details ")

class class_type:
    def students(self):
        print("print the class type of the students ")

''' this function is performing many oprations this fii=unction is called polymorphism'''
def ineuron_external(a):
    a.students()

i = ineuron()  # i is a  object variable for class ineuron
j = class_type()  # j is a object variable for class class_type

ineuron_external(i)  # performing opration for class ineuron
ineuron_external(j)  # performing opration for class class_type


# 'Example'
def function(a,b):
    return a+b

print('------------', function(3,4))                #Addition opration
print('------------', function('MOH', 'NAL'))       #Concatination opration