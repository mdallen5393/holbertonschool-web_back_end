# PROJECT: Basic authentication

AUTHOR: Matthew Allen

## TASKS

### 0. Simple-basic-API

`archive.zip` contains a simple API with one model: `User`.  Storage of these users is done via a serialization/deserialization in files.

In this task, a simple servier is set up and started in order to host the API.

### 1. Error handler: Unauthorized - `api/v1/app.py`, `api/v1/views/index.py`

Adds an error handler for the `401` unauthorized request status code.  The response is:

* a JSON: `{"error": "Unauthorized"}`
* status code `401`
* uses `jsonify` from Flask

For testing, a new endpoint is added in `api/v1/views/index.py`:

* Route: `GET /api/v1/unauthorized`
* This endpoint raises a 401 error by using `abort`

By calling `abort(401)`, the error handler for 401 is executed.

### 2. Error handler: Forbidden - `api/v1/app.py`, `api/v1/views/index.py`

Adds an error handler for the `403` forbidden status code.  The response is:

* a JSON: `{"error": "Forbidden"}
* a status code `403`
* using `jsonify` from Flask

For testing, a new endpoint is added in `api/v1/views/index.py`:

* Route: `GET /api/v1/forbidden`
* This endpoint raises a 403 error by using `abort`

By calling `abort(403)`, the error handler for 403 will be executed.

### 3. Auth class - `api/v1/auth`, `api/v1/auth/__init__.py`, `api/v1/auth/auth.py`

A class `Auth` to manage the API authentication.

* located in the file `api/v1/auth/auth.py`
* imports `request` from `flask`
* contains a public method `require_auth` that returns `False` - `path` and `excluded_paths` to be used later.
* contains a public method `authorization_header` that returns `None` - `request` will be the Flask request object.
* contains a public method `current_user` that returns `None` - `request` will be the Flask request object.

This class is the template for all authentication systems that will be implemented.

### 4. Define which routes don't need authentication - `api/v1/auth/auth.py`

Updates `require_auth` in `Auth` that returns `True` if the `path` is not in the list of strings `excluded_paths`.

* Returns `True` if `path` is `None`
* Returns `True` if `excluded_paths` is `None` or empty
* Returns `False` if `path` is in `excluded_paths`
* Assumes `excluded_paths` contains string path always ending by a `/`
* This is slash tolerant: `path=/api/v1/status` and `path=/api/v1/status/` must be returned `False` if `excluded_paths` contains `/api/v1/status/`

### 5. Request validation! - `api/v1/app.py`, `api/v1/auth/auth.py`

This task validates all requests to secure the API.

Updates the method `authorization_header` in `api/v1/auth/auth.py`:

* If `request` is `None`, returns `None`
* If `request` doesn't contain the header key `Authorization`, returns `None`
* Otherwise, returns the value of the header request `Authorization`

Updates the file `api/v1/app.py`:

* Contains a variable `auth` initialized to `None` after the `CORS` definition
* Based on the environment variable `AUTH_TYPE`, loads and assigns the right instance of authentication to `auth`
  * if `auth`:
    * imports `Auth` from `api.v1.auth.auth`
    * creates an instance of `Auth` and assigns it to the variable `auth`

Now the request is filtered using the Flask method `before_request`

* Adds a method in `api/v1/app.py` to handler `before_request`
  * if `auth` is `None`, does nothing
  * if `request.path` is not part of this list `['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']`, does nothing; uses the method `require_auth` from the `auth` instance
  * if `auth.authorization_header(request)` returns `None`, raises the error `401`; uses `abort`
  * if `auth.current_user(request)` returns `None`, raises the error `403`; uses `abort`

### 6. Basic auth - `api/v1/app.py`, `api/v1/auth/basic_auth.py`

Defines the empty class `BasicAuth` that inherits from `Auth`.

Updates `api/v1/app.py` for using `BasicAuth` instead of `Auth` depending on the value of the environment variable `AUTH_TYPE`, if `AUTH_TYPE` is equal to `basic_auth`:

* imports `BasicAuth` from `api.v1.auth.basic_auth`
* creates an instance of `BasicAuth` and assigns it to the variable `auth`

Otherwise, keeps the previous mechanism with `auth` an instance of `Auth`.

### 7. Basic - Base64 part - `api/v1/auth/basic_auth.py`

Adds the method `extract_base64_authorization_header` in the `BasicAuth` class that returns the Base64 part of the `Authorization` header for a Basic Authorization:

* Returns `None` if `authorization_header` is `None`
* Returns `None` if `authorization_header` is not a string
* Returns `None` if `authorization_header` doesn't start by `Basic` (with a space at the end)
* Otherwise, return the value after `Basic` (after the space)
* Assumes `authorization_header` contains only one `Basic`

### 8. Basic - Base64 decode - `api/v1/auth/basic_auth.py`

Adds the method `def decode_base64_authorization_header` in the class `BasicAuth` that returns the decoded value of a Base64 string `base64_authorization_header`:

* Returns `None` if `base64_authorization_header` is `None`
* Returns `None` if `base64_authorization_header` is not a string
* Returns `None` if `base64_authorization_header` is not a valid Base64; uses `try/except`
* Otherwise, returns the decoded value as UTF8 string; uses `decode('utf-8')

### 9. Basic - User credentials - `api/v1/auth/basic_auth.py`

Adds the method `extract_user_credentials` in the class `BasicAuth` that returns the user email and password from the Base64 decoded value.

* This method returns 2 values
* Returns `None, None` if `decoded_base64_authorization_header` is `None`
* Returns `None, None` if `decoded_base64_authorization_header` is not a string
* Returns `None, None` if `decoded_base64_authorization_header` doesn't contain `:`
* Otherwise, returns the user email and user password - these 2 values are separated by a `:`
* Assumes `decoded_base64_authorization_header` will contain only one `:`

### 10. Basic - User object - `api/v1/auth/basic_auth.py`

Adds the method `user_object_from_credentials` in the class `BasicAuth` that returns the `User` instance based on his email and password.

* Returns `None` if `user_email` is `None` or not a string
* Returns `None` if `user_pwd` is `None` or not a string
* Returns `None` if the database (file) doesn't contain any `User` instance with email equal to `user_email`; uses the class method `search` of the `User` to lookup the list of users based on their email.
* Returns `None` if `user_pwd` is not the password of the `User` instance found; uses the method `is_valid_password` of `User`
* Otherwise, returns the `User` instance

### 11. Basic - Overload current_user - and BOOM! - `api/v1/auth/basic_auth.py`

Adds the method `current_user` in the class `BasicAuth` that overloads `Auth` and retrieves the `User` instance for a request:

* Uses `authorization_header`
* Uses `extract_base64_authorization_header`
* Uses `decode_base64_authorization_header`
* Uses `extract_user_credentials`
* Uses `user_object_from_credentials`

With this addition, the API is fully protected by a Basic Authentication.
