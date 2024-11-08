import { useState, useEffect } from 'react'; // Hooks
import './App.css';

// Most important thing on React. Components. Let's create a new functional component. 
// This is our Person Component. A Component is a piece of code that return or renders some jsx. 
const Person = () => {
  return(
    <>
    <h1>Name: John</h1>
    <h2>Last Name: Doe</h2>
    <h2>Age: 30</h2>
    </>
  )
}
// We can call the person component into other component, like for example in the App function component. 

// Custom component
const Person1 = (props) => {
  return( 
    <>
    <h1>Name: {props.name}</h1>
    <h2>Last Name: {props.lastName}</h2>
    <h2>Age: {props.age}</h2>
    </>
  )
}

// const App with an arrow function component. 
const App = () => {
  // We can create various variables inside the functional component. That can be used inside the jsx within {}.
  const name = 'John';
  const isNameShowing = false;

  return (
    <div className="App">
      <h1>Hello, {isNameShowing ? name : 'None'}!</h1>  
      {/* empty blocks, called react fragments. Used to wrap more elements h1, h2, p, etc. together */}
      {isNameShowing ? (
        <>  
        test
        </>
      ) : (
        <> 
        <h1>Test1</h1>
        <h2>There is no name</h2>
        </>
      )}

      <h1>-*-*-*-*-*-*-*-*-*-*-*-*-*-</h1>

      {/*Calling the Person component in here. And all the code from the called component gets injected inside of the app
      One of the advantage is that you can call the same component multiple times.*/}
      <Person />
      {/*Props are a very important thing is React. they allows you to pass dynamic data thorugh react components.
      Props are just arguments that you pass into react components, and they are pass via attributes. Just a shorter way of saying properties.*/}
      <Person1 name={"Ale"} lastName={"Caula"} age={28} /> {/*This is a jsx line*/}
      <Person1 name="Alessia" lastName="Campo" age={27}/>
      <Person1 name={"Simo"} lastName={"Galva"} age={59}/>
      {/*This can be very useful when for example you have many user and profiles. If we didn't use custom components we would have to copy and paste
      all the jsx every single time. But if we put all of that code into a component, we can simply call it every time in a single line and pass new dynamic 
      properties based on a different user.*/}

      <h1>-*-*-*-*-*-*-*-*-*-*-*-*-*-</h1>

      {/*Let's do the count for using the react useState Hook*/}
      <CounterComponent/>

      <h1>-*-*-*-*-*-*-*-*-*-*-*-*-*-</h1>
      
      <h1> useEffect, message on page reloads </h1>  
      {/* Let's call the component for the useEffect Hook */}
      <UseEffectHook/>

      <h1>-*-*-*-*-*-*-*-*-*-*-*-*-*-</h1>

    </div>
  );
}

// Let's now learn about react State. State in react is a plain javasctipt object used to represent a piece of information about the component's current situation.
// It is completely managed by the component itself. How to create state in react:
// First we have to import the so called useState hook from react.
// Let's Create a counter Component. 
const CounterComponent = () => {
  // concept of array destructuring. That is how state works. 
  const [counter, setCounter] = useState(0); // Calling the useState as a function (this is a Hook). Whenever you call something as a function and you use the "use" in React is called hook.
  // The first part in the square brackets is going to be name of that state "counter". The second part is the Setter function "set" + state_name ("counter").
  // Inside the useState you put the initial value, and this case will be 0.
  // Event is an action that can be triggered as a result of a user action or some kind of a system generated event. I.e. a mouse click or a button press. 
  
  // !!IMPORTANT rule: NEVER modify the state (counter) manually. This is not just a variable, it is a state. Therefore, it can only be changed by the Setter Function "setCounter".
  // Here we can use the useEffect Hook in order to modify the counter (strictly using the "setCouner") at reaload, to 100.
  useEffect(() => {
    setCounter(100);
  }, []);
  // The problem now is that every time you click on the + or - button, the useEffect reset the counter to 100. It happens as soon as the value increases. 
  // The second parameter of the useEffect hooks, comes in handy. Which is called the dependecy array "[]". With this, the counter value is only modified at start.
  // That's because, when the dependency array is empty, the code inside the use effect parameter function (the code that set the counter to 100), is going to only happen
  // at the initial load of the component. 
  // But if we put some variable inside the "[]" then, the useEffect(parameter function) code is going to update every time the variable inside the "[]" array changes.
  // So what we can do is something like this.
  useEffect(() => {
    alert('You have changed the counter to: ' + counter);
  }, [counter]);
  // !!! This is not a very nice user experience, but this is done in order to see that you can call some code whenever something happens in your react application. By simply
  // providing the variable inside the dependency array "[]". And whenever this variable changes, then you can call the code inside the useEffect parameter-function. 

  return (
    <>
    {/*In order to make the button do something we have to use the State*/}
    {/*This is how we can handle event in react. i.e. by adding the onClick property in the button.
    Inside it we are gonna have a callback function (a function that does not have any name that is just waiting for some kind of a command)
    Inside the onClick callback function we want to change the state.
    Inside the setCounter, create another callback function in order to increment or decrement the counter.
    prevCounter is just the parameter of the setCounter.*/}
    <button onClick={() => setCounter((prevCounter) => prevCounter - 1)}>-</button>
    <h1>{counter}</h1>
    <button onClick={() => setCounter((prevCounter) => prevCounter + 1)}>+</button>
    </>
  )
}

const UseEffectHook = () => {
  // The useEffect Hook will be called in a different way in respect to the useState Hook.
  // We call it as a function and it accept another function as the first parameter. 
  // useEffect allows us to do  something on sime kind of an event.
  useEffect(() => {
    alert('Reload, useEffect action'); // this code here will run as soon as the page loads.
  })
}


export default App;
