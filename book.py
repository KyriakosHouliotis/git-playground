@app.route('/books')
def get_books():
	books = get_all_books_from_db() # Some function that returns the list of book entries from the database.
return render_template('book_list.html', books=books)
