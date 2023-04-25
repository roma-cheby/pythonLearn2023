"""
Иван Совин - эффективный менеджер.
Когда к нему приходит сотрудник просить повышение з/п -
    Иван может повысить её только на 10%.

Если после повышения з/п сотрудника будет больше з/п самого
    Ивана Совина - сотрудника увольняют, в противном случае з/п
    сотрудника повышают.

Давайте поможем Ивану стать ещё эффективнее,
    автоматизировав его нелёгкий труд.
    Пожалуйста реализуйте функцию которая по имени сотрудника
    либо повышает ему з/п, либо увольняет сотрудника
    (удаляет запись о нём из БД).

Таблица с данными называется `table_effective_manager`
"""
import sqlite3


def ivan_sovin_the_most_effective(
        c: sqlite3.Cursor,
        name: str,
) -> None:
    c.execute("SELECT salary FROM table_effective_manager WHERE name = 'Иван Совин'")
    salary_manager = c.fetchall()[0][0]
    c.execute(f"SELECT salary FROM table_effective_manager WHERE name = '{name}'")
    salary_name = c.fetchall()[0][0]
    if salary_name * 1.1 > salary_manager:
        c.execute(f"DELETE FROM table_effective_manager WHERE name = '{name}'")
        print(f"Сотрудник слишком наглый, пришлось его уволить. {name} уволен")
    else:
        c.execute(f"UPDATE table_effective_manager SET salary = {salary_name * 1.1} WHERE name = '{name}'")
        print(f"Сотрудник может получить повышение зарплаты. Зарплата {name} была {salary_name}, а стала {int(salary_name * 1.1)}")

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        name = input("Введите фамилию и инициалы сотрудника (например Иванов И.И.): ")
        ivan_sovin_the_most_effective(cursor, name)