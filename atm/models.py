# For simplicity, we are using an in-memory data store
class Account:
    accounts = {}

    @staticmethod
    def create_account(account_id, balance=0):
        if account_id in Account.accounts:
            raise ValueError("Account already exists.")
        Account.accounts[account_id] = {'balance': balance}

    @staticmethod
    def get_account(account_id):
        return Account.accounts.get(account_id)

    @staticmethod
    def update_balance(account_id, amount):
        if account_id not in Account.accounts:
            raise ValueError("Account does not exist.")
        Account.accounts[account_id]['balance'] += amount

    @staticmethod
    def delete_account(account_id):
        if account_id in Account.accounts:
            del Account.accounts[account_id]
