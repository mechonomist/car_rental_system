from abc import ABC, abstractmethod
import datetime 


class Address(object):
	def __init__(self, street, city):
		self.__street = street
		self.__city = city

	@property
	def street(self):
		return self.__street

	@street.setter
	def street(self, street):
		self.__street = street

	@property
	def city(self):
		return self.__city

	@city.setter
	def city(self, city):
		self.__city = city


class Person(object):
	def __init__(self, name, address, age):
		self.__name = name
		self.__address = address
		self.__age = age

	@property	
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		self.__name = name

	@property	
	def address(self):
		return self.__address
	
	@address.setter
	def address(self, address):
		self.__address = address

	@property	
	def age(self):
		return self.__age
	
	@age.setter
	def age(self, age):
		self.__age = age


class Account(ABC):
	def __init__(self, account_id, password, name, age, street, city):
		self.__account_id = account_id
		self.__password = password
		self.__age = age
		self.__address = Address(street, city)
		self.__person = Person(name, age, self.__address)
		self.__date_joined = datetime.date.today()

	@property	
	def account_id(self):
		return self.__account_id

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, age):
		self.__age = age

	@property	 # was throwing an error without a getter - should check this
	def password(self):
		return self.__password

	@password.setter
	def password(self, password):
		self.__password = password

	@property	
	def person(self):
		return self.__person

	@property
	def address(self):
		return self.__address


class Admin(Account):
	
	def __init__(self, account_id, password, name, age, street, city):
		super().__init__(account_id, password, name, age, street, city)
		self.__account_type = 'Admin'

	@property
	def account_type(self):
		return self.__account_type


class Member(Account):
	def __init__(self, account_id, password, name, age, street, city):
		super().__init__(account_id, password, name, age, street, city)
		self.__account_type = 'Member'

	@property
	def account_type(self):
		return self.__account_type


class AdditionalDriver:   # additional drivers need not have an account on the application
	def __init__(self, driver_id, name, age, street, city):
		self.__driver_id = driver_id
		self.__address = Address(street, city)
		self.__person = Person(name, age, self.__address)


if __name__ == '__main__':
	admin = Member('123','password', 'R', 'T', 'Str1', 'Hyd')
	print(admin.password)
	print(admin.person.name)
	admin.person.name = 'S'
	print(admin.person.name)

