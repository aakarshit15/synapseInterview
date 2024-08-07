def money_owed(request_spending, account_id):
    account = request_spending[account_id]
    transactions = account["transactions"]
    moneyOwed = 0
    for transaction in transactions:
        moneyOwed += transaction["amount"]
    return moneyOwed