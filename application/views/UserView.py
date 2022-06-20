
from flask import  redirect, render_template, request, url_for,flash
from flask_classful import FlaskView, route
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from application import login_manager
from application.models.models import *
from sqlalchemy import text

@login_manager.user_loader 
def load_user(user_id):
	return User.query.get(int(user_id))

class UserView(FlaskView):
	@route('/login', methods=['GET','POST'])
	def login(self):
		if request.method == 'POST':
			email = request.form.get('email')
			password = request.form.get('password')
			user = User.query.filter_by(email=email).first()
			if user:
				if check_password_hash(user.password,password):
					login_user(user)
					if user.email == "admin@gmail.com":
						return redirect(url_for('AdminView:home'))
					else:
						return redirect(url_for('HomeView:home'))
				else:
					flash("Your password is incorrect")
					return redirect(url_for('UserView:login'))
			else:
				flash("This user does not exist")
				return redirect(url_for('UserView:login'))
		else:
			return render_template('signin.html')
			
			
	@route('/signup', methods=['GET','POST'])
	def signup(self):
		if request.method == 'POST':
			username = request.form.get('username')
			email = request.form.get('email')
			password = request.form.get('password')
			hashed_password = generate_password_hash(password,method='sha256')
			new_user = User(username=username,email=email,password=hashed_password)
			try:
				db.session.add(new_user)
				db.session.commit()
				return redirect(url_for('UserView:login'))
			except:
				return "There was an issue"
		else:
			return render_template('signup.html')

	@route("/logout")
	@login_required
	def logout(self):
		logout_user()
		return redirect(url_for('UserView:login'))




    