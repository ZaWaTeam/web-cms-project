# Учетная запись пользователей - UserManagement

Аккаунт пользователей важен для безопасности и управлением над WEBCMS.

**UserManagement** - выполняет работу по управлению учетными записями пользователй.

В него входят функции:

- Создание пользователя.
- Создание супер пользователя.
- Управление пользователем.
- Подробнее о каком то пользователе.
- Список пользователей которые зарегистрированы.
- Хранение информации о пользователе.
- Проверка заргистрирован ли пользователь.
- Аутентикация пользователя. Верификация пароля и логина.

## Документация по UserManagement

Простой пример по создании нового пользователя:

    from core.managers.user import UserManagement
    from core.logging import Log

    # Объявляем класс UserManagement
    user_manager = UserManagement()

    # Создаем пользователя методом UserManagement.create_user()
    create_user = user_manager.create_user(username="Zahcoder34", email="example@gmail.com", password="qwerty123", group=None)

    # Делаем проверку. Если пользователь создан успешно. То метод create_user() возвращает True. Если нет, то False
    if create_user:

        # Отображаем в консоль о том что наш пользователь создан успешно
        Log("Пользователь Zahcoder34 успешно создан!", 3)
        # В консоли: [success (timestamp)] Пользователь Zahcoder34 успешно создан!

***

### Создание нового пользователя (Регистрация)

**UserManagement** уже обладает функциональностью для создании пользователя. 

Для начало необходимо импортировать UserManagement

    from core.managers.users import UserManagement

так-же необходимо объявить его в переменную. Если вам нужен доступ к UserManagement с класса. То можно объявить переменную класса.

Метод для создании нового пользователя:

***UserManagement.create_user(username: str, email: str, password: str, group: str = None)***

Аргументы:

- **username: string** - Новая имя пользователя
- **email: string** - Почта нового пользователя
- **password: string** - Пароль нового пользователя. UserManagement автоматически зашифрует пароль в bcrypt
- **group: int (по умолчанию: None)** - ID идентификатор группы которой пользователь будет унаследован. Если не указать или указать в значение **None** то пользователь не будет наследоваться никакой группы.

Возвращает:

- **True (bool)** - Пользователь успешно создан.
- **False (bool)** - Не получилось создать нового пользователя.

**Примеры**

    from core.managers.user import UserManagement
    from core.logging import Log

    # Объявляем класс UserManagement
    user_manager = UserManagement()

    # Создаем пользователя методом UserManagement.create_user()
    create_user = user_manager.create_user(username="Zahcoder34", email="example@gmail.com", password="qwerty123", group=None)

    # Делаем проверку. Если пользователь создан успешно. То метод create_user() возвращает True. Если нет, то False
    if create_user:

        # Отображаем в консоль о том что наш пользователь создан успешно
        Log("Пользователь Zahcoder34 успешно создан!", 3)
        # В консоли: [success (timestamp)] Пользователь Zahcoder34 успешно создан!

Создание пользователя в классе

    from core.managers.user import UserManagement
    from core.logging import Log

    class ClassA:

        # Данная функция вызывается при инициализации класса
        def __init__(self):
            # Объявляем переменную пользователя
            self.user_manager = UserManagement()

        # Какая-то нужная функция
        def some_function(self):
            # Создание пользователя
            create_user = self.user_manager.create_user(username="Zahcoder34", email="example@gmail.com", password="qwerty123")
            
            # Делаем проверку создался ли пользователь.
            if create_user:
                # Отображаем в консоль о том что наш пользователь создан успешно
                return Log("Пользователь Zahcoder34 успешно создан!", 3)
    
    # Объявляем класс. После этого вызывается функция __init__()
    class_a = ClassA()

    # Вызываем функцию
    class_a.some_function()