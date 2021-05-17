from models import vehicle
from services import vehicle_service, account_service


class VehicleController:

	def __init__(self, vehicle_service, account_service):
		self.vehicle_service = vehicle_service
		self.account_service = account_service

	def add_vehicle(self, license_plate_number, color, transmission_type, barcode, passenger_capacity, vehicle_type, account_id):
		if self.account_service.check_account_type(account_id) == "Admin":
			new_vehicle = self.vehicle_service.add_vehicle(license_plate_number, color, transmission_type, barcode, passenger_capacity, vehicle_type)
			return new_vehicle
		else:
			raise ValueError("Only admins can add vehicles to inventory")

	def book_vehicle(self, license_plate_number):
		vehicle_obj = self.vehicle_service.get_vehicle_by_license_plate(license_plate_number)
		if vehicle_obj:
			try:
				self.vehicle_service.reserve_vehicle(license_plate_number) # can't we directly pass the vehicle object here?
				return True
			except ValueError as e:
				return e
		else:
			raise ValueError('Cannot perform reservation as requested vehicle is not found')

	def get_vehicle_details(self, license_plate_number):
		vehicle_obj = self.vehicle_service.get_vehicle_by_license_plate(license_plate_number)
		return vehicle_obj

