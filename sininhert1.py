class X:
    def m1(self):
        print("in m1 of x")
x1=X()
p=x1.__hash__()
print(p)
x1.m1()
