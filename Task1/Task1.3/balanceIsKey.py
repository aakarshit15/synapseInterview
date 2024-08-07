from my_package.totalBalance import *;
from my_package.totalSpending import *;
from my_package.moneyOwed import *;
from my_package.requestSpending import *;

for account_id in list(request_spending.keys()):
    print("---------------------------------")
    print("---------------------------------")
    print("---------------------------------")
    account = request_spending[account_id]
    print(f"{account_id} ----------------------------->")
    for transaction in account["transactions"]:
        print(f"{transaction["category"]} --------------------------------->")
        print(total_spending(request_spending, account_id, transaction["category"]))
    print(total_balance(request_spending, account_id))
    print("---------------------------------")
    print("---------------------------------")
    print("---------------------------------")
    print(money_owed(request_spending, account_id))
