class X:
    def m1(self):
        print("in m1 of x")
class Y:
    def m2(self):
        print("in m2 of y")
class Z(X,Y):
    def m3(self):
        print("in m3 of z")
z1=Z()
i=z1.__hash__()
print(i)
z1.m1()
z1.m2()
z1.m3()
