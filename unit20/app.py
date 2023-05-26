import datetime

from flask import Flask, request, jsonify
from create_db import Books, ReceivingBooks, session

app = Flask(__name__)


@app.route('/get_all_books', methods=["GET"])
def get_all_books():
    books = Books.get_all_books()
    books_as_dict = []
    for book in books:
        book_as_dict = book.to_json()
        books_as_dict.append(book_as_dict)
    return jsonify(books_as_dict), 200


@app.route('/get_debtors', methods=["GET"])
def get_debtors():
    debtors = ReceivingBooks.get_debtors()
    debtors_as_dict = []
    for debtor in debtors:
        debtor_as_dict = debtor.to_json()
        if debtor.count_date_with_book > 14:
            debtors_as_dict.append(debtor_as_dict)
    return jsonify(debtors_as_dict), 200


@app.route('/give_book_to_student', methods=["POST"])
def give_book_to_student():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    receiving_book = ReceivingBooks(book_id=book_id, student_id=student_id, date_of_issue = datetime.datetime.now())
    session.add(receiving_book)
    session.commit()
    return "Книга выдана", 201


@app.route('/pass_book', methods=["POST"])
def pass_book_by_student():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    receiving_book = session.query(ReceivingBooks).filter(ReceivingBooks.book_id == book_id, ReceivingBooks.student_id == student_id).one_or_none()
    if receiving_book is not None:
        receiving_book.date_of_return = datetime.datetime.now()
        session.commit()
        return "Книга сдана", 202
    else:
        return f"Студент {student_id} не брал книгу {book_id}", 404

@app.route('/search_books/<string:search_book>', methods=["GET"])
def search_books(search_book):
    books = Books.search_books(search_book)
    books_as_dict = []
    for book in books:
        book_as_dict = book.to_json()
        books_as_dict.append(book_as_dict)
    return jsonify(books_as_dict), 200

if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.run()