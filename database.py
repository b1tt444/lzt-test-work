import sqlite3


class Database:
    """Класс для взаимодействия с SQLite бд."""
    def __init__(self, db_name="notes.db"):
        """
        Инициализация класса базы данных.

        Параметры:
        db_name (str): Название бд.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Создает таблицу 'notes' если ее не существует"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS notes (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                content TEXT
                            )""")
        self.connection.commit()

    def add_note(self, title, content):
        """
        Добавляет заметку в бд.

        Параметры:
            title (str): Заголовок заметки
            content (str): Содержимое заметки
        """
        self.cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)",
                            (title, content))
        self.connection.commit()

    def get_all_notes(self):
        """
        Получает все заметки из бд.

        Возвращает:
            list: список всех заметок.
        """
        self.cursor.execute("SELECT * FROM notes")
        return self.cursor.fetchall()

    def search_notes(self, keyword):
        """
        Получает заметки из бд на основе ключевого слова.

        Параметры:
            keyword (str): Ключевое слово для поиска.

        Возвращает:
            list: список соответствующих заметок.
        """
        self.cursor.execute("""SELECT * FROM notes
                                     WHERE title LIKE ? OR content LIKE ?""",
                            '%' + keyword + '%', '%' + keyword + '%')
        return self.cursor.fetchall()

    def delete_note(self, note_id):
        """
        Удаляет заметку по id.

        Параметры:
            note_id (int): ID заметки.
        """
        self.cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
        self.connection.commit()

    def get_note_content_by_title(self, title):
        """
        Получает содержимое заметки из бд по заголовку.

        Параметры:
            title (str): Заголовок заметки.

        Возвращает:
            str: Содержимое заметки.
        """
        self.cursor.execute("SELECT content FROM notes WHERE title=?",
                            (title,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def get_note_id_by_title(self, title):
        """
        Получает ID заметки из бд по заголовку.

        Параметры:
            title (str): Заголовок заметки.

        Возвращает:
            int: ID заметки.
        """
        self.cursor.execute("SELECT id FROM notes WHERE title=?", (title,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def __del__(self):
        """Закрывает соединение с бд когда объект удален"""
        self.connection.close()
