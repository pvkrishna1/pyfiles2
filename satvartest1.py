class Test:
    """sample class to test the variables"""
    a=1000
    b=2000
    def display(self):
        print(Test.a)
        print(Test.b)
t1=Test()
t1.display()
print(Test.a)
print(Test.b)
print(t1.a)
print(t1.b)
