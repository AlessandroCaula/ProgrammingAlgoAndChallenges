import React from 'react'

export default function Footer(props) {

  // Deconstructuring the props that are coming from the app component.
  const { data, handleToggleModel } = props;

  return (
    <footer>
      <div className='bgGradient'></div>
      <div>
        {/*Checking with the ? if the data exist*/}
        <h1>APOD PROJECT</h1>
        <h2>{data?.title}</h2>
      </div>
      {/*Assign the handleToggleModel function to the onClick event of the button. So that when it is clicked, the function handleToggleModel is executer, changes the showModel state and the sideBar is shown.*/}
      <button onClick={handleToggleModel}>
        <i className="fa-solid fa-circle-info"></i>
      </button>
    </footer>
  )
}
