# PROJECT: Session authentication

AUTHOR: Matthew Allen

## TASKS

### 0. Et moi et moi et moi! - `api/v1/app.yp`, `api/v1/views/users.py`

This version (continuation from Basic Authentication project) implements a Basic authentication for giving you access to all user endpoints:

* GET /api/v1/users
* POST /api/v1/users
* GET /api/v1/users/<user_id>
* PUT /api/v1/users/<user_id>
* DELETE /api/v1/users/<user_id>

Adds the endpoint `GET /users/me` to retrieve the authenticated `User` object.

* Copies folder `models` and `api` from the previous project Basic authentication.
* Updates `@app.before_request` in `api/v1/app.py`:
  * Assign the result of `auth.current_user(request)` to `request.current_user`
* Updates method for the route `GET /api/v1/users/<user_id>` to `request.current_user`
  * If `<user_id>` is equal to `me` and `request.current_user` is `None`: `abort(404)`.
  * If `<user_id>` is equal to `me` and `request.current_user` is not `None`: return the authenticated `User` in a JSON response (like a normal case of `GET /api/v1/users/<user_id>` where `<user_id>` is a valid `User` ID)
  * Otherwise, keeps the same behavior

### 1. Empty session - `api/v1/auth/session_auth.py`, `api/v1/app.py`

Creates an empty class `SessionAuth` that inherits from `Auth`.

* validates if everything inherits correctly without any overloading
* validates the "switch" by using environment variables

Update `api/v1/app.py` for using `SessionAuth` instance for the variable `auth` depending on the value of the environment variable `AUTH_TYPE`.  If `AUTH_TYPE` is equal to `session_auth`:

* import `SessionAuth` from `api.v1.auth.session_auth`
* create an instance of `SessionAuth` and assign it to the variable `auth`

Otherwise, keeps the previous mechanism.

### 2. Create a session - `api/v1/auth/session_auth.py`

Updates `SessionAuth` class:

* Creates a class attribute `user_id_by_session_id` initialized by an empty directory
* Creates an instance method `def create_session(self, user_id: str = None) -> str:` that creates a Session ID for a `user_id`:

  * Returns `None` if `user_id` is `None`
  * Returns `None` if `user_id` is not a string
  * Otherwise:
    * Generates a Session ID using `uuid` module and `uuid4()` like `id` in `Base`
    * Uses this Session ID as key of the dictionary `user_id_by_session_id` - the value for this key must be `user_id`
    * Return the Session ID
  * The same `user_id` can have multiple Session ID - indeed, the `user_id` is the value in the dictionary `user_id_by_session_id`.

This defines an "in-memory" Session ID store.  Now a `User` id can be retrieved based on a Session ID.

### 3. User ID for Session ID - `api/v1/auth/session_auth.py`

Updates `SessionAuth` class:

Creates an instance method `def user_id_for_session_id(self, session_id: str = None) -> str:` that returns a `User` ID based on a Session ID:

* Returns `None` if `session_id` is `None`
* Returns `None` if `session_id` is not a string
* Returns the value (the User ID) for the key `session_id` in the dictionary `user_id_by_session_id`
* Uses `.get()` built-in for accessing a dictionary based on key

Now there are 2 methods for storing and retrieving a link between a `User` ID and a Session ID.

### 4. Session cookie - `api/v1/auth/auth.py`

Updates `api/v1/auth/auth.py` by adding the method `def session_cookie(self, request=None):` that returns a cookie value from a request:

* Returns `None` if `request` is `None`
* Returns the value of the cookie named `_my_session_id` from `request` - the name of the cookie must be defined by the environment variable `SESSION_NAME`
* Uses the `.get()` built-in for accessing the cookie in the request cookies dictionary
* Uses the environment variable `SESSION_NAME` to define the name of the cookie used for the Session 
ID

### 5. Before request - `api/v1/app.py`

Updates the `@app.before_request` method in `api/v1/app.py`:

* Add the URL path `/api/v1/auth_session/login/` in the list of excluded paths of the method `require_auth`; this route does not exist yet, but will be accessible outside authentication
* If `auth.authorization_header(requests)` and `auth.session_cookie(request)` return `None`, `abort(401)`

### 6. Use Session ID for identifying a User - `api/v1/auth/session_auth.py`

Updates `SessionAuth` class:

Creates an instance method `def current_user(self, request=None):` (overload) that returns a `User` instance based on a cookie value:

* Uses `self.session_cookie(...)` and `self.user_id_for_session_id(...)` to return the User ID based on the cookie `_my_session_id`
* By using this User ID, you will be able to retrieve a `User` instance from the database - you can use `User.get(...)` for retrieving a `User` from the database.

Now, you can get a User based on their session ID.

### 7. New view for Session Authentication - `api/v1/views/session_auth.py`, `api/v1/views/__init__.py`

Creates a new Flask view that handles all routes for the Session authentication.

In the file `api/v1/view/session_auth.py`, creates a route `POST /auth_session/login` (= `POST /api/v1/auth_session/login`):

* Slash tolerant (`/auth_session/login` == `/auth_session/login/`)
* Uses `request.form.get()` to retrieve `email` and `password` parameters
* If `email` is missing or empty, return the JSON `{ "error": "email mising" }` with the status code `400`
* If `password` is missing or empty, return the JSON `{ "error": "password missing" }` with the status code `400`
* Retrieve the `User` instance based on the `email` - you must use the class method `search` of `User` (same as the one user for the `BasicAuth`)
  * If no `User` found, return the JSON `{ "error": "no user found for this email" }` with the status code `404`
  * If the `password` is not the one of the `User` found, returns the JSON `{ "error": "wrong password" }` with the status code `401` - you must use `is_valid_password` from the `User` instance
  * Otherwise, creates a Session ID for the `User` ID:
    * Uses `from api.v1.app import auth` - WARNING: please import it only where you need it - not on top of the file (can generate circular import - and breaks first tasks of this project)
    * Uses `auth.create_session(...)` for creating a Session ID
    * Returns the dictionary representation of the `User`; uses `to_json()` method from User
    * Sets the cookie to the response - using the value of the environment variable `SESSION_NAME` as cookie name.

In the file `api/v1/views/__init__.py`, adds this new view at the end of the file.

### 8. Logout - `api/v1/auth/session_auth.py`, `api/v1/views/session_auth.py`

Updates the class `SessionAuth` by adding a new method `def destroy_session(self, request=None):` that deletes the user session/logout:

* If the `request` is equal to `None`, returns `False`
* If the `request` doesn't contain the Session ID cookie, returns `False` using `self.session_cookie(request)`
* If the Session ID of the request is not linked to any User ID, returns `False`; uses `self.user_id_for_session_id(...)`
* Otherwise, deletes in `self.user_id_by_session_id` the Session ID (as key of this dictionary) and returns `True`

Updates the file `api/v1/views/session_auth.py`, by adding a new route `DELETE /api/v1/auth_session/logout`:

* Slash tolerant
* Uses `from api.v1.app import auth`
* Uses `auth.destroy_session(request)` for deleting the Session ID contains in the request as cookie:
  * If `destroy_session` returns `False`, `abort(404)`
  * Otherwise, returns an empty JSON dictionary with the status code 200.
  