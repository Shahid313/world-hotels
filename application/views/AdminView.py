from flask import  redirect, render_template, request, url_for,flash
from application.utils import save_file
from flask_classful import FlaskView, route
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from application import login_manager
from application.models.models import *
from sqlalchemy import text
import numpy as np
from fpdf import FPDF 
import os

class AdminView(FlaskView):
    @route('/home')
    @login_required
    def home(self):
        all_bookings = Booking.query.all()
        return render_template('admin_panel/index.html', all_bookings=all_bookings)

    @route('/add_hotel', methods=['GET', 'POST'])
    @login_required
    def add_hotel(self):
        if request.method == 'POST':
            hotel_name = request.form.get('hotel_name')
            rooms_capicity = request.form.get('rooms_capicity')
            off_peak_season_room_price = request.form.get('off_peak_season_room_price')
            peak_season_room_price = request.form.get('peak_seasons_room_price')
            city_name = request.form.get('city_name')
            print(city_name)
            new_hotel = Hotel(hotel_name=hotel_name,city_name=city_name,rooms_capicity=rooms_capicity, 
                        off_peak_season_room_price=off_peak_season_room_price,peak_season_room_price=peak_season_room_price)
            try:
                db.session.add(new_hotel)
                db.session.commit()
                flash("Hotel Added Successfully")
                return redirect(url_for('AdminView:add_hotel'))
            except Exception as e:
                return "There was an issue adding hotel"+str(e)
        else:
            return render_template('admin_panel/add_hotel.html')

    @route('/admin_cancel_booking/<int:id>', methods=['GET','POST'])
    @login_required
    def admin_cancel_booking(self, id):
        if request.method == 'POST':
            booking_to_delete = Booking.query.get_or_404(id)
            db.session.delete(booking_to_delete)
            db.session.commit()
            flash("Booking Canceled Successfully")
            return redirect(url_for('AdminView:home'))

    @route('/admin_get_all_hotels')
    @login_required
    def admin_get_all_hotels(self):
        all_hotels = Hotel.query.all()
        return render_template('admin_panel/hotels.html', all_hotels=all_hotels)

    @route('/delete_hotel/<int:id>', methods=['GET','POST'])
    @login_required
    def delete_hotel(self, id):
        if request.method == 'POST':
            hotel_to_delete = Hotel.query.get_or_404(id)
            db.session.delete(hotel_to_delete)
            db.session.commit()
            flash("Hotel Deleted Successfully")
            return redirect(url_for('AdminView:admin_get_all_hotels'))

    @route("/admin_receipt/<int:id>")
    def admin_receipt(self, id):
        receipt_sql = text("SELECT * FROM booking WHERE id = "+str(id))
        booking_receipt = db.engine.execute(receipt_sql)
        for item in booking_receipt:
            my_receipt = item

        pdf = FPDF() 
        pdf.add_page()
        pdf.set_font("Arial", size = 16)
        pdf.cell(200, 10, txt = "Payment Receipt",ln = 1, align = 'C')
        pdf.cell(200, 10, txt = "Hotel Name: "+my_receipt[1],ln = 2, align = 'C')
        pdf.cell(200, 10, txt = "City: "+my_receipt[2],ln = 3, align = 'C') 
        pdf.cell(200, 10, txt = "Total Amount Paid : "+my_receipt[3]+" "+my_receipt[8],ln = 4, align = 'C') 
        pdf.cell(200, 10, txt = "Additional Services Amount : "+my_receipt[9]+" "+my_receipt[8],ln = 4, align = 'C')
        pdf.cell(200, 10, txt = "Advance Booking Time: "+my_receipt[4]+" days",ln = 5, align = 'C')
        pdf.cell(200, 10, txt = "Booking ID: "+my_receipt[5],ln = 5, align = 'C')
        path = os.path.join(app.static_folder, "receipts/")
        pdf.output(path+my_receipt[5]+'.pdf')
        pdf.close()
        return render_template("admin_panel/admin_receipt.html", my_receipt=my_receipt)