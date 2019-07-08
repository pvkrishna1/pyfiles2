class X:
    def m1(self):
        print("in m1 of X")
    def m2(self):
        print("in m2 of X")
    def __str__(self):
        return "lokeshit"
x1=X()
print(x1)
p=x1.__str__()
print(p)
x1.m1()
x1.m2()
