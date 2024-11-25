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
//   setTimeout takes two arguments: - A callback function function to execute after the delay (resolve in this case). - The delay time in milliseconds (2000 here).
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
// To use the await, the enclosing function must be declared as async.

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
if (false) {

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

/////////////////////////////////////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////////////////////////////

// 3) Sequential Execution 

if (false) {

    async function countDown() {
        // A loop to count down from 5 to 1. 
        for (let i = 5; i > 0; i--) {
            console.log(i); // Logs the current number

            // Pause for 1 second before moving to the next iteration. 
            await new Promise(resolve => setTimeout(resolve, 1000));
        }

        // After the loop finishes, log "Go!"
        console.log("Go!");
    }

    // Call the function
    countDown();
}

// - Because of await, the next iteration only starts after the delay is completed. This creates a smooth countdown effect. 

/////////////////////////////////////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////////////////////////////

// 4) Running Multiple Async Tasks in Parallel

if (false) {

    // Simulate an async task with a name and delay
    async function task(name, delay) {
        // Waits for 'delay' milliseconds before continuing. 
        await new Promise(resolve => setTimeout(resolve, delay));

        // Logs that the task is completed.
        console.log(`${name} completed in ${delay}ms`);
    }

    // Function to run all tasks in parallel.
    async function runTasksInParallel() {
        // Starts all tasks simultaneously (doesn't wait for any to finish before moving to the next).
        const task1 = task("Task 1", 1000);
        const task2 = task("Task 2", 3000);
        const task3 = task("Task3 ", 2000);

        // Waits until ALL tasks are finished.
        await (Promise.all([task1, task2, task3]));

        // Logs after all tasks complete. 
        console.log("All tasks completed!");
    }

    // Call the function. 
    runTasksInParallel();
}

// - Simulates a task by using await to pause for the given delay. After the delay, logs that the task is completed. 
// - task1, task2 and task3 are initialized simultaneously. 
// - Promise.all: Waits for all tasks to resolve before continuing to the next line of code. 
// - The total time taken is determined by the longest task (task 2 in this case)

// JavaScript does not have a built-in parallel for construct like in some other programming languages, but you can achieve parallelism in certain cases using promises. 
// By leveraging Promise.all, you can execute multiple asynchronous tasks concurrently. 

if (false) {

    // Array of tasks to process. 
    const tasks = [1, 2, 3, 4, 5];

    // Function to simulate an asynchronous task.
    async function processTask(task) {
        console.log(`Processing task ${task}`);
        await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate delay (coding execution time)
        console.log(`Task ${task} done`);
        return task * 2; // Return a simple result. 
    }

    // Parallel execution using Promise.all
    async function runParallel() {
        console.log("Starting parallel tasks...");

        const results = await Promise.all(
            tasks.map(task => processTask(task)) // Map each task to a promise
        );

        console.log("All tasks completd:", results);
    }

    runParallel()
}


/////////////////////////////////////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////////////////////////////

// 5) Retry Logic

if (false) {

    async function retryExample() {
        let attempts = 0; // Keep track of the number of attempts.

        // Retry up to 3 times. 
        while (attempts < 3) {
            try {
                attempts++; // Increment attempts on each iteration. 

                console.log(`Attempt ${attempts}`); // Log the current attempt number

                // Simulate a random failure.
                if (Math.random() > 0.5) {
                    throw new Error("Random failure!"); // Generate an error. 
                }

                // If no error is thrown, log success and exit. 
                console.log("Success!");
                return; // Exit the function after success.

            } catch (error) {
                console.log("Error:", error.message); // Log the error
            }

            // Wait 1 second before retrying
            await new Promise(resolve => setTimeout(resolve, 1000));
        }

        // If all attempts fails, log this message. 
        console.log("Failed after 3 attempts.");
    }

    // Call the function. 
    retryExample();
}

// - try/catch: catches any error thrown by throw new Error(...).

// TEST: Same concept, we have the while loop, and the maximum attempts that we can do are 3. In every while loop I want to do something, like fetching some data or whatever.
// If the fetching takes more than 2 seconds, the request has failed, and we have to retry another time. 
// 1. Use a while loop for the retry mechanism. 
// 2. For each attempt, race the main task (i.e. fetching data) against a timeout using Promise.race. 
// 3. If the task finishes within 2 seconds, proceed; otherwise, retry.
// 4. Stop after 3 failed attempts. 

//// KEY CONCEPT 
// 1. Task:
//  - In this context, a "task" represents an operation (like fetching data) that might succeed or fail. 
//  - Tasks often involved asynchronous operations, meaning they don't block the execution of the rest of the program while waiting to complete. 
// 2. Promise:
//  - A Promise represents a value that may be available now, in the future, or never. 
//  - It has three states:
//      - Pending: The operation hasn't completed yet. 
//      - Resolved: The operation succeeded.
//      - Rejected: The operation failed. 
// 3. async and await:
//  - async function always return a Promise.
//  - await pauses the execution of an async function until the Promise resolves or rejects. 
// 4. Promise.race:
//  - This method runs multiple Promises concurrently and resolves/rejects as soon as one of them does. 
//  - Useful for timeouts because we can "race" a long-running task against a short timeout. 

if (false) {

    async function retryWithTimeout() {
        let attempts = 0; // Keep track of the attempts. 
        const maxAttempts = 3; // Maximum number of retries allowed
        const timeoutDuration = 1000; // Timeout in milliseconds 

        /* Function to simulate a task (e.g. fetching data)
            * Simulates an asynchronous task.
            * This could represent a real-world operation like fetching data, which takes some time, in this case we are simulating it with the use of the setTimeout. 
            * - Randomly takes between 0 and 3 seconds. 
            * - If the task completes within the timeout, it resolves successfully. 
            * - If the task takes longer than the timeout, it rejects. 
        */
        function fetchData() {
            return new Promise((resolve, reject) => {
                const randomTime = Math.random() * 3000; // Simulate a random delay (0-3 seconds)
                // setTimeout is a JS function used to delay the execution of a specific piece of code. It takes two arguments.
                // 1. A callback function: the code to execute after the delay.
                // 2. A delay in milliseconds: how long to wait before executing the callback
                setTimeout(() => {  // This callback function inside the setTimeout runs after the delay specified by randomTime. It evaluates whether the simulated task completes successfully or fails based on how long it took.
                    if (randomTime < timeoutDuration) { // Resolve(value): marks the Promise as successful and passes value to the .then() handler or await.
                        resolve(`Fetch data in ${randomTime.toFixed(0)} ms`);
                    } else {
                        reject(new Error("Task failed internally")); // reject(error): Marks the Promise as failed and passes error to the .catch() handler. 
                    }
                }, randomTime);
            });
        }

        /**
         * Creates a timeout Promise.
         * This Promise will reject after a specified duration. 
         * Used to limit the maximum time allowed for the task.
         */
        function createTimeout(ms) {
            return new Promise((_, reject) => {
                setTimeout(() => reject(new Error("Request timed out")), ms); // Rejecting and throwing an error after timeDuration (1000)
            })
        }

        /**
         * The retry loop.
         * This loop retries the task up to 'maxAttempts' times. 
         */
        while (attempts < maxAttempts) {
            attempts++; // Increment the attempts counter
            console.log(`Attempt ${attempts}`);

            try {
                // Race the task (fetchData) against the timeout. 
                const result = await Promise.race([
                    fetchData(), // The task to complete
                    createTimeout(timeoutDuration), // The timeout
                ]);

                console.log("Success: ", result); // Log success if the task completes
                return; // Exit the loop and the function after success
            } catch (error) {
                console.log("Error: ", error.message); // Log the error
            }
        }

        console.log("Failed after 3 attempts."); // If all attempts fail, log this.
    }

    retryWithTimeout();

}

// 1. Simulating the Task (fetchData)
//  - Purpose: Simulate an operation that might succeed or fail.
//  - How:
//      - A Promise is created
//      - The operation randomly takes between 0ms and 3000ms to complete.
//      - If it completes in less than the timeoutDuration, the Promise resolves successfully.
//      - Otherwise, it rejects with an error.
// 2. Creating a Timeout (createTimeout)
//  - Purpose: Define a maximum allowed time for a task.
//  - How:
//      - A Promise is created.
//      - It rejects after timeoutDuration milliseconds with the error: "Request timed out".
//      - This works alongside Promise.race to ensure a task doesn't take too long. 
// 3. Racing Promises (Promise.race)
//  - What it Does:
//      - Runs multiple Promises concurrently.
//      - Resolves or rejects as soon as one Promise finishes (whether it's success or failure).
//  - Why it Works:
//      - In the code, Promise.race([fetchData(), createTimeout(timeoutDuration)]) races the simulated task (fetchData) against the timeout (createTimeout).
//      - If the task finishes first, the Promise resolves with the result.
//      - The the timeout finishes first, the Promise rejects with a timeout error.


//// PROMISES
// 
// A Promise is an object in JS used to handle asynchronous operations. It represents a placeholder for a value that may be available now, in the future, or never. 
// It helps avoid "callback hell" and makes asynchronous code easier to read and write. 
//
// How does a Promise Work?
// When you create a Promise, it is in one of three states:
// - Pending: The operation is ongoing, and the final result is not yet available. 
// - Fulfilled: The operation was successful, and the result is available. 
// - Rejected: The operation failed, and an error reason is available. 
// Once a Promise is fulfilled or rejected, it becomes settled and cannot change states. 

// -- Basic Syntax

if (false) {

    const promise = new Promise((resolve, reject) => {
        // Asynchronou operation here
        const operation = true;

        /* operation succeeds */
        if (operation) {
            resolve('Success'); // Fulfulled
        } else {
            reject('Error message'); // Rejected
        }
    });
}

// -- Parameters of the Promise constructor.
//
// - resolve: A function to call when the asynchronous operation is successful. It passes the result to .then().
// - reject: A function to call when the asynchronous operation fails. It passes the error to .catch().

// Example Simple Promise
if (false) {

    const exampelPromise = new Promise((resolve, reject) => {
        let success = true; // Simulate success or failure. 

        if (success) {
            resolve('Operation was successful!');
        } else {
            reject('Something went wrong.');
        }
    });

    // Handling the result. 
    exampelPromise
        .then(result => {
            console.log(result); // Logs: Operation was successful!
        })
        .catch(error => {
            console.log(error); // Logs: Something went wrong.
        });
}

// -- Chaining Promises
//
// Promises can be chained to handle multiple asynchronous steps in sequence. 

if (false) {

    new Promise((resolve, reject) => {
        resolve(2); // It resolves and return 2 to .then()
    })
        .then(value => {
            console.log(value); // Logs 2
            return value * 2; // Return 4, that is chaned and passed to the next .then();
        })
        .then(value => {
            console.log(value); // Logs 4
            return value * 2;
        })
        .then(value => {
            console.log(value); // Logs 8
        })
}

///// Common methods:
// 
//
// -- then(onFulfilled, onRejected) :
// 
// - Handles the results when the Promise is resolved or rejected. 

if (false) {
    promise.then(
        result => console.log('Fulfilled:', result),
        error => console.error('Rejected:', error)
    );
}

// -- catch(onRejected) :
// 
// - Handles errors from rejected Promises.

if (false) {
    promise.catch(error => console.error('Error:', error));
}

// -- finally(onFinally) :
// 
// - Runs a function regardless of whether the Promise was resolved or rejected. 

if (false) {
    promise.finally(() => console.log('Promise settled.'));
}

// -- Promise.all(promises) :
// 
// - Resolves when all Promises in an array succeed, or rejects if any fail. 

if (false) {
    Promise.all([promise1, promise2, promise3])
        .then(results => console.log(results))
        .catch(error => console.error(error))
}

// -- Promise.race(promises) :
//
// - Resolves or rejects as soon as one Promsie settles (wither resolves or rejects).
if (false) {
    Promise.race([promise1, promise2])
        .then(result => console.log('One promise Settled', result))
        .then(error => console.log('One promise Failed', error));
}


/////////////////////////////////////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////////////////////////////

// 5) Async Functions Inside Loops

// --- Sequenctial Execution

if (false) {

    async function processItemsSequentially(items) {
        // Loop through items one at a time. 
        for (const item in items) {
            // Simulate processing each item with a 1-second delay.
            await new Promise(resolve => setTimeout(resolve, 1000));

            console.log(`Processed: ${item}`); // Log the index of the array, because the for...in loops through the keys of the array (the numeric indexes)
            console.log(`Processed: ${items[item]}`);
        }
    }

    processItemsSequentially(['a', 'b', 'c']);
}

// - Each item is processed one at a time because of the await. 
// - The loop waits for the delay (1 second) before moving to the next item.


////// FOR...IN
//
// The `for...in` loop iterates over enumerable properties of an object, including the keys of an array (which are the numeric indexes).
if (false) {

    for (const key in object) {
        // Code to execute.
    }
}
// - key: represents the property name (or index if the object is an array).
// - object: the object whose properties will be iterated over. 

if (false) {
    const person = { name: "John", age: 30, city: "New York" };

    for (const key in person) {
        console.log(`${key}: ${person[key]}`); // Log first the key, and then the value corresponding to that key.
    }
}

if (false) {
    const fruits = ["Apple", "Banana", "Cherry"];

    for (const index in fruits) {
        console.log(`Index: ${index}, Value: ${fruits[index]}`);
    }
}

// When to use for...in? 
// - Best for Objects: Use for...in to iterate over an object's properties.
// - Avoid for Arrays: Since arrays have numeric indexes, using for...in can lead to issues (e.g., iterating over inherited properties).

////// FOR...OF
//
// If you're working with arrays and want a simpler, more predictable loop compared to for...in, use for...of.
if (false) {
    const fruits = ["Apple", "Banana", "Cherry"];

    for (const fruit of fruits) {
        console.log(fruit);
    }
}

////// forEach
//
// Use forEach when you need to iterate over an array to process its values.
// It is cleaner, avoids pitfalls like inherited properties, and ensures predictable iteration order.
if (false) {
    // An array of numbers
    const numbers = [1, 2, 3, 4, 5];

    // Using forEach to log each number
    numbers.forEach((number) => {
        console.log(`Number: ${number}`);
    });
}

if (false) {
    // An array of prices
    const prices = [10, 20, 30, 40];

    // Apply a discount to each price
    prices.forEach((price, index, array) => {
        array[index] = price * 0.9; // Apply a 10% discount
    });

    // Log the updated prices
    console.log(prices)
}
// The callback function takes three arguments:
// - price: The current element.
// - index: The index of the current element.
// - array: The original array.

// forEach does not return a value; it is used for performing operations on array elements.


// --- Parallel Execution

if (false) {

    async function processItemsInParallel(items) {
        // USe the `.map()` to create an array of promises for all items. 
        const promises = items.map(item =>
            new Promise(resolve =>
                setTimeout(() => {
                    console.log(`Processed: ${item}`); // Log after processing the item. 
                    resolve(); // Resolve the Promise
                }, 1000) // 1-second delay for each item. 
            )
        );

        // Wait for all promises to resolve.
        await Promise.all(promises);
    }

    processItemsInParallel([1, 2, 3]);
}

// Each item starts processing simultaneously.
// Total execution time is the same as the longest task.


//// EXAMPLE:
//
// Process one element at a time in a loop, where the next process starts only after the previous one finishes, you can use an async function combined with await and a for...of loop.
//
// 1. Simulate a time-consuming process:
//      -We'll use setTimeout within a Promise to simulate a task that takes varying amounts of time.
// 2. Iterate one at a time:
//      - Use an async function to ensure tasks are executed sequentially.
//      - Use await to wait for each process to complete before moving to the next.
// 3. Control over task execution:
//      -Each task is processed in order, and subsequent tasks don't start until the previous one resolves.

if (false) {

    // Simulate a time-consuming task
    function processTask(task) {
        return new Promise((resolve) => {
            const processingTime = Math.floor(Math.random() * 3000) + 1000; // Random time between 1-4 seconds
            console.log(`Starting task: ${task}, estimated time: ${processingTime}ms`);
            setTimeout(() => {
                console.log(`Completed task: ${task}`);
                resolve(); // Resolve the promise after the "processing" time. 
            }, processingTime);
        });
    }

    // Sequentially process tasks. 
    async function processTasksSequentially(tasks) {
        for (const task of tasks) {
            await processTask(task); // Wait for the current task to complete before continuing.
        }
        console.log('All tasks completed!');
    }

    // Example tasks to process
    const tasks = ["Task A", "Task B", 'Task C', 'Task D'];

    // Start processing tasks
    processTasksSequentially(tasks);
}

// 1. Simulating the process:
//  - The processTask function returns a Promise that resolves after a random timeout to simulate varying processing times.
//  - resolve() is called after the task is "processed".
// 2. Iterating sequentially:
//  - The for...of loop in the processTasksSequentially function iterates over the tasks array.
//  - The await keyword pauses the loop until the current task's promise resolves.


///// ASYNC !!!!!!!
//
// 1. Code Inside an async Function:
//  - When an await statement is encountered, the execution of the async function pauses at that point until the await expression resolves.
//  - However, the await does not block the JavaScript main thread; it simply pauses the execution of that specific async function, allowing other code outside or elsewhere to continue running.
// 2. Code Outside the async Function:
//  - The code outside the async function continues to execute normally and is unaffected by the await statement.

if (true) {
    // Define an async function
    async function fetchData() {
        console.log("Inside async function: Start");

        // Simulate an async operation with a delay
        await new Promise((resolve) => setTimeout(resolve, 2000));

        console.log("Inside async function: End");
    }

    // Code outside the async function
    console.log("Outside async function: Before calling fetchData");

    fetchData(); // Call the async function

    console.log("Outside async function: After calling fetchData");

}