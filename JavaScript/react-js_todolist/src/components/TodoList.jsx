import React from 'react'
import TodoCard from './TodoCard'

// Function Component. 
function TodoList(props) {
  // Decostructuring the todos properties. I.e. The todos list and the handleDeleteTodo function.  
  const { todos } = props;

  return (
    // Returning each of the element in the todos list, using the map function. 
    // Rendering out every todo item as a paragrapgh in the TodoCard function component. 
    // In order to pass the prop to multiple components (i.e. TodoCard) we can use curly parenthesis where we would normally add a new prop
    // to a subcomponent, and we can just spread out all the props that the TodoList component received.
    // Passing the index of the element to delete to the TodoCard. Since the index is neede to the handleDeleteTodo function. 
    <ul className='main'>
      {todos.map((todo, todoIndex) => {
        return (
          <TodoCard {...props} key={todoIndex} index={todoIndex}>
            <p>{todo}</p>
          </TodoCard>
        );
      })}
    </ul>
  )
}

export default TodoList