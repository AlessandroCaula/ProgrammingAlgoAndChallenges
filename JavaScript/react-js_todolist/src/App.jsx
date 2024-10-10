import { useState } from "react"
import TodoInput from "./components/TodoInput"
import TodoList from "./components/TodoList"

// Function Component. This is the highest level parent functional component. The starting point of our App. 
// Itself gets rendered in the main.jsx as a component. And fetched as a "root" and thrown in the HTML page in the index.html file.
function App() {
  // Demonstrate how the Todo list would be.
  // Moving the todos list to the parent component, so that the other components can access it at the same time. We pass the list as props to the other function components.   
  // Using the React State variables. These are used whenever you're defining a variable that a user is going to interact with, for example a list that we're going to modify via
  // user interaction in our page, then you will want to define it as a Stateful variable.
  // By defining a variable, and a setter function that is used to update the value of that variable. 
  // We pass to the useState a default variable (we can also not pass any default variable). But since we know that our variable will be a list, we will pass an empty list. 
  const [todos, setTodos] = useState([]);

  // Create a function that is used to handle update todos.
  function handleAddTodos(newTodo) {
    // Creating a new array. By spredding out the old todos (adding the new todo).
    const newTodoList = [...todos, newTodo];
    // Calling the setter function, by simply passing the new updated todos list.
    setTodos(newTodoList);
  }

  // Function that handles the delete action. 
  function handleDeleteTodo(index) {
    // Creating a new list with all the elements, minus the deleted one. 
    const newTodoList = todos.filter((todo, todoIndex) => {
      // If the todoIndex is NOT equal to the index, it is allowed to stay in the list. 
      return todoIndex !== index
    });
    // Call the setTodo State and pass the new list, without the removed element. 
    setTodos(newTodoList);
  }

  // Function that handles the edit action. 
  function handleEditTodo(index) {

  }

  // In the return function we have jsx. Which is basically plain HTML in which we can write JavaScript code. 
  return (
    <>
      {/*Rendering components*/}
      {/*Inside the TodoInput we have to update the todos stateful list variable, using the handleAddTodos funciton*/}
      <TodoInput handleAddTodos={handleAddTodos}/>
      {/*Passing the list of todos to the TodoList component as props (properties)*/}
      <TodoList todos={todos} />
    </>
  )
}

export default App
