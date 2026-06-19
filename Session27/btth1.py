from abc import ABC, abstractmethod

class BaseAccount(ABC):
    bank_name = "Vietcombank" 
    def __init__(self, account_name, account_number, balance=0):
        self.__balance = balance
        self.account_name = account_name.strip().upper()
        self.account_number = account_number
    
    @property
    def balance(self):
        return self.__balance
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @staticmethod
    def validate_account_number(account_number):
        if not (account_number.isdigit() and len(account_number) == 10):
            return False
        return account_number
    
    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name

    def __add__(self, other):
        return self.balance + other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def _increase_amount(self, amount):
        self.__balance += amount
    
    def _decrease_amount(self, amount):
        self.__balance -= amount

# public => ở đâu cũng dc
# proteched => có thể sử dụng trong class và thằng con
# private => chỉ sủ dụng trong class khai báo

class SavingsAccount(BaseAccount):
    def __init__(self, interest_rate, account_name, account_number, balance = 0):
        super().__init__(account_name, account_number, balance)
        self.interest_rate = interest_rate 
    def deposit(self, amount):
        self._increase_amount(amount)
        
    def withdraw(self, amount):
        penatly = amount*0.02
        total_amount = amount + penatly
        if total_amount > self.balance:
            print("Tài khoản không đủ!")
            return False
        self._decrease_amount(total_amount)

    def apply_interest(self):
        amount = self.balance * self.interest_rate
        self._increase_amount(amount)
        return amount

class CreditAccount(BaseAccount):
    def __init__(self, credit_limit, account_name, account_number, balance = 0):
        super().__init__(account_name, account_number, balance)
        self.credit_limit = credit_limit
    def deposit(self, amount):
        self._increase_amount(amount)
    def withdraw(self, amount):
        if not ((self.balance - amount) >= -self.credit_limit):
            return False
        self._decrease_amount(amount)

class DigitalPremiumMixin:
    def cashback_reward(self, amount): 
        if amount > 5000000:
            return amount*0.01

class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    pass

class VNPayGateway:
    def execute_pay(self, account, amount):
        account.withdraw(amount)

class ViettelMoneyGateway:
    def execute_pay(self, account, amount):
            account.withdraw(amount)


def check_float_data(message):
    try:
        value = float(input(message))
        return value
    except ValueError as err:
        print("Giá trị nhập vào phải số!")
        return False

# Chức năng 1: Mở tài khoản mới

def check_exits_account(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return True
    return False

def open_account(accounts, current_account):
    print("--- CHỌN LOẠI TÀI KHOẢN ---")
    choice_type_account = input("""1. Savings Account (Tài khoản Tiết kiệm)
2. Credit Account (Tài khoản Tín dụng)
3. Hybrid Account (Tài khoản Đa năng)
Chọn loại tài khoản (1-3): """)
    if choice_type_account not in ["1","2","3"]:
        print("Lựa chọn không hợp lệ!")
        return
    
    account_number = input("Nhập số tài khoản 10 chữ số: ")
    if not BaseAccount.validate_account_number(account_number):
        print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
        return
    if check_exits_account(accounts, account_number):
        print("Số tài khoản đã tồn tại trong hệ thống!")
        return
    account_name = input("Nhập tên chủ tài khoản: ")
    if choice_type_account == "1":
        interest_rate = check_float_data("Nhập lãi suất năm (ví dụ 0.05): ")
        if not interest_rate:
            return
        current_account = SavingsAccount(interest_rate, account_name, account_number)
    if choice_type_account == "2":
        credit_limit = check_float_data("Nhập hạn mức: ")
        if not credit_limit:
            return
        current_account = CreditAccount(credit_limit, account_name, account_number)
    if choice_type_account == "3":
        interest_rate = check_float_data("Nhập lãi suất năm (ví dụ 0.05): ")
        if not interest_rate:
            return
        current_account = HybridAccount(interest_rate, account_name, account_number)
    accounts.append(current_account)
    print("Mở tài khoản Tiết kiệm thành công!")
    print(f"Chủ tài khoản: {current_account.account_name}")
    return current_account


def display_info(current_account):
    if not current_account:
        print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
        return
    print("--- THÔNG TIN TÀI KHOẢN HIỆN TẠI ---")
    type_account = current_account.__class__.__name__
    print(f"Loại tài khoản: {type_account}")
    print(f"Ngân hàng: {current_account.bank_name}")
    print(f"Số tài khoản: {current_account.account_number}")
    print(f"Chủ tài khoản: {current_account.account_name}")
    print(f"Số dư: {current_account.balance:,.0f} VND")
    
    if type_account in ['SavingsAccount', 'HybridAccount']:
        print(f"Lãi suất: {current_account.interest_rate*100}% / năm")
    else:
        print(f"Hạn mức của tài khoản: {current_account.credit_limit}")

def transaction_amount(current_account):
    print("--- GIAO DỊCH NẠP / RÚT TIỀN ---")
    choice = input("""1. Nạp tiền
2. Rút tiền
Chọn giao dịch (1-2): """)
    if choice == '1':
        amount = check_float_data("Nhập số tiền nạp: ")
        current_account.deposit(amount)
        print("Nạp tiền thành công!")
        if current_account.__class__.__name__ == "HybridAccount":
            reward = current_account.cashback_reward(amount)
            current_account.deposit(reward)
            print(f"[Ưu đãi Premium]: Bạn được hoàn tiền 1% ({amount*0.01} VND) vào tài khoản!")
        print(f"Số dư mới: {current_account.balance:,.0f} VND")
    if choice == "2":
        amount = check_float_data("Nhập số tiền cần rút: ")
        change = current_account.withdraw(amount)
        if not change:
            print("Quá trình rút thất bại!")
            return
        print("Rút tiền thành công!")
        print(f"Số tiền rút: {amount:,.0f} VND")
        if current_account.__class__.__name__ in ['SavingsAccount', 'HybridAccount']:
            print(f"Phí phạt rút trước hạn (2%): {amount*0.02:,.0f} VND")
        print(f"Số dư còn lại: {current_account.balance:,.0f} VND")

def accumulate_money(current_account):
    if current_account.__class__.__name__ == "CreditAccount":
        print("Tính năng không hỗ trợ!")
        return
    print(f"Số dư trước tính lãi: {current_account.balance:,.0f} VND")
    print(f"Lãi suất năm: {current_account.interest_rate*100}%")
    print(f"Tiền lãi nhận được: +{current_account.apply_interest()} VND")
    print(f"Số dư mới sau khi cộng lãi: {current_account.balance:,.0f} VND")

def choose_accounts(accounts, current_account):
    position = 0
    for index, account in enumerate(accounts, 1):
        if account.account_number == current_account.account_number:
            position = index
            print(f"{index} - {account.account_name} - {account.account_number} [Tài khoản hiện tại]")
            continue
        print(f"{index} - {account.account_name} - {account.account_number}")
    choice = input("Vui lòng chọn tài khoản bạn muốn so sánh, VD:1 : ")
    if int(choice) == position:
        print("Chọn tài khoản khác với tài khoản hiện tại!")
    return accounts[int(choice)-1]

def compare_account(accounts, current_account):
    if not current_account:
        print("Cần tạo tài khoản ở bước 1!")
    print("--- ĐỒNG BỘ & SO SÁNH TÀI KHOẢN (OPERATOR OVERLOADING) ---")
    print(f"Tài khoản hiện tại (A): {current_account.account_name} (Số dư: {current_account.balance:,.0f} VND)")
    other_account = choose_accounts(accounts, current_account)
    print(f"Chọn tài khoản đối ứng (B) từ danh sách hệ thống: {other_account.account_number} ({other_account.account_name} - Số dư: {other_account.balance:,.0f} VND)")
    if current_account < other_account:
        print(f"[Kết quả So sánh (__lt__)]: Số dư tài khoản A NHỎ HƠN số dư tài khoản B.")
    elif current_account == other_account:
        print(f"[Kết quả So sánh (__eq__)]: Số dư tài khoản A BẰNG số dư tài khoản B.")
    else:
        print(f"[Kết quả So sánh (__lt__)]: Số dư tài khoản A NHỎ HƠN số dư tài khoản B.")
    total_amount = current_account + other_account
    print(f"[Kết quả Tổng hợp (__add__)]: Tổng số tiền sở hữu của cả 2 tài khoản là: {total_amount:,.0f} VND.")

def process_payment(payment_gateway, account, amount):
    payment_gateway.execute_pay(account,amount)

def payment_amount(current_account):
    print("--- THANH TOÁN HÓA ĐƠN QUA CỔNG TRUNG GIAN ---")
    choice = input("""1. Thanh toán qua VNPay
2. Thanh toán qua Viettel Money
Chọn cổng thanh toán (1-2): """)
    amount = check_float_data("Nhập số tiền hóa đơn: ")
    name_gateway = ""
    if choice == "1":
        name_gateway = "VNPayGateway"
        payment_gateway = VNPayGateway()
    if choice == "2":
        name_gateway = "ViettelMoneyGateway"
        payment_gateway = ViettelMoneyGateway()
    process_payment(payment_gateway, current_account, amount)
    print(f"[Hệ thống {name_gateway}]: Đang kết nối tới tài khoản {current_account.account_number}...")
    print(f"Xác thực thanh toán bằng Duck Typing thành công!")
    print(f"Tài khoản đã thanh toán hóa đơn giá trị: {amount:,.0f} VND.")
    print(f"Số dư mới: {current_account.balance:,.0f} VND.")

def main():
    accounts = [SavingsAccount(0.03,"Kien","0986865654", 000000),
                HybridAccount(0.05,"Kien1","0986865654", 200000),
                CreditAccount(20000000,"Kien2","0986865654", 300000),
                SavingsAccount(0.04,"Kien3","0986865654", 100000)]
    current_account = None
    while True:
        choice = input("""===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====
1. Mở tài khoản mới (Chọn loại tài khoản)
2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)
3. Giao dịch Nạp / Rút tiền & Tính điểm thưởng (Đa hình)
4. Tích lũy / Áp dụng lãi suất định kỳ
5. Kiểm tra tính năng gộp tài khoản & So sánh (Overloading)
6. Thanh toán hóa đơn qua Cổng trung gian (Duck Typing)
7. Thoát chương trình
==============================================
Chọn chức năng (1-7): """)
        match choice:
            case "1":
                current_account = open_account(accounts, current_account)
            case "2":
                display_info(current_account)
            case "3":
                transaction_amount(current_account)
            case "4":
                accumulate_money(current_account)
            case "5":
                compare_account(accounts, current_account)
            case "6":
                payment_amount(current_account)
            case "7":
                break
            case _:
                print("Lựa chọn không phù hợp!")

if __name__ == "__main__":
    main()