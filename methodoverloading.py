class A:
    def add(self, x, y=0, z=0):
        return x + y + z

calc = A()
print(calc.add(6))        
print(calc.add(6, 3))     
print(calc.add(6, 3, 7))  