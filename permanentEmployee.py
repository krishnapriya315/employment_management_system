from Employee import Employee   #import perant class

class PermanentEmployee(Employee):    #child class
    def calculate_salary(self):  #polimorphisam

        total_salary=self.basic_salary+(self.basic_salary*20)/100
        print("totalsalary:",total_salary)
        return total_salary
    def display_detials(self):   #polimorphisam
        print("name:",self.name)
        print("basicsalary:",self.basic_salary)
        print("work model:",self.work_model)
