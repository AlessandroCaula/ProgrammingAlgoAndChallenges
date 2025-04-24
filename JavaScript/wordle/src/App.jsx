import { useEffect, useState } from "react"
import { words } from "./utils/words"
import { Line } from "./components/Line"


function App() {

  // State that will store the final correct word solution. 
  const [solution, setSolution] = useState('')
  // Create a state that will store each of our guess. It will be an array of size 6, with null elements at first
  const [guesses, setGuesses] = useState(Array(6).fill(null))
  // useState that will store the current input guess. 
  const [inputGuess, setInputGuess] = useState('')
  // // State for endgame.
  // const [isGameWon, setIsGameWon] = useState(false)
  const [resetGame, setResetGame] = useState(false)


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
    console.log("------ Solution:", randomWord)
  }, [resetGame])

  const handleTyping = (event) => {
    setInputGuess(event.target.value)
    // console.log(inputGuess)
  }

  const handleEnterKeyPress = (event) => {
    // Check if the key pressed is the Enter key
    if (event.key === "Enter") {
      // Validate the guess word
      validateGuess()
    }
  }
  
  const validateGuess = () => {
    // The guess needs to be 5 char in length
    if (inputGuess.length > 5) {
      alert("Guess is too long. It needs to be 5 char long")
      return
    } else if (inputGuess.length < 5) {
      alert("Guess is too short. It needs to be 5 char long")
      return
    } else {
      // Add it to the list of guesses
      const new_guesses = [...guesses] // Create a shallow copy of the guesses array
      const firstNullIdx = guesses.findIndex(val => val === null) // Find the index of the first null value in guesses
      new_guesses[firstNullIdx] = inputGuess.toUpperCase()
      setGuesses(new_guesses)
      setInputGuess('')

      // Now check for the end game.
      // If the word added is equal to the solution.
      if (inputGuess.toUpperCase() === solution.toUpperCase()) {
        setTimeout(() => {
          confirm("CORRECT ANSWER!!!! \n\nRestart Game")
          gameReset()
        }, 300)
      } else if (new_guesses.findIndex(val => val === null) === -1) {
        // Check if this is the last possible attempt
        setTimeout(() => {
          confirm("NO MORE ATTEMPTS!!!!! \n\nTry Again")
          gameReset()
        }, 300)
      }
    }
  }

  const gameReset = () => {
    setResetGame(!resetGame)
    setGuesses(Array(6).fill(null))
    setInputGuess('')
  }

  return (
    <div className="board">
      {/* Map through all the guesses and return a single line (component) */}
      {guesses.map((guess, i) => (
        <div key={i}>
          {/* Rendering the Line component */}
          <Line guess={guess} solution={solution} />
        </div>
      ))}

      {/* Adding the text input component */}
      <input 
        className="input"
        value={inputGuess}
        onChange={handleTyping}
        onKeyDown={handleEnterKeyPress}
        placeholder="Type your guess here"
      />

    </div>
  )
}

export default App
