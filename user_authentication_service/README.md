# PROJECT: User authentication service

AUTHOR: Matthew Allen

## TASKS

### 0. User model - `user.py`

Creates a SQLAlchemy model named `User` for a database table named `users` by using the mapping declaration of SQLAlchemy.

The model has the following attributes:

* `id`, the integer primary key
* `email`, a non-nullable string
* `hashed_password`, a non-nullable string
* `session_id`, a nullable string
* `reset_token`, a nullable string

### 1. create user - `db.py`

Class with the `add_user` method implementation.

Note: `DB._session` is a private property and hence is never used outside the `DB` class.

The `add_user` method has two required string arguments: `email` and `hashed_password`, and returns a `User` object.  It saves the user to the database.

### 2. Find user - `db.py`

Implements the `DB.find_user_by` method, which takes in arbitrary keyword arguments and returns the first row found in the `users` table as filtered by the method's input arguments.

Ensures that SQLAlchemy's `NoResultFound` and `InvalidRequestError` are raised when no results are found, or when wrong query arguments are passed, respectively.

### 3. update user - `db.py`

Implements the `DB.update_user` method that takes as argument a required `user_id` integer and arbitrary keyword arguments, and returns `None`.

The method uses `find_user_by` to locate the user to update, then updates the user's attributes as passedin the method's arguments, then commits changes to the database.

If an argument that does not correspond to a user attribute is passed, raises a `ValueError`.

### 4. Hash password - `auth.py`

Defines a `_hash_password` method that takes in a `password` string argument and returns bytes.

The returned bytes is a salted hash of the input password, hashed with `bcrypt.hashpw`.

### 5. Register user - `auth.py`

Implements the `Auth.register_user` in the `Auth` class.

Note that `Auth._db` is a private property and is never used from outside the class.

`Auth.register_user` takes mandatory `email` and `password` string arguments and returns a `User` object.

If a user already exists with the passed email, raises a `ValueError` with the message `User <user's email> already exists`.

If not, the password is hashed with `_hash_password`, and the user is saved to the database using `self._db`.  The `User` object is then returned.

### 6. Basic Flask app - `app.py`

Sets up a basic Flask app.

Creates a Flask app that has a single `GET` route (`"/"`) and uses `flask.jsonify` to return a JSON payload of the form `{"message": "Bienvenue"}`.

Adds an `if __name__ == "__main__":` statement.

### 7. Register user - `app.py`

Implements the end-point to register a user.  Defines a `users` function that implements the `POST /users` route.

Imports the `Auth` object and instantiates it at the root of the module.

The end-point expects two form data fields: `"email"` and `"password"`.  If the user does not exist, the end-point registers it and responds with the following JSON payload: `{"email": "<registered email>", "message": "user created"}`.

If the user is already registered, catches the exception and returns a JSON payload of the form `{"message": "email already registered"}` and return a 400 status code.

This app only uses `AUTH`.  `DB` is a lower abstraction that is proxied by `Auth`.

### 8. Credentials validation - `auth.py`

Implements the `Auth.valid_login` method.  It expects `email` and `password` required arguments and returns a boolean.

Attempts to locate the user by email - if it exists, checks the password with `bcrypt.checkpw`.  If it matches, returns `True`.  In any other case, return `False`.

### 9. Generate UUIDs - `auth.py`

Implements a `_generate_uuid` function in the `auth` module.  The function returns a string representation of the new UUID.  Uses the `uuid` module.

Note that the method is private to the `auth` module and is not used outside of it.

### 10. Get session ID - `auth.py`

Implements the `Auth.create_session` method, which takes an `email` argument and returns the session ID as a string.

Method finds the user corresponding to the email, generates a new UUID and stores it in the database as the user's `session_id`, then returns the session ID.

Only public methods of `self._db` can be used.

### 11. Log in - `app.py`

Implements a `login` function to respond to the `POST /sessions` route.

The request is expected to contain form data with `"email"` and `"password"` fields.

If the login infomation is incorrect, uses `flask.abort` to respond with a 401 HTTP status.

Otherwise, creates the new session for hte user, stores the session ID as a cookie with key `"session_id"` on the response and returns a JSON payload of the form `{"email": "<user email>", "message": "logged in"}`.

### 12. Find user by session ID - `auth.py`

Implements the `Auth.get_user_from_session_id` method, which takes a single `session_id` string argument and returns the corresponding `User` or `None`.

If the session ID is `None` or no user is found, returns `None`.  Otherwise returns the corresponding user.

Only uses public methods of `self._db`.

### 13. Destroy session - `auth.py`

Implements `Auth.destroy_session`, which takes a single `user_id` integer argument and returns `None`.

The method updates the corresponding user's session ID to `None`.

Uses only public methods of `self._db`.

### 14. Log out - `app.py`

Implements a `logout` function to respond to the `DELETE /sessions` route.

The request is expected to contain the session ID as a cookie with key `"session_id"`.

Finds the user with the requested session ID.  If the user exists destroys the session and redirects the user to `GET /`.  If the user does not exist, responds with a 403 HTTP status.

### 15. User profile - `app.py`

Implements a `profile` function to respond to the `GET /profile` route.

The request is expected to contain a `session_id` cookie.  Uses it to find the user.  If the user exists, responds with a 200 HTTP status and the following JSON payload: `{"email": "<user email>"}`.

If the session ID is invalid or the user does not exist, responds with a 403 HTTP status.

### 16. Generate reset password token - `auth.py`

Implements the `Auth.get_reset_password_token` method, which takes an `email` string argument and returns a string.

Finds the user corresponding to the email.  If the user does not exist, raises a `ValueError` exception.  If it exists, generates a UUID and updates the user's `reset_token` database field.  Returns the token.

### 17. Get reset password token - `app.py`

Implements a `get_reset_password_token` function to respond to the `POST /reset_password` route.

The request is expected to contain form data with the `"email"` field.

If the email is not registered, responds with a 403 status code.  Otherwise, generates a token and responds with a 200 HTTP status and the following JSON payload: `{"email": "<user email>", "reset_token": "<reset token>"}`.

### 18. Update password - `auth.py`

Implements the `Auth.update_password` method, which takes `reset_token` string argument and a `password` string argument and returns `None`.

Uses the `reset_token` to find the corresponding user.  If it does not exist, raises a `ValueError` exception.

Otherwise, hashes the password and updates the user's `hashed_password` field with the new hashed password and the `reset_token` field to `None`.

### 19. Update password end-point - `app.py`

Implements the `update_password` function in the `app` module to respond to the `PUT /reset_password` route.

The request is expected to contain form data with fields `"email"`, `"reset_token"` and `"new_password"`.

Updates the password.  If the token is invalid, catches the exception and responds with a 403 HTTP code.

If the token is valid, results with a 200 HTTP code and the following JSON payload: `{"email": "<user email>", "message": "Password updated"}`.
