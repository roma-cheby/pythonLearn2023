import datetime

from flask import Flask, request, jsonify
from sqlalchemy import func

from create_db import Books, ReceivingBooks, session, Students

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

@app.route('/get_books_by_author/<int:author_id>', methods=["GET"])
def get_books_by_author(author_id):
    available_books = session.query(Books).filter(Books.author_id == author_id, Books.id == ReceivingBooks.book_id, ReceivingBooks.date_of_return == None).all()
    books_list = []
    for book in available_books:
        json_book = book.to_json()
        books_list.append(json_book)
    return jsonify(books_list), 200

@app.route('/get_average_books_month', methods=['GET'])
def get_average_books_month():
    month_now = datetime(datetime.now().year, datetime.now().month, 1, 0, 0, 0, 0)
    taken_books_count = session.query(func.count(ReceivingBooks.book_id)).filter(ReceivingBooks.date_of_issue >= month_now).scalar()
    students_count = session.query(func.count(Students.id)).scalar()
    avg_book_month_count = round(taken_books_count / students_count, 2)
    return f'Среднее количество книг в этом месяце {avg_book_month_count}', 200

@app.route('/get_popular_book', methods=['GET'])
def get_popular_book():
    book_id = session.query(func.count(ReceivingBooks.id)).\
        filter(ReceivingBooks.student_id == Students.id, Students.average_score >= 4.0).\
        group_by(ReceivingBooks.book_id).order_by(func.count(ReceivingBooks.id).
                                                  desc()).limit(1).all()
    book = session.query(Books).filter(Books.id == book_id[0][0]).all()
    return jsonify(book.to_json()), 200

if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.run()
