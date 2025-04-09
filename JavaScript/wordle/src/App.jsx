import { useEffect, useState } from "react"
import { words } from "./utils/words"
import { Line } from "./components/Line"

const WORD_LENGTH = 5
const MAX_GUESSES = 6

function App() {

  // State that will store the final correct word solution. 
  const [solution, setSolution] = useState('')
  // Create a state that will store each of our guess. It will be an array of size 6, with null elements at first
  const [guesses, setGuesses] = useState(Array(6).fill(null))
  // useState that will store the current input guess. 
  const [inputGuess, setInputGuess] = useState('')

  // // Fetching the list with all the 5 words from which we are gonna choose a random one. It is gonna run at mount time (cause we have an empty array)
  // useEffect(() => {
  //   // Creating an async function to fetch the data
  //   const fetchWords = async () => {
  //     // // Fetching the data from the api
  //     const response = await fetch('http://localhost:3001/words')
  //     // Get the json from the response, with all the words
  //     const words = await response.json()
  //     console.log(words)
  //     // Pick one random world from the array 
  //     const randomWord = words[Math.floor(Math.random() * words.length)]
  //     console.log(randomWord)
  //     // Store it in a state
  //     setSolution(randomWord)
  //   }
  //   // Now we have to call the fetch word when the useEffect is called. 
  //   fetchWords();
  // }, [])

  useEffect(() => {
    // Pick one random world from the array 
    const randomWord = words[Math.floor(Math.random() * words.length)]
    // Store it in a state
    setSolution(randomWord)
  }, [])

  const HandleTyping = (event) => {
    setInputGuess(event.target.value)

    console.log(inputGuess)
  }

  return (
    <div className="board">
      {/* Map through all the guesses and return a single line (component) */}
      {guesses.map((guess, i) => (
        <div key={i}>
          {/* Rendering the Line component */}
          <Line guess={guess} />
        </div>
      ))}

      {/* Adding the text input component */}
      <input 
        className="input"
        onChange={HandleTyping}
        placeholder="Type your guess here"
      />

    </div>
  )
}

export default App
