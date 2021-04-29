class persegiPanjang :
    # variable
    counter = 0
    #constructor
    def __init__(self, p, l):
        #object variable
        self.panjang = p
        self.lebar = l
# Encapsulation
    def ubahPanjang (self, p) :
        self.panjang = p

    def ubahLebar (self, l) :
        self.lebar = l

#---End Encapsulastion

    def hitungLuas(self):
        return self.panjang * self.lebar

    def hitungKeliling(self):
        return  2 * (self.panjang+self.lebar)

    def cetakLuas(self):
        print(f'Luas persegi Panjang\t:{self.hitungLuas()} ')
    def cetakKeliling(self):
        print(f'Keliling persegi Panjang\t: {self.hitungKeliling()}')

objectPP1 = persegiPanjang(10, 8)

objectPP2 = persegiPanjang(9, 8)

objectPP3 = persegiPanjang(8, 8)

objectPP1.cetakLuas()

objectPP1.cetakKeliling()

objectPP1.counter = 10

