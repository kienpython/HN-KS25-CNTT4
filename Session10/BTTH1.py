cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]
while True:
    choice = input(''' 
    =========================================
   |      SHOPEE CART MANAGEMENT SYSTEM      |
    =========================================
     1: Xem chi tiết giỏ hàng và Tổng tiền
     2: Thêm sản phẩm mới hoặc Tăng số lượng
     3: Cập nhật số lượng sản phẩm
     4: Xóa sản phẩm khỏi giỏ hàng
     5: Thoát chương trình.
    =========================================
    Mời bạn chọn chức năng (1-5):   ''')
    if choice == '1':
        print("")
        total_price = 0
        total_quantity = 0
        print(f"{'Mã SP':<10}{'Tên sản phẩm':<25}{'Số lượng':<10}{'Đơn giá':<15}{'Thành tiền':<15}")
        print("-" * 75)
        for index, item in enumerate(cart_items):
            subtotal = item[2] * item[3]
            total_price += subtotal
            total_quantity += item[2]
            print(f"{item[0]:<10}{item[1]:<25}{item[2]:<10}{item[3]:<15}{subtotal:<15}")
        print("-" * 75)
        print("Tổng số lượng sản phẩm:", total_quantity)
        print("Tổng tiền đơn hàng:", total_price)
    elif choice =='2':
        product_id = input("Nhập mã sản phẩm: ")
        found = False
        for index, item in enumerate(cart_items):
            if product_id == item[0]:
                found = True
                try:
                    quantity = int(input("Nhập số lượng: "))
                    if quantity <= 0:
                        print("Lỗi: Số lượng thêm vào phải lớn hơn 0!")
                    else:
                        item[2] += quantity
                        print("Thông báo: Cộng dồn số lượng thành công!")
                except ValueError:
                    print("Lỗi: Số lượng phải là số nguyên!")
                break
        if found == False:
            product_name = input("Nhập tên sản phẩm: ")
            try:
                quantity = int(input("Nhập số lượng sản phẩm: "))
                price = float(input("Nhập đơn giá sản phẩm: "))
                if quantity <= 0 or price < 0:
                    print("Lỗi: Số lượng phải > 0 và đơn giá phải >= 0!")
                else:
                    cart_items.append([product_id, product_name, quantity, price])
                    print("Thông báo: Thêm sản phẩm mới vào giỏ hàng thành công!")
            except ValueError:
                print("Lỗi: Số lượng và đơn giá phải là số!")
    elif choice == '3':
        product_id = input("Nhập mã sản phẩm cần cập nhật: ")
        found = False
        for index, item in enumerate(cart_items):
            if product_id == item[0]:
                found = True
                try:
                    new_quantity = int(input("Nhập số lượng mới: "))
                    if new_quantity <= 0:
                        print("Lỗi: Số lượng phải lớn hơn 0!")
                    else:
                        item[2] = new_quantity
                        print("Thông báo: Cập nhật số lượng thành công!")
                except ValueError:
                    print("Lỗi: Số lượng phải là số nguyên!")
                break
        if found == False:
            print("Lỗi: Mã sản phẩm không tồn tại trong giỏ hàng.")
    elif choice == '4':
        product_id = input("Nhập mã sản phẩm muốn xóa: ")
        found = False
        for index, item in enumerate(cart_items):
            if product_id == item[0]:
                found = True
                cart_items.pop(index)
                print("Thông báo: Xóa sản phẩm khỏi giỏ hàng thành công!")
                break
        if found == False:
            print("Lỗi: Mã sản phẩm không tồn tại trong giỏ hàng.")
    elif choice == '5':
        print("Chương trình kết thúc. Cảm ơn bạn đã sử dụng dịch vụ!")
        break
    else:
        print("Lỗi: Lựa chọn không hợp lệ, vui lòng chọn lại từ 1 đến 5!")