class person:
    def __init__(self,name,sname,email):
        self.name = name            #public variable
        self._sname=sname           #privet variable
        self.__email = email        #protected variable

swa=person("swapnil",'manwatkar', "smanwatkar1@gmaill")

print(swa.name)
print(swa._sname)
print(swa._person__email)