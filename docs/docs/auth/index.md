# Авторизация и учетные записи

В каждом CMS должны быть учетные записи. Аутентикация и авторизация.
WEBCMS не исключение. Данная функциональность все ещё в разработке.
Здесь будет предоставлена документация для разработки.

Какие функции должны быть и какие должны быть. Все будет здесь.

Данная функциональность будет разделена на 3 категории. 

- [**Учетная запись пользователей**](UserManager/). UserManagement, UserModel, UserAccount

- **Группы / Роли / Категории** - Группы это роли которых пользователи могут наследоваться. У каждой группы будут свои права. И пользователи которые состоят в группе имеют права которые имеет сама группа. **GroupManager** - управление группой

- **Права / доступ / разрешение** - У каждого плагина есть `manifest.json` а у самого WEBCMS есть в директории `core/core.json`. Там указаны все права которые могут быть записаны в базу данных. В БД они записываются в виде (Идентификатор или название пермишена, какой группе они наследуют или же какому пользователю). В БД можно сохранить только объявленные права в `manifest.json` или `core.json`. Вам следует изучить их если вас интересует разработка **PermissionsManager** - управление правами.