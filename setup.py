from core.configreader import DataBaseConfig
from core.utils.funcs import input

print(r"""----------------------------------------------------
                                _               
                               | |              
   ___ _ __ ___  ___   ___  ___| |_ _   _ _ __  
  / __| '_ ` _ \/ __| / __|/ _ \ __| | | | '_ \ 
 | (__| | | | | \__ \ \__ \  __/ |_| |_| | |_) |
  \___|_| |_| |_|___/ |___/\___|\__|\__,_| .__/ 
                                         | |    
                                         |_|    
----------------------------------------------------""")
print("""Select mode of installation:
         - [1] Quick install
         - [2] Custom install
>>> """, end='')
a = input()
while a not in ('1', '2'):
    print('Invalid choice!')
    a = input('>>> ')
if a == '1':
    """
    Sets config.ini to default values, and sets active_plugins=[], and active_template=test
    """

    print("Installing quick version...\n")
    with open('config.ini', 'w+') as f:
        f.write(f'''[DATABASE]
Driver = Sqlite
Path = subconf.sqlite3

[DEVELOPMENT]
Debug = off
HashTime = 12
Host = 127.0.0.1
Port = 5000''')
        database_config = DataBaseConfig()

        plugin_config = database_config.create_and_parse_config(
            "active_plugins", [])

        template_config = database_config.create_config(
            "active_template", "test")
elif a == '2':
    """
    Asks for all options in config.ini also allows to set active_plugins, active_template
    """

    print("Custom installation, press enter to use default of option\n\n")
    print("[DATABASE] Category:")
    db = input('Database type (Sqlite): ', 'Sqlite')
    if db.lower() == "mysql":
        host = input('Host (localhost): ', 'localhost')
        port = input('Port (8889): ', 8889)
        name = input('Name (cms): ', 'cms')
        user_login = input('Username (admin): ', 'admin')
        user_password = input('Password (admin): ', 'admin')
    else:
        path = input('Path to database (db.db, none for mysql): ', 'db.db')
    print("[DEVELOPMENT] Category:")
    debug = input('Debug (off): ', 'off')
    hash_time = input("Hash complexity (12): ", 12)
    web_host = input('Flask host (127.0.0.1): ', '127.0.0.1')
    web_port = input('Flask port (5000): ', 5000)
    if db.lower() == "mysql":
        with open('config.ini', 'w+') as f:
            f.write(f'''[DATABASE]
Driver = MySql
Host = {host}
Name = {name}
User = {user_login}
Password = {user_password}
Port = {port}

[DEVELOPMENT]
Debug = {debug}
HashTime = {hash_time}
Host = {web_host}
Port = {web_port}''')
    else:
        with open('config.ini', 'w+') as f:
            f.write(f'''[DATABASE]
Driver = Sqlite
Path = {path}

[DEVELOPMENT]
Debug = {debug}
HashTime = {hash_time}
Host = {web_host}
Port = {web_port}''')
    database_config = DataBaseConfig()

    plugin_config = database_config.create_and_parse_config(
        "active_plugins", dict(input('Active plugins ([])', dict())))

    template_config = database_config.create_config(
        "active_template", input('Active template (test): ', 'test'))

print("Installed!")
print("Now run main.py to start webserver!")
