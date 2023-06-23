# PROJECT: NodeJS Basics

AUTHOR: Matthew Allen

## TASKS

### 0. Executing basic javascript with NodeJS - `0-main.js`, `0-console.js`

Defines a function named `displayMessage` that prints in `STDOUT` the string argument.

### 1. Using Process stdin - `1-stdin.js`

Program that is executed through the command line:

* Displays the message `Welcome to Holberton School, what is your name?` (followed by a new line)
* The user inputs their name on a new line
* The program displays `Your name is: INPUT`
* When the user ends the program, displays `This important software is now closing` (followed by a new line)

Requirements:

* The code is tested through a child process

### 2. Reading a file synchronously with Node JS - `2-main_0.js`, `2-main_1.js`, `2-read_file.js`

Uses the database `database.csv` and defines a function `countStudents`

* Function `countStudents` accepts a path in argument
* The script attempts to read the database file synchronously
* If the database is not available, it throws an error with the text `Cannot load the database`
* If the database is available, it logs the following message to the console `Number of students: NUMBER_OF_STUDENTS`
* It logs the number of students in each field, and the list with the following format: `Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES`
* The CSV file can contain empty lines (at the end), which is not considered a valid student

### 3. Reading a file asynchronously with Node JS - `3-main_0.js`, `3-main_1.js`, `3-read_file_async.js`

Uses the database `database.csv` and defines a function `countStudents`

* Defines a function named `countStudents` which accepts a path argument (same as in task 2)
* Script attempts to read the database file asynchronously
* The function returns a Promise
* If the database is not available, it logs the following message to the console `Cannot load the database`
* If the database is available, it logs the following message to the console `Number of students: NUMBER_OF_STUDENTS`
* It logs the number of students in each field, and the list with the following format: `Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES`
* The CSV file may contain empty lines (at the end), which is not considered a valid student

### 4. Create a small HTTP server using Node's HTTP module - `4-http.js`

Creates a small HTTP server using the `http` module:

* It is assigned to the variable `app`, which is exported
* The HTTP server listens on port 1245
* Displays `Hello Holberton School!` in the page body for any endpoint as plain text

### 5. Create a more complex HTTP server using Node's HTTP module - `5-http.js`

Creates a small HTTP server using the `http` module:

* It is assigned to the variable `app`, which is exported
* The HTTP server listens on port 1245
* It returns plain text
* When the URL path is `/`, it displays `Hello Holberton School!` in the page body
* When the URL path is `/students`, it displays `This is the list of our students` followed by the same content as the file `3-read_file_async.js` (with and without the database) - the name of the database is passed as argument of the file
* The CSV file may contain empty lines (at the end), which is not considered a valid student

### 6. Create a small HTTP server using Express - `6-http_express.js`

Creates a small HTTP server using the Express module:

* It should be assigned to the variable `app`, which is exported.
* The HTTP server listens on port 1245
* Displays `Hello Holberton School!` in the page body for the endpoint `/`

### 7. Create a more complex HTTP server using Express - `7-http_express.js`

Recreates the small HTTP server using `Express`:

* It is assigned to the variable `app`, which is exported
* The HTTP server listens on port 1245
* It returns plain text
* When the URL path is `/`, it displays `Hello Holberton School!` in the page body
* When the URL path is `/students`, it displays `This is the list of our students` followed by the same content as the file `3-read_file_async.js` (with an d without the database) - the name of the database is passed as argument of the file
* The CSV file may contain empty lines (at the end), which is not considered a valid student

### 8. Organize a complex HTTP server using Express - `full_server/utils.js`, `full_server/controllers/AppController.js`, `full_server/controllers/StudentsController.js`, `full_server/routes/index.js`, `full_server/server.js`

Creates a full server in a directory named `full_server`

Uses `babel-node` to allow the use of ES6 functions like `import` or `export`

#### 8.1 Organize the structure of the server

* Creates 2 directories within `full_server`:
  * `controllers`
  * `routes`
* Creates a file `full_server/utils.js`, which defines a function named `readDatabase` that accepts a file path as argument:
  * Reads the database asynchronously
  * Returns a promise
  * When the file is not accessible, rejects the promise with the error
  * When the file can be read, it returns an object of arrays of the firstname of students per fields

#### 8.2 Write the App controller

Inside the file `full_server/controllers/AppController.js`:

* Creates a class named `AppController` and adds a static method named `getHomepage`
* `getHomepage` accepts `request` and `response` as argument.  It returns a 200 status and the message `Hello Holberton School!`

#### 8.3 Write the Students controller

Inside the file `full_server/controllers/StudentsController.js`, defines a class named `StudentsController` and defines two static methods:

The first one is `getAllStudents`:

* The method accepts `request` and `response` as argument
* Returns a status 200
* Calls the function `readDatabase` from the `utils` file, and displays in the page:
  * First line: `This is the list of our students`
  * And for each field (ordered by alphabetic order case insensitive), a line that displays the number of students in the field, and the list of first names (ordered by appearance in the database file) with the following format: `Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES`
* If the database is not available, it returns a status 500 and the error message `Cannot load the database`

The second one is `getAllStudentsByMajor`:

* The method accepts `request` and `response` as argument
* Returns a status 200
* Uses a parameter that the user can pass to the browser `major`.  The `major` must be either `CS` or `SWE`. If the user passes another parameter, the server returns a 500 and the error `Major parameter must be CS or SWE`
* Calls the function `readDatabase` from the `utils` file, and displays in the page the list of first names for the students (ordered by appearance in the database file) in the specified field `List: LIST_OF_FIRSTNAMES_IN_THE_FIELD`
* If the database is not available, it returns a status 500 and the error message `Cannot load the database`

#### 8.4 Write the routes

Inside the file `full_server/routes/index.js`:

* Links the route `/` to the `AppController`
* Links the route `/students` and `/students/:major` to the `StudentsController`

#### 8.5 Write the server reusing everything you created

In the file named `full_server/server.js`, creates a small Express server:

* Uses the routes defined in `full_server/routes/index.js`
* Uses the port 1245

#### 8.6 Update `package.json` (if running it from outside the folder `full_server`)

If starting node from outside the folder `full_server`, upgrade the command `dev` by `nodemon --exec babel-node --presets babel-preset-env ./full_server/server.js ./database.csv`
