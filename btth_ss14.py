def display_grades(grade_book):
    print("--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{"Mã SV":<6} | {"Tên Học Sinh":<15} | {"Điểm Toán":<5} | {"Điểm Anh":<5} | {"ĐTB":<5}")
    print(f"-----------------------------------------------------------------------")
    for grade in grade_book:
        print(f"{grade["id"]:<6} | {grade["name"]:<15} | {grade["info"][0]:<5} | {grade["info"][1]:<5} | {(grade["info"][0]+grade["info"][1])/2:<5}")
    print(f"-----------------------------------------------------------------------")

def add_student(grade_book):
    while True:
        new_id = input('Nhập mã học sinh mới: ')
        found = False
        for grade in grade_book:
            if grade['id'] == new_id:
                print(f"Lỗi: Mã học sinh {new_id} đã tồn tại! Vui lòng nhập mã khác.")
                found = True
                break
        if not found:
            new_name = input('Nhập tên học sinh: ')
            new_math_score = float(input('Nhập điểm Toán: '))
            new_english_score = float(input('Nhập điểm Anh: '))
            new_grade_book = {
                "id": new_id, "name": new_name, "info": (new_math_score, new_english_score)
            }
            grade_book.append(new_grade_book)
            print("Thành công: Đã thêm học sinh SV03 vào hệ thống!")
            break

def update_scores(grade_book):
    update_id = input('Nhập mã học sinh mới: ')
    found = False
    for grade in grade_book:
        if grade['id'] == update_id:
            new_math_score = float(input('Nhập điểm Toán: '))
            new_english_score = float(input('Nhập điểm Anh: '))
            new_info = (new_math_score,new_english_score)
            grade['info'] = new_info
            found = True
            break
    if not found:
        print(print(f"Lỗi: Mã học sinh {update_id} khong tồn tại! Vui lòng nhập mã khác."))

def delete_student(grade_book):
    delete_id = input('Nhập mã học sinh mới: ')
    found = False
    for grade in grade_book:
        if grade['id'] == delete_id:
            grade_book.remove(grade)
            print(f"Thành công: Đã xóa hồ sơ học sinh {delete_id} khỏi hệ thống!")
            found = True
            break
    if not found:
        print(print(f"Lỗi: Mã học sinh {delete_id} khong tồn tại! Vui lòng nhập mã khác."))


def main():
    grade_book = [
        {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
        {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
    ]
    while True:
        choice = input("""=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
    1. Xem bảng điểm học sinh
    2. Thêm hồ sơ học sinh mới
    3. Cập nhật điểm số
    4. Xóa hồ sơ học sinh
    5. Thoát chương trình
    ================================
    Chọn chức năng (1-5): """)
        match choice:
            case "1":
                display_grades(grade_book)
            case "2":
                add_student(grade_book)
            case "3":
                update_scores(grade_book)
            case "4":
                delete_student(grade_book)
            case "5":
                print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
                break
            case _:
                print("Vui long chon tinh nang tu (1-5)!")

main()
