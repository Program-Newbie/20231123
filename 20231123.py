class Employee :
    def __init__(self,emp_name,emp_id,emp_salary,emp_department) :
        self.id = emp_id
        self.name = emp_name
        self.salary = emp_salary
        self.department = emp_department

    def calculate_emp_salary(self,hours_worked) :
        total = self.salary * hours_worked
        if(hours_worked > 50) :
            overtime = hours_worked - 50
            total += overtime*(self.salary/50)
        print(f"{self.name}'s Total Salary: {total}")

    def emp_assign_department(self,new_dep):
        self.department = new_dep

    def print_employee_details(self):
        print(f"Name: {self.name}, Id: {self.id}, Salary: {self.salary}, Department: {self.department}.")

if __name__ == "__main__" :
    print("---------------------------------------------------------------")
    E1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
    E2 = Employee("JONES", "E7499", 45000, "RESEARCH")
    E1.print_employee_details()
    E2.print_employee_details()
    E1.calculate_emp_salary(60)
    E1.emp_assign_department("Microsoft")
    print("---------------------------------------------------------------")
    E1.print_employee_details()
    E2.print_employee_details()
    print("---------------------------------------------------------------")
