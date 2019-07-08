class Test:
    """sample test to test non static variables"""
    def insert(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
t1=Test()
t1.insert()
t1.display()
print(t1.a)
print(t1.b)
t2=Test()
t2.insert()
t2.display()
print(t2.a)
print(t2.b)
