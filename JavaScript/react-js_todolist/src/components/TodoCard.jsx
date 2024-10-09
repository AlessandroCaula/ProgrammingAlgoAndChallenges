import React from 'react'

// Function Component
function TodoCard(props) {
  const {children} = props
  return (
    <li className='todoItem'> 
      {children}
      <div className='actionsContainer'>
        <i className="fa-solid fa-pen-to-square"></i>
        <i className="fa-solid fa-trash-can"></i>
      </div>
  </li>
  )
}

export default TodoCard