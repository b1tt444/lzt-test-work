# Менеджер заметок

Это приложение представляет собой простой менеджер заметок, написанный на Python.

## Запуск

Для запуска приложения необходим Python 3.10.

### Установка библиотек

Перед запуском приложения убедитесь, что у вас установлены необходимые библиотеки. Выполните следующую команду:

```bash
pip install -r requirements.txt
```
### Запуск

После установки библиотек можно запустить приложение. Для этого выполните:

```
python main.py
```
### Использование

После запуска приложения вы сможете создавать, просматривать, редактировать и удалять заметки.

### Вкладка Добавить Заметку

Ввода заголовка и содержания и нажатие кнопки "Добавить Заметку" добавляет Заметку

### Вкладка Управлять Заметками

- После нажатия кнопки "Найти" с пустой строкой поиск будут найдены все заметки

- После нажатия кнопки "Найти" с заполненой строкой поиск будут найдены все заметки которые имеют строку поиск в заголовке или содержаниию

- После выбора заголовка в списке будет отображено содержание заметки

- После выбора заголовка в списке и нажатия кнопки "Удалить Заметку" будет удалена выбранная заметка