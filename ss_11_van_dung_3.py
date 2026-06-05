product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    choice = input("""===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
Nhập vào lựa chọn của bạn: """)
    match choice:
        case "1":
            if not product_list:
                print("Danh sách sản phẩm hiện đang trống.")
                continue
            print("Danh sách sản phẩm hiện tại:")
            for key, product in enumerate(product_list):
                print(f"{key+1}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | Giá: {product['price']} | Số lượng: {product['quantity']}")
        case "2":
            new_id = input("- Nhập mã sản phẩm: ").strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == new_id:
                    found = True
                    break
            if found:
                print("Mã đã trùng!")
                continue
            

            new_name = input("- Nhập tên sản phẩm: ").strip().upper()
            new_price = int(input("- Nhập giá sản phẩm: ").strip().upper())
            new_quantity = int(input("- Nhập số lượng sản phẩm: ").strip().upper())

            if new_price <= 0:
                print('Giá sản phẩm không được bé hơn không!')
                continue

            if new_quantity <= 0:
                print("Số lượng sản phẩm không được bé hơn không!")
                continue

            new_product = {
                "product_id" : new_id,
                "product_name":new_name,
                "price":new_price,
                "quantity":new_quantity
            }
            product_list.append(new_product)

        case "3":
            ma_sp = input("Nhập mã sản phẩm cần cập nhật:").strip().upper()
            found = None
            for product in product_list:
                if product['product_id'] == ma_sp:
                    print("Tìm thấy sản phẩm!")
                    found = product
                    break
            if not found:
                print("Không tìm thấy!")
            else:
                product_name = input("Tên sản phẩm: ")
                product_price = input("Giá sản phẩm: ")
                product_quantity = input("Số lượng sản phẩm: ")
                if not(int(product_price) > 0 and int(product_quantity) > 0):
                    print("Giá và số lượng không hợp lệ!")
                else:
                    found['product_name'] = product_name
                    found['price'] = product_price
                    found['quantity'] = product_quantity
                    
        case "4":
            product_id = input("Nhập mã sản phẩm cần xóa: ")
            found = False
            for i in range(len(product_list)):
                if product_list[i]["product_id"] == product_id:
                    del(product_list[i])
                    print("Đã xóa sản phẩm thành công!")
                    found = True
                    break

            if not found:
                print("Không tìm thấy sản phẩm")

        case "5":
            break   

        case _:
            print("Vui lòng chọn lựa chọn từ 1-5!")