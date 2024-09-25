// Creating a variable using the var keyword
var variableNameVar = "Welcome to Variables in var";
console.log(variableNameVar);

// Preferred way of creating variables is with the let keyword 
let variableNameLet = "Welcome to Variables in let (preferred way)";
console.log(variableNameLet);

// Their values canNOT change through the code. You canNOT reassign it. 
const variableNameConst = "Welcome to Variables in const";
console.log(variableNameConst);

console.log('');

//// Data Types

// ---- Primitive Data Types

// String
//
// Simple strings. There is absolutely no difference between the single or double quotes. 
const singleQuote = 'Single Quote';
console.log(singleQuote);
const doubleQuote = "Double Quote";
console.log(doubleQuote);
// Complex strings. With backticks (alt + 96). They allow to embed in the string functions and variables between $ and {}
const firstName = "Jane";
const backticks = `Hello, ${firstName}`;
console.log(backticks);
// Inspecting the type of each value
console.log(typeof backticks);

console.log('');

// ---- Number
//
// JS is untyped, cause you don't have to specify if the number is an integer or a decimal.
const wholeNumber = 5;
const decimalNumber = 0.5;
const backticksFunction = `${2 + 2}`;
console.log(backticksFunction)
// If you divide or made a mathematical operationg between a number and a string you get a NaN restult.
const string = 'Prova';
const number = 2;
console.log("Result", string / number);
// But attention cause, if in the string you put a number
const stringNumber = "10"
console.log("Number string divided by a number: ", stringNumber / number); // 10 / 2 = 5

console.log('');

// ---- Null
//
// It has only one value => Null. It's a special value which represents nothing. 
let nullVariable = null;
console.log(nullVariable);
console.log(typeof nullVariable); // => object .. This is a bug inside JS, cause null is a primitive dataType. 
// But it will never be solved, cause this has been used from many programmers.  

// ---- Undefined
//
// A variable that has not been assinged a value. A variable without a value.
let undefinedVariable;
console.log(undefinedVariable);
console.log(typeof undefinedVariable);

console.log('');

// ---- Objects
//
// Most complex and important dataType. It is not a primitive dataType (one vale at the time).
// Objects are used to store collections of data and more complex entyties. 

// Dictionary (basically): In JS a dictionary is the same as an object.
//
// Creating an object to connect these two variables (name and age). Just by adding {}.
// Inside the {} you can specify properties and varables.
const person = {
    name: 'John',
    age: 25
}
console.log(person);
console.log(typeof person);
// Dot notation to get a single variable
console.log(person.name);
console.log(person.age);
console.log(typeof person.age);

// Array 
const arr = [1, 2, 3, 4]
console.log(arr);
console.log(typeof arr);

// Date Object
const dateObject = new Date();
console.log(dateObject);

// There are no tuples in JS.

//
// Statically typed languages: are languages where each variable and expression is already known at compile time (i.e. C#, C, C++, Java). A variable is declared with a certain type of data from the begining, and you cannot assing to it a differe value type.
//
// Dinamically typed languages: variables can receive different data types over time (i.e. JS, python). A variable in JS can contain any type of data. 
//
let message = 'Hello world';
console.log(message);
console.log(typeof message);
// Changing its value type
message = 5;
console.log(message);
console.log(typeof message);


// Comparison Operators => return true/false.
const a = 5;
const b = 10;
console.log(a > b);
console.log(a >= b);
console.log(a < b);
console.log(a == b);
console.log(a != b);

// Stric equality (===): PREFERRED TO USE
// The most notable difference between this operator and the strict equality (===) operator is that the strict equality operator does not attempt type conversion.
// It basically compares VALUES and DATA TYPES.
const numStr = '5';
const numInt = 5;
console.log("Loose equality (==):", numStr == numInt);
console.log("Loose equality (===):", numStr === numInt);

// Stric equality (!==): PREFERRED TO USE
// The most notable difference between this operator and the strict inequality (!==) operator is that the strict equality operator does not attempt type conversion.
