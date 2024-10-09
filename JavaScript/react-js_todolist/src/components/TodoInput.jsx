import { useState } from "react";

// Entire React Functional component
export default function TodoInput(props) {
  // Destructuring the function that is sent as a prop to this component. 
  const { handleAddTodos } = props;
  // Creating a Stateful variable for the element that the user type in the <input placeholder="Enter todo..." ></input>. 
  const [todoValue, setTodoValue] = useState('');

  return (
    <header>
      <input value={todoValue} onChange={(e) => {
        setTodoValue
      }} placeholder="Enter todo..." ></input> {/*Self closing tag*/}
      <button onClick={() => {
        handleAddTodos(todoValue)
      }}>Add</button>
    </header>
  )
}