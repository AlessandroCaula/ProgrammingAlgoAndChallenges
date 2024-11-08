import './App.css';
import { useEffect, useState } from 'react';
import SearchIcon from './search.svg';
import MovieCard from './MovieCard';

// Movie DB API key ==> fb51dfdf

// Create a static variable that will be used to call the API
const API_URL = 'http://www.omdbapi.com?apikey=fb51dfdf';

const movie1 = {
    "Title": "Amazing Spiderman Syndrome",
    "Year": "2012",
    "imdbID": "tt2586634",
    "Type": "movie",
    "Poster": "N/A"
}

function App() {
  // Create a new state in order to pass the data from our search to be displayed as a MovieCard. Using Hook. The initial state will be an empty array.
  const [movies, setMovies] = useState([]);
  // Adding another state for letting the search work. It is possible to have multiple state for component. The initial state will be an ampty string. 
  const [searchTerm, setSearchTerm] = useState('');

  // Create an async arrow function. Async means that it takes some time to fecth these movies. 
  const searchMovies = async (title) => {
    const response = await fetch(`${API_URL}&s=${title}`); // This is going to call our API and request for that movie. 
    const data = await response.json(); // Inside this data object, we should have the data of the movie requested. 

    // Passing the movie data to the setter state of the useState hook. 
    setMovies(data.Search);
    // In this way we can dynamically pass the movie search to the movie card.
  };
  
  return (
    <div className='app'>
      <h1>MovieLand</h1>
      
      {/*Search Div*/}
      <div className='search'>
        <input 
          placeholder='Search for movies'
          value= {searchTerm} // "Superman" // The input has to have a static value, which in this case will be superman. 
          // In order to let this static value be editable, and changable, we have to have an onchange which accepts a callback function.
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <img
          src={SearchIcon}
          alt="search"
          onClick={() => searchMovies(searchTerm)}
        />
      </div>

      {/*Opening a dynamic set of blocks using {}. To check if movies has been populated. If there is some movie in it, render the movie card*/}
      {
        movies?.length > 0 
          ? (
            <div className='container'>
              {/*Calling the MovieCard component. <MovieCard movie={movies[0]}/>
              Open a dynamic block of code and map over movies. For each movie in the movies array, we map it and we want a movieCard for each of it.*/}
              {
                movies.map((movie) => (
                  <MovieCard movie={movie}/>
                ))
              }
            </div>
          ) : (
            <div className='empty'>
              <h2>No movie found</h2>
            </div>
          )
      }
    </div>
  );
  // First of all we want to fetch the data from the movie database as soon as the component loads.
  // In order to do this, we can use the useEffect hook.

  // Create a custom component in order to display multiple movies, without have to copy and pase the movie div multiple times.
  // To do so create a new file in the src directory called MovieCard. And put there the movie div code.   
}

export default App;
