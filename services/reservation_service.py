from models import reservations
import datetime


class ReservationService:
    reservations = {}

    def make_a_reservation(self, res_num, due_date, account, vehicle, pickup_loc, return_loc):
        new_reservation = reservations.VehicleReservation(res_num, due_date, account, vehicle, pickup_loc, return_loc)
        self.reservations[res_num] = new_reservation
        return new_reservation

    def end_reservation(self, res_num):
        if res_num in self.reservations:
            self.reservations[res_num].return_date = datetime.date.today()
            self.reservations[res_num].status = 'Complete'
            return True
        else:
            raise ValueError('Reservation not found')

    def get_reservation_by_member(self, member_id):
        reservation_by_member = []
        for reservation in self.reservations:
            if reservation.member_details.account_id == member_id:
                reservation_by_member.append(reservation)
        return reservation_by_member

    def get_reservation_by_id(self, reservation_number=None):
        if reservation_number:
            return self.reservations[reservation_number]
        else:
            return self.reservations.items()

    def get_reservation_by_vehicle_type(self, vehicle_type):
        reservation_by_type = []
        for reservation in self.reservations.values():
            if reservation.vehicle_details.vehicle_type == vehicle_type:
                reservation_by_type.append(reservation)
        return reservation_by_type

    def get_reservation_by_pickup_location(self, pickup_location):
        reservation_by_location = []
        for reservation in self.reservations.values():
            if reservation.pickup_location == pickup_location:
                reservation_by_location.append(reservation)
        return reservation_by_location

    def get_additional_drivers(self, reservation_num):
        reservation_obj = self.get_reservation_by_id(reservation_num)
        return reservation_obj.additional_drivers

    def add_additional_driver(self, reservation_num, account):
        reservation_obj = self.get_reservation_by_id(reservation_num)
        reservation_obj.additional_drivers = account
        return True

    def modify_a_reservation(self, reservation_num,  **kwargs):
        reservation_obj = self.get_reservation_by_id(reservation_num)
        try:
            for key, value in kwargs:
                reservation_obj.key = value
        except AttributeError as e:
            return e

