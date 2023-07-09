class ineuron:

    def __init__(self):
        ''' Public Variable '''
        self.students1 = "Data Science"

    def students(self):
        print(self.students1)

i = ineuron()
i.students()
i.students1 = "Data Analytics"
i.students()

class ineuron1:

    def __init__(self):
        ''' Privet Variable '''
        self.__students1 = "Data Science"

    def students(self):
        print(self.__students1)


        '''this is use to change the data from data science to big data '''

    '''def students_change(self):       
        self.__students1 = "Big Data" '''

    def students_change(self, new_values):
        self.__students1 = new_values

i1 = ineuron1()
i1.students()

'''in private variable this methoode is not applicable to change the data thats why we create new method  called students_change'''
i1.__students1 = "big Data"
i1.students()

'''to change the value of the private variable we have to call'''
# i1.students_change()
i1.students_change('swapnil')
i1.students()