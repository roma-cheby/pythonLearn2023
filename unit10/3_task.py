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

    cursor.execute("SELECT COUNT(DISTINCT value) FROM "
                   "table_1 LEFT JOIN table_2 USING (value) "
                   "WHERE NOT(table_2.id IS NULL)")
    result = cursor.fetchall()
    print(f"В первой таблице встречется {result[0][0]} записей из второй таблицы")

    cursor.execute("SELECT COUNT(DISTINCT value) FROM "
                   "(SELECT DISTINCT value FROM "
                   "table_1 LEFT JOIN table_2 USING (value) "
                   "WHERE NOT(table_2.id IS NULL))"
                   "LEFT JOIN table_3 USING(value)"
                   "WHERE NOT(table_3.id IS NULL)")
    result = cursor.fetchall()
    print(f"В первой таблице встречется {result[0][0]} записей из второй и третьей таблицы")
