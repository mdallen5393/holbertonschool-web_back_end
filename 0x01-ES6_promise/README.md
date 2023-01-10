# PROJECT: 0x01. ES6 Promises

## AUTHOR: Matthew Allen

## TASKS

### 0. Keep every promise you make and only make promises you can keep - `0-promise.js`

Returns a promise using the prototype `function getResponseFromAPI()`.

### 1. Don't make a promise...if you know you can't keep it - `1-promise.js`

Using the prototype `getFullResponseFromAPI(success)`, return a `promise`.

When the argument is:

* `true`
  * resolve the promise by passing an object with 2 attributes:
    * `status`: `200`
    * `body`: `Success`
  * `false`
    * reject the promise with an error object with the message `The fake API is not working currently`.

### 2. Catch me if you can! - `2-then.js`

Using the function prototype `function handleResponseFromAPI(promise)`, append three handlers to the function:

* When the Promise resolves, return an object with the following attributes
  * `status`: `200`
  * `body`: `success`
* When the promise rejects, return an empty `Error` object
* For every resolution, log `Got a response from the API` to the console

### 3. Handle multiple successful promises - `3-all.js`

In this file, import `uploadPhoto` and `createUser` from `utils.js`.

Knowing that the functions in `utils.js` return promises, use the prototype `function handleProfileSignup()` to collectively resolve all promises and log `body firstName lastName` to the console.

In the event of an error, log `Signup system offline` to the console.

### 4. Simple promise - `4-user-promise.js`

Using the prototype `function signUpUser(firstName, lastName)` that returns a resolved promise with this object:

    {
      firstName: value,
      lastName: value,
    }

### 5. Reject the promises - `5-photo-reject.js`

Write and export a function named `uploadPhoto` that accepts one argument `fileName` (string).

It should return a Promise rejecting with an Error and the string `$fileName cannot be processed`, and should use the prototype `export default function uploadPhoto(filename)`.

### 6. Handle multiple promises - `6-final-user.js`

Import `signUpUser` from `4-user-promise.js` and `uploadPhoto` from `5-photo-reject.js`.

Write and export a function named `handleProfileSignup`.  It should accept three arguments `firstName` (string), `lastName` (string), and `fileName` (string).  The function should call the two other functions.  When the promises are all settled it should return an array with the following structure:

    [
      {
        status: status_of_the_promise,
        value: value or error returned by the Promise
      },
      ...
    ]

### 7. Load balancer - `7-load_balancer.js`

Write and export a function named `loadBalancer`.  It should accept two arguments `chinaDownload` (Promise) and `USDownload` (Promise).

The function should return the value returned by the promise that resolved the first, using the prototype `export default function loadBalancer(chinaDownload, USDownload)`.

### 8. Throw error / try catch - `8-try.js`

Write a function named `divideFunction` that will accept two arguments: `numerator` (Number) and `duminator` (Number).

When the `denominator` argument is equal to 0, the function should throw a new error with the message `cannot divide by 0`.  Otherwise it should return the numerator divided by the denominator.

Use the prototype `export default function divideFunction(numerator, denominator)`.

### 9. Throw an error - `9-try.js`

Write a function named `guardrail` that will accept one argument `mathFunction` (Function).

This function should create and return an array named `queue`.

When the `mathFunction` is executed, the value returned by the function should be appended to the queue.  If this function throws an error, the error message should be appended to the queue.  In every case, the message `Guardrail was processed` should be added to the queue.

Example:

    [
      1000,
      'Guardrail was processed'
    ]
