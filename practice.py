class ineuron:
    _name="swapnil"
    __sname="manwatkar"
    yob=1999

    def _age(self, current):
        return current-ineuron.yob

    def __age1(self,current):
        return current-ineuron.yob

class nuro(ineuron):
    def _age(self, current):
        return current - ineuron.yob

    def __age1(self, current):
        return current - ineuron.yob


swa=ineuron()
man=nuro()
print(man._nuro__age1(2002))
print(swa._age(2022))

print(swa._ineuron__age1(2024))