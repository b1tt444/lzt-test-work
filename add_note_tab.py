import tkinter as tk
import tkinter.ttk as ttk
from database import Database
from tkinter import messagebox


class AddNoteTab(tk.Frame):
    """Класс для добавления заметок в отдельной вкладке интерфейса"""
    def __init__(self, master):
        """Инициализация класса
        :param master: Master widget
        """
        super().__init__(master)
        self.db = Database()

        # Константы для сообщений
        self.SUCCESS_MESSAGE = "Заметка добавлена успешно!"
        self.UNIQUE_TITLE_ERROR = "Заголовок заметки должен быть уникальным."
        self.INPUT_ERROR = "Пожалуйста, введите текст и заголовок заметки."

        #Виджеты
        self.title_label = ttk.Label(self, text="Заголовок:")
        self.title_entry = ttk.Entry(self)
        self.content_label = ttk.Label(self, text="Содержание:")
        self.content_entry = tk.Text(self)
        self.add_button = ttk.Button(self, text="Добавить Заметку",
                                     command=self.add_note)

        #Расположение в сетке
        self.title_label.grid(row=0, column=0, sticky="w")
        self.title_entry.grid(row=0, column=1, sticky="ew", padx=5)
        self.content_label.grid(row=1, column=0, sticky="w")
        self.content_entry.grid(row=1, column=1, sticky="ew", padx=5)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_note(self):
        """Добавление новой вкладки"""
        title = self.title_entry.get()
        content = self.content_entry.get("1.0", tk.END)
        if title and content.strip():
            if self.db.get_note_id_by_title(title) is None:
                self.db.add_note(title, content)
                self.title_entry.delete(0, tk.END)
                self.content_entry.delete("1.0", tk.END)
                messagebox.showinfo("Успех!", self.SUCCESS_MESSAGE)
            else:
                messagebox.showwarning("Ошибка!", self.UNIQUE_TITLE_ERROR)
        else:
            messagebox.showwarning("Ошибка ввода!", self.INPUT_ERROR)
