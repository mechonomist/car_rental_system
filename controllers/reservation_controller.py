from services import vehicle_service, account_service, reservation_service


class VehicleReservationController:

	def __init__(self, vehicle_service, account_service, reservation_service):
		self.account_service = account_service
		self.vehicle_service = vehicle_service
		self.reservation_service = reservation_service

	def make_reservation(self, res_num, due_date, account, vehicle, pickup_loc, return_loc):
		new_reservation = self.reservation_service.make_a_reservation(res_num, due_date, account, vehicle, pickup_loc, return_loc)
		self.vehicle_service.reserve_vehicle(vehicle.license_plate_number)
		return new_reservation

	def end_reservation(self, res_num):
		# business logic can be implemented to calculate late fees etc.
		res_obj = self.reservation_service.get_reservation_by_id(res_num)
		veh_num = res_obj.vehicle_details.license_plate_number
		self.reservation_service.end_reservation(res_num)
		self.vehicle_service.return_vehicle(veh_num)
		return True

	def filter_reservations(self, **kwargs):
		vehicle_type = kwargs.get("vehicle_type", None)
		pickup_location = kwargs.get("pick_up_location", None)

		if vehicle_type and pickup_location:
			res_by_type = self.reservation_service.get_reservation_by_vehicle_type(vehicle_type)
			res_by_location = self.reservation_service.get_reservation_by_pickup_location(pickup_location)
			return [obj for obj in res_by_type if obj in res_by_location]
		elif vehicle_type:
			res_by_type = self.reservation_service.get_reservation_by_vehicle_type(vehicle_type)
			return res_by_type
		elif pickup_location:
			res_by_location = self.reservation_service.get_reservation_by_pickup_location(pickup_location)
			return res_by_location
		else:
			raise ValueError('Please provide either vehicle type or location')

	def get_reservation_details(self, reservation_number):
		return self.reservation_service.get_reservation_by_id(reservation_number)

	def get_additional_drivers(self, reservation_number):
		return self.reservation_service.get_additional_drivers(reservation_number)

	def add_additional_driver(self, account, reservation_number):
		return self.reservation_service.add_additional_driver(reservation_number, account)


if __name__ == "__main__":
	from controllers.vehicle_controller import VehicleController

	veh_service_1 = vehicle_service.VehicleService()
	acc_service_1 = account_service.AccountService()
	res_service_1 = reservation_service.ReservationService()

	# adding two accounts, 1 admin and 1 member
	admin_acc = acc_service_1.add_account('account_id_1', 'password1', 'name1', 20, 'street1', 'Hyd', 'Admin')
	member_acc_1 = acc_service_1.add_account('account_id_2', 'password2', 'name2', 30, 'street2', 'Bang', 'Member')
	member_acc_2 = acc_service_1.add_account('account_id_3', 'password3', 'name3', 40, 'street3', 'Chennai', 'Member')

	veh_controller_1 = VehicleController(veh_service_1, acc_service_1)
	vehicle_1 = veh_controller_1.add_vehicle('abc1', 'Red', 'Manual', 'barcode123', 5, 'SUV', 'account_id_1')
	vehicle_2 = veh_controller_1.add_vehicle('abc2', 'Blue', 'Auto', 'barcode234', 3, 'Truck', 'account_id_1')
	vehicle_3 = veh_controller_1.add_vehicle('abc3', 'Green', 'Manual', 'barcode345', 5, 'SUV', 'account_id_1')
	vehicle_4 = veh_controller_1.add_vehicle('abc4', 'White', 'Auto', 'barcode456', 4, 'Van', 'account_id_1')
	vehicle_5 = veh_controller_1.add_vehicle('abcf5', 'White', 'Auto', 'barcode567', 4, 'Van', 'account_id_1')

	veh_res_controller_obj = VehicleReservationController(veh_service_1, acc_service_1, res_service_1)
	# print(veh_res_controller_obj)
	veh_res_controller_obj.make_reservation('res_num123', '2021-05-23', member_acc_1, vehicle_1, 'Hyderabad', 'Hyderabad')
	print(veh_res_controller_obj.get_reservation_details('res_num123'))

	veh_res_controller_obj.end_reservation('res_num123')

	print(len(res_service_1.reservations))

	veh_res_controller_obj.make_reservation('res_num124', '2021-05-21', member_acc_2, vehicle_1, 'Hyderabad', 'Hyderabad')
	print(len(res_service_1.reservations))



