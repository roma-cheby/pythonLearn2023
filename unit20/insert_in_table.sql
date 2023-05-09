INSERT INTO books (id, name, count, release_date, author_id)
VALUES (1, "Book1", 1, '2022-10-10', 1), (2, "Book2", 1, '2022-10-10', 1);

INSERT INTO receiving_books (id, book_id, student_id, date_of_issue, date_of_return)
VALUES (1, 1, 1, "2022-05-05", "2022-05-07"), (2, 1, 1, "2022-04-05", "2022-05-07");