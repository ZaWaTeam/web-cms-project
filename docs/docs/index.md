# Добро пожаловать в WEBCMS DOCS

Данная документация содержит информацию о функциональности ядра WEBCMS

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Иерархия и дерево проекта

    core/
        managers/   # Директория отвечающий за управление функциональности
            ...
        loaders/    # Загрузчик. Подгружает все необходимые файлы.
            ...
        database/
            models/    # Модели базы данных
                ...
            connect.py  # Файл отвечающий за подключения к базе данных
            crud.py  # Контроллер запросов в базу данных. Здесь происходят все запросы