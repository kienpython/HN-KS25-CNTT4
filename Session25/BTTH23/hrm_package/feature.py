def check_exits(attendance_book, employee_id):
    for employee in attendance_book:
        if employee['id'] == employee_id:
            return employee
    return False
