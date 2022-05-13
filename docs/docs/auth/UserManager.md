# Учетная запись пользователей - UserManagement

Аккаунт пользователей важен для безопасности и управлением над WEBCMS.

**UserManagement** - выполняет работу по управлению учетными записями пользователй.

В него входят функции:

- [Создание пользователя.](#_1)
- [Создание супер пользователя.](#_2)
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

    from core.managers.auth.user import UserManagement

    # Если вы вызываете UserManagement с директории core:
    from .managers.auth.user import UserManagement

    # Если вы вызываете UserManagement с директории managers:
    from .auth.user import UserManagement

так-же необходимо объявить его в переменную. Если вам нужен доступ к UserManagement с класса. То можно объявить переменную класса.

Метод для создании нового пользователя:

***UserManagement.create_user(username: str, email: str, password: str, group: int = None)***

Аргументы:

- **username: string** - Новая имя пользователя
- **email: string** - Почта нового пользователя
- **password: string** - Пароль нового пользователя. UserManagement автоматически зашифрует пароль в bcrypt
- **group: int (по умолчанию: None)** - ID идентификатор группы которой пользователь будет унаследован. Если не указать или указать в значение **None** то пользователь не будет наследоваться никакой группы.

Возвращает:

- **True (bool)** - Пользователь успешно создан.
- **False (bool)** - Не получилось создать нового пользователя.

**Примеры**

    from core.managers.auth.user import UserManagement
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

    from core.managers.auth.user import UserManagement
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

### Создание супер пользователя

При необходимсти. Необходимо создать супер пользователя у которого есть * в **Permissions**.

**UserManagement** обладает таким методом как `create_super_user()` при помощи которого, можно быстро создать супер пользователя.
У которого будут все права.

Для начало необходимо импортировать **UserManagement**

    from core.managers.auth.user import UserManagement

    # Если вы вызываете UserManagement с директории core:
    from .managers.auth.user import UserManagement

    # Если вы вызываете UserManagement с директории managers:
    from .auth.user import UserManagement

Так-же необходимо объявить его в переменную. Если вам нужен доступ к UserManagement с класса. То можно объявить переменную класса.

Метод для создании нового пользователя:

***UserManagement.create_superuser(username: str, email: str, password: str)***

Аргументы:

- **username: string** - Имя пользователя нового супер пользователя
- **email: string** - Почта нового супер пользователя
- **password: string** - Пароль нового супер пользователя, в последствии он будет автоматически зашифрован **UserManagement**

Возвращает:

- **True: boolean** - Пользователь успешно создан и к нему присвоена * в **Permissions**.
- **False: boolean** - Не удалось создать пользователя.
- **None** - Не удалось создать пользователя.

Примеры:

    from core.managers.auth.user import UserManagement

    # Объявляем класс UserManagement
    user_manager = UserManagement()
    
    # Создаем супер пользователя методом UserManagement.create_super_user()
    create_user = user_manager.create_super_user(username="Zahcoder34", email="example@gmail.com", password="qwerty123")

Пример с классом:

    from core.managers.auth.user import UserManagement
    from core.managers.logging import Log

    class ClassA:
        # Вызов при инициализации класса
        def __init__(self):

            # Объявляем класс UserManagement
            self.user_manager = UserManagement()
        
        def some_func(self):
            # Создаем пользователя
            create_user = self.user_manager.create_super_user("Zahcoder34", "example@gmail.com", "qwerty123")

            return create_user
    
    # Тестируем
    class_a = ClassA()

    # Выводим в консоль результат. Как правило если пользователь создан успешно, ответ положительный. Если нет = None
    Log(class_a.some_func(), 0)
