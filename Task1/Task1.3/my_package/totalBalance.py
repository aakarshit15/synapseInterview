def total_balance(request_spending, account_id):
    account = request_spending[account_id]
    transactions = account["transactions"]
    totalBalance = account["balance"]
    for transaction in transactions:
        totalBalance += transaction["amount"]
    return totalBalance