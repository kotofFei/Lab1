groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [2, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 2, 5]
    },
    {
        "name": "Афанасий",
        "surname": "Крылов",
        "exams": ["Математика", "ИТИП", "ИСИС"],
        "marks": [4, 5, 3]
    },
    {
        "name": "Карамнов",
        "surname": "Даниил",
        "exams": ["Обществознание", "Искусство", "Пение"],
        "marks": [5, 5, 5]
    }
]

def print_students(students):
    """Функция выводит информацию о студентах."""
    for student in students:
        print(f"{student['name']} {student['surname']}")
        print(f"  Экзамены: {', '.join(student['exams'])}")
        print(f"  Оценки: {student['marks']}")
        avg = sum(student['marks']) / len(student['marks'])
        print(f"  Средний балл: {avg:.2f}\n")

def filter_by_avg(students, min_avg):
    """Фильтрует студентов по минимальному среднему баллу."""
    return [s for s in students if sum(s["marks"]) / len(s["marks"]) >= min_avg]

# Основная программа
try:
    threshold = float(input("Введите минимальный средний балл для фильтрации: "))
    filtered_students = filter_by_avg(groupmates, threshold)

    if filtered_students:
        print(f"\nСтуденты со средним баллом выше или равным {threshold}:")
        print_students(filtered_students)
    else:
        print("\nНет студентов с таким средним баллом.")
except ValueError:
    print("Ошибка: введите число!")
