
                                    # Methode Overwriting

class ineuron:

    def students(self):
        print('print the details of all the students ("ineuron")')

    def achivers(self):
        print("print the list of all the ahivers ('ineuron')")

    def hall_of_frame(self):
        print('print everyone from hall of frame')

class ineuron_vision(ineuron):

 # '''this will overwrite in student method  and achivers method'''
    def students(self):
        print('this are filtered students list ("ineuron_vision")')

    def achivers(self):
        print("this are the list of all achivers ('ineuron_vision')")

i = ineuron_vision()
i.students()
i.achivers()
i.hall_of_frame()