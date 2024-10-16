import React from 'react'

export default function SideBar() {
	return (
		<div className='sidebar'>
			<div className='bgOverlay'></div>
			<div className='sidebarContents'>
				<h2>The Brutal Martian Land</h2>
				<div>
					<p>Description</p>
					<p><i>Loren ipsum</i></p>
				</div>
				<button>
					<i className="fa-solid fa-right-long"></i>
				</button>
			</div>
		</div>
	)
}
