/////////////////////
// ASYNC FUNCTIONS //
/////////////////////

// An async function is a modern JavaScript construction that simplifies asynchronous programming. 
// It allows to wrtie asynchronous code that reads and behaves more like synchronous code using async and await keywords. 

// How ASYNC functions work:
//
// 1) Declaring an async function
//  - Use the async keyword before the function declaration. 
//  - An async function always returns a Promise. 
// 2) Using await:
//  - The await keyword pauses the execution of the function until the promise is resolved or rejected. 
//  - It must be used inside an async function. 


/////////////////////////////////////////////////////////////////////////////////////////////////

// 1) Basic Async Function

// Declaring an asynchronous function using 'async' keyword.
async function sayHello() {
    return 'Hello, World!'; // Returns a string. Since the function is 'async', it wraps this string in a Promise. 
}

// Calling the async function. It returns a Promise, which we handle using '.then()'.
sayHello().then(message => {
    console.log(message); // Output: "Hello, World!" because the Promise resolved with that value.
})

// - The async keyword makes the function asynchronous, meaning it always returns a Promise, even if you don't explicitly use Promise in the code. 
// - Inside the function, the return value ("Hello, World!") gets automatically wrapped in a resolved Promise.
// - .then() is used to handle the resolved value of the Promise (message), which is the logged to the console.  

/////////////////////////////////////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////////////////////////////

// 2) Using await with a Timer. 

async function waitAndGreet() {
    console.log("Waiting..."); // Immediate log to indicate the 
}
