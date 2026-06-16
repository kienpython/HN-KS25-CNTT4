from tabulate import tabulate

def display_attendance_book(attendance_book):
    attendances = list()
    for attendance in attendance_book:
        times = attendance['times']
        clock_in = times[0]
        clock_out = times[1]
        if not clock_out:
            clock_out = "[Đang làm việc]"
        attendances.append([attendance['id'],attendance['name'],clock_in,clock_out])
    table = tabulate(attendances,["Mã NV","Tên Nhân Viên","Giờ Vào","Giờ Ra"],tablefmt="grid")
    print(table)