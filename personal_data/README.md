# PROJECT: Personal data

AUTHOR: Matthew Allen

## TASKS

### 0. Regex-ing - `main.py`, `filtered_logger.py`

Function called `filter_datum` that returns the log message obfuscated:

* Arguments:
  * `fields`: a list of strings representing all fields to obfuscate
  * `redaction`: a string representing by what the field will be obfuscated
  * `message`: a string representing the log line
  * `separator`: a string representing by which character is separating all fields in the log line (`message`)
* The function should use a regex to replace occurrences of certain field values.
* `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.

### 1. Log formatter - `filtered_logger.py`

Using code copied from `filtered_logger.py`, update the class to accept a list of strings `fields` constructor argument.

Implement the `format` method to filter values in incoming log records using `filter_datum`.  Values for fields in `fields` should be filtered.

It does not extrapolate `FORMAT` manually.  The `format` method should be less than 5 lines long.

### 2. Create logger - `main.py`, `filtered_logger.py`

This task uses `user_data.csv`.

Implements a `get_logger` function that takes no arguments and returns a `logging.Logger` object.

The logger is named `"user_data"` and only logs up to the `logging.INFO` level.  It does not propagate messages to other loggers.  It has a `StreamHandler` with `RedactingFormatter` as formatter.

A tuple `PII_FIELDS` at the root of the module contains fields from `user_data.csv` that are considered PII.  `PII_FILEDS` only contains 5 fields, including information that must be hidden.  It is used to parameterize the formatter.

### 3. Connect to secure database - `main.sql`, `main.py`, `filtered_logger.py`

Connects to a secure `holberton` database to read a `users` table.  The database is protected by a username and password that are set as environment variables on the server named `PERSONAL_DATA_DB_USERNAME` (with the default as "root"), `PERSONAL_DATA_DB_PASSWORD` (with the default set as an empty string) and `PERSONAL_DATA_DB_HOST` (with the default as "localhost").

The database name is stored in `PERSONAL_DATA_DB_NAME`.

The `get_db` function returns a connector to the database (`mysql.connector.connection.MySQLConnection` object).

* Uses the `os` module to obtain credentials form the environment
* Uses the module `mysql-connector-python` to connect to the MySQL database (`pip3 install mysql-connector-python`)

### 4. Read and filter data - `main.sql`, `filtered_logger.py`

A `main` function that takes no arguments and returns nothing.

It obtains a database connection using `get_db` and retrieve all rows in the `users` table and display each row under a filtered format.

Filtered fields:

* name
* email
* phone
* ssn
* password

Only the `main` function runs when the module is executed.

### 5. Encrypting passwords - `main.py`, `encrypt_password.py`

A `hash_password` function that expects one string argument name `password` and returns a salted, hashed password, which is a byte string.

Uses the `bcrypt` package to perfrom the hashing (with `hashpw`).

### 6. Check valid password - `main.py`, `encrypt_password.py`

An `is_valid` function that expects 2 arguments and returns a boolean.

Arguments:

* `hashed_password`: `bytes` type
* `password`: string type

Uses `bcrypt` to validate that the provided password matches the hashed password.
