import os

# ---------------------------------------------------------
# НОВЫЕ ФУНКЦИИ ИЗ ДОМАШНЕГО ЗАДАНИЯ (0.0.4 - 0.0.5)
# ---------------------------------------------------------

def show_message(message: str):
    """
    Информирует пользователя о результатах (удаление, редактирование, добавление).
    """
    print(f"\n[СИСТЕМА]: {message}")
    input("Нажмите Enter, чтобы продолжить...")


def show_collection(collection: list):
    """
    Принимает список и форматированно выводит его в консоль.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана для красоты
    print("=" * 40)
    print("        СПИСОК ВАШИХ ЗАМЕТОК")
    print("=" * 40)
    
    if not collection:
        print("  У вас пока нет заметок. Добавьте первую!")
    else:
        for index, note in enumerate(collection, start=1):
            print(f" {index}. {note}")
            
    print("=" * 40)


# ---------------------------------------------------------
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ (ЛОГИКА ПРИЛОЖЕНИЯ)
# ---------------------------------------------------------

def add_note(collection: list):
    note = input("Введите текст новой заметки: ").strip()
    if note:
        collection.append(note)
        show_message("Заметка успешно ДОБАВЛЕНА.")
    else:
        show_message("Ошибка: Заметка не может быть пустой.")


def delete_note(collection: list):
    show_collection(collection)
    if not collection:
        return
    
    try:
        index = int(input("Введите номер заметки для УДАЛЕНИЯ: ")) - 1
        if 0 <= index < len(collection):
            deleted_note = collection.pop(index)
            show_message(f"Заметка '{deleted_note}' успешно УДАЛЕНА.")
        else:
            show_message("Ошибка: Заметки с таким номером не существует.")
    except ValueError:
        show_message("Ошибка: Пожалуйста, введите число.")


def edit_note(collection: list):
    show_collection(collection)
    if not collection:
        return
    
    try:
        index = int(input("Введите номер заметки для РЕДАКТИРОВАНИЯ: ")) - 1
        if 0 <= index < len(collection):
            new_text = input("Введите новый текст заметки: ").strip()
            if new_text:
                collection[index] = new_text
                show_message("Заметка успешно ИЗМЕНЕНА.")
            else:
                show_message("Ошибка: Текст не может быть пустым.")
        else:
            show_message("Ошибка: Заметки с таким номером не существует.")
    except ValueError:
        show_message("Ошибка: Пожалуйста, введите число.")


# ---------------------------------------------------------
# ГЛАВНЫЙ ЦИКЛ ПРИЛОЖЕНИЯ
# ---------------------------------------------------------

def main():
    # Наш список, который будет хранить заметки в памяти
    notes_collection = []
    
    # Тестовые данные для быстрой проверки (можно удалить)
    notes_collection.append("Купить хлеб")
    notes_collection.append("Выучить Python")

    while True:
        show_collection(notes_collection)
        print("МЕНЮ:")
        print("1. Добавить заметку")
        print("2. Удалить заметку")
        print("3. Редактировать заметку")
        print("4. Выход")
        
        choice = input("Выберите действие (1-4): ").strip()
        
        # Использование match-case по заданию
        match choice:
            case "1":
                add_note(notes_collection)
            case "2":
                delete_note(notes_collection)
            case "3":
                edit_note(notes_collection)
            case "4":
                print("\nДо встречи! Программа завершена.")
                break
            case _:  # Аналог else
                show_message("Ошибка: Неверный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
    main()
