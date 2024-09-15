# signup, login, authntication, authorization,logout

from application.blueprints.auth import auth
from extensions import db
from flask import render_template, request, redirect, url_for,session,flash
from werkzeug.security import check_password_hash, generate_password_hash
from application.models import User
from .forms import LoginForm, RegisterForm



# User Registration
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()  # Instantiate the form

    if form.validate_on_submit():  # Validate form submission
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Hash the password and create a new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    # Render the registration form
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Create an instance of LoginForm here, outside the POST block

    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.email.data  # Assuming you're using email to log in
            password = form.password.data
            user = User.query.filter_by(username=username).first()  # Verify you're filtering by username or email
            
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['is_admin'] = user.is_admin
                return redirect(url_for('view_books'))  # Redirect to the correct view

            flash('Invalid credentials!', 'danger')  # Display flash message if credentials are invalid

    # For GET requests, or if the form is not valid, render the login page again
    return render_template('login.html', form=form)



# Logout
@auth.route('/logout')
def logout():
    if 'user_id' in session.keys():
        session.pop('user_id')
        session.pop('is_admin')
    return redirect(url_for('auth.login'))



# Delete User
@auth.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    if not session.get('is_admin'):
        return "Access Denied!"
    User.delete_user(user_id)
    return redirect(url_for('books.admin_dashboard'))