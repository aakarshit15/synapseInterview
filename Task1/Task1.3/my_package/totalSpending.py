def total_spending(request_spending, account_id, category):
    account = request_spending[account_id]
    transactions = account["transactions"]
    for transaction in transactions:
        if transaction["category"] == category:
            return transaction["amount"]