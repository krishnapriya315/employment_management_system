from Employee import Employee   #import perant class

class ContractEmlpoye(Employee): #chiled class
    def calculate_salary(self):   # calculate salary methord for calculating salary
        total_salary= self.display_detials+(self.basic_salary*0.2)
        print("totalsalary:",total_salary)
        return total_salary

    def display_detials(self):  # display methord for displaying some details
        print("name:",self.name)
        print("basicsalary:",self.basic_salary)
        print("work model:",self.work_model)
        