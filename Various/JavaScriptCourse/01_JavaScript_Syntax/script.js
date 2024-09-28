/////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////
// VARIABLES and DATA TYPE
/////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////


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
console.log("Number string divided by a number: " + stringNumber / number); // 10 / 2 = 5

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

// ---- Array (still an object)
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
// LOOSE equality => Does NOT compare DATA TYPES 
console.log(a == b);
// LOOSE disequality
console.log(a != b);

// STRICT equality (===): PREFERRED TO USE
// The most notable difference between this operator and the strict equality (===) operator is that the strict equality operator does not attempt type conversion.
// It compares VALUES and DATA TYPES. Return true only if both are equal.
const numStr = '5';
const numInt = 5;
console.log(`Loose equality ${numStr} == "${numInt}":`, numStr == numInt);
console.log(`Loose equality ${numStr} === "${numInt}"`, numStr === numInt);

// STRICT equality (!==): PREFERRED TO USE
// The most notable difference between this operator and the strict inequality (!==) operator is that the strict equality operator does not attempt type conversion.

// The GOOD ones => === and !==  ---> Use almost eerytime these. 
// The evil twins => == and != 

// Look at this thing which is very strange
console.log(0 == ''); // true   => This is quite strange and brings you into errors.
console.log(false == 'false'); // false
console.log(true == 1); // true
// With the loose equality there are a lot of unexpected results.

// ALWAYS USE the STRICT (dis)equality => === and !==

//
// LOGICAL OPERATORS
//
// AND => && => All operands are true
// OR => || => At least one operand is true
// NOT => ! => Reverses the boolean value => !false === true: true


/////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////
// LOGIC and DECISION MAKING
/////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////

// IF statement
const age = 19;
if (age > 18) {
    console.log('You may enter');
} else if (age == 18) {
    console.log('Just made it')
} else {
    console.log('You shall not PASSSS')
}

// WHILE loop
let i = 0;
while (i < 10) {
    console.log(i);
    i++;
}

// FOR loop
for (i = 0; i < 10; i++) {
    console.log(i  + 10);
}
console.log('');

// Looping through array
const arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for (let i = 0; i < arr1.length; i++) {
    console.log(i + ' => ' + arr1[i]);
}


/////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////
// FUNCTIONS
/////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////

// -- Function declaration
function square(number) {
    // statements.
    return number * number
    // the only way of wrinting a function which have access to "this" keyword.
}
console.log(square(5))

// -- Function expression
// Assigning to a variable a function. 
const funtionVariableName = function(parameters) {
    // statements
    return parameters + " => from function"
}
console.log(funtionVariableName("Hello"))


// -- Arrow function => most modern way of writing function in JS
// Shorter syntax for writing function expression. 
const functionVariableName1 = (parameters) => {
    // statements
    return parameters + " => from arrow function"
}
console.log(functionVariableName1("Hello"))

// Every function in JS returns "Undefined" if we don't specify any return.

// Arrow function
// We declare arrow function like normal variables, with const or let. 
// And then we add the variable name.
// Then we add a set of parenthesis. And then the arrow which point to the function block.  
const square1 = (number) => {
    return number * number;
}
// Function call to the arrow function. The call is dentical to a call to the more classical functions.
const result = square1(10);
console.log(result);

// Arrow function have also a more concise way of defining them, ONLY if there is just the single RETURN statement to perform. 
// Remove the return statements and the brackets. 
const square2 = (number) => number * number;
const result1 = square2(5);
console.log(result1);

// ONLY If you have only one parameter you can also remove the ( ).
const square3 = number => {
    return number * number;
}



//////////////////////////////////////////
// From Javascript to React
//////////////////////////////////////////

// Working with Functions

// - Arrow functionss
const DoSomething = (args) => {
    // Code block
}

// How to export arrow functions in order to use them in another file.
export const DoSomething1 = (args) => {
    // Code block
}

// What you usually do in React is working with components, which are basically these functions
/*
const MyComponent = (args) => {
    // Return html
    return <div></div> // <div> is a container element
}
*/

// Anonymous functions. Function without a name. 
// In react you can just define the anonymous function inline inside the onClick actions. 
/*
<button onClick={(args) => {  Code block  }}>
</button>
*/

// Working with conditionals using the ternary operators. Shorter notation of writing IF/ELSE statements.  
let agePerson = 16;
// Now I want a variable to store a string "adult" or "underage" if the age is greater than 18.
let adultOrMinor = agePerson >= 18 ? "adult" : "underage";
console.log(adultOrMinor);

// In React for example, a thing that is usually done.
/*
const MyComponent = (args) => {
    return age >= 18 ? <div> adult </div> : <div> underage </div>;
}
*/

// Objects/Dictionary
// Very important in JavaScript and React. 

// Destructuring
const person1 = {
    name: "Pedro", 
    age: 20,
    isMarried: false
}
// Deconstructuring. 
const { name, age1, isMarried } = person1;
console.log(person);

// Spread Operator
// In this case is used to create another person, which is equal to person, but with a different name
const person2 = {...person, name: "Jack"};
console.log(person2);
const names = ['Ale', 'Bonfi', 'Leo'];
console.log(names);
const names2 = [...names, 'Gabo'];
console.log(names2);
names2.push('Pedro');
console.log(names2);
const names3 = names2.concat("Ale", "Ludo");
console.log(names3);

// Functino to manipulate arrays
// .map() - .filter() 

// .map()
// In order to access each element of the array. A for loop in one line. 
names.map((name) => {console.log(name)});
//.map() creates a new array with the transformed values but doesn't modify the original array
const names3_1 = names3.map((name) => {
    return name + "1";
});
console.log(names3_1);
//.filter()
const arr2 = ['Ale', 'Bonfi', 'Bonfi', 'Bonfi', 'Bonfi'];
const arr_filtered = arr2.filter((name) => {return name !== 'Bonfi'});
console.log(arr_filtered)
