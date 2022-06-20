from flask import  redirect, render_template, request, url_for, jsonify, flash
from application.utils import save_file
from flask_classful import FlaskView, route
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from application import login_manager, app
from application.models.models import *
from sqlalchemy import text
import numpy as np
from fpdf import FPDF 
import os
from datetime import date

intList = ['A', 'B', 0,1,2,3,4,5,6,7,8,9]


class HomeView(FlaskView):
    @route('/home')
    @login_required
    def home(self):
        return render_template('index.html')

    @route('/make_booking', methods=['GET', 'POST'])
    @login_required
    def make_booking(self):
        if request.method == 'POST':
            AdditionalServicesPrce = 0
            convertedAdditionalServicesPrce = None
            FRoomPrice = None
            BookingId = ''
            city_name = request.form.get('city_name')
            currency = request.form.get('currency')
            hotel_name = request.form.get('hotel_name')
            room_price = request.form.get('room_price')
            checklist = request.form.getlist('check')
            for value in checklist:
                AdditionalServicesPrce = AdditionalServicesPrce + int(value)
            if currency == 'USD':
                convertedAdditionalServicesPrce = AdditionalServicesPrce * 1.6
            elif currency == 'Euros':
                convertedAdditionalServicesPrce = AdditionalServicesPrce * 1.2
            elif currency == 'QAR':
                convertedAdditionalServicesPrce = AdditionalServicesPrce * 4.5
            elif currency == 'AED':
                convertedAdditionalServicesPrce = AdditionalServicesPrce * 4.5
            elif currency == 'VND':
                convertedAdditionalServicesPrce = AdditionalServicesPrce * 3000
            elif currency == 'INR':
                convertedAdditionalServicesPrce = AdditionalServicesPrce * 100
            elif currency == 'NPR':
                convertedAdditionalServicesPrce = AdditionalServicesPrce * 150
            else:
                convertedAdditionalServicesPrce = AdditionalServicesPrce
            
            advance_booking_time = request.form.get('advance_booking_time')
            if int(advance_booking_time) >= 100 and int(advance_booking_time) <= 120:
                flash("You have been given 25% discount")
                FRoomPrice = (25 * int(room_price) / 100) + convertedAdditionalServicesPrce
            elif int(advance_booking_time) >= 80 and int(advance_booking_time) <= 99:
                flash("You have been given 15% discount")
                FRoomPrice = (15 * int(room_price) / 100) + convertedAdditionalServicesPrce
            elif int(advance_booking_time) >= 60 and int(advance_booking_time) <= 79:
                flash("You have been given 10% discount")
                FRoomPrice = (10 * int(room_price) / 100) + convertedAdditionalServicesPrce
            elif int(advance_booking_time) >= 46 and int(advance_booking_time) <= 59:
                flash("You have been given 5% discount")
                FRoomPrice = (5 * int(room_price) / 100) + convertedAdditionalServicesPrce
            else:
                FRoomPrice = int(room_price) + convertedAdditionalServicesPrce
            booking_id = np.random.choice(intList, size=(9,))
            for i in range(len(booking_id)):
                BookingId += str(booking_id[i]) 
            new_booking = Booking(hotel_name=hotel_name,city_name=city_name,room_price=FRoomPrice,
                            advance_booking_time=advance_booking_time,booking_id=BookingId,booked_by=current_user.username, 
                            booking_date=date.today(), currency=currency, additional_services_price=convertedAdditionalServicesPrce, user_id=current_user.id)
            db.session.add(new_booking)
            db.session.commit()
            city_id = None
            currency = None
            hotel_name = None
            room_price = None
            advance_booking_time = None
            return redirect(url_for('HomeView:make_booking'))
        else:
            return render_template('make_booking.html')

    @route("/get_all_hotels", methods=['GET'])
    def get_all_hotels(self):
        all_hotels = Hotel.query.all()
        results = hotels_schema.dump(all_hotels)
        return jsonify(results)

    @route("/receipt/<int:id>")
    def receipt(self, id):
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
        return render_template("receipt.html", my_receipt=my_receipt)
    
    @route('/bookings')
    def bookings(self):
        bookings_sql = text("SELECT * FROM booking WHERE user_id = "+ str(current_user.id))
        bookings = db.engine.execute(bookings_sql)
        return render_template('bookings.html', bookings=bookings)
    
    @route('/cancel_booking/<int:id>', methods=['GET','POST'])
    def cancel_booking(self, id):
        if request.method == 'POST':
            booking = Booking.query.get_or_404(id)
            year = int(booking.booking_date[0:4])
            month = int(booking.booking_date[5:7])
            day = int(booking.booking_date[8:10])

            todayDate =  date.today()
            tyear = int(todayDate.year)
            tmonth = int(todayDate.month)
            tday = int(todayDate.day)

            print(tyear,tmonth,tday)
            
            def diff_dates(date1, date2):
                return abs(date2-date1).days

            def main():
                d1 = date(year,month,day)
                d2 = date(tyear,tmonth,tday)
                result1 = diff_dates(d2, d1)
                return result1
                
            if main() >= 50 and main() <= 74:
                flash("Incurred 30% charges of booking price")
            elif main() >= 31 and main() <= 49:
                flash("Incurred 50% charges")
            elif main() >= 0 and main() <= 30:
                flash("Incurred 100% charges")
            else:
                flash("No charges have been incurred")
            
            try:
                db.session.delete(booking)
                db.session.commit()
            except Exception as e:
                return str(e)
            return redirect(url_for('HomeView:bookings'))


