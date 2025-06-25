import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Создать соединение с базой данных SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # Исправленная версия без deprecated-функции
        print(f"Подключение к SQLite (версия через sqlite3.sqlite_version: {sqlite3.sqlite_version})")
        return conn
    except Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
    return conn


def create_table(conn):
    """Создать таблицу Дисциплины"""
    try:
        sql = '''CREATE TABLE IF NOT EXISTS disciplines (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    specialty TEXT NOT NULL,
                    lectures INTEGER NOT NULL CHECK(lectures >= 0),
                    practical INTEGER NOT NULL CHECK(practical >= 0),
                    laboratory INTEGER NOT NULL CHECK(laboratory >= 0),
                    report_form TEXT NOT NULL CHECK(report_form IN ('Экзамен', 'Зачет', 'Диф.зачет'))
                '''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Таблица 'Дисциплины' успешно создана")
    except Error as e:
        print(f"Ошибка создания таблицы: {e}")


def add_discipline(conn, discipline):
    """Добавить новую дисциплину"""
    sql = '''INSERT INTO disciplines(code, name, specialty, lectures, practical, laboratory, report_form)
             VALUES(?,?,?,?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, discipline)
        conn.commit()
        print(f"Дисциплина '{discipline[1]}' успешно добавлена")
        return cursor.lastrowid
    except Error as e:
        print(f"Ошибка добавления дисциплины: {e}")
        return None


def get_all_disciplines(conn):
    """Получить все дисциплины в виде форматированной таблицы"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM disciplines")
        disciplines = cursor.fetchall()

        if not disciplines:
            print("В базе данных нет дисциплин")
            return

        # Вывод красивой таблицы
        print("\nСписок всех дисциплин:")
        print("-" * 90)
        print(
            f"{'ID':3} | {'Код':8} | {'Наименование':25} | {'Специальность':12} | {'Лекции':6} | {'Практ.':6} | {'Лаб.':6} | {'Отчетность':12}")
        print("-" * 90)
        for row in disciplines:
            print(
                f"{row[0]:3} | {row[1]:8} | {row[2]:25} | {row[3]:12} | {row[4]:6} | {row[5]:6} | {row[6]:6} | {row[7]:12}")
        print("-" * 90)
    except Error as e:
        print(f"Ошибка получения данных: {e}")


def main():
    database = "study_plan.db"

    # Создаем соединение с базой данных
    conn = create_connection(database)

    if conn is not None:
        # Создаем таблицу
        create_table(conn)

        # Пример добавления дисциплин
        disciplines = [
            ('INF-101', 'Информатика', '09.03.01', 36, 18, 18, 'Экзамен'),
            ('MATH-201', 'Высшая математика', '09.03.01', 72, 36, 0, 'Зачет'),
            ('PHYS-301', 'Физика', '09.03.02', 54, 18, 18, 'Экзамен'),
        ]

        for disc in disciplines:
            add_discipline(conn, disc)

        # Выводим все дисциплины
        get_all_disciplines(conn)

        # Закрываем соединение
        conn.close()
    else:
        print("Ошибка! Не удалось подключиться к базе данных.")


if __name__ == '__main__':
    main()