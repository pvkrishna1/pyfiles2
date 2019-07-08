class X:
    def m1(self):
        print("in m1 of X")
class Y:
    def m2(self):
        print("in m2 of Y")
class Z:
    def m3(self):
        print("in m3 of Z")
class A(X,Y):
    def m4(self):
        print("in m4 of A")
class B(Y,Z):
    def m5(self):
        print("in m5 of B")
class M(A,B,Z):
    def m6(self):
        print("in m6 of M")
m=M()
i=m.__hash__()
print(i)
m.m1()
m.m2()
m.m3()
m.m4()
m.m5()
m.m6()
