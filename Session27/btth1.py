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
    
    def _increase_amount(self, amount):
        self.balance += amount
    
    def _decrease_amount(self, amount):
        self.balance -= amount

# public => ở đâu cũng dc
# proteched => có thể sử dụng trong class và thằng con
# private => chỉ sủ dụng trong class khai báo

class SavingsAccount(BaseAccount):
    def __init__(self, interest_rate, account_name, account_number, balance = 0):
        super().__init__(account_name, account_number, balance)
        self.interest_rate = interest_rate 
    def deposit(self, amount):
        pass
    def withdraw(self, amount):
        penatly = amount*0.02
        total_amount = amount + penatly
        self._decrease_amount(total_amount)

    def apply_interest(self):
        amount = self.balance * self.interest_rate
        self._increase_amount(amount)

class CreditAccount(BaseAccount):
    def __init__(self, credit_limit, account_name, account_number, balance = 0):
        super().__init__(account_name, account_number, balance)
        self.credit_limit = credit_limit
    def deposit(self, amount):
        pass
    def withdraw(self, amount):
        if not ((self.balance - amount) >= -self.credit_limit):
            return
        pass

class DigitalPremiumMixin:
    def cashback_reward(self, amount): 
        if amount > 5000000:
            return amount*0.01

class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    pass


# Chức năng 1: Mở tài khoản mới
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
    # if not BaseAccount("","").validate_account_number(account_number):
    #     print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
    #     return
    
    account_name = input("Nhập tên chủ tài khoản: ")
    if choice_type_account == "1":
        interest_rate = input("Nhập lãi suất năm (ví dụ 0.05): ")
        current_account = SavingsAccount(interest_rate, account_name, account_number)
    if choice_type_account == "2":
        credit_limit = input("Nhập hạn mức: ")
        current_account = CreditAccount(credit_limit, account_name, account_number)
    if choice_type_account == "3":
        interest_rate = input("Nhập lãi suất năm (ví dụ 0.05): ")
        current_account = HybridAccount(interest_rate, account_name, account_number)
    accounts.append(current_account)
    print("Mở tài khoản Tiết kiệm thành công!")
    print(f"Chủ tài khoản: {current_account.account_name}")

def main():
    accounts = []
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
                open_account(accounts, current_account)
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                break
            case _:
                print("Lựa chọn không phù hợp!")

if __name__ == "__main__":
    main()