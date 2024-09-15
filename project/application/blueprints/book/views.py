from application.blueprints.auth import auth
from application.models import User,Book
from flask import render_template, request, redirect, url_for,session,flash
from application.blueprints.book import book 


# Add Book
@book.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if 'user_id' in session.keys():
        if request.method == 'POST':
            title = request.form['title']
            image = request.files['image'].read()  # Store image as BLOB
            data = {'title':title, 'image':image, 'user_id':session['user_id']}
            Book.add_book(data)
            return redirect(url_for('book.view_books'))
        return render_template('add_book.html')
    return redirect(url_for('auth.login'))


# View Books
@book.route('/book')
def view_books():
    print("View_books HIT!")
    if 'user_id' in session.keys():
        user = User.query.get(session['user_id'])
        books = user.books
        return render_template('books.html', books=books)
    return redirect(url_for('auth.login'))



# Delete Book
@book.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    Book.delete_book(book_id)
    return redirect(url_for('book.view_books'))

# Admin Dashboard
@book.route('/admin_dashboard')
def admin_dashboard():
    if not session.get('is_admin'):
        return "Access Denied!"
    users = User.query.all()
    books = Book.query.all()
    return render_template('admin.html', users=users, books=books)
