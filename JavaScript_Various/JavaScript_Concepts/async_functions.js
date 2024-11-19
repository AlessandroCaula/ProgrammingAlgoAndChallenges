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
if (false) {
    async function sayHello() {
        return 'Hello, World!'; // Returns a string. Since the function is 'async', it wraps this string in a Promise. 
    }

    // Calling the async function. It returns a Promise, which we handle using '.then()'.
    sayHello().then(message => {
        console.log(message); // Output: "Hello, World!" because the Promise resolved with that value.
    });
}
// - The async keyword makes the function asynchronous, meaning it always returns a Promise, even if you don't explicitly use Promise in the code. 
// - Inside the function, the return value ("Hello, World!") gets automatically wrapped in a resolved Promise.
// - .then() is used to handle the resolved value of the Promise (message), which is the logged to the console.  

/////////////////////////////////////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////////////////////////////

// 2) Using await with a Timer. 
//
// - A Promise is an object in JavaScript that represents a value that might not be available yet but will be resolved (or rejected) in the future.
// - Promises are often used to handle asynchronous operations like waiting for something to complete. 
// - setTimeout is a built-in JavaScript function that delays the execution of code for a specific duration. 
// setTimeout takes two arguments: - A callback function function to execute after the delay (resolve in this case). - The delay time in milliseconds (2000 here).
// - The promise will resolve automatically after 2 seconds because seTimeout calls the resolve function after the delay. 

if (false) {
    async function waitAndGreet() {
        console.log("Waiting..."); // Immediate log to indicate the function has started

        // 'await' pauses the execution until the Promise resolves after 2000ms (2s).
        // A new Promise is created. Inside the promise, setTimeout delays for 2000 ms and then calls the resolve function. 
        await new Promise(resolve => setTimeout(resolve, 2000));

        // Once the Promise resolves, execution continues. 
        console.log("Hello after 2 seconds!"); // This log happens after 2 seconds delay.
    }

    // Call the async function
    waitAndGreet();
}

// - await: Pauses the function until the Promise resolves. The rest of the code inside the function won't execute until that happens. 
// - setTimeout: Creates a delay by resolving the Promise after 2 seconds. 
// - This example demonstrates how you can use await to delay execution eithout blocking the entire JavaScript thread. 

// To demonstrate that using await with setTimeout in the example does not blick the JavaScript thread, you can perform another another action concurrently, such as logging a message or interacting with the UI, while the delay occurs the delay occurs in the async function. 

if (false) {
    async function waitAndPrint() {
        console.log("Waiting for 2 seconds...");
        await new Promise(resolve => setTimeout(resolve, 2000)); // Non-blocking delay. 
        console.log("Done waiting!");
    }

    // Start the async function
    waitAndPrint();

    // Run other code while the async function is pause
    console.log("This runs immediately, without waiting!");
}

// Trigger Action Outside of the Async Function. 
// This situation is common when you want to ensure that some operation is completed (like loading data, completing a calculation, or waiting for user input) before executing additional logic outside the async function.

if (false) {
    // Async function that simulates a delay
    async function fetchGreeting() {
        console.log("Fetching greeting...");
        await new Promise(resolve => setTimeout(resolve, 2000)); // Simulate a delay
        console.log("Greeting fetched!");
        return "Hello, world!";
    }

    // Another function that waits for the async function
    async function main() {
        const greeting = await fetchGreeting(); // Wait until the async function resolves
        console.log(greeting); // Only runs after fetchGreeting resolves
    }

    main();
}

// In this example, a follow-up task occurs outside the async functino but waits for it to finish.
if (true) {
    async function downloadFile() {
        console.log("Downloading file...");
        await new Promise(resolve => setTimeout(resolve, 3000)); // Simulate a 3-second download
        console.log("File downloaded!");
        return "file.txt";
    }

    // Call the async function and wait for it to finish
    downloadFile().then(file => {
        console.log(`Processing ${file}...`); // Only runs after the file download completes
    });
}

