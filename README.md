# https://python-webcms.readthedocs.io/en/latest/

# Structure
![scheme.drawio.svg](scheme.drawio.svg)

# Install deps + run tests
- `{python-executable} setup.py`

# Start Webserver
- for mac/linux: `python3 main.py`

- for windows `py main.py` or `python main.py`

- to get crashreport run `start.py`
### Project in development, so debug mode is active

***

## Config.ini template

**For Mysql Driver**
```editorconfig
[DATABASE]
Driver = MySql
Host = localhost
Name = CMSProj
User = root
Password = root
Port = 8889

[DEVELOPMENT]
Debug = on
Host = 127.0.0.1
Port = 5000
```
**For SQLite Driver**
```editorconfig
[DATABASE]
Driver = Sqlite
Path = /path/to/database

[DEVELOPMENT]
Debug = on
Host = 127.0.0.1
Port = 5000
```
