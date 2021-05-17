from abc import ABC, abstractmethod
import datetime
from .reservations import *


class Vehicle(ABC):

	def __init__(self, license_plate_number, color, transmission_type, barcode, passenger_capacity):
		self.__license_plate_number = license_plate_number
		self.__color = color
		self.__transmission_type = transmission_type
		self.__barcode = barcode
		self.__passenger_capacity = passenger_capacity
		self.__status = 'Available'

	@property
	def license_plate_number(self):
		return self.__license_plate_number
	
	@property
	def color(self):
		return self.__license_plate_number

	@property
	def transmission_type(self):
		return self.__transmission_type
	
	@property
	def barcode(self):
		return self.__barcode

	@property
	def passenger_capacity(self):
		return self.__passenger_capacity

	@property
	def status(self):
		return self.__status

	@status.setter
	def status(self, status):
		self.__status = status

class SUV(Vehicle):
	
	def __init__(self, license_plate_number, color, transmission_type, barcode, passenger_capacity):
		super().__init__(license_plate_number, color, transmission_type, barcode, passenger_capacity)
		self.__vehicle_type = 'SUV'

	@property	
	def vehicle_type(self):
		return self.__vehicle_type
		

class Van(Vehicle):
	
	def __init__(self, license_plate_number, color, transmission_type, barcode, passenger_capacity):
		super().__init__(license_plate_number, color, transmission_type, barcode, passenger_capacity)
		self.__vehicle_type = 'Van'

	@property	
	def vehicle_type(self):
		return self.__vehicle_type

class Truck(Vehicle):
	
	def __init__(self, license_plate_number, color, transmission_type, barcode, passenger_capacity):
		super().__init__(license_plate_number, color, transmission_type, barcode, passenger_capacity)
		self.__vehicle_type = 'Truck'

	@property	
	def vehicle_type(self):
		return self.__vehicle_type


if __name__ == "__main__":
	vehicle1 = Truck(123, "black", "manual", barcode=312313, passenger_capacity=5)
	print(vehicle1.vehicle_type)

