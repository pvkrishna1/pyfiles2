class X:
    def m1(self):
        print("in m1 of x")
class Y(X):
    def m2(self):
        print("in m2 of y")
class Z(Y):
    def m3(self):
        print("in m3 of Z")
z1=Z()
p=z1.__hash__()
print(p)
z1.m1()
z1.m2()
z1.m3()
