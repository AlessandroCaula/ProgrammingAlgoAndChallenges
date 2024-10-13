import { useState, useEffect } from "react"
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

  // For the handleEditTodo it is a bit more complicated, since we want to put the value that we want to edit (which is in the TodoList component) in the TodoInput function component. 
  // But since the TodoList and TodoComponent are at the same level, the TodoInput does not have access to the TodoList. For this reason, we have to re-initialize the todoList State over here, which is the upper function component. 
  // We then have to pass these State to the TodoInput component, so that it can still access to it normally. 
  const [todoValue, setTodoValue] = useState('');

  // Define a small function, that is used whenever eny Edit, Delete action is performed for letting the todos persist on page refresh. 
  function persistData(newList) {
    localStorage.setItem('todos', JSON.stringify({ todos: newList }));
  }

  // Create a function that is used to handle update todos.
  function handleAddTodos(newTodo) {
    // Creating a new array. By spredding out the old todos (adding the new todo).
    const newTodoList = [...todos, newTodo];
    // Calling the persistData function, in order to store the new todos list in the JSON localStorage file. 
    persistData(newTodoList);
    // Calling the setter function, by simply passing the new updated todos list.
    setTodos(newTodoList);
  }

  // Function that handles the delete action. Before it starts, we have to assign it to the delete button, which is defined in the todoList
  function handleDeleteTodo(index) {
    // Creating a new list with all the elements, minus the deleted one. 
    const newTodoList = todos.filter((todo, todoIndex) => {
      // If the todoIndex is NOT equal to the index, it is allowed to stay in the list. 
      return todoIndex !== index;
    });
    // Calling the persistData function. 
    persistData(newTodoList);
    // Call the setTodo State and pass the new list, without the removed element. 
    setTodos(newTodoList);
  }

  // Function that handles the edit action. Pass the function as a prop to the todoList. That will automatically pass it to the todoCard. 
  function handleEditTodo(index) {
    // Since we now have access to the todoValue and setTodoValue in here, we can make use of them for the EditTodo
    const valueToBeEdited = todos[index];
    // Set the todoValue to the value to be edited.
    setTodoValue(valueToBeEdited);
    // We can simply delete the old value of the value that we want to edit. 
    handleDeleteTodo(index);
  }

  // In order to not delete the todos list when we refresh the page we can use local storage that allows to persist the todos list at all times to the local storage and then just read them in when we load the web page.
  // To listen to those kind of events in react we use a different React Hook, the useEffect.
  // The useEffect takes a dependency array. It will essentially listen to different events and run code based on when those events happen. 
  // The useEffect State, takes as input an arrow function and a [] which is the dependency array. If we want to listen to the change of a variable, you would pass the variable into the [].  
  // If we want to run the code of the arrow function on page load, the [] are left as an empty array. 
  // In this case check if the localStorage exists.
  useEffect(() => {
    if (!localStorage) {
      return;
    }
    // If the localStorage exist 
    let localTodos = localStorage.getItem('todos');
    // Check if it existed before (if it doesn't it returns "undefined"). If it existed, we can override it.
    if (!localTodos) {
      return;
    }
    // If the localTodos exist. Parsing the JSON local storage and retrive the todos.
    localTodos = JSON.parse(localTodos).todos;
    // Set the localTodos to the todos. 
    setTodos(localTodos);
  }, []);

  // In the return function we have jsx. Which is basically plain HTML in which we can write JavaScript code. 
  return (
    <>
      {/*Rendering components*/}
      {/*Inside the TodoInput we have to update the todos stateful list variable, using the handleAddTodos funciton
      We will also have to pass the todoList State since we have defined it here in order to let it access to the TodoList component as well*/}
      <TodoInput todoValue={todoValue} setTodoValue={setTodoValue} handleAddTodos={handleAddTodos} />
      {/*Passing the list of todos to the TodoList component as props (properties)
      Passing the handleDeleteTodo as a Prop to the TodoList component. handleDeleteTodoProp is the name of the prop. The one within the {} is the value of the Prop*/}
      <TodoList handleDeleteTodo={handleDeleteTodo} todos={todos} handleEditTodo={handleEditTodo} />
    </>
  )
}

export default App
