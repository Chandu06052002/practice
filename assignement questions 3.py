# programming on shopping

class Shopping:
    def __init__(self):
        self.items = {}

    def selected_items(self,items_names,price):
        if items_names in self.items:
            self.items[items_names] += price
        else:
            self.items[items_names] = price
            print(f'item-name : {items_names} price is{price:.2f}Rs to the cart')

    def remove_items(self,items_names):
        if items_names in self.items:
            removed_price = self.items.pop(items_names)
            print("REmoved{items_names} which costs {removed_price:.2f}Rs from the cart")
        else:
            print(f'{items_names} is not found')

    def calculation(self):
        total = sum(self.items.values())
        return total
    
    def show_cart(self):
        if self.items:
            print("Your shopping items are here")
            for items,price in self.items.items():
                print(f'{items} : Rs{price:.2f}')
        else:
            print("your shopping cart is empty")


cart = Shopping()
cart.selected_items("Juice",200)
cart.selected_items("Thump up",100)
cart.selected_items("Jeans",2000)
cart.selected_items("Shirts",228)
cart.selected_items("Electric rice cooker",2477)
cart.selected_items("Tables",208820)
cart.show_cart()
print(f'Total:Rs{cart.calculation():.2f}')
cart.remove_items("Tables")
cart.show_cart()
print(f'Total:Rs{cart.calculation():.2f}')
        

# program on banking

class Banking:
    def __init__(self,bank_name):
        self.bank_name = bank_name
        self.accounts = {}

    def create_account(self,account_number,account_holder):
        if account_number in self.accounts:
            print(f'Account with number{account_number} already exists')
        else:
            self.accounts[account_number] = {"holder":account_holder,'balance':0.0}
            print(f'account created for{account_holder} with account number {account_number}')

    def deposit(self,account_number,amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited Rs{amount} to account number {account_number} .New Balance: Rs{self.accounts[account_number]['balance']}.")
        else:
            print(f"Account number {account_number} does not exist.")

    def withdraw(self,account_number,amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(f"withdraw Rs{amount} from account number {account_number}. New balance Rs{self.accounts[account_number]['balance']}")
            else:
                print(f"Insufficient balance in account number {account_number}")
        else:
            print(f"Account number {account_number} does not exist")

    def get_account_details(self,account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Account number : {account_number} \n Account holder : {account['holder']} \n Balance: Rs{account['balance']}")
        else:
            print(f"Account number {account_number} does not exist")


bank = Banking("Some thing")
bank.create_account("123","chandu")
bank.create_account("456","Hari")

bank.deposit("123",2777)
bank.deposit("456",66367)

bank.withdraw("123",777)
bank.withdraw("456",367)

bank.get_account_details("123")
bank.get_account_details("456")




