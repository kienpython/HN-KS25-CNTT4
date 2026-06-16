from hrm_package.ui_display import display_attendance_book
from hrm_package.attendance_logic import clock_in
from hrm_package.feature import check_exits
from datetime import datetime

def clock_out(attendance_book):
    employee_id = input("Nhập mã nhân viên: ").strip().upper()
    employee = check_exits(attendance_book, employee_id)
    if not employee:
        print("Nhân viên không tồn tại!")
        return
    if employee['times'][1]:
        print("Nhân viên đã chấm công ra!")
        return 
    clock_out = input("Nhập giờ ra: ")

    split_clock_out = clock_out.split(":") #["09","45"]
    hour = split_clock_out[0]
    minute = split_clock_out[1]
    if not((hour.isdigit() and int(hour) >= 0 and int(hour) <= 23) and (minute.isdigit() and int(minute) >= 0 and int(minute) < 60)):
        print("Định dạng time không đúng!")
        return
    new_times = (employee['times'][0],clock_out)
    employee["times"] = new_times
    

def main():
    attendance_book = [
        {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
        {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)}, # Đang làm việc, chưa chấm công ra
        {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
    ]
    while True:
        choice = input("""=== HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===
1. Xem bảng chấm công ngày
2. Chấm công Vào (Clock-in)
3. Chấm công Ra (Clock-out)
4. Đánh giá vi phạm
5. Thoát chương trình 
================================================= 
Chọn chức năng (1-5): """)
        match choice:
            case "1":
                display_attendance_book(attendance_book)
            case "2":
                clock_in(attendance_book)
            case "3":
                clock_out(attendance_book)
            case "4":
                pass
            case "5":
                break
if __name__ == "__main__":
    main()