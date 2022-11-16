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
    def __init__(self, name="Tim", emp_id="E0001", exp=5, dept="R&D"):
        self.Name = name
        self.Emp_id = emp_id
        self.Exp = exp
        self.Dept = dept
        print("Employee {} is created".format(self.Emp_id))
        
    def calcSalary(self): #self is passing the object that gets created
        if self.Exp > 5 and self.Dept == "R&D":
            self.Salary = 200000
        else:
            self.Salary = 80000
        print("Salary of {} calculated".format(self.Name))
            
    def empDesc(self):
        print("Employee {} from {} department working with us for this many years".format(self.Name,self.Dept,self.Exp))


# empl = employee(name="Dan",emp_id="E0002",exp=0,dept="HR")
# empl.calcSalary()
# print(empl.Salary)
# empl.empDesc()

# class newEmployee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     def get_salary(self):
#         return self.salary

# newEmp = newEmployee("Tadeo",600)

# print(newEmp.name)
# print(newEmp.get_salary())

# ================================
# Inheritance: pass the properties of one class onto another
# ================================

class subEmployee(employee): #employee is the super class
    def __init__(self, name="Tim", emp_id="E0001", exp=5, dept="R&D",sub_id="001"):
        super(subEmployee,self).__init__(name,emp_id,exp,dept)
        # self.Name = name
        # self.Emp_id = emp_id
        # self.Exp = exp
        # self.Dept = dept
        self.Sub_ID = sub_id
        print("Employee {} is created for subsidiary {}".format(self.Emp_id, self.Sub_ID))

    def calcSalary(self):
        self.Salary = min(max(1,self.Exp)*30000,200000)

empl_sub = subEmployee("Tadeo","E0004",10,"Marketing","7009")
empl_sub.calcSalary()
print(empl_sub.Salary)
# print(empl_sub)
