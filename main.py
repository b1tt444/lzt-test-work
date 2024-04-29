import tkinter as tk
from add_note_tab import AddNoteTab
from manage_notes_tab import ManageNotesTab


class NoteManagerApp(tk.Tk):
    """Main класс приложения"""

    def __init__(self):
        """Инициализация класса"""
        super().__init__()
        self.title("Note Manager")

        #Создание виджета для вкладок
        self.notebook = tk.ttk.Notebook(self)

        #Создание экземпляра класса
        self.add_note_tab = AddNoteTab(self.notebook)
        self.manage_notes_tab = ManageNotesTab(self.notebook)

        #Добавление вкладок
        self.notebook.add(self.add_note_tab, text="Добавить Заметку")
        self.notebook.add(self.manage_notes_tab, text="Управлять Заметками")

        self.notebook.pack(expand=True, fill="both")


if __name__ == "__main__":
    #Создание экземпляра класа и запуск цикла Tkinter
    app = NoteManagerApp()
    app.mainloop()
