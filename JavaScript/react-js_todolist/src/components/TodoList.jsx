import React from 'react'
import TodoCard from './TodoCard'

// Function Component. 
function TodoList(props) {
  // Decostructuring the todos properties. 
  const {todos} = props;
  
  return (
    // Returning each of the element in the todos list, using the map function. 
    // Rendering out every todo item as a paragrapgh in the TodoCard function component. 
    <ul className='main'>
      {todos.map((todo, todoIndex) => {
        return (
          <TodoCard key={todoIndex}>
            <p>{todo}</p>
          </TodoCard>
        );
      })}
    </ul>
  )
}

export default TodoList