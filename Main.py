#Budget App
class Transaction:
    def __init__ (Trans_Num, Amount, Vendor, Account):
        Trans_Num.Amount = Amount
        Trans_Num.Vendor = Vendor
        Trans_Num.Account = Account

class Spend_Cats:
    def __init__ (Category, Target_Amt, Balance, Acct_Type):
        Category.Target_Amt = Target_Amt
        Category.Balance = Balance
        Category.Acct_Type = Acct_Type


print("Welcome to Jackson's Budget App")
