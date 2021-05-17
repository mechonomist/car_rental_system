# from accounts import *
# from insurance import *
# from reservations import *
# from vehicle import *

# address1 = Address('Necklace Road', 'Hyderabad')
# person1 = Person('Teja', address1, 31)


# # self, account_id, password, person, status=None)
# member1 = Member(123, 'xyz', person1)
# vehicle1 = SUV(1, 'red', 'auto', '1234', 4)

# # reservation_number, due_date, return_date, pickup_location, dropoff_location, account, vehicle
# reservation1 = VehicleReservation(345, '2021-05-31', 'Hyderabad', 'Hyderabad', member1, vehicle1)
# member1.update_reservations(reservation1)

# for res in member1.get_reservations():
# 	print(res.get_vehicle_details().get_passenger_capacity())

# print(reservation1.get_status())
# print(vehicle1.get_status())
# vehicle1.return_vehicle()
# print(vehicle1.get_status())

