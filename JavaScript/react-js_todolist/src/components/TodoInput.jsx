import { useState } from "react";

// Entire React Functional component
export default function TodoInput(props) {
  // Destructuring the function that is sent as a prop to this component. 
  const { handleAddTodos } = props;
  // Creating a Stateful variable for the element that the user type in the <input placeholder="Enter todo..." ></input>. 
  const [todoValue, setTodoValue] = useState('');

  return (
    <header>
      {/*The onChange event listen for changes, and whenever the value od the input (todoValue) changes it cause this function to receives an event (e)*/}
      {/*e.target.value => is the new text that gets enetered in our todo input*/}
      <input value={todoValue} onChange={(e) => {
        setTodoValue(e.target.value) 
      }} placeholder="Enter todo..." ></input> {/*Self closing tag*/}
      <button onClick={() => {
        handleAddTodos(todoValue)
        {/*re-setting the "Enter todo..."" with an empty string*/}
        setTodoValue('');
      }}>Add</button>
    </header>
  )
}