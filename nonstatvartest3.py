class Test:
    """sample class to test nonstatic variables"""
    def insert(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
    def modify(self):
        self.a=self.a+100
        self.b=self.b-100
t1=Test()
t1.insert()
t1.display()
t2=Test()
t2.display()

        
