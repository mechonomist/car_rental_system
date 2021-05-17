class ParkingSlot:
	def __init__(self, parking_slot_id, parking_slot_type, parking_slot_size):
		self.__parking_slot_id = parking_slot_id
		self.__parking_slot_type = parking_slot_type
		self.__parking_slot_size = parking_slot_size

	@property
	def parking_slot_id(self):
		return self.__parking_slot_id

	@property
	def parking_slot_size(self):
		return self.__parking_slot_size

	@property
	def parking_slot_type(self):
		return self.__parking_slot_type
