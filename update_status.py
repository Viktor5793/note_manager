# Создаем словарь для хранения информации о заметке
note = {
    "username": "Виктор",
    "content": "Прогулка по парку.",
    "status": "Активна",
    "created_date": "10-01-2025",
    "issue_date": "11-01-2025",
    "titles": ["Прогуляться по парку", "Покататься на роликах", "Зайти в кафе", "Вернуться домой"]
}

# Запрос статуса заметки
status_options = ["Активна", "Выполнена", "В работе", "Отложена", "Забыта"]

# Запрос на изменение статуса заметки и проверка корректности ввода
print(f"Выберите новый статус заметки: {', '.join(status_options)}")
for option, value in enumerate(status_options, start=1):
    print(f"{option} : {value}")
new_status = None
while new_status not in status_options:
    print("Ваш выбор: ", end="")
    new_status = input("Введите номер статуса (1-5): ")
    if new_status.isnumeric():
        try:
            new_status = int(new_status) - 1  # Исправлена проверка индекса
            if 0 <= new_status < len(status_options):
                note["status"] = status_options[new_status]
                print("Статус успешно изменен.")
                break
            else:
                print("Некорректный выбор. Пожалуйста введите число от 1 до 5.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите только число.")
    else:
        print("Некорректный ввод. Пожалуйста, введите только число.")

# Выводим собранные данные
print("Собранная информация о заметке:",
      f"Имя пользователя: {note['username']}",
      f"Описание заметки: {note['content']}",
      f"Статус заметки: {note['status']}",
      f"Дата создания заметки: {note['created_date'][0:5]}",
      f"Дата истечения заметки: {note['issue_date'][0:5]}",
      sep='\n'
      )

# Выводим список всех добавленных заголовков
print("Заголовки заметки:")
for title in note["titles"]:
    print("-", title)