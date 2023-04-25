import sqlite3

if __name__ == "__main__":
    with sqlite3.connect("hw_4_database.db") as conn:
        cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM salaries WHERE salary < 5000")
    result = cursor.fetchall()
    print(f"{result[0][0]} человек находятся за чертой бедности")

    cursor.execute("SELECT AVG(salary) FROM salaries")
    result = cursor.fetchall()
    print(f"Средняя зарплата {result[0][0]}")

    cursor.execute("SELECT salary FROM salaries ORDER BY salary LIMIT (SELECT COUNT(*) FROM salaries)/2, (SELECT COUNT(*) FROM salaries)/2")
    result = cursor.fetchall()
    print(f"Медианная зарплата {result[0][0]}")

    cursor.execute("SELECT 100 * ROUND(X / Y, 2)"
                   "X = SELECT SUM(salary) FROM TOP10"
                   "TOP10 = SELECT SUM(salary) FROM salaries ORDER BY salary DESC LIMIT 0.1 * TOTAL"
                   "TOTAL = SELECT COUNT(salary) FROM salaries")
    result = cursor.fetchall()
    print(f"Средняя зарплата {result[0][0]}")

