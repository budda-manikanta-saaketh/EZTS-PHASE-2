class Employees():
    def __init__ (self):
        self.emp_id=int(input("enter employee id:"))
        self.emp_name=input("enter employee name:")
        self.emp_salary=input("enter employee salary:")
        self.department=input("enter the department:")
    def calculate_emp_salary(self):
        self.hours_worked=int(input("\nenter hours worked:"))
        if self.hours_worked>50:
            self.overtime=self.hours_worked-50
            self.overtime_amount=self.overtime*(self.emp_salary/50)
    def emp_details(self):
        print("\nName:",self.emp_name,"\nEmp id:",self.emp_id,"\nSalary:",self.emp_salary,"\nDepartment:",self.department)
emp1=Employees()
while(True):
    choice=int(input("\n1.Calculate Salary \n2.Employee Details\n3.Exit\nEnter choice:"))
    if choice==1 :
        emp1.calculate_emp_salary()
    if choice==2:
        emp1.emp_details()
    if choice==3:
        break


        