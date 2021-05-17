from services import account_service


class AccountController:
	def __init__(self, account_service):
		self.account_service = account_service

	def create_account(self, account_id, password, name, age, street, city, account_type):
		new_account = self.account_service.add_account(account_id, password, name, age, street, city, account_type)
		return new_account

	def get_member(self, account_id=None):
		if account_id:
			return self.account_service.search_member(account_id)
		else:
			ValueError('Member does not exist')

	def change_account_address(self, account_id, street, city):
		return self.account_service.modify_address(account_id, street, city)


if __name__ == "__main__":
	acc_service_1 = account_service.AccountService()
	acc_controller = AccountController(acc_service_1)

	acc_controller.create_account('account_id_1', 'password1', 'name1', 20, 'street1', 'Hyd', 'Admin')
	print(len(acc_service_1.accounts))
	acc1 = acc_controller.get_member('account_id_1')
	print(acc1.address.city)
	acc_controller.change_account_address('account_id_1', 'Street12', 'Hyd1')
	print(acc1.address.city)

