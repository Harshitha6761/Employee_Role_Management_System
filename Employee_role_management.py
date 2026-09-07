#employee role management system
import abc
from abc import ABC,abstractmethod
class Employee(ABC):
    employee_count=0 #class Attribute
    company = "Tech solutions"
    def __init__(self,name="none",id_numb = "none",role="none"):
        self.name=name
        self.id_numb = id_numb
        self.role = role
        self.dep=self.department(role)
        self.salary=self.calculate_salary()
        Employee.employee_count+=1
    def department(self,role):
        if role == "developer":
            self.dep="Development department"
        elif role == "manager":
            self.dep = "Administration"
        elif role == "intern":
            self.dep = "Internship"
        else:
            self.dep = "invalid_role"
        return self.dep    
    @abstractmethod
    def calculate_salary(self):
        pass
    @classmethod
    def total_employees(cls):
        return cls.employee_count
    def summary(self,id_numb):
        print(f"Name of employee --> {self.name}")
        print(f"Id of employee --> {self.id_numb}")
        print(f"Departmnet of employee --> {self.dep}")
        print(f"Salary of employee --> {self.salary}")
        print(f"Role of employee --> {self.role}")
        print(f"Name of company --> {Employee.company}")
class Manager(Employee):
    def calculate_salary(self):
        salary=500000
        return salary
    def mrole(self):
        print("The role of manager is to assign tasks to everyone and handle the administration tasks")
class Developer(Employee):
    def calculate_salary(self):
        salary=200000
        return salary
    def drole(self):
        print("Develops the website and applications")
    
class Intern(Employee):
    def calculate_salary(self):
        salary=30000
        return salary
    def irole(self):
        print("assist the developer")
class Promotion:
    def __init__(self,employee):
        self.employee=employee
    def check_promotion_eligibility(self,project,experience):
        if project>5 and experience>6:
            print(f"{self.employee.name} is eligible for the promotion")
        else:
            print(f"{self.employee.name} is not eligible for promotion")

class Performance:
    def __init__(self,employee):
        self.employee=employee
    @staticmethod
    def get_rating_label(rating):
        labels = {
            5: "Excellent (5-star)",
            4: "Very Good (4-star)",
            3: "Good (3-star)",
            2: "Needs Improvement (2-star)",
            1: "Poor (1-star)",
            0: "No Rating"
        }
        return labels.get(rating, "Invalid Rating")
    def performance_rating(self,ontime_work,attendance,client_numb):
        if ontime_work==True and 90<=attendance<=100 and client_numb>10:
            rating=5
        elif ontime_work ==True and 70<=attendance<90  and 8<=client_numb<10:
            rating=4
        elif ontime_work ==True and 50<=attendance<70 and 8<=client_numb<10:
            rating=3
        elif ontime_work == False and 50<=attendance<70 and 6<=client_numb<8:
            rating = 2
        elif ontime_work == False and 30<=attendance<50 and 6<=client_numb<8:
            rating =1
        else:
            rating = 0
        return rating
    def incentives(self,rating):
        amount=0
        try:
            rating=int(rating)
            if rating>=3:


                amount = 10000
            elif rating>=1:
                amount = 5000
            else:
                amount = 0
        except (ValueError,TypeError) as e:
            print("Enter valid rating")
        self.employee.salary += amount
        print(f"Incentive of {amount} added. New salary of {self.employee.name} --> {self.employee.salary}")
        return amount


'''d = Developer("Ravi", "DEV-0001", "Developer")
print("Before:", d.salary)          
perf = Performance(d)
rating = perf.performance_rating(True, 95, 12)
print(rating)
perf.incentives(rating)            
print("After:", d.salary)          
d.summary()

while True:
    print("1.Employee Registration\n2.Department Management\n3.Developer role\n4.Manager role\n5.Intern Role\n6.Salary Calculation\n7.Performance Rating\n8.Incentive calculation\n9.Promtion\n10.Employee Summary\n11.Exit")
    choice=int(input("enter your choice"))
    if choice ==1 :
        name=input("Enter name of employee")
        ids=input("Enter id number")
        role=input("Enter role")
        if role.lower()=="developer":
            d=Developer(name,ids,role)
            print("Employee registration successful")
        elif role.lower()=="manager":
            m=Manager(name,ids,role)
            print("Employee registration successful")
        elif role.lower()=="intern":
            i=Intern(name,ids,role)
            print("Employee registration successful")
        else:
            print("invalid role")
    elif choice == 2:
        role=input("Enter role of employee")
        if role.lower()=="developer":
            d=Developer(role)
            print(d.department(role))
        elif role.lower()=="manager":
            m=Manager(role)
            print(m.department(role))
        elif role.lower()=="intern":
            i=Intern(role)
            print(i.department(role))
        else:
            print("invalid role")
    elif choice == 3:
        role=input("Enter the role of employee")
        if role.lower()=="developer":
            d=Developer(role)
            d.drole()
        else:
            print("invalid")
    elif choice ==4:
        role=input("Enter the role of employee")
        if role.lower()=="manager":
            m=Manager(role)
            m.mrole()
        else:
            print("invalid")
    elif choice ==5:
        role=input("Enter the role of employee")
        if role.lower()=="intern":
            i=Intern(role)
            i.irole()
        else:
            print("invalid role")
    elif choice == 6:
        role=input("Enter role")
        if role.lower()=="developer":
            d=Developer(role)
            print(d.salary)
        elif role.lower()=="manager":
            m=Manager(role)
            print(m.salary)
        elif role.lower()=="intern":
            i=Intern(role)
            print(i.salary)
        else:
            print("invalid role")
    elif choice == 7:
        on_time = input("Enter whether the candidate is on time or not. True or False")
        attendance=int(input("enter attendance % 0 to 100"))
        client_number=int(input("no of clients candidate registered"))
        p=Performance()
        p.performance_rating(on_time,attendance,client_number)
        
'''
employees = []   # add this once, right before the while loop

while True:
    print("1.Employee Registration\n2.Department Management\n3.Developer role\n4.Manager role\n5.Intern Role\n6.Salary Calculation\n7.Performance Rating\n8.Incentive calculation\n9.Promtion\n10.Employee Summary\n11.Exit")
    choice = int(input("enter your choice"))

    if choice == 1:
        name = input("Enter name of employee")
        ids = input("Enter id number")
        role = input("Enter role")
        if role.lower() == "developer":
            d = Developer(name, ids, role)
            employees.append(d)
            print("Employee registration successful")
        elif role.lower() == "manager":
            m = Manager(name, ids, role)
            employees.append(m)
            print("Employee registration successful")
        elif role.lower() == "intern":
            i = Intern(name, ids, role)
            employees.append(i)
            print("Employee registration successful")
        else:
            print("invalid role")
    elif choice == 2:
        emp_id = input("Enter employee ID")
        emp = next((e for e in employees if e.id_numb == emp_id), None)
        if emp is None:
            print("Employee not found")
        else:
            print(f"Department --> {emp.dep}")

    elif choice == 3:
        emp_id = input("Enter employee ID")
        emp = next((e for e in employees if e.id_numb == emp_id), None)
        if emp is None:
            print("Employee not found")
        elif isinstance(emp, Developer):
            emp.drole()
        else:
            print("This employee is not a Developer")

    elif choice == 4:
        emp_id = input("Enter employee ID")
        emp = next((e for e in employees if e.id_numb == emp_id), None)
        if emp is None:
            print("Employee not found")
        elif isinstance(emp, Manager):
            emp.mrole()
        else:
            print("This employee is not a Manager")

    elif choice == 5:
        emp_id = input("Enter employee ID")
        emp = next((e for e in employees if e.id_numb == emp_id), None)
        if emp is None:
            print("Employee not found")
        elif isinstance(emp, Intern):
            emp.irole()
        else:
            print("This employee is not an Intern")

    elif choice == 6:
        emp_id = input("Enter employee ID")
        emp = next((e for e in employees if e.id_numb == emp_id), None)
        if emp is None:
            print("Employee not found")
        else:
            print(f"Salary of {emp.name} --> {emp.salary}")

    elif choice == 7:
        emp_id = input("Enter employee ID")
        emp = next((e for e in employees if e.id_numb == emp_id), None)
        if emp is None:
            print("Employee not found")
        else:
            on_time = input("Is the employee on time? (True/False): ").strip().lower() == "true"
            attendance = int(input("enter attendance % 0 to 100"))
            client_number = int(input("no of clients candidate registered"))
            p = Performance(emp)
            rating = p.performance_rating(on_time, attendance, client_number)
            print("Rating:", p.get_rating_label(rating))
    elif choice == 8:
        emp_id = input("Enter employee ID")
        emp = next((e for e in employees if e.id_numb == emp_id), None)
        if emp is None:
            print("Employee not found")
        else:
            # reuse the rating stored during choice 7, if available
            rating = getattr(emp, "last_rating", None)
            if rating is None:
                rating = input("No rating found. Enter rating manually (0-5): ")
            p = Performance(emp)
            amount = p.incentives(rating)
            print(f"Incentive awarded --> {amount}")

    elif choice == 9:
        emp_id = input("Enter employee ID")
        emp = next((e for e in employees if e.id_numb == emp_id), None)
        if emp is None:
            print("Employee not found")
        else:
            try:
                project = int(input("Enter number of projects completed"))
                experience = int(input("Enter years of experience"))
                promo = Promotion(emp)
                promo.check_promotion_eligibility(project, experience)
            except ValueError:
                print("Please enter valid numeric values for project and experience")

    elif choice == 10:
        emp_id = input("Enter employee ID")
        emp = next((e for e in employees if e.id_numb == emp_id), None)
        if emp is None:
            print("Employee not found")
        else:
            emp.summary(emp.id_numb)

    elif choice == 11:
        print("Exiting Employee Role Management System. Goodbye!")
        break

    else:
        print("Invalid choice, please select a number between 1 and 11")
        







