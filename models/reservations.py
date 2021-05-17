import datetime


class VehicleReservation(object):
	def __init__(self, reservation_number, due_date, account, vehicle, pickup_location, return_location):
		self.__reservation_number = reservation_number
		self.__creation_date = datetime.date.today()
		self.__status = 'Active'
		self.__due_date = due_date
		self.__return_date = None
		self.__pickup_location = pickup_location
		self.__return_location = return_location

		self.__member_details = account
		self.__insurance = []
		self.__additional_drivers = []
		self.__vehicle_details = vehicle

	
	@property
	def status(self):
		return self.__status

	@status.setter
	def status(self, status):
		self.__status = status

	@property
	def return_date(self):
		return self.__return_date

	@return_date.setter
	def return_date(self, return_date):
		self.__return_date = return_date

	@property
	def due_date(self):
		return self.__due_date

	@due_date.setter
	def due_date(self, due_date):
		self.__due_date = due_date

	@property
	def additional_drivers(self):
		return self.__additional_drivers

	@additional_drivers.setter
	def additional_drivers(self, account):
		self.__additional_drivers.append(account)

	@property
	def vehicle_details(self):
		return self.__vehicle_details
