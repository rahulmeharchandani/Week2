def studentfile():
    try:
        file=open("student.txt","a")
        name=input("enter a name = ")
        age=input("enter age = ")
        marks=input("enter marks = ")
        file.write(f"{name}, {age}, {marks}\n")
        file.close()
        print("Student details saved.")
        
        file=open("student.txt","r")
        print("\n __student records__")
        print(file.read())
        file.close
        
    except exception as e:
        print("Error= ",e)
        
        
def divisiontask():
    try:
        n1=int(input("Enter first no. ="))  
        n2=int(input("Enter second no. ="))              
        result=n1/n2
        print("Result =",result)
    except ZeroDivisionError:
        print("Error: division by zero not allowed")
    except ValueError:
        print("Error: please enter valid value")
        
class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def save_file(self):
        file=open("employee.txt","a")
        file.write(f"{self.name}, {self.age}, {self.salary}\n")
        file.close()
        
    def display_employees():
        try:
            file = open("employee.txt", "r")
            print("\n--- Employee Records ---")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No employee records found.")

def employee_task():
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    salary = input("Enter employee salary: ")

    emp = employee(name, age, salary)
    emp.save_file()
    print("Employee details saved successfully!")

    employee.display_employees()   
        
print("Choose a task:")
print("1. Student File Handling")
print("2. Exception Handling (Division)")
print("3. Employee File Handling with Class")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    studentfile()
elif choice == "2":
    divisiontask()
elif choice == "3":
    employee_task()
else:
    print("Invalid choice.")        