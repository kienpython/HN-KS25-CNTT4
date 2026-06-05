raw_input = "   nGuyen vaN aN  ;  2004   "
CURRENT_YEAR = 2026

while True:

    print("\n===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")
    

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    

    if choice == "1":
        print(f"\n[Kết quả] Chuỗi dữ liệu gốc: '{raw_input}'")
        
  
    elif choice == "2":
   
        parts = raw_input.split(";")
        raw_name = parts[0].strip()
        raw_year = parts[1].strip()
        
        clean_name = " ".join(raw_name.split()).title()
        age = CURRENT_YEAR - int(raw_year)
        
        print("\n--- KẾT QUẢ CHUẨN HÓA ---")
        print(f"Họ và tên: {clean_name}")
        print(f"Tuổi:      {age} tuổi")
        print("-------------------------")
        
    elif choice == "3":
    
        parts = raw_input.split(";")
        raw_name = parts[0].strip()
        raw_year = parts[1].strip() 
        
        name_parts = raw_name.split() 
        
        if len(name_parts) >= 2:
            ho = name_parts[0]
            ten_chinh = name_parts[-1]
            
            ten_dem_list = name_parts[1:-1]
            ten_dem = "".join(ten_dem_list) 
            
 
            char_ho = ho[0]
            char_ten_dem = ten_dem[0] if ten_dem else ""
            
            email = f"{char_ho}{char_ten_dem}{ten_chinh}".lower() + "@company.com"          
            id_code = f"{ten_chinh.upper()}{raw_year[2:]}"
            full_name_clean = " ".join(name_parts).title()
            

            print("\n--------------------------------------")
            print(f"| {'THẺ THÀNH VIÊN CLUB':^34} |")
            print("*------------------------------------*")
            print(f"| Họ & Tên: {full_name_clean:<24} |")
            print(f"| Mã Số ID: {id_code:<24} |")
            print(f"| Email:    {email:<24} |")
            print("*------------------------------------*")
        else:
            print("\n[Lỗi] Định dạng họ tên trong chuỗi gốc không đủ thành phần để tạo thẻ!")
            
    elif choice == "4":
        print("\nCảm ơn bạn đã sử dụng hệ thống. Chào tạm biệt!")
        break 
    else:
        print("\n[Cảnh báo] Lựa chọn không hợp lệ, vui lòng nhập lại!")