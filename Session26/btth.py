"""
Input:

class Employee(ABC):
def __init__(self, employee_id, name):
- employee_id
- name
def display_info(self):
pass
Abstract Method:
calculate_salary() 

"""

from tabulate import tabulate

# Class trừu tượng Employee
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
    def display_info(self):
        print(self.employee_id)
        print(self.name)
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus
        self.type_employee = "Full-time"
    def calculate_salary(self):
        salary = self.base_salary + self.bonus
        return salary
    def display_info(self):
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: Full-time")
    
class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate
        self.type_employee = "Part-time"

    def calculate_salary(self):
        salary = self.working_hours * self.hourly_rate
        return salary

    def display_info(self):
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: Part-time")
    
class InternEmployee(Employee):
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance
        self.type_employee = "Intern"

    def calculate_salary(self):
        salary = self.allowance
        return salary
    
    def display_info(self):
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: Intern")

def display_employees(employees):
    print("--- DANH SÁCH NHÂN VIÊN ---")

    for employee in employees:
        employee.display_info()

    # data = list()
    # for employee in employees:
    #     data.append([employee.employee_id, employee.name, employee.type_employee])
    # table = tabulate(data, headers=['Mã NV',"Họ tên", "Loại"], tablefmt="grid")
    # print(table)

def display_salaries(employees):
    print("--- BẢNG LƯƠNG NHÂN VIÊN ---")

    FullTimeEmployee.calculate_salary
    for employee in employees:
        print(f"{employee.employee_id} | {employee.name} | Lương: {employee.calculate_salary():,.0f} VND")


def main():
    employees = [
        FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
        PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
        InternEmployee("E003", "Le Van C", 3000000)
    ]
    choice = ""
    while choice != "3":
        print("""\n=== EMPLOYEE SALARY MANAGER ===
1. Xem danh sách nhân viên
2. Tính lương toàn bộ nhân viên
3. Thoát chương trình
================================""")
        choice = input("Chọn chức năng (1-3): ")

        match choice:
            case "1":
                display_employees(employees)
            case "2":
                display_salaries(employees)
            case "3":
                print("Cảm ơn bạn đã sử dụng Employee Salary Manager!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()