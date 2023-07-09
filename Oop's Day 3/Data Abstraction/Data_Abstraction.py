class ineuron:

    __students = "Data science"  #privet variamle

    '''dont want to sho my data directly / i want to hide my data that's why i create student method'''
    def students(self):
        print("print the class of students", ineuron.__students)

i=ineuron()
i.students()
i._ineuron__students

