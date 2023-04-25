import sqlite3

if __name__ == "__main__":
    with sqlite3.connect("hw_3_database.db") as conn:
        cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM table_1")
    result = cursor.fetchall()
    print(f"В первой таблице {result[0][0]} записей")
    cursor.execute("SELECT COUNT(*) FROM table_2")
    result = cursor.fetchall()
    print(f"Во второй таблице {result[0][0]} записей")
    cursor.execute("SELECT COUNT(*) FROM table_3")
    result = cursor.fetchall()
    print(f"В третьей таблице {result[0][0]} записей")

    cursor.execute("SELECT COUNT(*) FROM (SELECT DISTINCT * FROM table_1)")
    result = cursor.fetchall()
    print(f"В первой таблице {result[0][0]} уникальных записей")

    cursor.execute("SELECT COUNT(*) FROM (SELECT DISTINCT * FROM table_1) JOIN table_2 USING (value)")
    result = cursor.fetchall()
    print(f"В первой таблице {result} уникальных записей")

