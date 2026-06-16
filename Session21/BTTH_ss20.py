"""
INPUT
ticket_db = [
    {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
    {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
    {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
]

Khoi tao main
main()
if __name__ == "__main__":


# Xem danh sach ve ban
Tao ham display_tickets(tickets) 
Tao file arena_tickets.log
Check 
- Trường hợp danh sách vé rỗng
- Trường hợp dữ liệu vé bị thiếu key => log : 2026-06-04 10:11:00,456 - ERROR - Missing key while displaying ticket: 'seat'

# Chức năng 2: Đặt vé mới
Tạo hàm book_ticket(tickets)
Nhập mã vé: Xử lý mã vé bị trùng, . => strip().upper()
Nhập tên khách hàng:
Nhập giá vé: Xử lý giá vé nhập chữ, Giá vé âm hoặc bằng 0
Nhập khu vực ghế: 
Nhập số ghế: Xử lý số nguyen duong, 
Seat : tuple => Chỉ xem, ko thêm sửa xóa

OUTPUT
# Chức năng 2: Đặt vé mới
Thành công: Đã đặt vé T04 cho khách hàng Pham Van D.


#Xem danh sach ve ban
Chọn chức năng (1-6): 1
--- DANH SÁCH VÉ ---
Mã Vé | Tên Khách Hàng  | Giá Vé  | Chỗ Ngồi | Trạng Thái
-----------------------------------------------------------
T01   | Nguyen Van A    | 500.0   | A-1      | Booked
T02   | Tran Thi B          | 300.0   | B-5      | Cancelled [ĐÃ HỦY]
T03   | Le Van C            | 500.0   | A-2      | Booked
-----------------------------------------------------------

"""
import logging

# def get_signal_render_data(index,data):
#     render_data = None
#     render_status = True
#     try:
#         render_data = f"{index}. {data["ticket_id"]} | {data["buyer_name"]} | {data["price"]} | {data["seat"][0]}{data["seat"][1]} | {data["status"]} | "
#     except:
#         logging.error("Missing key while displaying ticket: 'seat'")
#         return "Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại."
#     return render_data

def display_tickets(tickets):
    print("--- DANH SÁCH VÉ ---")
    print("Mã Vé | Tên Khách Hàng  | Giá Vé  | Chỗ Ngồi | Trạng Thái")
    print("-"*50)
    for index,data in enumerate(tickets):
        try:
            print(f"{index+1}. {data["ticket_id"]} | {data["buyer_name"]} | {data["price"]} | {data["seat"][0]}{data["seat"][1]} | {data["status"]} | ")
        except:
            logging.error("Missing key while displaying ticket: 'seat'")
            print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
    print("-"*50)


"""
INPUT
# Chức năng 2: Đặt vé mới
Tạo hàm book_ticket(tickets)
Nhập mã vé: Xử lý mã vé bị trùng, . => strip().upper()
Nhập tên khách hàng:
Nhập giá vé: Xử lý giá vé nhập chữ, Giá vé âm hoặc bằng 0
Nhập khu vực ghế: 
Nhập số ghế: Xử lý số nguyen duong, 
Seat : tuple => Chỉ xem, ko thêm sửa xóa

OUTPUT
# Chức năng 2: Đặt vé mới
Thành công: Đã đặt vé T04 cho khách hàng Pham Van D."""

def input_format_float(message):
    while True:
        try:
            price = float(input(message))
            if price <= 0:
                print("Giá vé phải (>0)! ")
                continue
            return price
        except ValueError:
            print("Giá vé phải là số. Vui lòng nhập lại.")
            logging.warning("Invalid price input while booking ticket")

def input_format_int(message):
    while True:
        try:
            price = int(input(message))
            if price <= 0:
                print("Số ghế phải (>0)! ")
                continue
            return price
        except ValueError:
            print("Só ghế phải là số nguyên. Vui lòng nhập lại.")
            logging.warning("Invalid price input while booking ticket")

def check_ticket_exits(tickets, ticket_id):
    for ticket in tickets:
        if ticket_id == ticket['ticket_id']:       
            return ticket
    return False

def book_ticket(tickets):
    ticket_id = input("Nhập ID vé mới: ").strip().upper()

    while ticket_id == '':
        ticket_id = input("Mã không được để trống! Vui lòng nhập lại: ").strip().upper()

    if check_ticket_exits(tickets, ticket_id):
        print(f"Mã {ticket_id} này đã tồn tại!")
        logging.warning(f"Duplicate ticket ID entered: {ticket_id}")
        return

    
    buyer_name = input("Nhập Tên: ").strip().title()
    while buyer_name == '':
        buyer_name = input("Lỗi: Tên không được để trống! Vui lòng nhập lại: ").strip().title()

    price = input_format_float("Nhập giá vé:")

    seat_id = input("Nhập khu vực ghế: ").strip().upper()
    while seat_id == '':
        seat_id = input("Lỗi: Khu vực ghế không được để trống! Vui lòng nhập lại: ").strip().upper()

    quantity = input_format_int("Nhập số lượng ghế: ")

    seat = (seat_id, quantity)

    new_ticket = {
        "ticket_id": ticket_id, "buyer_name": buyer_name, "price": price, "status": "Booked", "seat": seat
    }

    tickets.append(new_ticket)
    logging.info(f"Booked new ticket {ticket_id} for {buyer_name}")
    print(f"Thành công: Đã đặt vé {ticket_id} cho khách hàng {buyer_name}.")
    

def change_seat(tickets):
    print("--- ĐỔI CHỖ NGỒI ---")
    ticket_id = input("Nhập ID vé mới: ").strip().upper()
    if not ticket_id:
        print("Ticket id ko dc de rong!")
    
    ticket = check_ticket_exits(tickets,ticket_id)
    if not ticket:
        logging.warning(f"Change seat failed - Ticket {ticket_id} not found")
        print(f"Không tìm thấy vé mang mã {ticket_id}.")
        return
    
    quantity = input_format_int("Nhập số lượng ghế: ")
    seat_id = input("Nhập khu vực ghế: ").strip().upper()
    new_seat = (seat_id, quantity)
    ticket['seat'] = new_seat
    print(f"Thành công: Đã đổi chỗ vé {ticket_id} sang {seat_id}-{quantity}.")
    logging.info("Seat changed for ticket T01 to B-10")

def calculate_revenue(tickets):
    total = 0
    for ticket in tickets:
        if ticket['status'] == "Booked":
            total += ticket['price']
    print(total)
    return total

def main():
    logging.basicConfig(
        filename="arena_tickets.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    ticket_db = [
        {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
        {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
        {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("B", 5)}
    ]

    while True:
        select = input("""
=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===
1. Xem danh sách vé đã bán
2. Đặt vé mới
3. Đổi chỗ ngồi (Cập nhật vé)
4. Hủy vé
5. Báo cáo doanh thu
6. Thoát chương trình
======================================== 
Chọn chức năng (1-6):""")
        
        match select:
            case "1":
                display_tickets(ticket_db)
            case "2":
                book_ticket(ticket_db)
            case "3":
                change_seat(ticket_db)
            case "4":
                calculate_revenue(ticket_db)
            case "5":
                pass




if __name__ == "__main__":
    main()