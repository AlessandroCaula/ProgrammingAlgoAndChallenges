export default function Main(props) {
	// Detruct the fectched data that is passed as a prop to this component and which will then display the image.
	const { data } = props;

	return (
		// Give to the div of the image a className in order to be access and styled in the index.css file. 
		<div className="imgContainer">
			{/*Give the image the className of "bgImage" so that it can be styled in the index.css.*/}
			{/*Once the data is fetched, give a dynamic alt. 'bg-img' would be the text of the image, only if the image doesn't comes through for some reason.*/}
			<img src={data?.hdurl} alt={data?.title || 'bg-img'} className="bgImage" />
		</div>
	)
}