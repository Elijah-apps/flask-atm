from flask_restful import Api
from atm.endpoints import AccountAPI, DepositAPI, WithdrawAPI

def initialize_routes(app):
    api = Api(app)
    api.add_resource(AccountAPI, '/account/<string:account_id>')
    api.add_resource(DepositAPI, '/account/<string:account_id>/deposit')
    api.add_resource(WithdrawAPI, '/account/<string:account_id>/withdraw')
