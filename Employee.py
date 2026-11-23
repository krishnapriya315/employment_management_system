from abc import ABC ,abstractmethod   #import abstraction methord

class Employee(ABC):   #perent class
    @abstractmethod
    def calculate_salary(self): #this is abstract methord
        pass   #pass help to escape from errors
    def display_detials(self): #poly morphisam
        pass
    def __init__(self,name,basic_salary,work_model):
        self.name=name
        self.__basic_salary=basic_salary        #constracters
        self.work_model=work_model

    @property
    def basic_salary(self):  # encapsulation 
        return self.__basic_salary