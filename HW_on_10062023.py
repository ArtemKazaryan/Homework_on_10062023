
# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ  !!!!!!

# Домашняя работа на 10.06.2023.

# Задание

# Создание системы управления задачами:
# 1) Создайте класс TaskManager с атрибутами для хранения задач и информации о пользователях.
# 2) Реализуйте методы в классе TaskManager, чтобы добавлять задачи, назначать задачи пользователям,
# помечать задачи как выполненные и отображать сведения о задачах.
# 3) Создайте класс User с атрибутами для информации о пользователе, такой как имя,
# адрес электронной почты и роль (например, администратор или обычный пользователь).
# 4) Реализуйте методы в классе User для создания учетных записей пользователей,
# обновления информации о пользователях и просмотра назначенных задач.
# 5) Примените соответствующие методы инкапсуляции для защиты конфиденциальной пользовательской информации
# и гарантируйте, что операции, связанные с задачами, могут выполняться только авторизованными пользователями.
# 6) Используйте наследование для создания специализированных пользовательских ролей с различными разрешениями
# и возможностями (например, администраторы могут назначать задачи, обычные пользователи могут
# только просматривать задачи).
# 7) Внедрите проверку данных, чтобы гарантировать, что назначения задач и пользовательские операции выполняются
# с допустимыми входными данными и ограничениями.

# Решение:
class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.assigned_user = None
        self.completed = False

    def assign_user(self, user):
        self.assigned_user = user

    def mark_complete(self):
        self.completed = True

    def get_task_info(self):
        print()
        return f"Наименование задачи: {self.name}\nОписание: {self.description}\nКрайний срок: {self.deadline}\n" \
               f"Назначена для: {self.assigned_user}\nВыполнена: {self.completed}"

class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def update_info(self, name, email):
        self.name = name
        self.email = email

    def view_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task.get_task_info())
        else:
            print("Нет назначенных задач")

class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email, "Admin")

    def assign_task(self, task, name):
        task.assign_user(name)
        user.tasks.append(task)

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.users = []

    def add_task(self, task):
        self.tasks.append(task)
        return self.tasks

    def add_user(self, user):
        self.users.append(user)
        return self.users

    def authenticate_user(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def view_all_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task.get_task_info())
        else:
            print("Нет доступных задач")

    def view_assigned_tasks(self, user):
        user.view_tasks()

# Пример использования
tm = TaskManager()
admin = Admin("Иван", "Ivan@gmail.com")
user1 = User("Аня", "anna@mail.ru", "User")
user2 = User("Борис", "boris@yandex.ru", "User")

tm.add_user(admin)
tm.add_user(user1)
tm.add_user(user2)

task1 = Task("Задача 1", "Выполнить первое ДЗ №1", "10-06-2023")
task2 = Task("Задача 2", "Выполнить второе ДЗ №2", "11-06-2023")
task3 = Task("Задача 3", "Выгрузить ДЗ №1 на Гитхаб", "10-06-2023")
task4 = Task("Задача 4", "Выгрузить ДЗ №2 на Гитхаб", "11-06-2023")

task1.assign_user("Аня")
task2.assign_user("Борис")
task3.assign_user("Аня")
task4.assign_user("Борис")

tm.add_task(task1)
tm.add_task(task2)
tm.add_task(task3)
tm.add_task(task4)

tm.view_all_tasks()

