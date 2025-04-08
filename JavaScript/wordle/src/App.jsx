import { useEffect, useState } from "react"

// !!!!

function App() {

  const [solution, setSolution] = useState('')

  // Fetching the list with all the 5 words from which we are gonna choose a random one. It is gonna run at mount time (cause we have an empty array)
  useEffect(() => {
    // Creating an async function to fetch the data
    const fetchWords = async () => {
      // Fetching the data from the api
      const response = await fetch('https://api.frontendexpert.io/api/fe/wordle-words')()
      // Get the json from the response, with all the words
      const words = await response.json()
      // Pick one random world from the array 
      const randomWord = words[Math.floor(Math.random() * words.length)]
      console.log(randomWord)
      // Store it in a state
      setSolution(randomWord)
    }
    // Now we have to call the fetch word when the useEffect is called. 
    fetchWords();
  }, [])

  return (
    <>
      {solution}
    </>
  )
}

export default App
