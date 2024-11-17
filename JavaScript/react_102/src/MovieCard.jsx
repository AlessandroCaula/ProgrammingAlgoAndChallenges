import React from "react"

// Destructuring the props by adding the double braces {movie1}. 
const MovieCard = ( {movie} ) => {
    return (
        <div className='movie'>
          <div>
            <p>{movie.Year}</p>
          </div>

          <div>
            {/*Before adding the poster image, check if there is any image. Otherwise place a placeholder*/}
            <img src={movie.Poster !== 'N/A' ? movie.Poster : 'https://via.placeholder.com/400'} alt={movie.Title}/>
          </div>

          <div>
            <span>{movie.Type}</span>
            <h3>{movie.Title}</h3>
          </div>
        </div>
    );
}

// Now we can export this component, in order to access it from the App.js code. 
export default MovieCard;

// By creating this component, our life will be so much easier when we will have to add all the other movies card. 