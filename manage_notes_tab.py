import tkinter as tk
import tkinter.ttk as ttk
from database import Database
from tkinter import messagebox


class ManageNotesTab(tk.Frame):
    """Класс для управления заметками в отдельной вкладке интерфейса"""

    def __init__(self, master):
        """
        Инициализация вкладки управления заметками.

        master: Master widget
        """
        super().__init__(master)
        self.db = Database()

        #Виджеты
        self.search_label = ttk.Label(self, text="Поиск:")
        self.search_entry = ttk.Entry(self)
        self.search_button = ttk.Button(self, text="Найти",
                                        command=self.search_notes)
        self.notes_listbox = tk.Listbox(self)
        self.view_note_text = tk.Text(self, height=10, wrap="word",
                                      state="disabled")
        self.delete_button = ttk.Button(self, text="Удалить Заметку",
                                        command=self.delete_note)

        #Расположение в сетке
        self.search_label.grid(row=0, column=0, sticky="w")
        self.search_entry.grid(row=0, column=1, sticky="ew", padx=5)
        self.search_button.grid(row=0, column=2, padx=5)
        self.notes_listbox.grid(row=1, column=0, columnspan=3,
                                sticky="nsew", padx=5, pady=10)
        self.view_note_text.grid(row=2, column=0, columnspan=3,
                                 sticky="nsew", padx=5, pady=10)
        self.delete_button.grid(row=3, column=0, columnspan=3, pady=10)

        #Присваивание событий
        self.notes_listbox.bind("<<ListboxSelect>>", self.display_note)
        self.load_notes()

    def load_notes(self):
        """Загрузка всех заметок"""
        self.notes_listbox.delete(0, tk.END)
        notes = self.db.get_all_notes()
        for note in notes:
            self.notes_listbox.insert(tk.END, note[1])

    def search_notes(self):
        """Поиск заметок по ключевому слову."""
        keyword = self.search_entry.get()
        self.notes_listbox.delete(0, tk.END)
        if keyword:
            notes = self.db.search_notes(keyword)
            for note in notes:
                self.notes_listbox.insert(tk.END, note[1])
        else:
            self.load_notes()

    def display_note(self, event):
        """Показывает содержимое выбраной заметку."""
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            note_title = self.notes_listbox.get(selected_index)
            note_content = self.db.get_note_content_by_title(note_title)
            self.view_note_text.config(state="normal")
            self.view_note_text.delete("1.0", tk.END)
            self.view_note_text.insert(tk.END, note_content)
            self.view_note_text.config(state="disabled")
        else:
            # If no item is selected, clear the view note text
            self.view_note_text.config(state="normal")
            self.view_note_text.delete("1.0", tk.END)
            self.view_note_text.config(state="disabled")

    def delete_note(self):
        """Удаляет выбраную заметку."""
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            note_title = self.notes_listbox.get(selected_index)
            note_id = self.db.get_note_id_by_title(note_title)
            self.db.delete_note(note_id)
            self.load_notes()
            self.view_note_text.config(state="normal")
            self.view_note_text.delete("1.0", tk.END)
            self.view_note_text.config(state="disabled")
            messagebox.showinfo("Успех!", "Заметка удалена успешно!")
        else:
            messagebox.showwarning("Ошибка!", "Выберите заметку для удаления.")
