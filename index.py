# =============================================================================
# import math
# 
# radius = 10.4
# 
# def calAreaSquare(rad):
#     # return math.pi * rad * rad
#     print(math.pi * rad * rad)
# 
# dir(float)
# 
# print('testing with Spyder')
# 
# =============================================================================

class employee:
    def __inti__(self, name, emp_id, exp, dept): # this is a magic method, they will get executed automatically
        # attributes of class employee
        self.Name = name
        self.Emp_id = emp_id
        self.Exp = exp
        self.Dept = dept
        
    def calcSalary(self): #self is passing the object that gets created
        if self.Exp > 5 and self.Dept == "R&D":
            self.Salary = 200000
        else:
            self.Salary = 80000
            
    def empDesc(self):
        print("Employee {} from {} department working with us for this many years" . format(self.Name,self.Dept,self.Exp))
            
        