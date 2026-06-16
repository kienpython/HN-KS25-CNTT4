from tabulate import tabulate

class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price
    
    def menu_status(self):
        if self.is_available:
            return "Đang bán"
        return "Ngừng bán"
    
    def toggle_available(self):
        self.is_available = not self.is_available
        if self.is_available:
            return "Đang bán"
        else:
            return "Ngừng bán"

def change_status_drink(menu):
    drink_id = input("Nhập mã món: ").strip().upper()
    drink = check_exits(menu, drink_id)
    if not drink:
        print("Không tìm thấy món có mã này!")
        return
    status = drink.toggle_available()
    print(f"Đã cập nhật trạng thái món {drink_id}.")
    print(f"Trạng thái hiện tại: {status}")

def display_menu(menu):
    print("--- DANH SÁCH ĐỒ UỐNG ---")
    drinks = list()
    for drink in menu:
        drinks.append([drink.code, drink.name, drink.price, drink.menu_status()])

    table = tabulate(
        drinks, 
        headers=["Mã món", "Tên món", "Giá bán", "Trạng thái"], 
        tablefmt="grid"
    )
    print(table)

def check_exits(menu, drink_id):
    for drink in menu:
        if drink.code == drink_id:
            return drink
    return False

def add_drink(menu):
    drink_id = input("Nhập mã món: ").strip().upper()
    drink = check_exits(menu, drink_id)
    if drink:
        print("Mã món đã tồn tại trong hệ thống!")
        return 
    try:
        price = float(input("Nhập giá bán: "))
        if price <= 0 :
            print("Giá bán không hợp lệ!")
            return
    except ValueError as err:
        print("Giá bán không hợp lệ!")
        return
    name = input("Nhập tên món: ")
    menu.append(Drink(drink_id, name, price))
    print(f'Thành công: Đã thêm món {name} vào thực đơn!')


def main():
    menu = [
        Drink("CF01", "Cà phê sữa", 35000),
        Drink("TS01", "Trà sữa matcha", 45000),
        Drink("TD01", "Trà đào cam sả", 40000)
    ]
    while True:
        choice = input("""=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===

    1. Xem danh sách đồ uống
    2. Thêm đồ uống mới
    3. Cập nhật trạng thái kinh doanh
    4. Thoát chương trình

    ==============================================
    Chọn chức năng (1-4): """)
        
        match choice:
            case "1":
                display_menu(menu)
            case "2":
                add_drink(menu)
            case "3":
                change_status_drink(menu)
            case "4":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
                break
    
if __name__ == "__main__":
    main()    