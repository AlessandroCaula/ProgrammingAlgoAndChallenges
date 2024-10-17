export default function Main() {
	return (
		// Give to the div of the image a className in order to be access and styled in the index.css file. 
		<div className="imgContainer">
			{/*Give the image the className of "bgImage" so that it can be styled in the index.css.*/}
			<img src="Dall-E Mars.png" alt="Dall-E Mars image generated" className="bgImage" />
		</div>
	)
}