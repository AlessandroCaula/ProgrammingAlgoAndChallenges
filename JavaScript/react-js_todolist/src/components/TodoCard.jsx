import React from 'react'

// Function Component
function TodoCard(props) {
  // Deconstructing the properties. We can expect to receive the handleDeleteTodo function, since we have passed all the properties from the TodoList. 
  // Receiving as well the index of the element that we wan to delete from the TodoList component.
  const { children, handleDeleteTodo, index, handleEditTodo } = props;
  // Now that we have the handleDeleteTodo function, that handles the action of deleting a todo. We can simplu assign that function to the delete button. 
  return (
    <li className='todoItem'> 
      {children}
      <div className='actionsContainer'>
        <button onClick={() => {
          handleEditTodo(index);
        }}>
          <i className="fa-solid fa-pen-to-square"></i>
        </button>
        <button onClick={() => {
          handleDeleteTodo(index);
        }}>
          <i className="fa-solid fa-trash-can"></i>
        </button>
      </div>
  </li>
  )
}

export default TodoCard