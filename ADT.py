class Employee:
    count=0
    def __init__(self,name,desig,salary):
        self.name=name
        self.desig=desig
        self.salary=salary
        Employee.count+=1
    def displayCount(self):
        print("there are %d employees " %Employee.count)
    def displayDetails(self):
        print("name:", self.name , "designation:" , self.desig , "salary:", self.salary)
e1=Employee("Prakash","Manager",80000)
e2=Employee("Preetam","Team Leader",50000)
e3=Employee("subu","Programmer",30000)
e4=Employee("Devu","Assistant",25000)
e4.displayCount()
print("details of all employee")
e1.displayDetails() 
e2.displayDetails()        
e3.displayDetails()               
e4.displayDetails()        

