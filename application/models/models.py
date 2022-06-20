from locale import currency
from application import app, db, ma
from flask_login import (LoginManager,UserMixin,login_user,login_required,
logout_user,current_user)
from datetime import datetime

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), nullable=False)
    email = db.Column(db.String(55), nullable=False)
    password = db.Column(db.String(200))
    booking = db.relationship('Booking',backref='user',lazy='dynamic')


class Hotel(db.Model):
    hotel_id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(55), nullable=False)
    city_name = db.Column(db.String(100))
    rooms_capicity = db.Column(db.String(100))
    off_peak_season_room_price = db.Column(db.String(100))
    peak_season_room_price = db.Column(db.String(100))

    def __init__(self, hotel_name,city_name, rooms_capicity, off_peak_season_room_price, peak_season_room_price):
        self.hotel_name = hotel_name
        self.city_name = city_name
        self.rooms_capicity = rooms_capicity
        self.off_peak_season_room_price = off_peak_season_room_price
        self.peak_season_room_price = peak_season_room_price
        

class HotelSchema(ma.Schema):
    class Meta:
        fields = ('hotel_id', 'hotel_name', 'city_name', 'rooms_capicity', 'off_peak_season_room_price', 'peak_season_room_price')

hotel_schema = HotelSchema()
hotels_schema = HotelSchema(many=True)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(55), nullable=False)
    city_name = db.Column(db.String(55), nullable=False)
    room_price = db.Column(db.String(100))
    advance_booking_time = db.Column(db.String(100))
    booking_id = db.Column(db.String(100))
    booked_by = db.Column(db.String(100))
    booking_date = db.Column(db.String(100))
    currency = db.Column(db.String(100))
    additional_services_price = db.Column(db.String(100))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self, hotel_name, city_name, room_price, advance_booking_time, booking_id,booked_by, booking_date, currency,additional_services_price, user_id):
        self.hotel_name = hotel_name
        self.city_name = city_name
        self.room_price = room_price
        self.advance_booking_time = advance_booking_time
        self.booking_id = booking_id
        self.booked_by = booked_by
        self.booking_date = booking_date
        self.currency = currency
        self.additional_services_price = additional_services_price
        self.user_id = user_id

class BookingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'hotel_name', 'city_name', 'room_price', 'advance_booking_time', 'booking_id' 'booked_by', 'booking_date', 'currency', 'additional_services_price', 'user_id')

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)