from models.vehicle import SUV, Truck, Van


class VehicleService:
	vehicles = {}

	def get_vehicle_by_license_plate(self, license_plate_number):
		try:
			vehicle_obj = self.vehicles[license_plate_number]
			return vehicle_obj
		except KeyError:
			return False

	def add_vehicle(self, license_plate_number, color, transmission_type, barcode, passenger_capacity, vehicle_type):
		if vehicle_type == 'SUV':
			new_vehicle = SUV(license_plate_number, color, transmission_type, barcode, passenger_capacity)
		elif vehicle_type == 'Truck':
			new_vehicle = Truck(license_plate_number, color, transmission_type, barcode, passenger_capacity)
		elif vehicle_type == 'Van':
			new_vehicle = Van(license_plate_number, color, transmission_type, barcode, passenger_capacity)
		else:
			raise ValueError("Cannot create vehicle")

		self.__class__.vehicles[license_plate_number] = new_vehicle
		return new_vehicle

	def reserve_vehicle(self, license_plate_number):
		if license_plate_number in self.vehicles:
			if self.vehicles[license_plate_number].status == 'Available':
				self.vehicles[license_plate_number].status = 'Reserved'
				return True
			else:
				raise ValueError("Vehicle is already reserved")
		else:
			raise ValueError("Vehicle cannot be found")

	def return_vehicle(self, license_plate_number):
		if license_plate_number in self.vehicles:
			self.vehicles[license_plate_number].status = 'Available'
			return True
		else:
			raise ValueError("Vehicle cannot be found")


if __name__ == "__main__":
	vehicle_service = VehicleService()
	vehicle1 = vehicle_service.add_vehicle('abc', 'Red', 'Manual', 'barcode123', 5, 'SUV')

	print(vehicle1.status)
	vehicle_service.reserve_vehicle('abc')
	print(vehicle1.status)
	# vehicle_service.reserve_vehicle('abc')

