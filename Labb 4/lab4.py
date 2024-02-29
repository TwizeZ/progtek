account_dict = {}
account_file = "/Users/felix/Documents/University/Prog/progtek/Labb 4/accounts.csv"

class Account():
    def __init__(self, name, money, pin_code):
        self.name = name
        self.money = money
        self.pin_code = pin_code
        self.transactions = []
    
    def __str__(self):
        return f"\nAccount details\nName: {self.name}\nBalance: {self.money}\nTransactions: {self.transactions}"
    
    def deposit(self, amount):
        self.money += amount
        self.transactions.append({"type": "deposit", "amount": amount})
        return f"Deposited {amount} to account. New balance: {self.money}."

    def withdrawal(self, amount, pin):
        if self.ok_PIN(pin) == False:
            return "Invalid PIN code. Withdrawal failed."
        else:        
            self.money -= amount
            self.transactions.append({"type": "withdrawal", "amount": amount})
            return f"Withdrawal was successful. New balance: {self.money}."

    def ok_PIN(self, pin):
        if pin == self.pin_code:
            return True
        else:
            return False

    def change_PIN(self, old_pin, new_pin):
        if old_pin != self.pin_code:
            return "Failed to change PIN. Old PIN was incorrect."
        else:
            self.pin_code = new_pin
            return "PIN was successfully changed."
    
class PremiumAccount(Account):
    def withdrawal(self, amount, pin):
        if self.amount <= self.money:
            return super().withdrawal(amount, pin)
        else:
            return "Withdrawal failed due to insufficient funds. Would you like to take a loan?"

def read_accounts_from_file(file_name):
    with open(file_name, "r", encoding="utf8") as f:
        lines = f.readlines()
        accounts = []
        for line in lines:
            data = line.split(";")
            account = Account(data[0], int(data[1]), int(data[2]))
            accounts.append(account)
        return accounts

def write_accounts_to_file(accounts, file_name):
    with open(file_name, "a", encoding="utf8") as f:
        for account in accounts:
            find = account_dict[account]
            f.write(f"{find.name};{find.money};{find.pin_code};{find.transactions};\n")

def get_int_input(prompt_string):
    status = True
    while status:
        try:
            input_num = int(input(prompt_string))
            status = False
        except ValueError:
            print("Just pls enter a number...")
    return input_num 

def display_accounts(account_dict):
    for account in account_dict:
        print(account_dict[account])

def menu():
    print("""
What would you like to do?
1 - Set up a new account
2 - Deposit
3 - Withdrawal
4 - Change pin
5 - Display earlier transactions
6 - Exit
""")

def menu_choice():
    menu()
    loop = True
    while loop:
        choice = get_int_input("Enter your choice: ")
        if choice in range(1, 7):
            return choice
        else:
            print("Invalid choice. Please try again.")

def execute(choice):
    read_accounts_from_file(account_file)

    loop = True
    while loop:
        if choice == 1:
            name = input("Enter your name: ")
            pin = get_int_input("Create a PIN-code: ")
            money = get_int_input("Enter the amount of money you want to deposit: ")
            account_dict[name] = Account(name, money, pin)
            loop = False
        elif choice == 2:
            acc_name = input("Enter your account name: ")
            try:
                print(account_dict[acc_name].deposit(get_int_input("Enter the amount of money you want to deposit: ")))
                loop = False
            except AttributeError and KeyError:
                print("Account was not found. Please try again.")
        elif choice == 3:
            acc_name = input("Enter your account name: ")
            try:
                print(account_dict[acc_name].withdrawal(get_int_input("Enter the amount of money you want to withdrawal: "), get_int_input("Enter your PIN-code: ")))
                loop = False
            except AttributeError and KeyError:
                print("Account was not found. Please try again.")
        elif choice == 4:
            acc_name = input("Enter your account name: ")
            try:
                print(account_dict[acc_name].change_PIN(get_int_input("Enter your old PIN: "), get_int_input("Enter your new PIN: ")))
                loop = False
            except AttributeError and KeyError:
                print("Account was not found. Please try again.")
        elif choice == 5:
            acc_name = input("Enter your account name: ")
            try:
                print(account_dict[acc_name].transactions)
                loop = False
            except AttributeError and KeyError:
                print("Account was not found. Please try again.")
        elif choice == 6:
            loop = False
        
        account_dict["Lisa"] = Account("Lisa", 200, 1111)

        write_accounts_to_file(account_dict, account_file)

def main():
    execute(menu_choice())

if __name__ == "__main__":
    main()