import React from 'react'

export default function SideBar(props) {

	// Deconstructuring the props.
	const { data, handleToggleModel } = props;

	return (
		<div className='sidebar'>
			{/*When the background overlay is clicked, then the side bar disappear as well*/}
			<div onClick={handleToggleModel} className='bgOverlay'></div>
			<div className='sidebarContents'>
				{/*Display the Data title and explanation*/}
				<h2>{data?.title}</h2>
				<div className='descriptionContainer'> 
					<p className='descriptionTitle'>{data?.date}</p>
					<p>{data?.explanation}</p>
				</div>
				{/*When the button is clicke, then call the handleToggleModel which change the sate of the showModel state variable and close the SideBar.*/}
				<button onClick={handleToggleModel}>
					<i className="fa-solid fa-right-long"></i>
				</button>
			</div>
		</div>
	)
} 
