from hrm_package.feature import check_exits
def clock_in(attendance_book):
    employee_id = input("Nhập mã nhân viên: ").strip().upper()
    employee = check_exits(attendance_book, employee_id)
    if employee:
        print("Nhân viên đã tồn tại!")
        return
    employee_name = input("Nhập tên nhân viên: ")
    clock_in = input("Nhập giờ vào (HH:MM): ")
    times = (clock_in, None)
    attendance_book.append({
        "id": employee_id, 
        "name": employee_name, 
        "times": times
        })
    print(f"Thành công: Đã ghi nhận {employee_id} chấm công vào lúc {clock_in}!")
