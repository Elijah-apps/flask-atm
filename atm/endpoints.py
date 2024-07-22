from flask_restful import Resource, reqparse
from atm.models import Account

parser = reqparse.RequestParser()
parser.add_argument('amount', type=float, required=True, help="Amount cannot be blank!")

class AccountAPI(Resource):
    def get(self, account_id):
        account = Account.get_account(account_id)
        if not account:
            return {'message': 'Account not found'}, 404
        return account, 200

    def post(self, account_id):
        try:
            Account.create_account(account_id)
            return {'message': 'Account created'}, 201
        except ValueError as e:
            return {'message': str(e)}, 400

    def delete(self, account_id):
        try:
            Account.delete_account(account_id)
            return {'message': 'Account deleted'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

class DepositAPI(Resource):
    def post(self, account_id):
        args = parser.parse_args()
        amount = args['amount']
        try:
            Account.update_balance(account_id, amount)
            return {'message': 'Deposit successful'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

class WithdrawAPI(Resource):
    def post(self, account_id):
        args = parser.parse_args()
        amount = args['amount']
        try:
            Account.update_balance(account_id, -amount)
            return {'message': 'Withdrawal successful'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400
