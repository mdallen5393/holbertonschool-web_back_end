# PROJECT: 0x00. ES6 Basics

## AUTHOR: Matthew Allen

## TASKS

### 0. Const or let? - `0-constants.js`, `0-main.js`

Modify

    * function `taskFirst` to instantiate variables using `const`
    * function `taskNext` to instantiate variables using `let`

### 1. Block Scope - `1-block-scoped.js`, `1-main.js`

Using `var` and hoisting, modify the variables inside the function `taskBlock` so that the variables aren't overwritten inside the conditional block.

### 2. Arrow functions - `2-arrow.js`, `2-main.js`

Modify the function to use ES6's arrow syntax of the function `add`

### 3. Parameter defaults - `3-default-parameter.js`, `3-main.js`

Condense the internals of the following function to 1 line - without changing the name of each function/variable.

### 4. Rest parameter syntax for functions - `4-rest-parameter.js`, `4-main.js`

Modify the function to return the number of arguments passed to it using the rest parameter syntax.

### 5. The wonders of spread syntax - `5-spread-operator.js`, `5-main.js`

Using spread syntax, concatenate 2 arrays and each character of a string by modifying the function.

### 6. Take advantage of template literals - `6-string-interpolation.js`, `6-main.js`

Rewrite the return statement to use a template literal so you can substitute the variables you've defined.

### 7. Object property value shorthand syntax - `7-getBudgetObject.js`, `7-main.js`

Modify the following function's `budget` object to simply use the keyname instead.

### 8. No need to create empty objects before adding in properties - `8-getBudgetCurrentYear.js`, `8-main.js`

Rewrite the `getBudgetForCurrentYear` function to use ES6 computed property names on the `budget` object.

### 9. ES6 method properties - `9-getFullBudget.js`, `9-main.js`

Rewrite `getFullBudgetObject` to use ES6 method properties in the `fullBudget` object.

### 10. For...of Loops - `10-loops.js`, `10-main.js`

Rewrite the function `appendToEachArrayValue` to use ES6's `for...of` operator.

### 11. Iterator - `11-createEmployeesObject.js`, `11-main.js`

Function named `createEmployeesObject` that will recieve two arguments:

    * `departmentName` (String)
    * `employees` (Array of Strings)

The function should return an object.

### 12. Let's create a report object - `12-createReportObject.js`, `12-main.js`

Function named `createReportObject` whose parameter, `employeesList`, is the return value of the previous function `createEmployeesObject`.

`createReportObject` should return an object containing the key `allEmployees` and a method property called `getNumberOfDepartments`.

`allEmployees` is a key that maps to an object containing the department name and a list of all the employees in that department.

The method property receives `employeesList` and returns the number of departments.
