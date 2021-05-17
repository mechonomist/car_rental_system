from models import accounts as accounts_module


class AccountService:
    accounts = {}

    # should have admin privileges
    def add_account(self, account_id, password, name, age, street, city, account_type):
        if account_type == 'Admin':
            new_account = accounts_module.Admin(account_id, password, name, age, street, city)
        elif account_type == 'Member':
            new_account = accounts_module.Member(account_id, password, name, age, street, city)
        else:
            raise ValueError('Please provide valid account_type')

        self.__class__.accounts[account_id] = new_account
        return new_account

    # should have admin privileges
    def search_member(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        else:
            raise ValueError('Member not found')

    def reset_password(self, account_id, password):
        account = self.accounts[account_id]
        account.password = password
        return True

    def modify_username(self, account_id, name):
        account = self.accounts[account_id]
        account.name = name
        return True

    def modify_address(self, account_id, street, city):
        account = self.accounts[account_id]
        account.address.street = street
        account.address.city = city
        return True

    def modify_age(self, age):
        account = self.accounts[age]
        account.age = age

    def check_account_type(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].account_type
        else:
            raise ValueError('Account ID not found')


if __name__ == '__main__':
    account_service = AccountService()
    admin_account = account_service.add_account('account_id_1', 'password1', 'name1', 20, 'street1', 'Hyd', 'Admin')
    print(admin_account.account_id)
    print(admin_account.age)
    admin_account.age = 21
    print(admin_account.age)
    print(admin_account.address.street)
    print(admin_account.address.city)
    admin_account.address.city = 'Bangalore'
    print(admin_account.address.city)
