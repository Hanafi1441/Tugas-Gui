from abc import ABCMeta,abstractmethod

# class Abctrack

class DuaDimensi(metaclass=ABCMeta) :
    @abstractmethod

    def luas(self):

        pass
# Class SegiEmpat turunan dari class duaDimensi

class SegiEmpat(DuaDimensi):

    def __init__(self,p,l):

        self.panjang = p
        self.lebar = l

    def luas(self):
        return self.panjang * self.lebar
class Segitiga(DuaDimensi):

    def __init__(self,a , t):

        self.alas = a
        self.tinggi = t

    def luas(self):
        return (self.alas * self.tinggi) / 2
class Lingkaran(DuaDimensi):

    def __init__(self,r):
        self.jari2 = r

    def luas(self):
        import math
        return math.pi * (self.jari2 ** 2)
myList = []

myList.append(SegiEmpat(10, 8))

myList.append(Segitiga(3, 5))

myList.append(Lingkaran(4))

for obj in myList:
    if not issubclass(obj.__class__,DuaDimensi):
        raise TypeError('Objek harus turunan dari DuaDimensi')
    if isinstance(obj,SegiEmpat):
        print('Luas Segi empat= ', end='')
    elif isinstance(obj,Segitiga):
        print('Luas Segitiga = ',end='')
    else:
        print('Luas Lingkaran = ',end=' ')
    print(obj.luas())
