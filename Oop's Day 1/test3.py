#### code without using constructor

class person:

    def age(self):
        current_year=int(input("enter current year: "))
        year_of_birth=int(input("enter year of birth: "))
        return current_year - year_of_birth

    def email_id_input(self, email_id):
        print("take a mail id from a person and print it ", email_id)

    def ask_name(self):
        name = input("enter the name: ")
        return name

    def ask_dob(self):
        yob = input("enter the year of birth: ")
        return yob

sudh = person()
swapnil = person()
sahil = person()
gargi = person()


print(sudh.email_id_input("sudhanshu@gmail.com"))
print(swapnil.ask_dob())
print(sahil.age())