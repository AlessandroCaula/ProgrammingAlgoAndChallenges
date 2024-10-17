import React from 'react'

export default function Footer(props) {

  // Deconstructuring the props that are coming from the app component.
  const { handleToggleModel } = props;

  return (
    <footer>
      <div className='bgGradient'></div>
      <div>
        <h2>Footer: Dall-E Mars generated image</h2>
        <h1>APOD PROJECT</h1>
      </div>
      {/*Assign the handleToggleModel function to the onClick event of the button. So that when it is clicked, the function handleToggleModel is executer, changes the showModel state and the sideBar is shown.*/}
      <button onClick={handleToggleModel}>
        <i className="fa-solid fa-circle-info"></i>
      </button>
    </footer>
  )
}
